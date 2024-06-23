def main():
  w, s, c, k = map(int, input().split())
  if max(w, s, c) > k and sum([w, s, c]) / 3 > k:
    print("NO")
  else:
    print("YES")

if __name__ == '__main__':
  main()