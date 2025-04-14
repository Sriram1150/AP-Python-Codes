def allinone(s):
    if len(s) > 3:
        print(f"4th element: {s[3]}")
    if len(s) > 2:
        print(f"All element except first two: {s[2:]}")
    print(f"Reversed order: {s[::-1]}")
    print(f"Sum: {sum(s)}")
    print(f"Max: {max(s)}")
    print(f"Min: {min(s)}")
    if 0 in s:
        print(s.index(0))
    else:
        print("-1")
    print(sorted(s))
    print(sorted(s,reverse=True))

allinone([1,4,6,7,3,2,4,5,7,8,4,2])