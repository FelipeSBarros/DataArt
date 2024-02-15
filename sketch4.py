import py5


def semi_leaf(x, y, r, end):
    if int(py5.random()) == 1:
        py5.stroke_weight(3)
        py5.arc(x, y, r, r, 0, py5.PI / 2)
        py5.arc(x + r, y, r, r, 0 + py5.PI, end + py5.PI)
    else:
        py5.stroke_weight(r / 20)
        py5.arc(x, y, r, r, 0, py5.PI / 2)
        py5.arc(x, y + r, r, r, 0 + py5.PI, end + py5.PI)


def setup():
    py5.size(600, 600)
    py5.background("#004477")
    py5.no_fill()
    py5.stroke("#FFFFFF")

    for i in range(150, 450, 50):
        semi_leaf(i, i, 50, py5.PI / 2)
        semi_leaf(i + 10, i, 50, py5.PI / 2)
        semi_leaf(i + 100, i, 50, py5.PI / 2)
        semi_leaf(i + 110, i, 50, py5.PI / 2)


# py5.run_sketch()

py5.save_frame(filename="sketch3.png")
