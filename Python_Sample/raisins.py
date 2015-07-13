"""
Generate VCARD per employee in Excel file
"""
import csv
from urllib2 import urlopen

vcard_template = '''\
BEGIN:VCARD
VERSION:2.1
N:%s;%s
FN:%s %s
ORG:Looney Tunes
TITLE:%s
TEL;WORK;VOICE:%s
ADR;WORK:;;1 Carrot Ave.;Los Angels;CA;90583;United States of America
EMAIL;PREF;INTERNET:%s
REV:20140609T195243Z
END:VCARD
'''
url_template = ('https://chart.googleapis.com/chart?cht=qr&chs=200x200&chl=%s')
#Get
fp=open('raisin_team.csv')

# Parse
for fields in csv.reader(fp):
           # Output vcard
           last, first, titel, email, phone = fields
           vcard = '%s_%s.vcf' % (first, last)
           #Context Manager - guarntee to close the file
           with open(vcard, 'w') as out:
            out.write(vcard_template % (first, last, last, first, titel, phone, email))
           # Output - QR
           data = 'http://raisns-r-us.com/vcf/%s' % vcard
           url = url_template % data
           ufp = urlopen(url)
           qr_file = '%s_%s.png' % (first, last)
           with open(qr_file, 'wb') as out:
                out.write(ufp.read())

# Analyze-- noop
