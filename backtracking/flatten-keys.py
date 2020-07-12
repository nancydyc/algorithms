"""
You are given a nested dictionary. You don't know how deeply nested it is. Your goal is to flatten all the keys


{
  "a": {
     "b": {
        "c": 5,
        "d": 6
     }
     "e": 10
  },
  "f": 10,
  "g": {
    "h":11
  }
}


{
  "a.b.c": 5,
  "a.b.d": 6,
  "a.e": 10,
  "f": 10,
  "g.h": 11
}


"""


def helper(k, val, answer):
  if not val:
    answer[k] = val
    return answer

  if isinstance(val, int):
    answer[k] = val
    return answer

  else:
    for i in val.items():
      k += '.' + i[0]
      helper(k, i[1], answer)
      # backtracking
      k = k[:-2]


def flatten(dict):
  answer = {}
  for i in dict.items():
    new_key = i[0]
    helper(new_key, i[1], answer)

  return answer


nested_dict = {
  "a": {
     "b": {
        "c": 5,
        "d": 6
     },
     "e": 10
  },
  "f": 10,
  "g": {
    "h":11
  }
}

test = {}
test1 = {'a': {}}

print(flatten(nested_dict))
print(flatten(test1))
print(flatten(test))
