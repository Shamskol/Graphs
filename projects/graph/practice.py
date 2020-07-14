dict = {
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}
sum = 0
for val in dict.values():
    if type(val) is int:
        sum += val
print(sum)
