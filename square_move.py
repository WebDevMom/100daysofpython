from graphics import Canvas

SQUARE_SIZE = 50
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500


def main():
    # makes a canvas
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # set y coordinates
    start_y = CANVAS_HEIGHT / 2 - SQUARE_SIZE / 2
    end_y = start_y + SQUARE_SIZE

    # draw the square
    canvas.create_rectangle(0, start_y, SQUARE_SIZE, end_y, "blue")


if __name__ == "__main__":
    main()
