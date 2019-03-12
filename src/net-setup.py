import ldap
import json


with open('config/net-config.json') as config_file:
    cfg_data = json.load(config_file)

## first you must open a connection to the server

l = ldap.initialize(cfg_data["ldap"]["ldap_uri"])

try:
    l.protocol_version = ldap.VERSION3	
except ldap.LDAPError, e:
    print e
	

searchScope = ldap.SCOPE_SUBTREE
searchFilter = cfg_data["netconfig"]["searchdn_dhcp"]
baseDN = cfg_data["ldap"]["basedn"]
retrieveAttributes = None 


try:
    result = l.search_s(baseDN, searchScope, searchFilter, retrieveAttributes)
    print result
    l.unbind_s()
except ldap.LDAPError, e:
    print e
