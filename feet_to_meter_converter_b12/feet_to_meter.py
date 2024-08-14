from parsers import parse
import converter

hight = input("Enter the hight in feet and inches\nProcess: feet space inches: ")

parsed_hight = parse(hight)

hight_in_meter = converter.feet_to_miter(parsed_hight["feet"], parsed_hight["inches"])

print(f"Your hight in meter scale is: {hight_in_meter} meters")

if hight_in_meter > 1.5:
    print("Congrats! You are illigible to take part in the compitision.")
else:
    print("Sorry you felt short!")