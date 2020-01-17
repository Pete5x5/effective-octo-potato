import sys      #Enable system functionality
import os       #Enable filesystem functionality
import shutil   #Enable file manipulation
from pathlib import Path        #Enable filesystem path joining
import pyautogui    #Enable clicking / keyboard input
import time     #for sleep
import csv      #for csv

mainpath = Path(r"C:\Users\Billing\Desktop\Spiffs")

invpath = mainpath/'invoices' #set invoice folder path
clickpath = mainpath/'clicks' #set invoice folder path
csvpath = mainpath/'spreadsheet'

spiffcsv = open(csvpath/'spiffcsv.csv') #open csv file of spiff info
spiffreader = csv.reader(spiffcsv)  #reader for csv file
spifflist = list(spiffreader)   #put csv info into a list

os.chdir(clickpath)

print ("\nPlease confirm the Panasonic Perks window is open, the tab is active, and user is logged in.")
print ("\nwhen you continue you will have 5 seconds to make the window active")
print ("\ny - continue")
while True:
        windowconfirm = input()
        if windowconfirm == 'y':  #List is OK, move on
            break

invlist = []
csvnum = 0

time.sleep(5)   #wait 5 seconds

# make a list of all filenames (should be 1.pdf, 2.pdf...)
for folderName, subfolders, filenames in os.walk(invpath):
    for filename in filenames:
        invlist += [filename]
        print(filename)

        pyautogui.click("0.png")  #click
        time.sleep(2)  #sleep for 3 seconds
        ## if unsuccessful type URL??
        pyautogui.click("1.png")  #click
        time.sleep(2)  #sleep for 3 seconds
        pyautogui.click("2.png")  #click
        time.sleep(2)  #sleep for 3 seconds
        pyautogui.click("3.png")  #click
        time.sleep(2)  #sleep for 3 seconds
        pyautogui.click("4.png")  #click
        time.sleep(2)  #sleep for 3 seconds
        pyautogui.write(filename)
        pyautogui.write(['enter'])
        time.sleep(15)  #sleep for 3 seconds
        pyautogui.write(['tab'])
        time.sleep(1)  #sleep for 1 second
        pyautogui.write(spifflist[csvnum][2])
        time.sleep(1)  #sleep for 1 second
        pyautogui.write(['tab'])
        time.sleep(1)  #sleep for 1 second
        pyautogui.write(spifflist[csvnum][1])
        time.sleep(1)  #sleep for 1 second
        # pyautogui.write(['enter'])
        # time.sleep(1)  #sleep for 1 second
        pyautogui.write(['tab'])
        time.sleep(1)  #sleep for 1 second
        pyautogui.write(spifflist[csvnum][0])
        time.sleep(1)  #sleep for 1 second
        pyautogui.write(['tab'])
        time.sleep(1)  #sleep for 1 second
        pyautogui.write(spifflist[csvnum][3])
        time.sleep(1)  #sleep for 1 second
        pyautogui.write(['tab'])
        time.sleep(1)  #sleep for 1 second
        pyautogui.write(['tab'])
        time.sleep(1)  #sleep for 1 second
        pyautogui.write(['enter'])
        time.sleep(2)  #sleep for 3 second
        csvnum += 1
        pyautogui.click("5.png")  #click
        time.sleep(8)  #sleep for 3 seconds

## if (error)
##     write error to log
## else
##     write success to log

## screenshot??
## log