
import netsnmp
import datetime



f=open('testresult', 'a')

host_ipa="10.10.10.10"
comm_string="public01"


session=netsnmp.Session(Version=2, Community=comm_string, DestHost=host_ipa, UseNumeric=1)




oid1=netsnmp.VarList(netsnmp.Varbind("sysDescr.0"))
result=session.get(oid1)
s=str(result)
f.write(s)
f.write("\n")


# gets sysDescr
oid1=netsnmp.VarList(netsnmp.Varbind(".1.3.6.1.2.1.1.1.0"))
result=session.get(oid1)
#print result

s=str(result)
f.write(s)
f.write("\n")

print

# gets sysUpTime
oid2=netsnmp.VarList(netsnmp.Varbind(".1.3.6.1.2.1.1.3.0"))
result2=session.get(oid2)
print result2

s=str(result2)
f.write(s)
f.write("\n")

print


# walks RFC 4546 CmtsCmStatus table
oid3=netsnmp.VarList(netsnmp.Varbind(".1.3.6.1.2.1.10.127.1.3.3"))
result3=session.walk(oid3)
#print result3



f.write("this is a test\n")
s=str(result3)
f.write(s)
f.close()


# gets DocsIf3.1CmtsCmStatus table
oid4=netsnmp.Varbind(".1.3.6.1.2.1.10.127.1.3.3.1.2.1")
result4=netsnmp.snmpwalk(oid4, Version=2, Community=comm_string, DestHost=host_ipa)
print result4


