print()
s = (s for s in range(0,1117) if s % 7 == 0)
for f in s:
    print(f, end='=-=')