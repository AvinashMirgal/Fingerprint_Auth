from base64 import decodebytes
import sqlite3
import os
conn = sqlite3.connect('fingerprints.db')
database = conn.execute("SELECT * FROM loginfingerprints")
string = {}
for row in database:
	string[row[0]] = (bytearray(row[1],'utf8'))
os.chdir('./login_FP_images')
for key in string:
	with open("%s.png"%(key),"wb") as f:
		f.write(decodebytes(string[key]))