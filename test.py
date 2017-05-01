
import netsnmp



host_ipa="10.10.10.10"
comm_string="public01"


oid1=netsnmp.Varbind("sysDescr.0")
result=netsnmp.snmpget(oid1, Version=2, Community=comm_string, DestHost=host_ipa)
print result
print

oid2=netsnmp.Varbind(".1.3.6.1.2.1.1.3.0")
result2=netsnmp.snmpget(oid2, Version=2, Community=comm_string, DestHost=host_ipa)
print result2
print


oid3=netsnmp.Varbind("system")
result3=netsnmp.snmpwalk(oid3, Version=2, Community=comm_string, DestHost=host_ipa)
print result3

