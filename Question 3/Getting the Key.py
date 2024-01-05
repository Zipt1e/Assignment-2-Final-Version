total = 0

for i in range(5):
    found_match = False
    for j in range(3):
        if i + j == 5:
            total += i + j
            found_match = True
            break  # Exit the inner loop once a match is found

    if not found_match:
        total -= i - j

print(total)

