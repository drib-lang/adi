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


def imwrite(pixels: list[list[list[int]]], filename: str):
    height = len(pixels)
    width = len(pixels[0])

    root = tk.Tk()
    root.withdraw()

    img = tk.PhotoImage(width=width, height=height)

    for y, row in enumerate(pixels):
        color_row = (
            "{"
            + " ".join(f"#{int(r):02x}{int(g):02x}{int(b):02x}" for (r, g, b) in row)
            + "}"
        )
        img.put(color_row, to=(0, y))

    fmt = filename.split(".")[-1]  # supposing the user does not enter a weird value
    img.write(filename, format=fmt)
