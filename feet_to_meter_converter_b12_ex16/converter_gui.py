import FreeSimpleGUI as fsg
import converter 

lable1 = fsg.Text("Enter Feet")
input_feet = fsg.Input(key="feet", do_not_clear=False)

lable2 = fsg.Text("Enter Inches")
input_inchi = fsg.Input(key="inches", do_not_clear=False)

convert_button = fsg.Button("Convert", key="Convert")
output_txt = fsg.Text(key="output")

window = fsg.Window("Feet to Meeter Converter", 
                    layout= [[lable1, input_feet],
                             [lable2, input_inchi],
                             [convert_button, output_txt]])

while True:
    event, values = window.read()
    print (event, values)
    if event == fsg.WIN_CLOSED:
        break
    meter_value = converter.feet_to_meter(float(values["feet"]), float(values["inches"]))
    window["output"].update(value=f"{meter_value}m")
    # window["feet"].update(value="")
    # window["inches"].update(value="")

window.close()
