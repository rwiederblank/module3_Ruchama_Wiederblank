
# Turtle Logic Lab
import turtle as T
# ----------------------------------------
# TODO 1: Setup
# - Define allowed shapes: square, triangle, circle
# - Define allowed colors: red, green, blue
# ----------------------------------------
shapes = ["square", "triangle" , "circle"]
colors = ['red', 'green', 'blue']
# ----------------------------------------
# TODO 2: User Input (function)
# - Ask user for shape choice
# - Ask user for color choice
# - Ask user if they want the shape filled (y/n)
# - If shape not valid OR color not valid → raise ValueError
# - Catch ValueError → print error, return defaults (triangle, blue, y)
# - Return all three values
# ----------------------------------------
def user_input():
    # TODO: write try/except structure
    try:
        shape_choice = input("what shape?: triangle/circle/square").strip().lower()
        color_choice = input("what color?: red/green/blue").strip().lower()
        fill_choice = input("Fill y/n?").strip().lower()

        if shape_choice  not in shapes or color_choice not in colors:
            raise ValueError
        return shape_choice, color_choice, fill_choice
    except ValueError:
        print(f'there is a value problem')
        return('triangle', 'blue', 'yes')
    # TODO: collect shape, color, and fill choice
    # TODO: check if shape in shapes AND color in colors
    # TODO: raise ValueError if invalid
    # TODO: return values (shape, color, fill)
   

# ----------------------------------------
# TODO 3: Select Color (function)
# - If color is red → set turtle color red
# - Else if green → set turtle color green
# - Else → set turtle color blue
# ----------------------------------------
def select_color(color_choice="blue"):
    # TODO: implement if/elif/else logic for colors
    T.color(color_choice)

pass
# ----------------------------------------
# TODO 4: Draw Shape (function)
# - If fill choice is NOT 'n' → begin_fill
# - If shape is circle → draw circle
# - Else if square → draw square (use forward + right turns)
# - Else → draw triangle
# - If fill choice is NOT 'n' → end_fill
# ----------------------------------------
def draw_shape(shape_choice="triangle", size=120, fill_choice="y"):

    # TODO: use if/elif/else to select correct shape
    # TODO: add begin_fill() and end_fill() around shape if needed
    if fill_choice == "y":
        T.begin_fill()
    if shape_choice == "circle":
        T.circle(size)
    elif shape_choice == "square":
        T.forward(size)
        T.right(90)
        T.forward(size)
        T.right(90)
        T.forward(size)
        T.right(90)
        T.forward(size)
        T.right(90)
    else:
        T.forward(size)
        T.right(120)
        T.forward(size)
        T.right(120)
        T.forward(size)
        T.right(120)
    if fill_choice == "y":
        T.end_fill()
        

# ----------------------------------------
# TODO 5: Main Program
# - Call user_input() → get shape, color, fill
# - Call select_color() with chosen color
# - Special AND rule:
# if shape is square AND color is red → set pencolor black
# - Call draw_shape() with chosen values
# - Finish with T.done()
# ----------------------------------------
if __name__ == "__main__":
    T.shape("turtle")
    # TODO: set pen width
    T.width(5)
    # TODO: call user_input() and unpack shape, color, fill
    shape_choice, color_choice, fill_choice = user_input()    
    # TODO: call select_color()
    select_color(color_choice)
    # TODO: implement AND condition (square AND red → black outline)
    if shape_choice == "square" and color_choice == "red":
        T.pencolor("black")

    # TODO: call draw_shape()
    draw_shape(shape_choice, 120, fill_choice)
    T.color("black")
    # TODO: finish with T.done()
    T.done()

# ----------------------------------------
# TODO 6: Optional Extensions
# - If shape is circle OR triangle → move turtle and draw a dot
# - If color is green AND fill is y → write "Go Green!"
# ----------------------------------------
# (students can implement this after the main program work
