import ldap
import json


with open('config/net-config.json') as config_file:
    cfg_data = json.load(config_file)

## first you must open a connection to the server
try:
	l = ldap.open(cfg_data['ldap_uri'])
	## searching doesn't require a bind in LDAP V3.  If you're using LDAP v2, set the next line appropriately
	## and do a bind as shown in the above example.
	# you can also set this to ldap.VERSION2 if you're using a v2 directory
	# you should  set the next option to ldap.VERSION2 if you're using a v2 directory
	l.protocol_version = ldap.VERSION3	
except ldap.LDAPError, e:
	print e
	

searchScope = ldap.SCOPE_SUBTREE
searchFilter = cfg_data['searchdn_dhcp']
baseDN = cfg_data['basedn']
retrieveAttributes = None 


try:
	ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
	result_set = []
	while 1:
		result_type, result_data = l.result(ldap_result_id, 0)
		if (result_data == []):
			break
		else:
			## here you don't have to append to a list
			## you could do whatever you want with the individual entry
			## The appending to list is just for illustration. 
			if result_type == ldap.RES_SEARCH_ENTRY:
				result_set.append(result_data)
	print result_set
except ldap.LDAPError, e:
	print e
