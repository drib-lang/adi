import tkinter as tk


def imread(filename: str):
    root = tk.Tk()
    root.withdraw()
    img = tk.PhotoImage(file=filename)

    width = img.width()
    height = img.height()

    pixels = [
        [[str(c) for c in img.get(x, y)] for x in range(width)] for y in range(height)
    ]
    root.destroy()

    return pixels


def imwrite(img: list[list[list[int]]], filename: str):
    fmt = filename.split(".")[1]
    img.write(filename, format=fmt)
