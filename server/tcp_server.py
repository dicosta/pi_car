#!/usr/bin/env python
from socket import *
from time import ctime          
import car.car as car

ctrl_cmd = ['forward', 'backward', 'stop', 'speed_slow', 'speed_normal', 'speed_fast', 'speed_faster', 'steer_left_20', 'steer_right_20' ]

HOST = ''           # The variable of HOST is null, so the function bind( ) can be bound to all valid addresses.
PORT = 21567
BUFSIZ = 1024       # Size of the buffer
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)    # Create a socket.
tcpSerSock.bind(ADDR)    					 # Bind the IP address and port number of the server. 
tcpSerSock.listen(5)     					 # The parameter of listen() defines the number of connections permitted at one time. Once the 
                         					 # connections are full, others will be rejected. 
mycar = car.Car()

while True:
	print 'Waiting for connection...'
	# Waiting for connection. Once receiving a connection, the function accept() returns a separate 
	# client socket for the subsequent communication. By default, the function accept() is a blocking 
	# one, which means it is suspended before the connection comes.
	tcpCliSock, addr = tcpSerSock.accept() 
	print '...connected from :', addr     # Print the IP address of the client connected with the server.

	while True:
		data = ''
		data = tcpCliSock.recv(BUFSIZ)    # Receive data sent from the client. 
										  # Analyze the command received and control the car accordingly.
		if not data:
			break
		if data == ctrl_cmd[0]:
			print 'direction forward'			
			car.set_direction_forward()
		elif data == ctrl_cmd[1]:
			print 'direction backward'			
			car.set_direction_backward()
		elif data == ctrl_cmd[2]:
			print 'stop'			
			car.stop()
		elif data == ctrl_cmd[3]:
			print 'set speed slow'			
			car.set_speed(car.MotorSpeed.SLOW)
		elif data == ctrl_cmd[4]:
			print 'set speed normal'			
			car.set_speed(car.MotorSpeed.NORMAL)
		elif data == ctrl_cmd[5]:
			print 'set speed fast'			
			car.set_speed(car.MotorSpeed.FAST)
		elif data == ctrl_cmd[6]:
			print 'set speed faster'			
			car.set_speed(car.MotorSpeed.FASTER)
		elif data == ctrl_cmd[7]:
			print 'steer left 20'			
			car.set_steering_angle(-20)
		elif data == ctrl_cmd[8]:
			print 'set right 20'			
			car.set_steering_angle(20)

		elif data[0:12] == 'steer_angle=':	#steering angle
			print 'data =', data
			angle = data.split('=')[1]
			try:
				angle = int(angle)
				car.set_steering_angle(angle)
			except:
				print 'Error: angle =', angle
		else:
			print 'Command Error! Cannot recognize command: ' + data

tcpSerSock.close()