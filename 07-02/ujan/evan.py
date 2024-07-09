# it works?

def main():
  n = int(input())
  heights = [*map(int, input().split())]
  rows = [[0] * n for _ in range(max(heights))]

  # generate the 2d water table (leetcode pic)
  for h, row in enumerate(rows, 1):
    for i, height in enumerate(heights):
      if height >= h:
        row[i] = 1

  # calculate the water in each row
  total_water = 0
  for row in rows:
    # find first and last index of a wall
    first = row.index(1)
    last = list_rindex(row, 1)

    # everything in between will be water
    space_btwn = (last - first) - 1

    # no space between outermost walls
    if space_btwn <= 0:
      continue

    # except for the other walls
    water_btwn = row[first:last].count(0)

    total_water += water_btwn
    print(row)
    print(first, last)
    print(water_btwn)

  print(total_water)

# from https://stackoverflow.com/questions/6890170/how-to-find-the-last-occurrence-of-an-item-in-a-python-list
def list_rindex(li, x):
    for i in reversed(range(len(li))):
        if li[i] == x:
            return i
    raise ValueError("{} is not in list".format(x))

if __name__ == '__main__':
  main()