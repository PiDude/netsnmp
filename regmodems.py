import netsnmp
import binascii
import netaddr
from netaddr import *
from datetime import datetime
import csv
import time



#info for the target CMTS
host_ipa="10.10.10.10"
comm_string="public01"


# set up netsnmp session for that CMTS
session=netsnmp.Session(Version=2, Community=comm_string, DestHost=host_ipa, UseNumeric=1)


# poll CMTS using DOCS-IF3-MIB
# this will return a list of MAC Addresses that are remembered.   May not all be registerd.
oid=netsnmp.VarList(netsnmp.Varbind(".1.3.6.1.4.1.4491.2.1.20.1.3.1.2"))
result=session.walk(oid)


#maclist1 is a new vector to store the formatted mac addresses
maclist1=[]


# convert mac addresses to something readable
for item in result:
    mac=str(netaddr.EUI(binascii.hexlify(item).decode('utf-8'), dialect=netaddr.mac_unix))
    print mac
    maclist1.append(mac)

# get start time
start_time = datetime.now()


try:
    while True:

        # get modem registration status (CMTS view)
        oid=netsnmp.VarList(netsnmp.Varbind(".1.3.6.1.4.1.4491.2.1.20.1.3.1.6"))
        regstat=session.walk(oid)

        number_of_reg_modems=0


        # count the number of modems that have a regstat = 8 (operational)
        for i, item in enumerate(regstat, start=0):

            if item == '8':
                number_of_reg_modems += 1

        # get a timestamp
        #sttime = datetime.now().strftime('%Y%m%d_%H:%M:%S')
        sttime = datetime.now().strftime('%H:%M:%S')

        # calculate the elapsed time
        now_time = datetime.now()
        elapsed_time = now_time - start_time

        # print the number of modems that are actually registered (status = 8)
        print sttime, ":there are ", number_of_reg_modems, " registered modems     ", elapsed_time 
        time.sleep(5)

except KeyboardInterrupt:
    print "interrupted !!"



