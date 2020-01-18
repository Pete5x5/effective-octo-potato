import sys      #Enable system functionality
import os       #Enable filesystem functionality
import shutil   #Enable file manipulation
from pathlib import Path        #Enable filesystem path joining
import pyautogui    #Enable clicking / keyboard input
import datetime #Enable date and time functionality
import time     #for sleep
import csv      #for csv

#LOGGING------
import logging

gendate = (datetime.datetime.now()).strftime('%Y%m%d-%H%M%S')

logging.basicConfig(filename='spifflog0' + gendate + '.txt', level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
#LOGGING------

while True:
    print ("""\nAre you using the billing PC or the laptop?
    B - Billing PC
    L - Laptop""")
    compconfirm = input()
    if compconfirm == 'B':  #Billing-PC, move on
        mainpath = Path(r"C:\Users\Billing\Desktop\Spiffs")
        break
    elif compconfirm == 'L':    #Laptop, move on
        mainpath = Path(r"C:\Users\Flippance\Desktop\Spiffs")
        break
    else:
        print ("\nInvalid entry.")  #invalid, repeat

invpath = mainpath/'invoices' #set invoice folder path
clickpath = mainpath/'clicks' #set invoice folder path
csvpath = mainpath/'spreadsheet'
screenpath = mainpath/('screenshots-' + compconfirm)

spiffcsv = open(csvpath/'spiffcsv.csv') #open csv file of spiff info
spiffreader = csv.reader(spiffcsv)  #reader for csv file
spifflist = list(spiffreader)   #put csv info into a list

os.chdir(clickpath) #change working directory to the clicks folder

while True:
    print ("""\nPlease confirm the Panasonic Perks window is open, the tab is active, and user is logged in.
    \nwhen you continue you will have 5 seconds to make the window active.
    \ny - continue""")
    windowconfirm = input()
    if windowconfirm == 'y':  #List is OK, move on
        break
    else:
        print ("\nInvalid entry.")  #invalid, repeat

invlist = []

skipnum = 0  #IMPORTANT - "starting number" - increasing this will skip the first n rows/invoices

csvnum = 0 + skipnum  #csv row to start at (0 is first row)
invnum = 5 + skipnum  #invoice pdf number to start at (starts at 1)

time.sleep(5)   #wait 5 seconds

# make a list of all filenames (should be 1.pdf, 2.pdf...)
for folderName, subfolders, filenames in os.walk(invpath):
    for filename in filenames:
        invlist += [filename]

while len(invlist) > 0:
    findinv = [i for i in invlist if i.startswith(str(invnum)+'-')] #find filename that starts with "invnum-"
    try:
        pyautogui.click("0.png")  #click
    except:
        if compconfirm == 'L':
            pyautogui.click(160,135)    #click logo area for laptop
    
    time.sleep(2)  #sleep for 2 seconds
    ## if unsuccessful type URL??
    pyautogui.click("1.png")  #click
    time.sleep(2)  #sleep for 2 seconds
    pyautogui.write(['end'])
    pyautogui.click("2.png")  #click
    time.sleep(2)  #sleep for 2 seconds
    pyautogui.write(['end'])
    pyautogui.click("3.png")  #click
    time.sleep(2)  #sleep for 2 seconds
    pyautogui.click("4.png")  #click
    time.sleep(2)  #sleep for 2 seconds
    pyautogui.write(findinv[0])
    pyautogui.write(['enter'])
    time.sleep(22)  #sleep for 22 seconds
    pyautogui.write(['tab'])
    time.sleep(1)  #sleep for 1 second
    pyautogui.write(spifflist[csvnum][2])
    time.sleep(1)  #sleep for 1 second
    pyautogui.write(['tab'])
    time.sleep(1)  #sleep for 1 second
    pyautogui.write(spifflist[csvnum][1])
    time.sleep(1)  #sleep for 1 second
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
    time.sleep(3)  #sleep for 3 second
    pyautogui.write(['end'])
    time.sleep(1)  #sleep for 1 second
    ##try/except here for click on 5??  Can add a fail and move on if the submission failed
    pyautogui.click("5.png")  #click
    time.sleep(8)  #sleep for 8 seconds
    gendate2 = (datetime.datetime.now()).strftime('%Y%m%d-%H%M%S')
    myScreenshot = pyautogui.screenshot()   #take screenshot
    myScreenshot.save(screenpath/(gendate2 + '-screenshot.png'))    #save screenshot
    time.sleep(1)  #sleep for 1 second
    csvnum += 1 #next csv row
    invnum += 1 #next invoice
    invlist.remove(findinv[0])  #remove the invoice that was just submitted
    pyautogui.write(['home'])
    time.sleep(1)  #sleep for 1 second
    