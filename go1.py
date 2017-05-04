import netsnmp
import binascii
import netaddr
from netaddr import *
from datetime import datetime
import csv


#w=5
#h=40
#matrix = [[0 for x in range(w)] for y in range(h)]



f=open('testresult', 'a')

f.write("\n\n\n")
sttime = datetime.now().strftime('%Y%m%d_%H:%M:%S -')
f.write(sttime + '\n')
f.write("\n")


host_ipa="10.10.10.10"
comm_string="public01"


session=netsnmp.Session(Version=2, Community=comm_string, DestHost=host_ipa, UseNumeric=1)

# poll CMTS RFC 4546 for MAC addresses of registered modems
# this oid is RFC4546 and is only those modems currently registered. 

oid=netsnmp.VarList(netsnmp.Varbind(".1.3.6.1.2.1.10.127.1.3.3.1.2"))
result=session.walk(oid)

# maclist is a new vector which will store the formatted mac addresses
maclist=[]

for item in result:
    mac=str(netaddr.EUI(binascii.hexlify(item).decode('utf-8'), dialect=netaddr.mac_unix))
    maclist.append(mac)


s=str(maclist)
f.write(s)
f.write("\n")




# poll CMTS using DOCS-IF3-MIB
# this will return a list of MAC Addresses that are remembered.   May not all be registerd.
oid=netsnmp.VarList(netsnmp.Varbind(".1.3.6.1.4.1.4491.2.1.20.1.3.1.2"))
result=session.walk(oid)

#maclist1 is a new vector to store the formatted mac addresses
maclist1=[]

for item in result:
    mac=str(netaddr.EUI(binascii.hexlify(item).decode('utf-8'), dialect=netaddr.mac_unix))
    print mac
    maclist1.append(mac)


w = 5
h = len(result)
matrix = [[0 for x in range(w)] for y in range(h)]
print h



matrix[0][:] = maclist1

f.write("MAC addresses from DOCS-IF3-MIB\n")
s=str(maclist1)
f.write(s)
f.write("\n")


# get modem registration status (CMTS view)
oid=netsnmp.VarList(netsnmp.Varbind(".1.3.6.1.4.1.4491.2.1.20.1.3.1.6"))
regstat=session.walk(oid)

matrix[1][:] = regstat

f.write("Registration Status\n")
s=str(regstat)
f.write(s)
f.write("\n")



# get total codewords from RFC4546
oid1=netsnmp.VarList(netsnmp.Varbind(".1.3.6.1.2.1.10.127.1.3.3.1.10"))
result=session.walk(oid1)

matrix[2][:] = result


f.write("total codewords\n")
s=str(result)
f.write(s)
f.write("\n")




# gets corrected codewords from RFC4546
oid2=netsnmp.VarList(netsnmp.Varbind(".1.3.6.1.2.1.10.127.1.3.3.1.11"))
result2=session.walk(oid2)

matrix[3][:]=result2

f.write("corrected codewords\n")
s=str(result2)
f.write(s)
f.write("\n")



# gets uncorrectable codewords from RFC4546
oid3=netsnmp.VarList(netsnmp.Varbind(".1.3.6.1.2.1.10.127.1.3.3.1.12"))
result3=session.walk(oid3)


matrix[4][:] = result3


f.write("uncorrectables\n")
s=str(result3)
f.write(s)
f.write("\n")


print("\n")
print matrix[0][:]
print("\n")

print matrix[1][:]
print("\n")

print matrix[2][:]
print("\n")

print matrix[3][:]
print("\n")

print matrix[4][:]
print("\n")


f.close()

#with open('some.csv', 'wb') as f:
#    writer = csv.writer(f)
#    writer.writerows(matrix[:][:])


with open('some.csv', 'wb') as f:
    writer = csv.writer(f)
    for row in matrix:
        writer.writerow(row)




