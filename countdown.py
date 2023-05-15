"""Countdown from 10 to 1 and then print Liftoff!
"""
def main():
    countdown()
    print("Liftoff!") 

def countdown():
    countdown = 10
    
    while countdown >= 1:
        print(countdown) 
        countdown -= 1
         