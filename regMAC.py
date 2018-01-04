import re
s = raw_input("Enter MAC Address : ")
if re.match(r"([\dA-F]{2}(?:[:][\dA-F]{2}){5})",s):
    print "valid"
else:
    print "Invalid"
