import os
import settings
import psycopg2
import pandas as pd
import pandas.io.sql as sqlio
import datetime

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
		return dataframe.dropna()

	def db_insert(self, predictionLst, interval=5):
		"""
		Insert data into predict_info db
		"""
		dt = datetime.datetime.now()
		idx = 0
		timer = 0
		for i in range(len(predictionLst)):
			timer += interval
			#tDelta = dt + datetime.timedelta(minutes = interval)
			tDelta = dt + datetime.timedelta(minutes = timer)
			time = tDelta.strftime("%Y-%m-%d %H:%M:%S")
			query = "INSERT INTO predict_info (time_stamp, cpu_utilization) VALUES (%s, %s)"
			qInput = (time, predictionLst[i])
			#print(query)
			self.session.execute(query, qInput)
			idx += 1
		self.connection.commit()	

	def db_close(self):
		self.session.close()	
		

#system = "SELECT time, value AS \"node_cpu_seconds_total\" FROM metrics WHERE labels->>'cpu' = '0' and labels->>'mode' = 'system'  AND name='node_cpu_seconds_total' ORDER BY time"

def createQuery(mode, interval, timebucket=5):
	"""
	Creating Query
	"""
	print("Creating query for mode", mode, " interval ", interval," time bucket", timebucket)
	if(interval != -1):
		query = "SELECT time_bucket('%s minutes', time) AS timebucket, avg(value) AS \"node_cpu_seconds_total\" FROM metrics WHERE labels->>'cpu' = '0' and labels->>'mode' = '%s'  AND name='node_cpu_seconds_total'  AND time > ( NOW() - interval '%s day' ) GROUP BY timebucket ORDER BY timebucket" % (timebucket, mode, interval)
	else:
		query =  "SELECT time_bucket('%s minutes', time) AS timebucket, avg(value) AS \"node_cpu_seconds_total\" FROM metrics WHERE labels->>'cpu' = '0' and labels->>'mode' = '%s'  AND name='node_cpu_seconds_total' GROUP BY timebucket ORDER BY timebucket" %(timebucket, mode)
	return query

"""
system = "SELECT time_bucket('%s minutes', time) AS timebucket, avg(value) AS \"node_cpu_seconds_total\" FROM metrics WHERE labels->>'cpu' = '0' and labels->>'mode' = 'system'  AND name='node_cpu_seconds_total'  AND time > ( NOW() - interval '%s day' ) GROUP BY timebucket ORDER BY timebucket" % (5, 1)

irq = "SELECT time, value AS \"node_cpu_seconds_total\" FROM metrics WHERE labels->>'cpu' = '0' and labels->>'mode' = 'irq'  AND name='node_cpu_seconds_total' ORDER BY time"
	
iowait = "SELECT time, value AS \"node_cpu_seconds_total\" FROM metrics WHERE labels->>'cpu' = '0' and labels->>'mode' = 'iowait'  AND name='node_cpu_seconds_total' ORDER BY time"

idle = "SELECT time, value AS \"node_cpu_seconds_total\" FROM metrics WHERE labels->>'cpu' = '0' and labels->>'mode' = 'idle'  AND name='node_cpu_seconds_total' ORDER BY time"

nice = "SELECT time, value AS \"node_cpu_seconds_total\" FROM metrics WHERE labels->>'cpu' = '0' and labels->>'mode' = 'nice'  AND name='node_cpu_seconds_total' ORDER BY time"

softirq = "SELECT time, value AS \"node_cpu_seconds_total\" FROM metrics WHERE labels->>'cpu' = '0' and labels->>'mode' = 'softirq'  AND name='node_cpu_seconds_total' ORDER BY time"

steal = "SELECT time, value AS \"node_cpu_seconds_total\" FROM metrics WHERE labels->>'cpu' = '0' and labels->>'mode' = 'steal'  AND name='node_cpu_seconds_total' ORDER BY time"

user = "SELECT time, value AS \"node_cpu_seconds_total\" FROM metrics WHERE labels->>'cpu' = '0' and labels->>'mode' = 'user'  AND name='node_cpu_seconds_total' ORDER BY time"
"""

def getDatafromDb(period):
	timebucket = 1
	#Creates a an object
	con = PostgresDb()

	#Executes a query
	#con.db_execute(system)

	#fetch all records
	#records = con.db_fetch()

	#gets data in pandaframes
	sData = con.db_getPDFrame(createQuery('system', period, timebucket))
	uData = con.db_getPDFrame(createQuery('user', period, timebucket))
	iData = con.db_getPDFrame(createQuery('idle', period, timebucket))
	ioData = con.db_getPDFrame(createQuery('iowait', period, timebucket))
	irData = con.db_getPDFrame(createQuery('irq', period, timebucket))
	nData = con.db_getPDFrame(createQuery('nice', period, timebucket))
	siData = con.db_getPDFrame(createQuery('softirq', period, timebucket))
	stData = con.db_getPDFrame(createQuery('steal', period, timebucket))
         
	sframe = pd.DataFrame(data=sData)
	sframe.rename({"node_cpu_seconds_total": "system"}, inplace=True, axis=1)

	uframe = pd.DataFrame(data=uData)
	uframe.rename({"node_cpu_seconds_total": "user"}, inplace=True, axis=1)

	iframe = pd.DataFrame(data=iData)
	iframe.rename({"node_cpu_seconds_total": "idle"}, inplace=True, axis=1)

	ioframe = pd.DataFrame(data=ioData)
	ioframe.rename({"node_cpu_seconds_total": "iowait"}, inplace=True, axis=1)

	irframe = pd.DataFrame(data=irData)
	irframe.rename({"node_cpu_seconds_total": "irq"}, inplace=True, axis=1)

	nframe = pd.DataFrame(data=nData)
	nframe.rename({"node_cpu_seconds_total": "nice"}, inplace=True, axis=1)

	siframe = pd.DataFrame(data=siData)
	siframe.rename({"node_cpu_seconds_total": "softirq"}, inplace=True, axis=1)

	stframe = pd.DataFrame(data=stData)
	stframe.rename({"node_cpu_seconds_total": "steal"}, inplace=True, axis=1)

	#print(uframe)
	#print(sframe)
	#print(ioframe)
	#print(iframe)

	#print(nframe)
	#print(siframe)
	#print(stframe)
	#print(iframe)

	uframe.reset_index(drop=True, inplace=True)
	sframe.reset_index(drop=True, inplace=True)
	ioframe.reset_index(drop=True, inplace=True)
	irframe.reset_index(drop=True, inplace=True)

	nframe.reset_index(drop=True, inplace=True)
	siframe.reset_index(drop=True, inplace=True)
	stframe.reset_index(drop=True, inplace=True)
	iframe.reset_index(drop=True, inplace=True)
	#print("Done Done Done Done Done")
	#print("-------------------------------------------")
	cuFrame = uframe[uframe.timebucket.isin(sframe.timebucket)]
	cioFrame = ioframe[ioframe.timebucket.isin(sframe.timebucket)]
	cirFrame = irframe[irframe.timebucket.isin(sframe.timebucket)]
	cnFrame = nframe[nframe.timebucket.isin(sframe.timebucket)]
	csiFrame = siframe[siframe.timebucket.isin(sframe.timebucket)]
	cstFrame = stframe[stframe.timebucket.isin(sframe.timebucket)]
	ciFrame = iframe[iframe.timebucket.isin(sframe.timebucket)]
	#print(cuFrame)
	#print(cioFrame)
	#print("-------------------------------------------")
	#print("End End End End End End")
	#dataframe = pd.concat([sframe, uframe], ignore_index=True)
	#dataframe = pd.concat([sframe, uframe['user'], ioframe['iowait'], irframe['irq'], nframe['nice'], siframe['softirq'], stframe['steal'], iframe['idle']], axis=1, sort=True)
	dataframe = pd.concat([sframe, cuFrame['user'], cioFrame['iowait'], cirFrame['irq'], cnFrame['nice'], csiFrame['softirq'], cstFrame['steal'], ciFrame['idle']], axis=1, sort=True)

	#close the sesssion
	con.db_close()
	return getCpuUtilization(dataframe)

def getCpuUtilization(dframe):
	"""
	Get CPU Utilization
	"""
	dframe.dropna()	
	last_idle = 0
	last_total = 0
	cpuUtilPct = []
	totalCpu = []
	usedCpu = []
	colN = getColumnNames(dframe)
	for index, row in dframe.iterrows():
		#print("index: ", index)
		cTotal = cSum(row, colN)
		idle = row['idle']
		#print("**************************")
		#print(cTotal, idle)
		idle_delta, total_delta = idle - last_idle, cTotal - last_total
		last_idle, last_total = idle, cTotal
		CpuUtilization = 100 * (1.0 - idle_delta/total_delta)
		#print(CpuUtilization)
		#print("**************************")
		cpuUtilPct.append(CpuUtilization)
		totalCpu.append(cTotal)
		usedCpu.append(cTotal-idle)
	dframe['CpuProvisioned'] = totalCpu
	dframe['CpuUsage'] = usedCpu
	dframe['CpuUtilization'] = cpuUtilPct
	return dframe

	
def getColumnNames(df):
	"""
	 get data frame column names
	"""
	Cname = []
	for col in df.columns:
		Cname.append(col)
	return Cname[1:]

def cSum(rdata, cnames):
	"""
	get the sum of values
	"""
	cTotal = 0.0 
	for cn in (cnames):
		#print(cn, rdata[cn])
		cTotal += rdata[cn]
	#print("cTotal: ", cTotal)
	return cTotal


def writeDataToDb(list):
	db_client = PostgresDb()
	db_client.db_insert(list)
	db_client.db_close()

if __name__ == "__main__":

	#con = PostgresDb()
	#s = con.db_getPDFrame(createQuery('system', 1, 5))
	#print(s)
	#u = con.db_getPDFrame(createQuery('user', 1, 5))
	#print(u)
	#i = con.db_getPDFrame(createQuery('irq', 1, 5))
	#print(i)
	#db_client = PostgresDb()
	#lst = [0.30, 0.31, 0.32, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.40]
	#db_client.db_insert(lst)
	#db_client.db_close()
	dFrame = getDatafromDb(1)
	print(dFrame)
	#df = getCpuUtilization(dFrame)
	#print(df)
	"""
	print("==============================")
	print(dFrame['system'][0])
	print("==============================")

	cnames = getColumnNames(dFrame)
	print(cnames)
	print("==============================")
	print(dFrame.loc[0])
	print("==============================")
	ct = cSum(dFrame.loc[0], cnames) 
	print("*******************************")
	print(ct)
	"""

   

