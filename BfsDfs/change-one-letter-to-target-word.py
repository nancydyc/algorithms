"""
start_word = "dog"
target_word = "cat"
allowed_words = {"dog", "cat", "dag", "cot", "cog", "cod", "cot", "tog", "bag", "cag", "dat", "dot", "dob", "cob"}

"dog" -> "dag" -> "dat" -> "cat" : 3
"dog" -> "dot" -> "dob" -> "cob" -> "cot" -> "cat" : 5

"min number of 1-character edits to go from start_word to target_word"


O(N) N is the len(allowed_words)

dog -> aog, bog,cog,...*og, dag,dbg,dcg,d*g, do*
26 * len(dog)

              dog
            /
        dag   cog  tog
        /     /     /
     dat      c     t

     ..

     ..

     cat

[dog] 0
[dag, cog, tog] items in level =3, distance=1
[bag, cag, dat, dog, dog, ]
"""
def find_children(word, allowed_words):
  children = []
  all_letters = 'qwertyuiopasdfghjklzxcvbnm'

  for j in range(len(word)):
    for i in all_letters:
      word[j] = i
      if word in allowed_words:
        children.append(word)
  return children


def find_distance(initial_word, target_word, allowed_words):
  distance = 0
  q = []
  q.append(initial_word)
  seen = set([initial_word])

  while q:
    items_in_level = len(q)
    for i in range(items_in_level):
      current = q.pop(0)
      if current == target_word:
        return distance

      children = find_children(current, allowed_words)
      for ch in children:
        if ch not in seen:
          q.append(ch)

    distance += 1

# q.append((ch, level))
