import sqlite3

def is_day(day):
	wd = "wrong"
	
	if day.weekday() == 0:
		wd = "Mandag"
	
	if day.weekday() == 1:
		wd = "Tirsdag"

	if day.weekday() == 2:
		wd = "Onsdag"

	if day.weekday() == 3:
		wd = "Torsdag"

	if day.weekday() == 4:
		wd = "Fredag"

	if day.weekday() == 5:
		wd = "Lørdag"

	if day.weekday() == 6:
		wd = "Søndag"
		
	return wd

def open_db():
	conn = sqlite3.connect('AntalDage.db')
	print("Database opened.")
	return(conn)

def num_days(today, dat):
	from datetime import date 
	return (dat-today).days


def read_db(conn):
	cursor = conn.execute("SELECT ID, begivenhed, dato from Dage")
	beg = []
	dat = []
	count = 0
	lineno  = []
	for row in cursor:
   		print("ID = ", row[0])
   		print("Begivenhed = ", row[1])
   		print("Dato = ", row[2], "\n")
   		lineno.append(row[0])
   		beg.append(row[1])
   		dat.append(row[2])
   		count = count + 1
	return lineno, beg, dat, count

def close_db(conn):
	conn.close()
	print("Database closed.")

conn = open_db()
import datetime
now = datetime.datetime.now()
today = datetime.date(now.year, now.month, now.day)
print(today)

from datetime import date 
#print(num_days(date(today),date("2017,11,2")))

lineno, beg, dat, count = read_db(conn)
print(lineno)
print(beg)
print(dat)
dato = dat[0].replace("-",",")
print("Min dato", dato)
#print((dato-today).days)
print(count)
close_db(conn)

a = date(2017,12,12)
print(a)
print(is_day(a))
print("Operation done successfully, bye, bye.")
