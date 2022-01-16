def temperatureConveter(C = 0, F = 0):
    "Automatic temperature conveter based on passed argument input"
    celciusToFarenheit = lambda C: (C * 9/5) + 32
    farenheitToCelcius = lambda F: (F - 32) * 5/9

    if F > 0:
        return f"Temperature {F} Farenheit Equal To {farenheitToCelcius(F)} Celcius"
    else:
        return f"Temperature {C} Celcius Equal To {celciusToFarenheit(C)} Farenheit"

print(temperatureConveter(C = 40))
print(temperatureConveter(F = 95))
print(temperatureConveter(30))
print(temperatureConveter())
