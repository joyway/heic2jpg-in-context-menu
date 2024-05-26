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
for file in sys.argv[1:]:
    if os.path.splitext(file)[1].upper() == '.HEIC':
        heic_list.append(file)

if not heic_list:
    ctypes.windll.user32.MessageBoxW(0, 'No HEIC files selected.', title, 0)
    os._exit(1)

for heic in heic_list:
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

ctypes.windll.user32.MessageBoxW(0, f'{len(heic_list)} files converted successfully.', title, 0)
