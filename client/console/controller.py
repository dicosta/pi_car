from pynput import keyboard
from socket import *
import time

ctrl_cmd = ['forward', 'backward', 'stop', 'speed_slow', 'speed_normal', 'speed_fast', 'speed_faster', 'steer_left_20', 'steer_right_20' ]

up=False
down=False
left=False
right=False
HOST = '10.0.0.10'    # Server(Raspberry Pi) IP address
PORT = 21567
BUFSIZ = 1024             # buffer size
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)   # Create a socket
tcpCliSock.connect(ADDR)                    # Connect with the server

def on_key_release(key):
    global down
    global up
    global tcpCliSock
    global ctrl_cmd
    if (key == keyboard.Key.down and down):
        down=False
        #print('down released')
        tcpCliSock.send('stop'.encode('utf-8'))
    elif (key == keyboard.Key.up and up):
        up=False
        tcpCliSock.send('stop'.encode('utf-8'))
        #print('up released')

def on_press(key):
    global down
    global up
    global tcpCliSock
    global ctrl_cmd

    if (key == keyboard.Key.down and not down):
        down = True
        tcpCliSock.send('backward'.encode('utf-8'))
        tcpCliSock.send('speed_slow'.encode('utf-8'))
        #print('down pressed')
    elif (key == keyboard.Key.up and not up):
        up=True
        tcpCliSock.send('forward'.encode('utf-8'))
        tcpCliSock.send('speed_slow'.encode('utf-8'))
        #print('up pressed')

#with keyboard.Listener(on_press=on_press, on_release = on_key_release) as listener:
#    listener.join()
# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_key_release)
listener.start()

while True:
    time.sleep(0.1)