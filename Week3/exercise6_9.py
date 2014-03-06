# Conversions between feet and meters
# Author: Brian Hamburg

def main():
    print(format("Feet", "<15s"), format("Meters", "<15s"), "  |    ", format("Meters", "<15s"), format("Feet", "<15s")) 
    print()

    #define starting variables
    feet = 1
    meters = 20
    i = 1
    while i <= 10:
        print(format(feet, "<15.1f"), format(footToMeter(feet), "<15.3f"), "  |    ", 
              format(meters, "<15.1f"), format(meterToFoot(meters), "<15.3f"))
        feet += 1
        #special meter list counter
        if meters % 10 == 0:
            meters += 6
        elif meters % 10 == 6:
            meters += 4
        i += 1
    
# Converts Feet to Meters
def footToMeter(feet):
    meters = 0.305 * feet 
    return meters

# Converts Meters to Feet
def meterToFoot(meters):
    feet = meters / 0.305
    return feet

main()
