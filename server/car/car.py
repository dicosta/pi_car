from enum import Enum

import car.car_motor as motor
import car.car_direction as direction
import car.video_direction as video_direction


class MotorDirection(Enum):
    FORWARD = 0
    BACKWARD = 1

class MotorState(Enum):
    STOP = 0
    RUN = 1

class MotorSpeed(Enum):
    STOP = 0
    SLOW = 25
    NORMAL = 50
    FAST = 75
    FASTER = 100

class Car:
    __MAX_STEERING_ANGLE = 45
    __MAX_PANNING_ANGLE = 45
    __MAX_TILTING_ANGLE = 45

    def __init__(self):        
        #motor state
        self.motor_state = MotorState.STOP
        self.motor_direction = MotorDirection.FORWARD
        self.motor_speed = MotorSpeed.STOP
        #steering state
        self.__current_steering_angle = 0
        #video direction
        self.__current_tilting_angle = 0
        self.__current_panning_angle = 0

        #servos_init
        motor.setup()
        direction.setup()
        video_direction.setup()

        #initialization
        self.__apply_motor_change()
        self.__apply_steering_change()
        self.__apply_tilting_and_panning_change()
        
    def __apply_motor_change(self):
        motor.ctrl(self.motor_state.value, self.motor_direction.value)
        motor.setSpeed(self.motor_speed.value)

    def __apply_steering_change(self):
        direction.set_angle(self.__current_steering_angle)
    
    def __apply_tilting_and_panning_change(self):
        video_direction.set_tilt_angle(self.__current_tilting_angle)
        video_direction.set_pan_angle(self.__current_panning_angle)

    def stop(self):
        self.motor_state = MotorState.STOP
        self.motor_speed = MotorSpeed.STOP
        self.__apply_motor_change()        

    def set_direction_forward(self):
        self.motor_direction = MotorDirection.FORWARD
        self.__apply_motor_change()

    def set_direction_backward(self):
        self.motor_direction = MotorDirection.BACKWARD
        self.__apply_motor_change()

    def set_speed(self, speed):
        if not isinstance(speed, MotorSpeed):
            raise TypeError('speed must be an instance of MotorSpeed Enum')
        self.motor_speed = speed
        self.__apply_motor_change()

    def set_steering_angle(self, angle):
        if (angle < (-1*self.__MAX_STEERING_ANGLE)):
            angle=-1*self.__MAX_STEERING_ANGLE
        elif (angle > self.__MAX_STEERING_ANGLE):
            angle=self.__MAX_STEERING_ANGLE
        self.__current_steering_angle = angle
        self.__apply_steering_change()

    def set_tilting_angle(self, angle):
        if (angle < (-1*self.__MAX_TILTING_ANGLE)):
            angle=-1*self.__MAX_TILTING_ANGLE
        elif (angle > self.__MAX_TILTING_ANGLE):
            angle=self.__MAX_TILTING_ANGLE
        self.__current_tilting_angle = angle
        self.__apply_tilting_and_panning_change()

    def set_panning_angle(self, angle):
        #invert so it matches with steering orientation
        angle = -1 * angle

        if (angle < (-1*self.__MAX_PANNING_ANGLE)):
            angle=-1*self.__MAX_PANNING_ANGLE
        elif (angle > self.__MAX_PANNING_ANGLE):
            angle=self.__MAX_PANNING_ANGLE
        self.__current_panning_angle = angle
        self.__apply_tilting_and_panning_change()