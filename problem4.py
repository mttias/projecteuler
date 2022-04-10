# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

factorOne = 500
factorTwo = 500

product = factorOne * factorTwo
productStr = str(product)

# print(productStr[-4:-1])
# print(productStr[:3])

largestPalindrome = 0

for x in range(500,1000,1):
    for y in range(500,1000,1):
        product = str(x * y)
        if product[-1] == product[0] and product[-2] == product[1] and product[-3] == product[2] and int(product) > largestPalindrome:
            largestPalindrome = int(product)
            factorOne = x
            factorTwo = y

print(factorOne)
print(factorTwo)
print(largestPalindrome)
        

