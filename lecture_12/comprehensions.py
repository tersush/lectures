a: list[Any] = []
for i in range(10):
    a.append(i**2)
print(a)

print([i**2 for i in range(10) if i%2==0])