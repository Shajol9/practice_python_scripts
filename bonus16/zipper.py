import FreeSimpleGUI as fsg
import zippper_backend

lable1 = fsg.Text("Choose files to zip/compress")
input_file_path_1 = fsg.Input()
choose_file_1 = fsg.FilesBrowse("Choose", key="filepaths")

lable2 = fsg.Text("Choose destination folder to store the zip file")
input_file_path_2 = fsg.Input()
choose_file_2 = fsg.FolderBrowse("Choose", key="folder")

lable3 = fsg.Text("Entalr a name for the zip file")
zip_file_name = fsg.Input(key="zip_name")

zip_compress = fsg.Button("ZIP/Compress")
output_lable = fsg.Text(key="output")

window = fsg.Window("ZIP/Compress Files", 
                    layout=[[lable1, input_file_path_1, choose_file_1],
                            [lable2, input_file_path_2, choose_file_2],
                            [lable3, zip_file_name],
                            [zip_compress, output_lable]])

while True:
    event, values = window.read()
    if event == fsg.WIN_CLOSED:
        break
    if values["filepaths"]:
        file_paths = values["filepaths"].split(";")
        folder_path = values["folder"]
        zf_name = values["zip_name"]
        zippper_backend.compress(filepaths=file_paths, dest_folder=folder_path, 
                                 compressed_file_name=zf_name)
        window["output"].update(value="Files compressed successfully!")
        window["zip_name"].update(value="")
    else:
        window["output"].update(value="No files selected for compression. Please select a file.")

window.close()