#!/usr/bin/python

import os
import time
import datetime
import pysftp
import shutil

DBUSER = 'manish'
DBPASS = 'mklinux123'
BACKUP_PATH = '/opt/dbbackup/'

DATETIME = time.strftime('%d%m%Y-%H%M')

TODAYBACKUPPATH= BACKUP_PATH + DATETIME

if not os.path.exists(TODAYBACKUPPATH):
    os.makedirs(TODAYBACKUPPATH)
    mysql_cmd = "mysqldump -u" + DBUSER + " -p" + DBPASS + " --all-databases" + " > " + TODAYBACKUPPATH + "/" + "alldb.sql"
    os.system(mysql_cmd)
else:
    print "backup not work"


localpath = (BACKUP_PATH)
remotepath = '/home/bkup/'


srv = pysftp.Connection(host="RemoteHOST", username="root", password="yourPASS",log="/tmp/pysftp.log")
srv.put_r(localpath, remotepath, preserve_mtime=True)
srv.close()
shutil.rmtree(TODAYBACKUPPATH)
