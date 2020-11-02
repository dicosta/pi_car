#!/usr/bin/env python
from socket import *
from time import ctime          
import car.car as car
import signal
import sys
import video.mjpg_streamer as video_streamer

ctrl_cmd = ['forward', 'backward', 'stop', 'speed_slow', 'speed_normal', 'speed_fast', 'speed_faster', 'steer_left_20', 'steer_right_20', 'pan_left_20', 
'pan_right_20', 'tilt_up_20', 'tilt_down_20', 'start_video_stream', 'stop_video_stream']

HOST = ''           # The variable of HOST is null, so the function bind( ) can be bound to all valid addresses.
PORT = 21567
BUFSIZ = 1024       # Size of the buffer
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)    # Create a socket.
tcpSerSock.bind(ADDR)    					 # Bind the IP address and port number of the server. 
tcpSerSock.listen(5)     					 # The parameter of listen() defines the number of connections permitted at one time. Once the 
                         					 # connections are full, others will be rejected. 
mycar = car.Car()
signal.signal(signal.SIGINT, signal.default_int_handler)

while True:
	try:
		print('Waiting for connection...')
		# Waiting for connection. Once receiving a connection, the function accept() returns a separate 
		# client socket for the subsequent communication. By default, the function accept() is a blocking 
		# one, which means it is suspended before the connection comes.
		tcpCliSock, addr = tcpSerSock.accept() 
		print('...connected from :', addr)     # Print the IP address of the client connected with the server.

		while True:
			data = ''
			data = tcpCliSock.recv(BUFSIZ)    # Receive data sent from the client. 
											  # Analyze the command received and control the car accordingly.
			data = data.decode('utf-8')
				
			if not data:
				break
			if data == ctrl_cmd[0]:
				#print('direction forward')
				mycar.set_direction_forward()
			elif data == ctrl_cmd[1]:
				#print('direction backward')			
				mycar.set_direction_backward()
			elif data == ctrl_cmd[2]:
				#print('stop')
				mycar.stop()
			elif data == ctrl_cmd[3]:
				#print('set speed slow')
				mycar.set_speed(car.MotorSpeed.SLOW)
			elif data == ctrl_cmd[4]:
				#print('set speed normal')
				mycar.set_speed(car.MotorSpeed.NORMAL)
			elif data == ctrl_cmd[5]:
				#print('set speed fast')
				mycar.set_speed(car.MotorSpeed.FAST)
			elif data == ctrl_cmd[6]:
				#print('set speed faster')
				mycar.set_speed(car.MotorSpeed.FASTER)
			elif data == ctrl_cmd[7]:
				#print('steer left 20')
				mycar.set_steering_angle(-20)
			elif data == ctrl_cmd[8]:
				#print('set right 20')
				mycar.set_steering_angle(20)
			elif data == ctrl_cmd[9]:
				#print('pan left 20')
				mycar.set_panning_angle(-20)
			elif data == ctrl_cmd[10]:
				#print('pan right 20')
				mycar.set_panning_angle(20)
			elif data == ctrl_cmd[11]:
				#print('tilt up 20')
				mycar.set_tilting_angle(-20)
			elif data == ctrl_cmd[12]:
				#print('tilt down 20')
				mycar.set_tilting_angle(20)
			elif data == ctrl_cmd[12]:
				#print('tilt down 20')
				mycar.set_tilting_angle(20)
			elif data == ctrl_cmd[13]:				
				print('Starting Video Streamer...')
				video_streamer.restart()							
			elif data == ctrl_cmd[14]:				
				print('Stopping Video Streamer...')
				video_streamer.stop()							

			elif data[0:12] == 'steer_angle=':	#steering angle
				#print('data =', data)
				angle = data.split('=')[1]
				try:
					angle = int(angle)
					mycar.set_steering_angle(angle)
				except:
					print('Error: angle =', angle)

			elif data[0:10] == 'pan_angle=':	#pan angle
				#print('data =', data)
				angle = data.split('=')[1]
				try:
					angle = int(angle)
					mycar.set_panning_angle(angle)
				except:
					print('Error: angle =', angle)				

			elif data[0:11] == 'tilt_angle=':	#tilt angle
				#print('data =', data)
				angle = data.split('=')[1]
				try:
					angle = int(angle)
					mycar.set_tilting_angle(angle)
				except:
					print('Error: angle =', angle)				
			else:
				print('Command Error! Cannot recognize command: ' + data)
	except KeyboardInterrupt:
	        print('TCP Server Shutdown')
	        tcpSerSock.close()
	        print('Streamer Shutdown')
	        video_streamer.stop()
	        print('Bye!')
	        sys.exit(0)

tcpSerSock.close()
