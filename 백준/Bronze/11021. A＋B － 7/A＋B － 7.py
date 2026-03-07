t = int(input())
total = []

for i in range(1, t+1):
  a, b = map(int, input().split())
  total.append(a+b)

for j in range(1, t+1):
  print(f'Case #{j}: {total[j-1]}')