import py5


def semi_leaf(x, y, r, start, end):
    py5.stroke_weight(3)
    py5.arc(x, y, r, r, 0, py5.PI / 2)
    py5.arc(x + r, y, r, r, 0 + py5.PI, end + py5.PI)

def setup():
    py5.size(600, 600)
    # py5.background("#004477")
    py5.no_fill()
    py5.stroke("#FFFFFF")

    for i in range(0, int(py5.PI), 1):
        for z in range(0, 180, 90):
            for x in range(0, 600, 100):
                semi_leaf(x, x, 50, z, i)
                semi_leaf(x+50, x+50, 50, i, z)


py5.run_sketch()

# py5.save_frame(filename="sketch3.png")
