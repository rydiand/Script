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
	#print("Database opened.")
	return(conn)

def num_days(today, dat):
	from datetime import date 
	return (dat-today).days


def read_db(conn):
	cursor = conn.execute("SELECT ID, begivenhed, dato from Dage order by dato")
	beg = []
	dat = []
	count = 0
	lineno  = []
	for row in cursor:
   		#print("ID = ", row[0])
   		#print("Begivenhed = ", row[1])
   		#print("Dato = ", row[2], "\n")
   		lineno.append(row[0])
   		beg.append(row[1])
   		dat.append(row[2])
   		count = count + 1
	return lineno, beg, dat, count

def opret_dato(conn):
	#print("Opret dato")
	#c = conn.cursor()
	beg = input("Angiv begivenhed:")
	dat = input("Angiv dato (YYYY-MM-DD):")
	conn.execute("INSERT into Dage (ID, begivenhed, dato) values(null, ?, ?)", (beg, dat))
	conn.commit()

def slet_dato(conn, id):
	#print("Slet dato")
	conn.execute("DELETE from Dage where ID = ?", id)
	conn.commit()

def opdater_dato(conn, id):
	print("Opdater dato",id)
	beg = input("Angiv begivenhed:")
	dat = input("Angiv dato (YYYY-MM-DD):")
	conn.execute("UPDATE Dage set begivenhed = ?, dato = ? where ID = ?", (beg, dat, id))
	conn.commit()


def close_db(conn):
	conn.close()
	#print("Database closed.")

def print_all(lineno, dat, beg, today, count):
	print("Nr.\tDage\tDato\t\tUgedag\t\tBegivenhed")
	for x in range(0, count):
		dato = datetime.datetime.strptime(dat[x], "%Y-%m-%d").date()
		count_days = num_days(today,dato)
		print(lineno[x],"\t", count_days, "\t", dato, "\t",is_day(dato), "\t", beg[x])

conn = open_db()
import datetime
today = datetime.date.today()

#print(today)

from datetime import date 
#print(num_days(date(today),date("2017,11,2")))

lineno, beg, dat, count = read_db(conn)

#print(lineno)
#print(beg)
#print(dat)
answer = 'n'
while answer.upper() != 'X':
	print("1. Læs alle datoer")
	print("2. Opret en dato")
	print("3. Opdater dato")
	print("4. Slet en dato")
	print("x. Afslut")
	answer = input("Vælg:")
	if answer == "1":
		print_all(lineno, dat, beg, today, count)
	if answer == "2":
		opret_dato(conn)
	if answer == "3":
		id = input("Hvilken record?")
		opdater_dato(conn, id)
	if answer == "4":
		id = input("Hvilken record?")
		slet_dato(conn, id)
	if (answer != "1" and answer.upper() != 'X'):
		#close_db(conn)
		#conn = open_db()
		lineno, beg, dat, count = read_db(conn)


#print((dato-today).days)
#print(count)
close_db(conn)

#print("Operation done successfully, bye, bye.")