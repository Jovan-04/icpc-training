import json

with open('./words_dictionary.json') as input:
  words: dict[str, int] = json.load(input)

with open('./bigtestcase.txt', 'w') as output:
  for word in words.keys():
    if len(word) >= 16:
      output.write(word[:16] + '\n')
  output.close()

