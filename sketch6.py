import py5
import pandas as pd

data = pd.read_csv("data/Posadas_2023_daily_wheatherdata.csv")


def setup():
    py5.size(600, 600)
    py5.background(255)
    for x in range(100, 500, 33):
        for l in data["prcp"]:
            print(l)
            py5.line(x, 300, x + l, x + l)

    py5.text_size(15)
    py5.fill(10)
    py5.text("Posadas' precipitation in 2023", 250, 550)
    py5.fill(100)
    py5.text("#DataArt", 300, 570)


# data.prcp
py5.run_sketch()
py5.save_frame(filename="sketch6_Posadas_prcp_2023.png")
