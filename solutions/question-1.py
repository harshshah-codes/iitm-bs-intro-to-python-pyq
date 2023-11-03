# Method 1

number = input()

mistakes = 0
incorrect_str = {'l': '1', 'o': '0'}
out = ''

for digit in number:
    if digit in incorrect_str:
        mistakes += 1
        digit = incorrect_str[digit]
    out += digit 

if mistakes:
    print('No of mistakes:', mistakes)
    print('Corrected number', out)
else:
    print('No mistakes')

# Method 2
n=input()
count=0

for x in n:
	if (x == 'o'):
		count = count + 1
	if(x == 'l'):
		count = count + 1

if(count == 0):
	print('No Mistake')
else:
	print(count)
	n=n.replace('o', '0')
	n=n.replace('l', '1')
	print(n)