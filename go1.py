
import netsnmp
from datetime import datetime


w=5
h=40
matrix = [[0 for x in range(w)] for y in range(h)]

f=open('testresult', 'a')

f.write("\n\n\n")
sttime = datetime.now().strftime('%Y%m%d_%H:%M:%S -')
f.write(sttime + '\n')
f.write("\n")


host_ipa="10.10.10.10"
comm_string="public01"


session=netsnmp.Session(Version=2, Community=comm_string, DestHost=host_ipa, UseNumeric=1)

# pull MAC addresses of registered modems
oid=netsnmp.VarList(netsnmp.Varbind(".1.3.6.1.2.1.10.127.1.3.3.1.2"))
result=session.walk(oid)
print result




s=str(result)
f.write(s)
f.write("\n")

# pull MACs from DOCS-IF3-MIB
oid=netsnmp.VarList(netsnmp.Varbind(".1.3.6.1.4.1.4491.2.1.20.1.3.1.2"))
result=session.walk(oid)
print result

f.write("MAC addresses from DOCS-IF3-MIB\n")
s=str(result)
f.write(s)
f.write("\n")


# get modem registration status (CMTS view)
oid=netsnmp.VarList(netsnmp.Varbind(".1.3.6.1.4.4491.2.1.20.1.3.1.6"))
regstat=session.walk(oid)
print("Registration Status Values\n")
print regstat

f.write("Registration Status")
s=str(regstat)
f.write(s)
f.write("\n")



# get total codewords from RFC4546
oid1=netsnmp.VarList(netsnmp.Varbind(".1.3.6.1.2.1.10.127.1.3.3.1.10"))
result=session.walk(oid1)
print result

f.write("total codewords\n")
s=str(result)
f.write(s)
f.write("\n")

matrix[1][:]=result


# gets corrected codewords from RFC4546
oid2=netsnmp.VarList(netsnmp.Varbind(".1.3.6.1.2.1.10.127.1.3.3.1.11"))
result2=session.walk(oid2)
print result2

matrix[2][:]=result2

print ("this is the matrix value\n")
print matrix[1][0]
print matrix[2][0]
print ("\n")


f.write("corrected codewords\n")
s=str(result2)
f.write(s)
f.write("\n")



# gets uncorrectable codewords from RFC4546
oid3=netsnmp.VarList(netsnmp.Varbind(".1.3.6.1.2.1.10.127.1.3.3.1.12"))
result3=session.walk(oid3)
print result3


f.write("uncorrectables\n")
s=str(result3)
f.write(s)
f.write("\n")




f.close()



