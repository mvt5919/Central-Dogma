import pyowm
owm = pyowm.OWM('2e98671aef6d8c2afd8fa291d2192f2e')
observation = owm.weather_at_place('Lafayette,us')
w = observation.get_weather()
print(w)

print(w.get_wind())
print(w.get_humidity())
print(w.get_temperature('fahrenheit'))