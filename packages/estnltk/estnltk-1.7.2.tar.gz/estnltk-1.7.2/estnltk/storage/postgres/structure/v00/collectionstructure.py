from psycopg2.sql import SQL, Literal
from psycopg2.extensions import STATUS_BEGIN

from estnltk import logger
from estnltk.storage import postgres as pg


__version__ = '0.0'


class CollectionStructure(pg.CollectionStructureBase):
    def __init__(self, collection):
        super().__init__(collection, __version__)

    def create_table(self):
        storage = self.collection.storage
        table = pg.table_identifier(storage, pg.structure_table_name(self.collection.name))
        temporary = SQL('TEMPORARY') if storage.temporary else SQL('')
        with storage.conn.cursor() as c:
            try:
                c.execute(SQL('CREATE {temporary} TABLE {table} ('
                              'layer_name text primary key, '
                              'detached bool not null, '
                              'attributes text[] not null, '
                              'ambiguous bool not null, '
                              'parent text, '
                              'enveloping text, '
                              '_base text, '
                              'meta text[]);').format(temporary=temporary,
                                                      table=table))
            except Exception:
                storage.conn.rollback()
                raise
            finally:
                if storage.conn.status == STATUS_BEGIN:
                    # no exception, transaction in progress
                    storage.conn.commit()
                    logger.debug(c.query.decode())

    def insert(self, layer, layer_type: str, meta: dict = None, loader: str = None, is_sparse: bool = False):
        if is_sparse:
            raise ValueError('(!) Sparse layers not supported in collectionstructure version {}'.format(__version__))
        self._modified = True

        detached = layer_type in pg.PostgresStorage.TABLED_LAYER_TYPES
        meta = list(meta or [])

        with self.collection.storage.conn.cursor() as c:
            try:
                c.execute(SQL("INSERT INTO {} (layer_name, detached, attributes, ambiguous, parent, enveloping, _base, meta) "
                              "VALUES ({}, {}, {}, {}, {}, {}, {}, {});").format(
                    pg.structure_table_identifier(self.collection.storage, self.collection.name),
                    Literal(layer.name),
                    Literal(detached),
                    Literal(list(layer.attributes)),
                    Literal(layer.ambiguous),
                    Literal(layer.parent),
                    Literal(layer.enveloping),
                    Literal(layer._base),
                    Literal(meta)
                )
                )
            except Exception:
                self.collection.storage.conn.rollback()
                raise
            finally:
                if self.collection.storage.conn.status == STATUS_BEGIN:
                    # no exception, transaction in progress
                    self.collection.storage.conn.commit()
                    logger.debug(c.query.decode())

    def load(self, update_structure:bool =False, omit_commit: bool=False, omit_rollback: bool=False):
        if not self.collection.exists(omit_commit=omit_commit, omit_rollback=omit_rollback):
            return None
        structure = {}
        with self.collection.storage.conn.cursor() as c:
            c.execute(SQL("SELECT layer_name, detached, attributes, ambiguous, parent, enveloping, _base, meta "
                          "FROM {};").
                      format(pg.structure_table_identifier(self.collection.storage, self.collection.name)))

            for row in c.fetchall():
                structure[row[0]] = {'attributes': tuple(row[2]),
                                     'ambiguous': row[3],
                                     'parent': row[4],
                                     'enveloping': row[5],
                                     '_base': row[6],
                                     'meta': row[7],
                                     'layer_type': 'detached' if row[1] else 'attached',
                                     'loader': None}
        if update_structure:
            self._structure = structure
            self._modified = False
        return structure
