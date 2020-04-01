import os
import settings
import psycopg2
import pandas as pd
import pandas.io.sql as sqlio

class DatabaseError(Exception):
	""" This will be raised when there is any db related error"""

class PostgresDb(object):
	"""

	"""

	def __init__(self, hostname=settings.PROMQL_HOSTNAME, port=settings.PROMQL_PORT, username=settings.PROMQL_USERNAME, password=settings.PROMQLDB_PASSWORD,
				database=settings.PROMQL_DB_NAME):
		self.host = hostname
		self.port = port
		self.username = username
		self.password = password
		self.database = database
		self.connection = psycopg2.connect(user = self.username, password=self.password, host=self.host, port=self.port, database=self.database)
		self.session = self.connection.cursor()

	def db_connect(self):
		#self.connection = psycopg2.connect(user = self.username, password=self.password, host=self.host, port=self.port, database=self.database)
		#self.session = self.connection.cursor
		#return self.session
		pass

	def db_execute(self, query):
		self.session.execute(query)

	def db_fetch(self):
		records = self.session.fetchall()
		#read each data record in a for loop 
		return records

	def db_getPDFrame(self, query):
		""" Executes the query and return the data in panda frame"""
		dataframe = sqlio.read_sql_query(query, self.connection)
		return dataframe

	def db_close(self):
		self.session.close()	
		

system = "SELECT time, value AS \"node_cpu_seconds_total\" FROM metrics WHERE labels->>'cpu' = '0' and labels->>'mode' = 'system'  AND name='node_cpu_seconds_total' ORDER BY time"

irq = "SELECT time, value AS \"node_cpu_seconds_total\" FROM metrics WHERE labels->>'cpu' = '0' and labels->>'mode' = 'irq'  AND name='node_cpu_seconds_total' ORDER BY time"
	
iowait = "SELECT time, value AS \"node_cpu_seconds_total\" FROM metrics WHERE labels->>'cpu' = '0' and labels->>'mode' = 'iowait'  AND name='node_cpu_seconds_total' ORDER BY time"

idle = "SELECT time, value AS \"node_cpu_seconds_total\" FROM metrics WHERE labels->>'cpu' = '0' and labels->>'mode' = 'idle'  AND name='node_cpu_seconds_total' ORDER BY time"

nice = "SELECT time, value AS \"node_cpu_seconds_total\" FROM metrics WHERE labels->>'cpu' = '0' and labels->>'mode' = 'nice'  AND name='node_cpu_seconds_total' ORDER BY time"

softirq = "SELECT time, value AS \"node_cpu_seconds_total\" FROM metrics WHERE labels->>'cpu' = '0' and labels->>'mode' = 'softirq'  AND name='node_cpu_seconds_total' ORDER BY time"

steal = "SELECT time, value AS \"node_cpu_seconds_total\" FROM metrics WHERE labels->>'cpu' = '0' and labels->>'mode' = 'steal'  AND name='node_cpu_seconds_total' ORDER BY time"

user = "SELECT time, value AS \"node_cpu_seconds_total\" FROM metrics WHERE labels->>'cpu' = '0' and labels->>'mode' = 'user'  AND name='node_cpu_seconds_total' ORDER BY time"

#Creates a an object
con = PostgresDb()

#Executes a query
con.db_execute(system)

#fetch all records 
records = con.db_fetch()

#gets data in pandaframes
dataframe = con.db_getPDFrame(system)
 
