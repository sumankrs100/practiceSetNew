import contextlib
import os
from dotenv import load_dotenv
import psycopg2


class Database:

    db = None
    un = None
    pas = None
    host = None
    port = None

    def __init__(self, env, db=None, un=None, pas=None, host=None, port=None):
        self.db = db
        self.un = un
        self.pas = pas
        self.host = host
        self.port = port
        self.get_connection_details(env)

    def get_connection_details(self, env):
        env_file = os.getcwd() + os.sep + "config" + os.sep + env + ".env"
        load_dotenv(env_file)
        if self.db is None:
            self.db = os.getenv("DB")
        if self.un is None:
            self.un = os.getenv("USER")
        if self.pas is None:
            self.pas = os.getenv("PASSWORD")
        if self.host is None:
            self.host = os.getenv("DB_HOST")
        if self.port is None:
            self.port = os.getenv("DB_PORT")

    @contextlib.contextmanager
    def create_connection(self):
        conn = psycopg2.connect(database=self.db,
                                host=self.host,
                                port=self.port,
                                user=self.un,
                                password=str(self.pas))
        try:
            yield conn
        except Exception:
            conn.rollback()
            raise
        else:
            conn.commit()
        finally:
            conn.close()

    @contextlib.contextmanager
    def cur(self):
        with self.create_connection() as con:
            cur = con.cursor()
            try:
                yield cur
            except Exception:
                raise
            finally:
                cur.close()

