# INTRODUCTION
This repo is for personal use. It will track your activity by logging every second which one is your active element on your desktop. Later on with the file "analyze_tracker.py" you will know how long did you spend using what and make statistics about it

# INSTALLATION
## For Linux
- Download the project and unzip it
- Make the file 'window_tracker.sh' executable. Open a terminal and go to the project folder. Run <code>chmod +x window_tracker.sh<code>
- Install xdotool with <code>apt-get install xdotool</code>
- Add window_tracker to starup aplications:
    • Open the "Startup Applications" utility
    • Click on "Add"
    • Enter any name you want for the command
    • Enter the command to run the script (e.g., /path/to/window_tracker.sh)
    • Click on "Add"

## For Windows
- Download the project and unzip it
- Install  AutoIt v3, a freeware scripting program that uses a programming language similar to BASIC which can be downloaded at [Autoit v3](https://www.autoitscript.com/cgi-bin/getfile.pl?autoit3/autoit-v3-setup.zip)
- Right click on the file "window_tracker.au3" and select "compile 32bits". It created the file window_tracker.exe
- Add window_tracker to starup aplications:
    • Right-click on the shortcut of the file you want to add to startup and select "Copy"
    • Press the Windows logo key + R to open the Run dialog box
    • Type shell:startup in the Run dialog box and press Enter. This will open the Startup folder
    • Right-click inside the Startup folder and select "Paste" to paste the shortcut of your file into this folder
