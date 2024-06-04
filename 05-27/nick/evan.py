def main():
  for line in open('input.txt').read().splitlines():
    print(calculate_num_substrings(line))

def calculate_num_substrings(line: str) -> int:
  min_proper_substrings = set()

  # generate all substrings
  all_substrings = [line[i: j] for i in range(len(line))
                    for j in range(i + 1, len(line) + 1)]

  # remove duplicates & the string itself
  unique_prop_substrings = set(all_substrings)
  unique_prop_substrings.remove(line)

  # calculate all periods
  substr_to_per = dict()
  for string in unique_prop_substrings:
    substr_to_per[string] = period_of_str(string)

  # only count substrings that are minimal, and ones that have the same period as full string
  full_string_period = period_of_str(line)
  for (k, v) in substr_to_per.items():
    if period_of_str(k[1:]) == v or period_of_str(k[:-1]) == v:
      continue

    if v == full_string_period: 
      min_proper_substrings.add(k)


  return len(min_proper_substrings)

def period_of_str(s: str) -> set[str]:
  period = set()
  for char in s:
    period.add(char)
  return period
  

if __name__ == '__main__':
  main()