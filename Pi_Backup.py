#!/usr/bin/python

import os, sys
print "Zipping..."

#Choose Folders to Zip
os.system ("sudo zip -rT /home/pi/scripts/Garage_Pi.tar.gz /home/pi/scripts/")
print "Complete"

#Upload to Dropbox
print "Uploading to Dropbox..."
os.system("/home/pi/scripts/Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/scripts/Garage_Pi.tar.gz /Garage_Pi-Backup/")
print "Backup Complete"

#Delete the zipped file
os.system("sudo rm /home/pi/scripts/Garage_Pi.tar.gz")
