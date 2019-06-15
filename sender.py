import socket

def files(conn):
	f_name=input("Enter File Name(with extension) :")
	f=open(f_name,'r')
	l=f.read(1024)
	while l:
		conn.send(l.encode())
		print('Sent ',repr(l))
		l=f.read(1024)
	f.close()

def chat(name,conn,conn1):
	while True:
		data=conn.recv(1024).decode()
		sender=conn1.recv(1024).decode()
		if not data:
			break
		print("From "+sender+" :"+data)
		data=input("->")
		conn.send(data.encode())
		conn1.send(name.encode())

name=input("Enter Your Name :")
print('''1.) Send Messages
2.) Send files''' )
choice = int(input("Choice :"))
host=socket.gethostname()
port=8800
por=8801
server_socket=socket.socket()
server_sock=socket.socket()
server_socket.bind((host,port))
server_sock.bind((host,por))
server_socket.listen(2)
server_sock.listen(2)
conn,address=server_socket.accept()
conn1,address=server_sock.accept()
print("Connection  from :"+str(address))
if choice == 1:
	chat(name,conn,conn1)	
elif choice == 2:
	files(conn)	
conn.close()
conn1.close()
