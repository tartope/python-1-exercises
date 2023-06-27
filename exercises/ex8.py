def c_to_f(input):
    fahrenheit = (input * 9//5) + 32
    return f"{input} Celsius is {fahrenheit} degrees Fahrenheit"


def f_to_c(input):
    celcius = (input -32) * 5//9
    return f"{input} Fahrenheit is {celcius} degrees Celsius."