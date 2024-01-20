import pandas as pd 
from geopy.geocoders import Nominatim

file = pd.read_csv("./uber_data.csv")
# print(file.head)
# for col in file.columns:
    # print(col)
sum = 0.0
for val in file['total_amount']:
    sum += val
print("total revenue : ", sum) #$1639072.0900016439
#75.057487 lat : 21.035400

# Initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")

lon = 75.057487 
lat = 21.035400

location = geolocator.geocode(str(lat)+","+ str(lon))
print(location)