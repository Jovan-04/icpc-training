def main():
  k, n = map(int, input().split())
  # ensure that the cards can be split into equal groups
  if n % k != 0:
    print("unfair")
    return
  
  # sort list
  nums = sorted(map(int, input().split()))
  groups = []
  
  # split into groups of k-size numbers
  for i in range(0, n, k):
    tmp = []
    for j in range(k):
      tmp.append(nums[i+j])
    groups.append(tmp)

  # check if groups are continuous
  for g in groups:
    if not is_consecutive(g):
      print("unfair")
      return
  
  # all groups are continuous, thus the hand is fair
  print("fair")
  
def is_consecutive(group: list[int]) -> bool:
  n, *nums = group
  for num in nums:
    if num == n + 1:
      n = num
    else: 
      return False
  return True

if __name__ == '__main__':
  main()