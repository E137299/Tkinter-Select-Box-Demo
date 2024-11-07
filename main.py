from tkinter import *

root = Tk()
root.title("Select Box Demo")
root.geometry("400x400")

''' MODEL '''
def on_click(event):
    global start_x, start_y
    start_x, start_y = event.x, event.y
    print(f"Start X: {start_x}\nStart Y: {start_y}")

def on_drag(event):
    global start_x, start_y, rect
    canvas.delete(rect)  # Delete the previous rectangle
    rect = canvas.create_rectangle(start_x, start_y, event.x, event.y, outline = "white", dash = (5,5))
    print(f"Start X: {start_x}\nStart Y: {start_y}\nEnd X: {event.x}\nEnd Y: {event.y}")

rect = None
start_x, start_y = 0, 0
end_x, end_y = 0,0

''' CONTROLLER '''

''' VIEW '''
canvas = Canvas(root, bg = "purple", width=400, height=400)
canvas.pack()

canvas.bind("<Button-1>", on_click)
canvas.bind("<B1-Motion>", on_drag)

root.mainloop()
