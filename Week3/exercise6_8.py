# Conversions between Celsius and Fahrenheit
# Author: Brian Hamburg

def main():
    print(format("Celsius", "<15s"), format("Fahrenheit", "<15s"), "  |    ", format("Fahrenheit", "<15s"), format("Celsius", "<15s")) 
    print()

    #define starting variables
    c = 40
    f = 120
    i = 1
    while i <= 10:
        print(format(c, "<15d"), format(celsiusToFahrenheit(c), "<15.2f"), "  |    ", 
              format(f, "<15d"), format(fahrenheitToCelsius(f), "<15.2f"))
        c -= 1
        f -= 10
        i += 1

# Converts from Celsius to Fahrenheit 
def celsiusToFahrenheit(c):
    return (9.0 / 5.0) * c + 32

# Converts from Fahrenheit to Celsius 
def fahrenheitToCelsius(f):
    return (5.0 / 9) * (f - 32)

main()
