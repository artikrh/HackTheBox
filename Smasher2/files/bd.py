import sys

cmd = " ".join(sys.argv[1:])
out = "$'\\''"
for ch in cmd:
  out += '\\\\' + oct(ord(ch))[2:]
out  += "'\\''"
print(out)
