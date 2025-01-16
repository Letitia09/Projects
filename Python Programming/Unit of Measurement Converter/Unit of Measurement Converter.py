# Project 1 : Unit of Measurement Converter
# Name : Anshu Pulipati
# Major : Computer Science
# UnitConverters website for reference : https://www.unitconverters.net/

#BASIC INFORMATION
'''
   1 foot = 12 inches
   1 yard = 3 feet
   1 yard = 36 inches
'''


class ConvertUnits:
    def __init__(self,cf,ct):
        self.convert_from = cf
        self.convert_to = ct

    def converter(self) -> None:
        if convert_from.lower() in ['inches', 'in', 'inch']:
            number_of_inches = int(input("Enter Starting Measurement in inches: "))
            if convert_to.lower() in ['feet', 'foot', 'ft']:
                print(f"Result: {number_of_inches} Inches = {round(number_of_inches / 12, 2)} Feet")
            elif convert_to.lower() in ['yards', 'yard', 'yd']:
                print(f"Result: {number_of_inches} Inches = {round(number_of_inches / 36, 2)} Yards")
            else:
                print("Your input was incorrect")
        elif convert_from.lower() in ['feet', 'foot', 'ft']:
            number_of_feet = int(input("Enter Starting Measurement in feet: "))
            if convert_to.lower() in ['inches', 'in', 'inch']:
                print(f"Result: {number_of_feet} Feet = {round(number_of_feet * 12)} Inches")
            elif convert_to.lower() in ['yards', 'yard', 'yd']:
                print(f"Result: {number_of_feet} Feet = {round(number_of_feet / 3, 2)} Yards")
            else:
                print("Your input was incorrect")
        elif convert_from.lower() in ['yards', 'yard', 'yd']:
            number_of_yards = int(input("Enter Starting Measurement in yards: "))
            if convert_to.lower() in ['inches', 'in', 'inch']:
                print(f"Result: {number_of_yards} Yards = {round(number_of_yards * 36)} Inches")
            elif convert_to.lower() in ['feet', 'foot', 'ft']:
                print(f"Result: {number_of_yards} Yards = {round(number_of_yards * 3)} Feet")
            else:
                print("Your input was incorrect")
        else:
            print("Please enter either Feet, Inches or Yards")


convert_from = input("Enter Starting Unit of Measurement(inches, feet, yards): ")
convert_to = input("Enter Unit of Measurement to Convert to (inches, feet, yards): ")

unit_obj = ConvertUnits(convert_from,convert_to)
unit_obj.converter()



