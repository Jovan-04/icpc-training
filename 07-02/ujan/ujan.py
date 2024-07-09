from sys import stdin

stdin.readline()
heights = [int(x) for x in stdin.readline().split()]

area = 0

height = 0
l, r = 0, len(heights) - 1

while l + 1 < r:
    new_height = min(heights[l], heights[r])
    width = r - l - 1
    area += width * (new_height - height)
    height = new_height

    if heights[l] < heights[r]:
        while l + 1 < r and heights[l] <= height:
            l += 1
            area -= min(height, heights[l])
    else:
        while l + 1 < r and heights[r] <= height:
            r -= 1
            area -= min(height, heights[r])

print(area)
