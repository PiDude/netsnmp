import netsnmp
import binascii
import netaddr
from netaddr import *
from datetime import datetime
import csv
import ipaddress


# open a file to stuff results in
f=open('testresult', 'a')

#append a timestamp to the file each time this program is run
f.write("\n\n\n")
sttime = datetime.now().strftime('%Y%m%d_%H:%M:%S')
f.write(sttime + '\n')
f.write("\n")


#info for the target CMTS
host_ipa="10.10.10.10"
comm_string="public01"


# set up netsnmp session for that CMTS
session=netsnmp.Session(Version=2, Community=comm_string, DestHost=host_ipa, UseNumeric=1)




# poll CMTS for list of registered modem MAC addresses using DOCS-IF3-MIB
# this will return a list of MAC Addresses that are remembered.   May not all be registered.
oid=netsnmp.VarList(netsnmp.Varbind(".1.3.6.1.4.1.4491.2.1.20.1.3.1.2"))
result=session.walk(oid)


#maclist1 is a new vector to store the formatted mac addresses
maclist1=[]


# convert mac addresses to something readable
for item in result:
    mac=str(netaddr.EUI(binascii.hexlify(item).decode('utf-8'), dialect=netaddr.mac_unix))
    print (mac)
    maclist1.append(mac)

# create a 2D list that will be used to store the data in a .csv file
w = 11
h = len(result)


matrix = [[0 for x in range(w)] for y in range(h)]

# write the mac addresses in the first column of the matrix to be used for .csv file

for i, item in enumerate(maclist1, start=0):
    matrix[i][0] = item



# write the mac addresses to the local file
f.write("MAC addresses from DOCS-IF3-MIB\n")
s=str(maclist1)
f.write(s)
f.write("\n")

# get modem registration status (CMTS view)
oid=netsnmp.VarList(netsnmp.Varbind(".1.3.6.1.4.1.4491.2.1.20.1.3.1.6"))
regstat=session.walk(oid)

number_of_reg_modems=0

# put regstat in second column of matrix used for .csv file
for i, item in enumerate(regstat, start=0):
    item = int(item)
    matrix[i][1] = item
    if matrix[i][1] == 8:
        number_of_reg_modems += 1

# count the number of modems that are actually registered (status = 8)

#print "\nThere are ", number_of_reg_modems, " registered modems\n\n"
print()
print("There are ", number_of_reg_modems, "registered modems")
print()





# iplist1 is a new vector to store the formatted IP addresses
iplist1=[]

#get the list of IPv4 addresses for registered modems
IPv4oid=netsnmp.VarList(netsnmp.Varbind(".1.3.6.1.4.1.4491.2.1.20.1.3.1.5"))
IPv4result=session.walk(IPv4oid)

print(IPv4result)


for i, item in enumerate(IPv4result, start=0):
    print(item)
    v = ipaddress.ip_address(item).exploded
    print(v)
    iplist1.append(v)
    matrix[i][2] = v

print(iplist1)


#write IP addresses to local file
f.write("IP addresses from DOCSIS-IF3-MIB\n")
s=str(iplist1)
f.write(s)
f.write("\n")


# close the local file
f.close()





# set up netsnmp session for modems


for item in iplist1:
    print("printing item")
    print(item)
    session=netsnmp.Session(Version=2, Community="public", DestHost=item, UseNumeric=1)
    oid=netsnmp.VarList(netsnmp.Varbind(".1.3.6.1.4.1.4491.2.1.28.1.1"))
    result=session.walk(oid)
    print(result)


#open a new .csv file to write the matrix into, this is openable with Excel.

with open(sttime+'.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    for row in matrix:
        writer.writerow(row)
f.close()


