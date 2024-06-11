from sys import stdin

def main():
  lists = stdin.read().split('\n\n')
  icpc, other = map(lambda x: x.split('\n'), lists)
  other.pop() # remove newline at end of file
  
  other_names = {}
  other_email = {}

  for line in other:
    [first, last, email] = line.split()
    name = ' '.join([first, last])
    other_names[name.lower()] = email
    other_email[email.lower()] = name

  icpc_mismatches = []
  for line in icpc:
    [first, last, email] = line.split()
    name = ' '.join([first, last])

    # if the email matches, remove it from both dictionaries
    if n := other_email.get(email.lower(), False):
      other_email.pop(email.lower())
      other_names.pop(n.lower())
      continue

    # if name matches, remove it from both dictionaries
    if e := other_names.get(name.lower(), False):
      other_names.pop(name.lower())
      other_email.pop(e.lower())
      continue

    # no match at all, so we add it to our mismatches
    icpc_mismatches.append(' '.join([email, name]))

  if len(icpc_mismatches) == 0 and len(other_email) == 0:
    print('No mismatches.')

  icpc_mismatches.sort(key=icpc_sort)
  for line in icpc_mismatches:
    [e, f, l] = line.split(' ')
    print('I', e, l, f)

  stuff = other_email.items()
  for (email, name) in sorted(stuff, key=stuff_sort):
    [f, l] = name.split(' ')
    print('O', email, l, f)

def icpc_sort(line):
  return line.lower()

def stuff_sort(thing):
  (email, _) = thing
  return email.lower()

if __name__ == '__main__':
  main()