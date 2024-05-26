# HEIC to JPG
Scripts to convert HEIC files to JPG

## Requirement
- I've only tested it under Windows 11, but it should work on Windows 7+
- Python >=3.8
- Python module `pillow-heif` https://github.com/bigcat88/pillow_heif/

## Install
1. Download both `context_menu_win.py` and `Convert HEIC to JPG.cmd` files in this repo and save them together anywhere you like on your PC
2. Press Win + R, then enter "shell:SendTo" to open the SendTo folder
3. Create a shortcut in the SendTo folder, point it to the `Convert HEIC to JPG.cmd` file you saved on your PC, name the shortcut anything you like

> If you don't want to see the terminal window popup every time you run the script, you can right click on the shortcut you created, choose "Properties", in the dropdown menu of "Run", select "Minimised", then click "OK"


# Usage
1. Select HEIC files in the Windows Explorer
2. Right click then "Send To" -> [The Shortcut You Created], for Windows 11 you may need to click "Show more options" to see the "Send To" option
3. A dialog will show up once the conversion is complete
4. The JPG files will be saved at the same folder of the original HEIC files
