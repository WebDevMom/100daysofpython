from graphics import Canvas
import random

CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_rectangle(0, 0, 450, 150, "red")
    show_mouse_position(canvas)

def show_mouse_position(canvas):
    while True:
        x = str(canvas.get_mouse_x())
        y = str(canvas.get_mouse_y())
        print(x + "," + y )
        time.sleep(0.5)

if __name__ == '__main__':
    main()
