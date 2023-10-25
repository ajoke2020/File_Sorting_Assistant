import os, shutil

# Define the source directory path
path = r"C:/Users/USER/Desktop/"

# Get a list of all file names in the source directory
file_names = os.listdir(path)

# Define the names of the target folders
folder_names = ['csv_files', 'image_files', 'text_files', 'short_cuts', 'audio_files', 'ini_files', 'links', 'python_files', 'markdown_files', 'html_files', 'pdf_files']

# Create the target folders if they don't exist
for folder_name in folder_names:
    folder_path = os.path.join(path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Iterate through the files in the source directory
for file in file_names:
    # Move CSV files to the 'csv_files' folder
    if '.csv' in file and not os.path.exists(os.path.join(path, 'csv_files', file)):
        shutil.move(os.path.join(path, file), os.path.join(path, 'csv_files', file))
    # Move MP3 files to the 'audio_files' folder
    elif '.mp3' in file and not os.path.exists(os.path.join(path, 'audio_files', file)):
        shutil.move(os.path.join(path, file), os.path.join(path, 'audio_files', file))
    # Move DOCX files to the 'text_files' folder
    elif '.docx' in file and not os.path.exists(os.path.join(path, 'text_files', file)):
        shutil.move(os.path.join(path, file), os.path.join(path, 'text_files', file))
    # Move INI files to the 'ini_files' folder
    elif '.ini' in file and not os.path.exists(os.path.join(path, 'ini_files', file)):
        shutil.move(os.path.join(path, file), os.path.join(path, 'ini_files', file))
    # Move shortcut (LNK) files to the 'links' folder
    elif '.lnk' in file:
        source_file_path = os.path.join(path, file)
        destination_file_path = os.path.join(path, 'links', file)
        if not os.path.exists(destination_file_path):
            try:
                shutil.move(source_file_path, destination_file_path)
                print(f"Moved '{file}' to the 'links' folder.")
            except Exception as e:
                print(f"Error moving '{file}': {e}")
        else:
            print(f"'{file}' already exists in the 'links' folder.")
    # Move Python (PY) files to the 'python_files' folder
    elif '.py' in file and not os.path.exists(os.path.join(path, 'python_files', file)):
        shutil.move(os.path.join(path, file), os.path.join(path, 'python_files', file))
    # Move PNG files to the 'image_files' folder
    elif '.png' in file and not os.path.exists(os.path.join(path, 'image_files', file)):
        shutil.move(os.path.join(path, file), os.path.join(path, 'image_files', file))
    # Move R Markdown (RMD) files to the 'markdown_files' folder
    elif '.rmd' in file and not os.path exists(os.path.join(path, 'markdown_files', file)):
        shutil.move(os.path.join(path, file), os.path.join(path, 'markdown_files', file))
    # Move HTML files to the 'html_files' folder
    elif '.html' in file and not os.path.exists(os.path.join(path, 'html_files', file)):
        shutil.move(os.path.join(path, file), os.path.join(path, 'html_files', file))
    # Move PDF files to the 'pdf_files' folder
    elif '.pdf' in file and not os.path.exists(os.path.join(path, 'pdf_files', file)):
        shutil.move(os.path.join(path, file), os.path.join(path, 'pdf_files', file))
    # Move TXT files to the 'text_files' folder
    elif '.txt' in file and not os.path.exists(os.path.join(path, 'text_files', file)):
        shutil.move(os.path.join(path, file), os.path.join(path, 'text_files', file))
