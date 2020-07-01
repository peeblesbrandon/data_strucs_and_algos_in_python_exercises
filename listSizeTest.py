import sys

data = []
print("####### TESTING APPEND METHOD #######")
for k in range(50):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    data.append(None)

print("####### TESTING POP METHOD #######")
for k in range(50):
    data.pop()
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
