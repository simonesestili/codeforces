t = int(input())

for _ in range(t):
    s = input()
    prev, curr = None, 0
    for c in s:
        if prev != c:
            if curr == 1:
                print('NO')
                break
            prev, curr = c, 0
        curr += 1
    else:
        print('NO' if curr == 1 else 'YES')



