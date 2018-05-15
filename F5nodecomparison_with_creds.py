from f5.bigip import ManagementRoot
import certifi
import urllib3
import requests
import re

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
x_file = open('/usr/local/bin/python_scripts/nodes.txt', 'r')
t=list()
for i in x_file:
    i=i.split('\n',1)[0]
    if i not in t:
       t.append(i)

# Below line will Connect to the BigIP##
mgmt = ManagementRoot(ip,username,password")

## Below lines will get a list of all nodes in the F5 device, compare them to the list from above, and print out the matching nodes##
test=list()
pools = mgmt.tm.ltm.pools.get_collection()
for pool in pools:
    for i in t:
        for member in pool.members_s.get_collection():
            if i in member.name:
               print i
               break
            else: continue
