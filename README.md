# Pi_Auto_Backup
Requires zip & unzip

$sudo apt-get install zip unzip

Requires Dropbox_Uploader from https://github.com/andreafabrizi/Dropbox-Uploader

Edit sudo crontab -e to include a 3am backup

#Backup to Dropbox
0 3 * * * /usr/bin/python /home/pi/scripts/backup.py
