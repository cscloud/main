"""Takes employee data from CSV (was Excel) and create one
VCARD per employee.

After that, generate QR file per employee. Data encoded in the QR is a URL to
the VCF on the company web server.
"""

import csv
from urllib2 import urlopen

vcard_template = '''\
BEGIN:VCARD
VERSION:2.1
N:%s;%s
FN:%s %s
ORG:Raisins R Us, Inc.
TITLE:%s
TEL;WORK;VOICE:%s
ADR;WORK:;;100 Flat Grape Dr.;Fresno;CA;95555;United States of America
EMAIL;PREF;INTERNET:%s
REV:20140609T195243Z
END:VCARD
'''

qr_url = 'https://chart.googleapis.com/chart?cht=qr&chs=200x200&chl=%s'


def gen_vcard(first, last, title, email, phone, outfile):
    """Generate VCARD file"""
    data = vcard_template % (
        last, first,
        first, last,
        title,
        phone,
        email
    )
    with open(outfile, 'w') as out:
        out.write(data)


def gen_qr(data, outfile):
    """Generate image with data encoded as QR"""
    url = qr_url % data
    fo = urlopen(url)
    image = fo.read()
    with open(outfile, 'wb') as out:
        out.write(image)

# Get
with open('raisin_team.csv') as fo:
    # Parse
    reader = csv.reader(fo)
    for fields in reader:
        last, first, title, email, phone = fields
        # Analyze
        # NOOP

        # Output
        vcf_file = '%s_%s.vcf' % (first, last)
        gen_vcard(first, last, title, email, phone, vcf_file)

        encoded_data = 'http://raisins.com/vcf/%s' % vcf_file
        png_file = '%s_%s.png' % (first, last)
        gen_qr(encoded_data, png_file)
