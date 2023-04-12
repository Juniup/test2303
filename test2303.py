import sys

N = int(input())
final_list = []

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    
    score = 100000000*a + 10*b
    
    if b < 0:
        score += 1
        
    final_list.append(score)

final_list.sort()

for i in range(len(final_list)):
    if final_list[i] % 2 == 0:
        b1 = (final_list[i] % 100000000) // 10
        a1 = final_list[i] // 100000000
        
    else:
        b1 = ((final_list[i] % 100000000)-100000000) // 10
        a1 = final_list[i] // 100000000 + 1

    print(a1, b1)