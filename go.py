
import netsnmp



host_ipa="10.10.10.10"
comm_string="public01"


# gets sysDescr
oid1=netsnmp.Varbind(".1.3.6.1.2.1.1.1.0")
result=netsnmp.snmpget(oid1, Version=2, Community=comm_string, DestHost=host_ipa)
print result
print

# gets sysUpTime
oid2=netsnmp.Varbind(".1.3.6.1.2.1.1.3.0")
result2=netsnmp.snmpget(oid2, Version=2, Community=comm_string, DestHost=host_ipa)
print result2
print


# walks RFC 4546 CmtsCmStatus table
oid3=netsnmp.Varbind(".1.3.6.1.2.1.10.127.1.3.3")
result3=netsnmp.snmpwalk(oid3, Version=2, Community=comm_string, DestHost=host_ipa)
print result3


gets DocsIf3.1CmtsCmStatus table
oid4=netsnmp.Varbind("")
result4=netsnmp.snmpwalk(oid4, Version=2, Community=comm_string, DestHost=host_ipa)
print result4


