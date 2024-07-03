import json

with open('./words_dictionary.json') as input:
  words: dict[str, int] = json.load(input)

with open('./bigtestcase7.txt', 'w') as output:
  for word in words.keys():
    if len(word) == 7:
      output.write(word[:7] + '\n')
  output.close()

