import netsnmp
import binascii
import netaddr
from netaddr import *
from datetime import datetime
import csv


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


# poll CMTS RFC 4546 for MAC addresses of registered modems
# this oid is RFC4546 and is only those modems currently registered. 

oid=netsnmp.VarList(netsnmp.Varbind(".1.3.6.1.2.1.10.127.1.3.3.1.2"))
result=session.walk(oid)

# maclist is a new vector which will store the formatted mac addresses
maclist=[]


# convert the mac addresses to something readable
for item in result:
    mac=str(netaddr.EUI(binascii.hexlify(item).decode('utf-8'), dialect=netaddr.mac_unix))
    maclist.append(mac)


# write mac addresses to local file
s=str(maclist)
f.write(s)
f.write("\n")




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
    matrix[i][1] = item
    if matrix[i][1] == '8':
        number_of_reg_modems += 1

# count the number of modems that are actually registered (status = 8)

print "\nThere are ", number_of_reg_modems, " registered modems\n\n"




# write regstat to the local file
f.write("Registration Status\n")
s=str(regstat)
f.write(s)
f.write("\n")

# get pre- total codewords from RFC4546
oid1=netsnmp.VarList(netsnmp.Varbind(".1.3.6.1.2.1.10.127.1.3.3.1.10"))
result=session.walk(oid1)

# write pre- total codewords in third column of matrix to be used for .csv file
for i, item in enumerate(result, start=0):
    matrix[i][3] = item

# write total codewords to local file
f.write("pre- total codewords\n")
s=str(result)
f.write(s)
f.write("\n")

# gets pre- corrected codewords from RFC4546
oid2=netsnmp.VarList(netsnmp.Varbind(".1.3.6.1.2.1.10.127.1.3.3.1.11"))
result2=session.walk(oid2)

# write pre- corrected codewords in sixth column of matrix to be used for .csv file
for i, item in enumerate(result2, start=0):
    matrix[i][6]=item

#write pre- corrected codewords to local file
f.write("pre- corrected codewords\n")
s=str(result2)
f.write(s)
f.write("\n")

# gets pre- uncorrectable codewords from RFC4546
oid3=netsnmp.VarList(netsnmp.Varbind(".1.3.6.1.2.1.10.127.1.3.3.1.12"))
result3=session.walk(oid3)

# write pre- unreliable codewords to ninth column of matrix to be used for .csv file
for i, item in enumerate(result3, start=0):
    matrix[i][9] = item

# write pre- unreliable codewords to local file.
f.write("pre- uncorrectables\n")
s=str(result3)
f.write(s)
f.write("\n")


print "\n\n"
raw_input("Press Enter to continue......")
print "\n\n"




# get post- total codewords from RFC4546
oid1=netsnmp.VarList(netsnmp.Varbind(".1.3.6.1.2.1.10.127.1.3.3.1.10"))
result=session.walk(oid1)

# write post- total codewords in second column of matrix to be used for .csv file
for i, item in enumerate(result, start=0):
    matrix[i][2] = item

# write total codewords to local file
f.write("post- total codewords\n")
s=str(result)
f.write(s)
f.write("\n")

# gets post- corrected codewords from RFC4546
oid2=netsnmp.VarList(netsnmp.Varbind(".1.3.6.1.2.1.10.127.1.3.3.1.11"))
result2=session.walk(oid2)

# write post- corrected codewords in sixth column of matrix to be used for .csv file
for i, item in enumerate(result2, start=0):
    matrix[i][5]=item

#write pre- corrected codewords to local file
f.write("post- corrected codewords\n")
s=str(result2)
f.write(s)
f.write("\n")

# gets post- uncorrectable codewords from RFC4546
oid3=netsnmp.VarList(netsnmp.Varbind(".1.3.6.1.2.1.10.127.1.3.3.1.12"))
result3=session.walk(oid3)

# write post- unreliable codewords to ninth column of matrix to be used for .csv file
for i, item in enumerate(result3, start=0):
    matrix[i][8] = item

# write post- unreliable codewords to local file.
f.write("pre- uncorrectables\n")
s=str(result3)
f.write(s)
f.write("\n")


# close the local file
f.close()



# calculate delta of total codewords

for i in range (0, h):
    matrix[i][4]  = int(matrix[i][2]) - int(matrix[i][3])
    matrix[i][7]  = int(matrix[i][5]) - int(matrix[i][6])
    matrix[i][10] = int(matrix[i][8]) - int(matrix[i][9])


#open a new .csv file to write the matrix into, this is openable with Excel.

with open(sttime+'.csv', 'wb') as f:
    writer = csv.writer(f)
    for row in matrix:
        writer.writerow(row)
f.close()



