"""find out how many packages are on pypi"""

from urllib2 import urlopen
import re
# Get
html = urlopen ('https://pypi.python.org/pypi').read()

# Parse
match = re.search('<strong>([0-9]+)</strong>',html)
assert match, 'cannot find number of packages'

# Output
print match.group(1)
