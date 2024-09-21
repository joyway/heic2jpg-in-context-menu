# Convert HEIC images to JPG in Windows Explorer context menu
# Author: Joyway
# Version: 1.0

import ctypes
import sys
import os
from PIL import Image
import pillow_heif


title = 'HEIC2JPG'
heic_list = []
fail_list = []
msg = ''
for file in sys.argv[1:]:
    if os.path.splitext(file)[1].upper() == '.HEIC':
        heic_list.append(file)

if not heic_list:
    ctypes.windll.user32.MessageBoxW(0, 'No HEIC files selected.', title, 0)
    os._exit(1)

success_count = 0
for heic in heic_list:
    try:
        heic_directory, heic_filename = os.path.split(os.path.realpath(heic))
        jpg_filename = f'{os.path.splitext(heic_filename)[0]}.jpg'
        heic_file = pillow_heif.read_heif(heic)
        image = Image.frombytes(
            heic_file.mode,
            heic_file.size,
            heic_file.data,
            "raw",
            )
        image.save(os.path.join(heic_directory, jpg_filename), format('jpeg'))
        success_count += 1
    except Exception as e:
        fail_list.append((heic_filename, str(e)))
        

msg += f'{success_count} files converted successfully.'

if fail_list:
    msg += f'\n\nFailed to convert follwing files:'
    for fail in fail_list:
        msg += f'\n - {fail[0]}: {fail[1]}'

ctypes.windll.user32.MessageBoxW(0, msg, title, 0)
