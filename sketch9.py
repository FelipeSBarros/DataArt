import py5
def setup():
    py5.size(980, 980)
    py5.background(50)
    cols = 10
    rows = 10
    for row in range(rows):
        for col in range(cols):
            py5.arc(80 + (col*100), 80*(row+1), (row*3)+50, (row*3)+50, 0, (2 * py5.PI) / (col+1))

# py5.run_sketch()
py5.save_frame(filename="sketch9.png")