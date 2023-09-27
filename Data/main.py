import pandas as pd
import numpy as np

trips = pd.read_csv('trips.txt')

del trips['service_id']
del trips['trip_headsign']
del trips['direction_id']
del trips['block_id']


trips.to_csv('newData\\new_trips.csv', index=False, header=True)

