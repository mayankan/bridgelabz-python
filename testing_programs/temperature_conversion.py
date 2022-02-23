class Util:
    @staticmethod
    def temperature_conversion(unit):
        """
        Converts Temperature from Celsius to Fahrenheit and Fahrenheit to Celsius.
        :param unit: Unit provided by user to take the temperature.
        :return: Both Initial Temperature and Converted Temperature values.
        """
        # Conversion from Celsius to Fahrenheit
        if unit == 'C' or unit == 'c':
            temperature = float(input("Enter temperature in Celsius: "))
            print("Conversion from Celsius to Fahrenheit:")
            fahrenheit = (temperature * (9 / 5)) + 32
            return temperature, fahrenheit

        # Conversion from Fahrenheit to Celsius
        elif unit == 'F' or unit == 'f':
            temperature = float(input("Enter temperature in Fahrenheit: "))
            print("Conversion from Fahrenheit to Celsius:")
            celsius = (temperature - 32) * (5 / 9)
            return temperature, celsius


def main():
    try:
        unit = 'a'
        while (unit != 'C' and unit != 'c') and (unit != 'F' and unit != 'f'):
            print("Choose the unit of temperature as input")
            unit = str(input("(Press 'c' for Celsius or 'f' for Fahrenheit): "))
        temperature_instance = Util()
        temperature, converted_temperature = temperature_instance.temperature_conversion(unit)
        if unit == 'C' or unit == 'c':
            print("{} Celsius = {} Fahrenheit".format(temperature, converted_temperature))
        elif unit == 'F' or unit == 'f':
            print("{} Fahrenheit = {} Celsius".format(temperature, converted_temperature))
    except Exception as e:
        print("{} is raised.".format(str(e)))


if __name__ == "__main__":
    main()
