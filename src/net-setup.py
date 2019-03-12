import ldap
import json


with open('config/net-config.json') as config_file:
    cfg_data = json.load(config_file)

## first you must open a connection to the server

l = ldap.initialize(cfg_data["ldap"]["ldap_uri"])

searchScope = ldap.SCOPE_SUBTREE
searchFilter = "(objectClass=dhcpHost)"
baseDN = cfg_data["netconfig"]["basedn_dhcp"]
retrieveAttributes = None 
binddn = cfg_data["netconfig"]["binduser"]
pw = cfg_data["netconfig"]["bindpw"]

try:
    l.protocol_version = ldap.VERSION3
    l.simple_bind_s(binddn, pw)
except ldap.LDAPError, e:
    print e

try:
    result = l.search_s(baseDN, searchScope, searchFilter, retrieveAttributes)
    print result
    l.unbind_s()
except ldap.LDAPError, e:
    print e
