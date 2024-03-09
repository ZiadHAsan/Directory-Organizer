import os
import argparse

parser = argparse.ArgumentParser(
    description= "make folders differently and put the file type in it"
)

parser.add_argument(
    "--path",
    type=str,
    default=".",
    help="path of the to be cleaned directory",
)

args = parser.parse_args()
path = args.path

print(f"cleaning up the directory {path}")

#getting the files of the given directory
dir_content = os.listdir(path)

#create a relative path form the path and the document name
path_dir_content = [os.path.join(path, doc) for doc in dir_content]

#filter the contents into a doc and folder list
docs = [doc for doc in path_dir_content if os.path.isfile(doc)]
folders = [folder for folder in path_dir_content if os.path.isdir(folder)]

#for keeping track
moved = 0
created_folders = []

print(f"cleaning up {len(docs)} of {len(dir_content)} elements")

# go through all files and move them into according folders
for doc in docs:
    # separte name from file extension
    full_doc_path, filetype = os.path.splitext(doc)
    doc_path = os.path.dirname(full_doc_path)
    doc_name = os.path.basename(full_doc_path)
    
    

    print(filetype)
    print(full_doc_path)
    print(doc_path)
    print(doc_name)

    if doc_name == "folder_clean" or doc_name.startswith('.'):
        continue

    subfolder_path = os.path.join(path, filetype[1:].lower())
          
    if subfolder_path not in folders and subfolder_path not in created_folders:
        try:
            os.mkdir(subfolder_path)
            created_folders.append(subfolder_path)
            print(f"Folder {subfolder_path} created.")
        except FileExistsError as err:
            print(f"Folder already exists at {subfolder_path}... {err}")

    new_doc_path = os.path.join(subfolder_path, doc_name) + filetype
    os.rename(doc, new_doc_path)
    moved += 1
        
    print(f"Moved file {doc} to {new_doc_path}")
        