from math import comb

p = 0.55
res = [comb(50,m)*(p**m)*((1-p)**(50-m)) for m in range(25, 51)]
print(sum(res))

