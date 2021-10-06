def get_in(arg):
    return float(input(arg))


def ly_to_miles(arg):
    x = 5.88
    y = (10 ** 12)
    z = x * y
    return arg * z

def ly_to_km(arg):
    x = 9.46
    y = (10**12)
    z = x*y
    return arg*z

def main():
    light_years = get_in("light years:")
    miles = ly_to_miles(light_years)
    km = ly_to_km(light_years)
    print(str(miles) + " miles")
    print(str(km) + "kilometers")


main()
