# String

s1 = 'Codekul'
s2 = "The 'Gurukul' for Coders!"

print(s1)
print(s2)

# "Codekul" - The 'Gurukul' for Coders!
s3 = '''"{}" - {}'''.format(s1,s2)

print('Int: %d, Float: %f, String: %s'%(45, 23.588, 'Codekul'))

print(s3)


# List

l1 = [1,2,3,4,5, 23.78, 73.98, 'Codekul', "Data", "Melayer"]
l1.append(30)
# l1.sort()
# l1.remove('Data')

print(l1)

# for item in l1:
#     if isinstance(item, float):
#         print(item)

# Remove all strings from the list

# for data in l1:
#     if isinstance(data, str):
#         l1.remove(data)

i = 0
while i < len(l1):
    if isinstance(l1[i], str):
        l1.remove(l1[i])
        continue
    i += 1

print(l1)



# Dictionary

d1 = {'key1': 'Value1', 'One': 1, 2: 'Two'}
print(d1[2])

d1['Three'] = 3

print(d1)

d2 = {'MyDict': d1, 'MyList': l1}
print(d2)

print(d2['MyDict']['One'])


# Tuple

t1 = (1,2,3,4,5)
print(t1[3])

t2 = ('A', 'B', 'C')

t3 = t1 + t2
print(t3)