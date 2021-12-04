import os, shutil, mimetypes


current_directory = os.getcwd()
files = os.listdir(current_directory)
file_types = ["audio", "image", "text", "video"]
additional_extensions = {
    "audio": [],
    "image": [".webp"],
    "text": [".docx", ".pdf"],
    "video": [".mkv"],
}


def get_extensions_for_type(general_type):
    for extension in mimetypes.types_map:
        if mimetypes.types_map[extension].split("/")[0] == general_type:
            yield extension


def folder_handler(extensions_list, file_type):
    for file in files:
        name, ext = os.path.splitext(file)
        if not os.path.exists(f"./{file_type}"):
            os.makedirs(f"./{file_type}")
        source = f"{current_directory}/{file}"
        destination = f"{current_directory}/{file_type}/{file}"
        if ext in extensions_list and ext != ".py":
            try:
                shutil.move(source, destination)
            except Exception as e:
                print(e)


def main():
    for file_type in file_types:
        try:
            extensions_list = (
                list(get_extensions_for_type(file_type))
                + additional_extensions[file_type]
            )
            folder_handler(extensions_list, file_type)
        except Exception as e:
            print(e)


main()
