import zipfile
import pathlib

def compress(filepaths, dest_folder, compressed_file_name):
    dest_f_path = pathlib.Path(dest_folder, compressed_file_name+".zip")
    with zipfile.ZipFile(dest_f_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)

if __name__ == "__main__":
    compress(filepaths=["habijabi1.txt","junk.txt"], dest_folder="bonus16",
              compressed_file_name=input("Enter zip file name: "))

