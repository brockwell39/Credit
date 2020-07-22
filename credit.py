from cs50 import get_int
# get card number from the user
while True:
    n = get_int("Number: ")
    if 9999999999999999 > n >= 0:
        break
# seperate out the digits
a = n % 10
b = (n // 10) % 10
c = (n // 100) % 10
d = (n // 1000) % 10
e = (n // 10000) % 10
f = (n // 100000) % 10
g = (n // 1000000) % 10
h = (n // 10000000) % 10
i = (n // 100000000) % 10
j = (n // 1000000000) % 10
k = (n // 10000000000) % 10
l = (n // 100000000000) % 10
m = (n // 1000000000000) % 10
nn = (n // 10000000000000) % 10
o = (n // 100000000000000) % 10
p = (n // 1000000000000000) % 10

# multiply every other digit by two

b = b * 2
d = d * 2
f = f * 2
h = h * 2
j = j * 2
l = l * 2
nn = nn * 2
p = p * 2

# work out products' digits
b1 = b % 10
b2 = (b // 10) % 10
d1 = d % 10
d2 = (d // 10) % 10
f1 = f % 10
f2 = (f // 10) % 10
h1 = h % 10
h2 = (h // 10) % 10
j1 = j % 10
j2 = (j // 10) % 10
l1 = l % 10
l2 = (l // 10) % 10
nn1 = nn % 10
nn2 = (nn // 10) % 10
p1 = p % 10
p2 = (p // 10) % 10

# add products' digits and complete checksum
sum1 = b1 + b2 + d1 + d2 + f1 + f2 + h1 + h2 + j1 + j2 + l1 + l2 + nn1 + nn2 + p1 + p2
sum2 = a + c + e + g + i + k + m + o
sum3 = sum1 + sum2
sum3 = sum3 % 10
# if check sum is 0 work out number of digits
if sum3 == 0:
    count = 0
    n2 = n
    while n > 0:
        n = n // 10
        count += 1
# if count is 15 check for amex
    if count == 15:
        n2 = n2 // 10000000000000
        print(n2)
        if n2 == 34 or n2 == 37:
            print("AMEX")
        else:
            print("INVALID")
# if count is 16 check for mastercard or visa
    elif count == 16:
        n2 = n2 // 100000000000000
        if n2 == 51 or n2 == 51 or n2 == 53 or n2 == 54 or n2 == 55:
            print("MASTERCARD")
        else:
            n2 = n2 // 10
            if n2 == 4:
                print("VISA")
            else:
                print("INVALID")
# if count is 13 check for visa
    elif count == 13:
        n2 = n2 // 1000000000000
        if n2 == 4:
            print("VISA")
        else:
            print("INVALID")
else:
    print("INVALID")