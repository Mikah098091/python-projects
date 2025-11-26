import os
import shutil

desktop = r"C:\Users\Mikah\Desktop"

file_extensions = {
    'pdf': 'PDFs',
    'png': 'Images',
    'jpg': 'Images',
    'jpeg': 'Images',
    'gif': 'Images',
    'doc': 'Documents',
    'docx': 'Documents',
    'txt': 'Documents',
    'csv': 'Data',
    'xlsx': 'Data',
    'zip': 'Archives',
    'rar': 'Archives',
    'exe': 'Executables',
    'mp3': 'Music',
    'wav': 'Music',
    'mp4': 'Videos',
    'avi': 'Videos',
    'flv': 'Videos',
    'wmv': 'Videos'
}


destinations = {}


entries = list(os.scandir(desktop))
i = 0
while i < len(entries):
    entry = entries[i]
    i += 1

    if entry.is_dir():
        continue


    parts = entry.name.rsplit('.', 1)
    if len(parts) == 2:
        ext = parts[1].lower()
    else:
        ext = ""

    folder_name = file_extensions.get(ext, "Others")


    if folder_name not in destinations:
        path = os.path.join(desktop, folder_name)
        os.makedirs(path, exist_ok=True)
        destinations[folder_name] = path

    target = os.path.join(destinations[folder_name], entry.name)


    shutil.move(entry.path, target)

