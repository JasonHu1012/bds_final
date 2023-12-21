a = 1
b = 1
for _ in range(int(input('n: ')) - 2):
    a, b = b, a + b
print(b)
