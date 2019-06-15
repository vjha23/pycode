import socket

def chat(name,client_socket,client_sock): 
	message=input("->")
	while message.lower()!="bye":
		client_socket.send(message.encode())
		client_sock.send(name.encode())
		data=client_socket.recv(1024).decode()
		server=client_sock.recv(1024).decode()
		print("Received From "+server+" :"+data)
		message=input("-->")

def files(client_socket,client_sock):
	f=open("received.txt",'w+')
	while True:
		data=client_socket.recv(1024)
		if not data:
			break
		f.write(data.decode())
	f.close()
	print("File Received ")

name=input("Enter Name to start Conversation :")
print('''1.) Send Messages
2.) Receive  files''' )
choice = int(input("Choice :"))
host=socket.gethostname()
port=8800
por=8801

client_socket=socket.socket()
client_sock=socket.socket()
client_socket.connect((host,port))
client_sock.connect((host,por))
if choice == 1:
	chat(name,client_socket,client_sock)
elif choice == 2:
	files(client_socket,client_sock)


