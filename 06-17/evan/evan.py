# works yay

def main():
  n, *nums = map(int, input().split())
  print(nums)
  # create a list to keep track of which numbers we've already done, of length n - 1
  tracker = [False] * (n-1)
  for p in range(n - 1):
    res = abs(nums[p] - nums[p+1])
    # because lists are zero-indexed, we offset the tracker by the same amount
    if tracker[res-1] == False:
      tracker[res-1] = True
    else: # already ran into that number (repeats not allowed)
      print("Not jolly")
      return
  if tracker == [True] * (n-1):
    print("Jolly")
  else:
    print("Not jolly")

if __name__ == '__main__':
  main()