import py5

def setup():
    py5.size(800, 800)
    py5.rect_mode(py5.CENTER)
    py5.background('#5A5A5A')

def draw():
    # retangulo
    py5.fill(255)
    py5.rect(800/2, 800/2, 200, 200)

    for n in range(int(0/2), 800, 5):
        # print(n)
        py5.line(400, 400, 0, n)



# py5.run_sketch()
py5.save_frame(filename="sketch2.png")