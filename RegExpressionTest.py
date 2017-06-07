import re
print("staring")
regex = r"[a-z A-Z]+ \d+"
regex1 = r"([a-z A-Z]+) \d+"
regex2 = r"([a-z A-Z]+) \d+"
regex3 = r"([a-z A-Z]+) (\d+)"
regex4 = r"\d+ [a-z A-Z]+ [a-z A-Z]+"
phonemacth = r"\d{10}"
matches = re.findall(regex,"June 24, August 9, Dec 12, 12Feb")
matches1 = re.findall(regex1,"June 24, August 9, Dec 12, 12Feb")
matches2 = re.finditer(regex2,"June 24, August 9, Dec 12, 12Feb")
macthes3 = re.sub(regex3,r"\2 of \1","June 24, August 9, Dec 12, 12Feb")
macthes4 = re.findall(regex4,macthes3)
for match in matches:
    print("Full match", match)
for match in matches1:
    print("Month match", match)
print("mobile --check--")
print(type(matches2))
for match in matches2:
    print("Match at index match", match.start(), match.end())
for match in macthes4:
    print("Full Match", match)    
mobileN0 = input("enter mobile no")
X = re.findall(phonemacth,str(mobileN0))
if X:
    print("valid mobile no",mobileN0)
else:    
    print("invalid mobile no",mobileN0)
