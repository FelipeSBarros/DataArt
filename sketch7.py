import py5
import pandas as pd

data = pd.read_csv("data/Posadas_2023_daily_wheatherdata.csv")


def setup():
    py5.size(600, 600)
    py5.background(255)
    for i, vals in data[0:25].iterrows():
        x = py5.random_int(600)
        y = py5.random_int(600)
        r = py5.random_int(255)
        g = py5.random_int(255)
        b = py5.random_int(255)
        py5.fill(r, g, b)
        py5.no_stroke()
        py5.ellipse_mode(py5.CENTER)
        py5.circle(x, y + 50, vals["wspd"] * 5)
        wind_dir = py5.radians(vals["wdir"])
        py5.no_fill()
        py5.stroke(0)
        py5.arc(x, y + 50, 70, vals["wspd"] * 2, 0, wind_dir)
        py5.text_size(15)
        py5.fill(10)


# py5.run_sketch()
py5.save_frame(filename="./data/sketch7_Posadas_wind_spd_dir_2023.png")
