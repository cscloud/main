""" A palindromic number reads the same both ways. The largest palindrome madefrom the product
of two 2-digit numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of two 3-digit numbers."""
#Algo in ENG
# biggest palindrom = 0
# for all 3 digit number x
# for all 3 digit number y
# product = x*y
#if product is palindrom and product bigger then biggest palindrom:
# biggest palindrom = product
#print bigger palindrom


def is_palindrom(n):
    s = '%s' % n
    return s == s[::-1]

# Get
max_pali = 0
for x in range(100, 1000):
    for y in range(100, 1000):
        n = x * y
        # Parse - NOOP
        # Analyze
        if is_palindrom(n) and n> max_pali:
            max_pali = n

# Output
print max_pali
