import requests
from base64 import decodestring
from base64 import decodebytes
import sqlite3
from subprocess import call
import os
#os.chdir('.\MSO Device Driver')
#call(['setup'])
#os.chdir('.\For_Testing')
conn = sqlite3.connect('fingerprints.db')
# conn.execute('''CREATE TABLE fingerprints(
# 	NAME TEXT NOT NULL,
# 	FINGERPRINT TEXT NOT NULL
# 	);''')
n = 1
name = input("Enter Name:")
for i in range(int(n)):
	print("Place your finger on the machine...")
	response = requests.get("http://localhost:8080/CallMorphoAPI")
	img_data = response.json()['Base64BMPIMage']
	#name1 = name+'_'+str(i )
	conn.execute("INSERT INTO fingerprints VALUES (?,?)",(name,img_data))
	conn.commit()
cursor = conn.execute("SELECT * FROM fingerprints")
for row in cursor:
	print('NAME: '+row[0],end = ' ')
	print('FINGERPRINT: '+str(row[1][:20]))
conn = sqlite3.connect('fingerprints.db')
database = conn.execute("SELECT * FROM fingerprints")
string = {}
for row in database:
	string[row[0]] = (bytearray(row[1],'utf8'))
os.chdir('./fingerprint_images')
for key in string:
	with open("%s.png"%(key),"wb") as f:
		f.write(decodebytes(string[key]))
