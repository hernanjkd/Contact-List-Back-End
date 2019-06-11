import sqlalchemy
from sqlalchemy import create_engine

engine = sqlalchemy.create_engine("mysql://root@localhost")
conn = engine.connect()
existing_databases = engine.execute("SHOW DATABASES;")
existing_databases = [d[0] for d in existing_databases]
if 'contact-list' not in existing_databases:
    conn.execute("CREATE DATABASE contact-list")
    conn.execute("commit")
conn.close()
