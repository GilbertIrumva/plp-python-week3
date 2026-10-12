count = 1
total = 0

# BUG: Added the missing colon because the while statement requires a colon.

# BUG: Changed < to <= so the loop includes 5 in the sum.

while count <= 5:
  total = total + count
  count = count + 1

# BUG: Used an f-string to display the integer total without a type error.

print(f"Sum of 1 to 5 is: {total}")
