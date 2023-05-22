from graphics import Canvas
import random

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
N_CIRCLES = 20

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    for i in range(N_CIRCLES):
        draw_one_random_circle(canvas)
        #draw a random circle
        
def draw_one_random_circle(canvas):
    left_x = random.randint(0, CANVAS_WIDTH - CIRCLE_SIZE)
    top_y = random.randint(0, CANVAS_HEIGHT - CIRCLE_SIZE)
    right_x = left_x + CIRCLE_SIZE
    bottom_y = top_y + CIRCLE_SIZE
    canvas.create_oval(left_x, top_y, right_x, bottom_y, random_color()) 
    
def random_color():
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    return random.choice(colors)
    
if __name__ == '__main__':
    main()
    