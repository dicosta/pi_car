import car.car as car
import car.car_motor as motor
import car.car_direction as car_direction
import car.video_direction as video_dir
import time

def test_motor():
    #setup
    motor.setup()    

    #sping forward at speed of 75 for 2 seconds and 50 for 2 seconds
    motor.ctrl(1, 1)
    motor.setSpeed(25)
    print(25)
    time.sleep(2)
    motor.setSpeed(50)
    print(50)
    time.sleep(2)
    motor.setSpeed(75)
    print(75)
    time.sleep(2)
    motor.setSpeed(100)
    print(100)
    time.sleep(2)
    motor.setSpeed(125)
    print(125)
    time.sleep(2)
    motor.setSpeed(0)
    motor.stop()

    #sping backward at speed of 75 for 3 seconds and 50 for 2 seconds
    motor.ctrl(1, -1)
    motor.setSpeed(75)
    time.sleep(2)
    motor.setSpeed(50)
    time.sleep(2)
    motor.setSpeed(0)
    motor.stop()

def test_car_direction():
    car_direction.setup()    
    car_direction.turn_left()
    time.sleep(2)
    car_direction.home()
    time.sleep(2)
    car_direction.turn_right()
    time.sleep(2)
    car_direction.home()  
    time.sleep(2) 
    car_direction.turn(90)

def test_car_direction_smooth():
    car_direction.setup()
    car_direction.turn_left()
    for i in range(258, 479, 3):
        car_direction.set_angle(i)
        time.sleep(0.1)

    time.sleep(2)
    car_direction.home()    

def test_video_direction():
    video_dir.setup()
    video_dir.setxleft()
    time.sleep(2)
    video_dir.setxcenter()
    time.sleep(2)
    video_dir.setxright()
    time.sleep(2)
    #video_dir.setxmoreright()
    time.sleep(2)
    video_dir.setxcenter()
    time.sleep(2)

    video_dir.setytop()
    time.sleep(2)
    #video_dir.setymoretop()
    #time.sleep(2)    
    video_dir.setycenter()
    time.sleep(2)
    video_dir.setybottom()
    time.sleep(2)
    video_dir.setycenter()
    #video_dir.calibrate(0, 0)
    #video_dir.home_x_y()
    #video_dir.setxangle()
    #time.sleep(2)

def test_short_ride():
    car_direction.setup()    
    car_direction.turn_right()
    time.sleep(0.1)

    motor.setup()
    motor.ctrl(1, 1)    
    motor.setSpeed(50)
    time.sleep(2)
    motor.setSpeed(0)

    motor.stop()
    car_direction.home()    

def test_car_object():
    mycar = car.Car()
    mycar.set_direction_forward()
    mycar.set_speed(car.MotorSpeed.NORMAL)
    time.sleep(1)
    mycar.stop()
    mycar.set_steering_angle(-45)
    time.sleep(1)
    #mycar.set_steering_angle(-30)
    #time.sleep(1)    
    #mycar.set_steering_angle(-15)
    #time.sleep(1)
    #mycar.set_steering_angle(-5)
    #time.sleep(1)
    mycar.set_steering_angle(0)
    time.sleep(1)
    mycar.set_steering_angle(45)
    time.sleep(1)
    #mycar.set_steering_angle(25)
    #time.sleep(1)
    #mycar.set_steering_angle(5)
    #time.sleep(1)
    mycar.set_steering_angle(0)
    time.sleep(1)
    mycar.set_panning_angle(-45)
    time.sleep(1)
    #mycar.set_panning_angle(-25)
    #time.sleep(1)
    mycar.set_panning_angle(0)
    time.sleep(1)
    #mycar.set_panning_angle(25)
    #time.sleep(1)
    mycar.set_panning_angle(45)
    time.sleep(1)
    mycar.set_panning_angle(0)
    time.sleep(1)
    mycar.set_tilting_angle(-45)
    time.sleep(1)
    #mycar.set_tilting_angle(-25)
    #time.sleep(1)
    mycar.set_tilting_angle(0)
    time.sleep(1)
    #mycar.set_tilting_angle(25)
    #time.sleep(1)
    mycar.set_tilting_angle(45)
    time.sleep(1)
    mycar.set_tilting_angle(0)
    time.sleep(1)

#test_motor()
#test_car_direction()
#test_video_direction()
#test_car_direction_smooth()
#test_short_ride()
#test_car_object()

import keyboard
#declaring it global so that it can be modified from function
global releaseListening
keepListening = True


def key_press(key):
    print('key press')
    print('key: ' + key.name)    
    if (key.name == 'esc'):
        keepListening = False
        
keyboard.on_press(key_press)

while keepListening :
    time.sleep(1)