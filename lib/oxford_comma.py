def oxford_comma(items):
  count = len(items)

  if count == 1:
    return(items[0])
  if count == 2:
    return(f"{items[0]} and {items[1]}")
  elif count > 2:
    return string_function(count, items)

def string_function(num, items):
  while num > 0:
    for i in range(num):
      last = items[-1]
      rest = ", ".join(items[:-1])
      return rest + ", and " + last