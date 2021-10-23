import re
result = []

for _ in range(int(input())):
    if re.fullmatch(r'(7|8|9)\d{9}',input()):
        result.append("YES")
    else:
        result.append("NO")

for i in result:
    print(i)