# DOM = All in memory
# SAX = Iteative parsing

import xml.etree.ElementTree as et

tree = et.parse ('books.xml')
catalog = tree.getroot()

# Print number of books
print 'We have %d books' % len(catalog)

# Print all books ids
print 'book ids:'
for elem in catalog:
    print '\t%s' % elem.get('id')

# Print author and description of bk102
print 'bk102:'
for book in catalog:
    if book.get('id') == 'bk102':
        print 'author: %s' % book.find('author').text
        print 'description: %s' % book.find('description').text

# find book directly with xpath
book = catalog.find('book[@id="bk102"]')
print 'author: %s' % book.find('author').text
print 'description: %s' % book.find('description').text


# Print all the book titels
print 'Titles'
for elem in catalog.findall('book/title'):
    print '\t%s' % elem.text

# print author and price of computer books
print 'computer books'
for book in catalog:
    if book.find('genre').text !='Computer':
        continue
    print u'\t%s: \N{pound sign}%s' % (
        book.find('author').text,
        book.find('price').text,
        )

# Print all Metadata
print 'bk102:'
book = catalog.find('book[@id="bk102"]')
for elem in book:
    print '%s: %s' % (elem.tag.title(), elem.text)
