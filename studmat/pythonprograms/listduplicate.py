values = [5, 5, 1, 1, 2, 3, 4, 4, 5]
output = []
seen = set()
for value in values:
        if value not in seen:
            output.append(value)
            seen.add(value)
print output
