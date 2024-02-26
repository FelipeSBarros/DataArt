import py5
import pandas as pd

data = pd.read_csv("data/Posadas_2023_daily_wheatherdata.csv")

min = data.wspd.min()
max = data.wspd.max()
rnge = max - min
data['wspdnorm'] = data.wspd.apply(lambda x: (x - min)/rnge*50)
data['wspdnorm'].max()
data['wspdnorm'].min()
def setup():
    py5.size(600, 600)
    py5.background(125)
    py5.stroke(0)
    coords = []
    for x in range(20, 590, 50):
        for y in range(20, 590, 50):
            py5.circle(x, y, 12)
            coords.append((x, y))
    py5.stroke(255)
    # for circle in py5.random_sample(coords, 10):
    for circle in coords:
        d = data.sample(ignore_index=True)
        py5.stroke_weight(3)
        if (d.iloc[0].wdir >= 0 and d.iloc[0].wdir <= 90):
            py5.line(circle[0], circle[1], circle[0] + d.iloc[0].wspdnorm, circle[1])
        if (d.iloc[0].wdir > 90 and d.iloc[0].wdir <= 180):
            py5.line(circle[0], circle[1], circle[0], circle[1] + d.iloc[0].wspdnorm)
        elif (d.iloc[0].wdir > 180 and d.iloc[0].wdir <= 270):
            py5.line(circle[0], circle[1], circle[0] - d.iloc[0].wspdnorm, circle[1])
        # elif d.wdir.between(90, 180):
        #     py5.line(circle[0], circle[1], circle[0] - 30, circle[1])


# py5.run_sketch()
py5.save_frame(filename="sketch8_Posadas_wdir_wdspdnorm_2023.png")
