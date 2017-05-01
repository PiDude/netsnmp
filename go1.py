
import netsnmp
import datetime



f=open('testresult', 'a')

host_ipa="10.10.10.10"
comm_string="public01"


session=netsnmp.Session(Version=2, Community=comm_string, DestHost=host_ipa, UseNumeric=1)

# pull MAC addresses of registered modems
macoid=netsnmp.VarList(netsnmp.Varbind(".1.3.6.1.2.1.10.127.1.3.3.1.2.1"))
result0=session.walk(macoid)
print result0

s=str(result0)
f.write(s)
f.write("\n")

# get total codewords from RFC4546
oid1=netsnmp.VarList(netsnmp.Varbind(".1.3.6.1.2.1.10.127.1.3.3.1.10"))
result=session.walk(oid1)
print result

s=str(result)
f.write(s)
f.write("\n")


# gets corrected codewords from RFC4546
oid2=netsnmp.VarList(netsnmp.Varbind(".1.3.6.1.2.1.10.127.1.3.3.1.11"))
result2=session.walk(oid2)
print result2

s=str(result2)
f.write(s)
f.write("\n")



# gets uncorrectable codewords from RFC4546
oid3=netsnmp.VarList(netsnmp.Varbind(".1.3.6.1.2.1.10.127.1.3.3.1.12"))
result3=session.walk(oid3)
print result3



f.write("this is a test\n")
s=str(result3)
f.write(s)

f.close()



