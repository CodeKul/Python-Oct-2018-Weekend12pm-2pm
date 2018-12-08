'''
1) if else -

if condition1:
    true part for condition1
else:
    false part for condition1

2) if elif else -

if condition1:
    true part for condition1
elif condition2:
    false part for condition1
    true part for condition2
else:
    false part for condition1
    false part for condition2

3) Nested if -

if condition1:
    true part for condition1
    if condition2:
        true part for condition2
    else:
        false part for condition2
else:
    false part for condition1
'''

a = 30

if a < 20:
    print('a is less than 20')
else:
    print('a is greater than or equal to 20')

if a < 20:
    print('a is less than 20')
elif a == 20:
    print('a is equal to 20')
else:
    print('a is greater than 20')

if a <= 20:
    if a == 20:
        print('a is equal to 20')
    else:
        print('a is less than 20')
else:
    print('a is greater than 20')

# Loops

'''
initialisation
while condition:
    statements
    incr/decr
'''

i = 0
while i < 10:
    if i % 2 == 0:
        print('Codekul-{}'.format(i))
    else:
        print('The Gurukul for coders!-{}'.format(i))
    i += 1

# for in
'''
for item in collection:
    use item
'''

for ch in "CodeKul-The Gurukul for Coders!":
    print(ch)

sum = 0
print(range(100))
for num in range(100):
    sum += num

print(sum)