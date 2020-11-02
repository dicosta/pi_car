from pynput import keyboard
from socket import *
import time

ctrl_cmd = ['forward', 'backward', 'stop', 'speed_slow', 'speed_normal', 'speed_fast', 'speed_faster', 'steer_left_20', 'steer_right_20',
'pan_left_20', 'pan_right_20', 'tilt_up_20', 'tilt_down_20']

up=False
down=False
left=False
right=False
tilt_up=False
tilt_down=False
pan_left=False
pan_right=False
HOST = '10.0.0.10'    # Server(Raspberry Pi) IP address
PORT = 21567
BUFSIZ = 1024             # buffer size
ADDR = (HOST, PORT)

def encode_and_send(message):
    global tcpCliSock
    print('encode and send: ' + message)    

def on_key_release(key):
    global down
    global up
    global left
    global right
    global tcpCliSock
    global ctrl_cmd
    global tilt_up
    global tilt_down
    global pan_left
    global pan_right

    try:
        if (key == keyboard.Key.down and down):
            down=False
            encode_and_send(ctrl_cmd[2])            
        elif (key == keyboard.Key.up and up):
            up=False
            encode_and_send(ctrl_cmd[2])            
        elif (key == keyboard.Key.left and left):
            left=False
            encode_and_send('steer_angle=0')            
        elif (key == keyboard.Key.right and right):
            right=False
            encode_and_send('steer_angle=0')            
        elif (key.char == 'a' and pan_left):
            pan_left=False        
            encode_and_send('pan_angle=0')
        elif (key.char== 'd' and pan_right):
            pan_right=False        
            encode_and_send('pan_angle=0')
        elif (key.char == 'w' and tilt_up):
            tilt_up=False        
            encode_and_send('tilt_angle=0')
        elif (key.char == 's' and tilt_down):
            tilt_down=False        
            encode_and_send('tilt_angle=0')
    except:
        print('ignored key release')

def on_press(key):
    global listening
    global down
    global up
    global left
    global right
    global tcpCliSock
    global ctrl_cmd
    global tilt_up
    global tilt_down
    global pan_left
    global pan_right

    try:
        if (key == keyboard.Key.esc):
            listening = False
            return False
        if (key == keyboard.Key.down and not down):
            down = True
            encode_and_send(ctrl_cmd[1])
            tcpCliSock.send('speed_faster'.encode('utf-8'))
        elif (key == keyboard.Key.up and not up):
            up=True
            encode_and_send(ctrl_cmd[0])
            tcpCliSock.send('speed_faster'.encode('utf-8'))
        elif (key == keyboard.Key.left and not left):
            left=True
            encode_and_send(ctrl_cmd[7])
        elif (key == keyboard.Key.right and not right):
            right=True
            encode_and_send(ctrl_cmd[8])
        elif (key.char == 'a' and not pan_left):
            pan_left=True        
            encode_and_send(ctrl_cmd[9])
        elif (key.char == 'd' and not pan_right):
            pan_right=True        
            encode_and_send(ctrl_cmd[10])
        elif (key.char == 'w' and not tilt_up):
            tilt_up=True        
            encode_and_send(ctrl_cmd[11])
        elif (key.char == 's' and not tilt_down):
            tilt_down=True        
            encode_and_send(ctrl_cmd[12])
    except:        
        print('ignored key release')    
    

tcpCliSock = socket(AF_INET, SOCK_STREAM)   # Create a socket
tcpCliSock.connect(ADDR)                    # Connect with the server    

print('Connected To ' + HOST)
print('Use wasd to control camera or arrow keys to control direction')
print('press ESC to close')

listener = keyboard.Listener(
    suppress=True,
    on_press=on_press,
    on_release=on_key_release)
listener.start()

listening = True
while listening:
    time.sleep(0.1)