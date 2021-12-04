import os, shutil, mimetypes

def get_extensions_for_type(general_type):
    for ext in mimetypes.types_map:
        if mimetypes.types_map[ext].split('/')[0] == general_type:
            yield ext
additional_extensions = {
    'text' : ['.docx', '.pdf'],
    'video' : ['.mkv'],
    'audio':[],
    'image': ['.webp']
    }
source_folder = os.getcwd() + "/"
files = os.listdir(source_folder)

def folder_handler(new_list, type):  
    print(type, new_list) 
    for file in files:
        name, ext = os.path.splitext(file)
        if not os.path.exists(".//" + type):
            os.makedirs("./" + type)
        source = source_folder + file
        destination = source_folder + type + "/" + file
        if ext in new_list and ext != '.py':
            try:
                shutil.move(source, destination)
                print(f"")
            except Exception as e:
                print(e)
types = ['video', 'audio', 'image', 'text']
for type in types:
    try:
        new_list = (list(get_extensions_for_type(type))+additional_extensions[type])
        folder_handler(new_list, type)
    except Exception as e:
        print()