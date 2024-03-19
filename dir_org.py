import os, shutil

current_dir = os.getcwd()

directories = ['Text files','Document files','Image files','Video files','Audio files','Other files']
for directory in directories:
    dir_path = os.path.join(current_dir, directory)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


for f in os.listdir(current_dir):
    filename, file_ext = os.path.splitext(f)
    # print(filename, file_ext)

    try:
        if not file_ext:
            pass

        elif file_ext in ('.py', '.txt', '.c', '.cpp' , '.js'):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Text files', f'{filename}{file_ext}'))
            
        elif file_ext in ('.pdf', '.docx', '.pptx', '.xlsx', '.xls', '.xlsm', '.xltx'):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Document files', f'{filename}{file_ext}'))
            
        elif file_ext in ('.jpg', '.png', '.heic', '.gif', '.jpeg'):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Image files', f'{filename}{file_ext}'))
            
        elif file_ext in ('.avi', '.mp4', '.avi', '.mkv', '.mov', '.mp4v',):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Video files', f'{filename}{file_ext}'))
            
        elif file_ext in ('.wav', '.mp3' ,'.opus', '.aac', '.aif'):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Audio files', f'{filename}{file_ext}'))
        else:
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Other files', f'{filename}{file_ext}'))


    except (FileNotFoundError, PermissionError):
        pass        

for directory in directories:
    dir_path = os.path.join(current_dir, directory)
    if not os.listdir(dir_path):
        os.rmdir(dir_path)
