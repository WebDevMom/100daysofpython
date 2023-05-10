from kareltherobot import *

def main():
    climb_up()
    put_beeper()
    climb_down()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def climb_up():
    while front_is_blocked():
     turn_left()
     move()
     turn_right()
     move()
    
def climb_down():
    while front_is_clear():
     move()
     turn_right()
     move()
     turn_left()
    
    
# don't change this code
if __name__ == '__main__':
    main()