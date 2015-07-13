import json

with open ('books.json') as fp:
    catalog = json.load(fp)

# Print number of book
print 'we have %d books' % len(catalog)

# Print bood ids, one per line sorted in reverse

print 'book ids:'
for bid in sorted(catalog, reverse = True):
    print '\t%s' % bid

# print author and description of book bk102

book = catalog['bk102']

# print 'Author: %s % catalog['bk102']['uthor']
print 'Author: %s' % book['author']
print 'Decription:\n%s' %book['description']

# Print all the titles

print 'Titles:'
for book in catalog.values():
    print '\t%s' % book['title']

# Print author and price of computer books

for book in catalog.values():
    if book['genre'] == 'Computer':
        print '%s: %.1f' % (book['author'], book['price'])

# print all metadata on bk102
print 'bk102:'
book = catalog['bk102']
for key, value in book.items():
    print '%s: %s' % (key, value)

# was
# for key in book:
#     print '%s: %s' % (key, book[key])  
    
# Using pprint

from pprint import pprint
pprint(book)
