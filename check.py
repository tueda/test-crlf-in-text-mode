import sys
import re

with open(sys.argv[1], "rb") as f:
    s = f.read().decode("utf-8")
s = s.replace("\r", "<CR>")
s = s.replace("\n", "<LF>")
s = re.sub("(<CR>|<LF>)+", "\\g<0>\n", s)
s = s.replace("<BR>", "\n")
print(s)
