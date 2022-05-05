#!/usr/bib/python3


txt_header = '''





▒▒▄▀▀▀▀▀▄▒▒▒▒▒▄▄▄▄▄▒▒▒
▒▐░▄░░░▄░▌▒▒▄█▄█▄█▄█▄▒
▒▐░▀▀░▀▀░▌▒▒▒▒▒░░░▒▒▒▒
▒▒▀▄░═░▄▀▒▒▒▒▒▒░░░▒▒▒▒
▒▒▐░▀▄▀░▌▒▒▒▒▒▒░░░▒▒▒▒

[ + ] Title : UFO Port Scanner  [ + ]
[ + ] Version : 0.0.1-May-2022  [ + ]
[ + ] Code : Python - KrdSploit [ + ]



										'''


print(txt_header)





def portsc():
	import socket
	import subprocess
	import sys
	from datetime import datetime


	subprocess.call('clear', shell=True)

	host_server = input("Enter The Host : ")
	ip_server = socket.gethostbyname(host_server)

	

	print ("Please Wait With Scanning The Host : ",ip_server)

	t1 = datetime.now()



	try:
		for port in range(1,1025):
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			result = sock.connect_ex((ip_server,port))
			if result ==0:
				print ("[!] Port {} : Open".format(port))
			sock.close()


	except KeyboardInterrupt:
		print ("You Pressed Ctrl + C")
		sys.exit()


	except socket.gaierror:
		print (" [ ! ] Hostname could not be resloved , exiting ")
		sys.exit()


	except socket.error:
		print (" Could not connect to the server")
		sys.exit()


		t2 = datetime.now()

		total = t2 - t1


		print ("Scanning Completed In : ", total)



portsc()