import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()
root.title("Image Background")

    # Load the image
image_path = "C:\Masters\sem-4\ASE\Project\EmployeeAttendanceSystem\qr.png"  # Replace with the path to your image
image = PhotoImage(file=image_path)

    # Get image dimensions
width, height = image.width(), image.height()

    # Set the window size to match the image size
root.geometry(f"{width}x{height}")

    # Create a Canvas widget and pack it to fill the window
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()

    # Display the image as a background
canvas.create_image(0, 0, anchor=tk.NW, image=image)

    # Your other GUI elements or logic can go here

root.mainloop()