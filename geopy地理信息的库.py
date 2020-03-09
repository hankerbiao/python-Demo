"""
geopy 关于地理位置的库
经纬度转换为详细地址
"""
from geopy.geocoders import Nominatim
address = 39.,117.
geolocator = Nominatim()
location = geolocator.reverse(address,timeout=15)
print(location)