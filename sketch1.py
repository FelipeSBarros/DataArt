import py5

def setup():
    py5.size(1000, 1000)
    py5.rect_mode(py5.CENTER)
    py5.background('#5A5A5A')

def draw():
    # retangulo
    py5.fill('#FF0000')
    py5.rect(500, 500, 200, 500)
    # triangulo
    py5.fill('#FF7F00')
    py5.triangle(700, 525,  # First corner
             600, 950,  # Second corner
             750, 875)
    py5.no_fill()
    py5.stroke_weight(3)
    py5.stroke('#FFFFFF')
    py5.ellipse(700, 600, 300, 300)



# py5.run_sketch()
py5.save_frame(filename="sketch1.png")