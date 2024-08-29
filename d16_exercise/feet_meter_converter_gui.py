import FreeSimpleGUI as fsg

lable_feet = fsg.Text("Enter Feet")
input_box_feet = fsg.Input(tooltip = "Input size in feets")

lable_inches = fsg.Text("Enter Inches")
input_box_inches = fsg.Input(tooltip = "Input size in inches")

convert_button = fsg.Button("Convert")

window = fsg.Window('Feet to Meter Comverter', 
                    layout=[[lable_feet, input_box_feet], 
                            [lable_inches, input_box_inches],
                            [convert_button]])

window.read()
window.close()