
from tkinter import *

def main():
    canvas_width = 600
    canvas_height = 600

    window = Tk() 
    window.title("Cool Circle Shape") 
    geometry_string = str(canvas_width)+"x"+str(canvas_height)+"+10+20"
    window.geometry(geometry_string)

    a_canvas = Canvas(window)
    a_canvas.config(background="misty rose")
    a_canvas.pack(fill=BOTH, expand = True) #Canvas fills the whole top level window

    centre_x = 300
    centre_y = 300
    radius = 250

    circle_pts = get_list_of_tuples_from_file("CircumferencePoints.txt")
    draw_outer_circle(a_canvas, centre_x, centre_y, radius)
    draw_cardioid_connections(a_canvas, circle_pts)

    window.mainloop()

def get_list_of_tuples_from_file(filename):
    in_file = open(filename, "r")
    contents = in_file.read()
    in_file.close()
    numbers_list = contents.split()
    tuple_list = []
    index = 0
    while index < (len(numbers_list) - 1):
        tuple_list.append((numbers_list[index], numbers_list[index + 1]))
        index += 2
    return tuple_list

def draw_outer_circle(a_canvas, centre_x, centre_y, radius):
    colour = "medium purple"
    a_canvas.create_oval(centre_x - radius, centre_y - radius, centre_x + radius, centre_y + radius, outline = colour)

def draw_cardioid_connections(a_canvas, points_on_circumference):
    colour = "medium orchid"
    for i in range(len(points_on_circumference) - 1):
        end_point_index = (i + 1) * 2 % len(points_on_circumference) - 1
        a_canvas.create_line(points_on_circumference[i], points_on_circumference[end_point_index], fill = colour)

main()

