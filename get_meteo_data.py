from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Daily
# Import Meteostat library
from meteostat import Stations

# Get nearby weather stations
stations = Stations()
stations = stations.nearby(-27.392457, -55.969035)
stations = stations.fetch(1)
# Set time period
start = datetime(2023, 1, 1)
end = datetime(2023, 12, 31)

# Get daily data
data = Daily(stations, start, end)
data = data.fetch()
data.columns

data.to_csv('data/Posadas_2023_daily_wheatherdata.csv')
# Plot line chart including average, minimum and maximum temperature
data.plot(y=['tavg', 'tmin', 'tmax'])
plt.show()