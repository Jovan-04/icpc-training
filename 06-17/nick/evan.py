# start with a string of all 'a's, and increment them one position and one character at a time
# wrong answer over input of n = 251 (no longer only english lowercase letters)
def main():
  WORD_LENGTH = 10
  n = int(input())
  if n == 0:
    return
  c = 0
  # 97 is the ascii code for 'a' - we initialize an array of 'a's, and 
  word = [97] * WORD_LENGTH
  while True:
    for i in range(WORD_LENGTH):
      print(''.join(map(chr, word)))
      word[i] += 1
      c += 1
      if c == n:
        return

if __name__ == '__main__':
  main()