# Requirements
# Walk the file system looking at files, directories, and sub-directories
# capture file info (file/directory?, size, path)
# Store info in a suitable data structure
# report sorted data: largest files

import os
file_size = {}
for root, directories, files in os.walk('.'):
    for _file in files:
        full_path = os.path.join(root, _file)
        size = os.path.getsize(full_path)
        file_size[size] = full_path
items_shown = 0
for size, path in sorted(file_size.items(), key=lambda x:x[0], reverse=True):
     if items_shown > 4:
         break
     print(f'size: {size} path: {path}')
     items_shown +=1
