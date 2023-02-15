T = int(input())

for test_case in range(1,T+1):
    hap = 0
    avg =  0
    a = list(map(int, input().split()))
    a.sort()
    
    
    for i in range(1,9):
        hap += a[i]
    avg = round(hap/8, 0)
    print('#%d %d' %(test_case, avg))