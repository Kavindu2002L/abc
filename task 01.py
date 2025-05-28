x=0
for i in range(1,11):
    sqr=i**2
    if sqr % 4 == 0:
        x += sqr
print("sum of squares divisible by 4 from 1 to 10 is:",x)
