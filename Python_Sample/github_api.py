"""Given github login, print name and number of public repos"""

from urllib2 import urlopen
import json

#Get
fp = urlopen('https://j.mp/ghcisco')
data = fp.read()

# Parse
reply = json.loads(data)

#Analyze

#output
print reply['name']
print reply['public_repos']
