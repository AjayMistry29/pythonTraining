check_string = "12abcbacbaba344ab"

count = {}
for s in check_string:
  if s in count:
    count[s] += 1
  else:
    count[s] = 1

for key in count:
  if count[key] > 0:
    print(key, count[key])