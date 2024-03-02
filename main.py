x = 96
y = x//16
z = int(input())
c = (z - 48 * x)//y
print(c)

x, y = map(str, input().split())
print(x, y, sep='\n')

S, R = map(int, input().split())
print(S + R)

kittens = 7 * 7 * 7 * 7
cats = 7 * 7 * 7
wives = 7
print(kittens + cats + wives + 2)

x = int(input())
y = int(x * 0.19 * 100) / 100
print(y)

m = float(input())
r = float(input())
m = m * 0.45359237
r = r * 0.0254
IMT = m / (r**2)
print(IMT)

print((10000 * 0.01) * 1000)

N, M = map(int, input().split())
print(M // (N+1))

N, K = map(int, input().split())
print(N % K)

m = int(input())
m = m / 1000
print(m / 1.609344)
