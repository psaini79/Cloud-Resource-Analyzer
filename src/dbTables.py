import os
import uuid
import tableModels as model
from sqlalchemy import create_engine                           
from sqlalchemy.exc import ProgrammingError                    
from sqlalchemy.orm import sessionmaker, scoped_session 
from datetime import datetime
import settings 

class DatabaseError(Exception):
    """ This will raised when there is any db related error """

class PostgresTb(object):
    """

    """

    def __init__(self, hostname=settings.PROMQL_HOSTNAME, port=settings.PROMQL_PORT, username=settings.PROMQL_USERNAME, password=settings.PROMQLDB_PASSWORD,
                database=settings.PROMQL_DB_NAME):
        self.host = hostname
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        connection_string = ("postgres://"+username+":"+password+"@"+hostname+"/"+database)
        root_connection_string = ("postgres://"+username+":"+password+"@"+hostname+"/"+database)
        root_engine = create_engine(root_connection_string)
        self.root_session = sessionmaker(bind=root_engine)()
        self._engine = create_engine(connection_string, pool_recycle=3600)
        self.session_factory = sessionmaker(bind=self._engine)
        self.scoped_session = scoped_session(self.session_factory)

    @property
    def engine(self):
        return self._engine
  
    def open(self):
        return self.session_factory()
  
    def get_factory(self):
        return self.session_factory
  
    def get_session(self):
        return self.scoped_session
  
    def create(self):
        try:
            self.root_session.connection().connection.set_isolation_level(0)
            self.root_session.execute("CREATE DATABASE {0}".format(
                  self.database_name))
            self.root_session.connection().connection.set_isolation_level(0)
        except ProgrammingError as err:
            if "already exists" not in err.orig:
                pass
  
            Base.metadata.create_all(self._engine)
  
    def drop(self):
        Base.metadata.drop_all(self._engine)
        self._engine.dispose()

        self.root_session.connection().connection.set_isolation_level(0)
        self.root_session.execute("DROP DATABASE {0}".format(
            self.database_name))
        self.root_session.connection().connection.set_isolation_level(0)


def create_all_tables(db_engine):
    model.Base.metadata.create_all(db_engine)

def upsert(dbs, table_obj, record):
  
    try:
        dbs.execute(table_obj.__table__.insert(), record)
    except IntegrityError as ierr:
        dbs.rollback()
        dbs.merge(table_obj(**record))
    except OperationalError as operr:
              raise
    finally:
        dbs.commit()

if __name__ == "__main__":

	pgClient = PostgresTb()
	dbSsession = pgClient.get_session()
	dbEngine = pgClient.engine
	create_all_tables(dbEngine) 	
