def conv_f_to_c(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return round(celsius)

fahrenheit_values = [212, 90, 72, 32, 0, -40]

for temp_f in fahrenheit_values:
    temp_c = conv_f_to_c(temp_f)
    print(f"{temp_f}°F is approximately {temp_c}°C")

print()

def conv_c_to_f(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return round(fahrenheit)

celsius_values = [100, 45, 19, 0, -7, -40]

for temp_c in celsius_values:
    temp_f = conv_c_to_f(temp_c)
    print(f"{temp_c}°C is approximately {temp_f}°F")