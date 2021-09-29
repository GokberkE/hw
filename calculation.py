# This code has functions to calculate given miles and turn it
# into kilometers, meters and centimeters.


def get_miles():
    print("Please write a distance in terms of miles")
    miles = float(input())
    return miles


def calculate_kmeter(miles):
    kmeter = miles * 1.609344
    return kmeter


def calculate_meter(miles):
    meter = miles * 1609.34
    return meter


def calculate_cmeter(miles):
    cmeter = miles * 160934
    return cmeter

def main():
    miles = get_miles()
    kmeter = calculate_kmeter(miles)
    meter = calculate_meter(miles)
    cmeter = calculate_cmeter(miles)

def display_calculations(miles, kmeter, meter, cmeter):
    print("You typed " + str(miles) + " as miles!")
    print("Which means it is " + str(kmeter) + " in kilometers!")
    print("Also it means " + str(meter) + " in meters!")
    print("And finally, it means " + str(cmeter) + " in centimeters!")

    
main()
display_calculations(miles, kmeter, meter, cmeter)
