import pandas as pd 
from geopy.geocoders import Nominatim
from datetime import datetime 
import matplotlib.pyplot as plt 

data = pd.read_csv("./uber_data.csv")
# print(data.head)
# for col in data.columns:
#     print(col)
sum = 0.0
for val in data['total_amount']:
    sum += val
print("total revenue : ", sum) #$1639072.0900016439
#75.057487 lat : 21.035400

# Initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")

lon = 75.057487 
lat = 21.035400

# location = geolocator.geocode(str(lat)+","+ str(lon))
# print(location)

#Filter non null tpep_pickup and dropoff times
df = data[data['tpep_pickup_datetime'] != 0]

#Filter using query function
# df = data.query("total_amount == 12.35")
# print(df)

#Filter using lambda
# print([df['VendorID'].isin([2])])
# df = data.apply(
#     lambda row: row[data['tpep_pickup_datetime'].isin([0])]
# )
# print(df)

#Calculate differece between dropoff time and pickup time
time_df = [df['tpep_dropoff_datetime']]
print(type(df['tpep_dropoff_datetime'][0]))
# df['tour_time'] = df.apply( lambda row: row[
#     datetime.strptime(df['tpep_dropoff_datetime'], '%Y-%m-%d %H:%M:%S') - datetime.strptime(df['tpep_pickup_datetime'], '%Y-%m-%d %H:%M:%S')]
# ], axis = 0
# )
#---------
# df['tour_time'] = df['tpep_dropoff_datetime'].apply(lambda row: row[datetime.strptime(str(df['tpep_dropoff_datetime']), '%Y-%m-%d %H:%M:%S')]) - \
    # df['tpep_pickup_datetime'].apply(lambda row: row[datetime.strptime(str(df['tpep_pickup_datetime']), '%Y-%m-%d %H:%M:%S')])

df['tout_time'] = df.apply(lambda row: (datetime.strptime(str(row.iloc[2]), '%Y-%m-%d %H:%M:%S') - \
                                        datetime.strptime(str(row.iloc[1]), '%Y-%m-%d %H:%M:%S') ).total_seconds()/60, axis = 1)
print(df['tout_time'].head)
df.plot(
    kind='scatter',
    x= 'trip_distance',
    y='tout_time',
    color='red'
)
plt.title('tour_time')
plt.show()
# df = pd.DataFrame()