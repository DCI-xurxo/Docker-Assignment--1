import sys

s = sys.argv[1] if len(sys.argv) > 1 else "hello docker"
print(s)
print(len(s))
print(len(s.split()))
print(s[::-1])