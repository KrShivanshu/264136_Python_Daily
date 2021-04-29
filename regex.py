import re

pattern = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern, "abcdefghi")
if match:
    print(match.group("first"))
    print(match.group())
    print(match.group(1))
    print(match.group(2))
    print(match.groups())

pattern = r"(.+) \1"

match = re.match(pattern, "word word")
if match:
    print("Match 1")

match = re.match(pattern, "?! ?!")
if match:
    print("Match 2")

match = re.match(pattern, "abc cde")
if match:
    print("Match 3")

pattern = r"(\D+\d)"

match = re.match(pattern, " ! $?")
if match:
    print("Match 1")