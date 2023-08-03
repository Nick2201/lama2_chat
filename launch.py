import sqlite3
conn_sqlite = sqlite3.connect('.chainlit\.langchain.db')
c = conn_sqlite.cursor()
request_task = """
select *
from sqlite_schema
"""

c.execute(request_task)
results = c.fetchall()
print(results)