import re

def match_text(text):
    limit = "(25[0-5]|1[0-9][0-9]|[1-9][0-9]?|0)"
    is_match = bool(re.match(rf"{limit}\.{limit}\.{limit}\.{limit}", text))
    return is_match

text1 = "192.168.1.1 is the default gateway"      #True
text2 = "255.255.255.0 subnet mask"               #True

text3 = "256.100.50.25 too high first octet"      #False
text4 = "192.168.1 is incomplete"                 #False
text5 = "IP is 10.0.0.1"                          #False

print(match_text(text1))
print(match_text(text2))
print(match_text(text3))
print(match_text(text4))
print(match_text(text5))