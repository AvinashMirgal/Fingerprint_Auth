from base64 import decodebytes
import sqlite3
import os
conn = sqlite3.connect('fingerprints.db')
database = conn.execute("SELECT * FROM fingerprints")
string = {}
for row in database:
	string[row[0]] = (bytearray(row[1],'utf8'))
os.chdir('./fingerprint_images')
i = 0
for key in string:
	with open("%s_%s.png"%(key),%(i),"wb") as f:
		f.write(decodebytes(string[key]))
		i+=1