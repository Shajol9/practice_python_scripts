import FreeSimpleGUI as fsg

lable1 = fsg.Text("Choose files to zip/compress")
input_file_path_1 = fsg.Input()
choose_file_1 = fsg.FileBrowse("Choose")

lable2 = fsg.Text("Choose files to zip/compress")
input_file_path_2 = fsg.Input()
choose_file_2 = fsg.FileBrowse("Choose")

zip_compress = fsg.Button("ZIP/Compress")

window = fsg.Window("ZIP/Compress Files", 
                    layout=[[lable1, input_file_path_1, choose_file_1],
                            [lable2, input_file_path_2, choose_file_2],
                            [zip_compress]])

window.read()
window.close()