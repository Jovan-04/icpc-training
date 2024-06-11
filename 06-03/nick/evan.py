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
    other_names[name] = email
    other_email[email] = name

  icpc_mismatches = []
  for line in icpc:
    [first, last, email] = line.split()
    name = ' '.join([first, last])

    # if the email matches, remove it from both dictionaries
    if n := other_email.get(email, False):
      other_email.pop(email)
      other_names.pop(n)
      continue

    # if name matches, remove it from both dictionaries
    if e := other_names.get(name, False):
      other_names.pop(name)
      other_email.pop(e)
      continue

    # no match at all, so we add it to our mismatches
    icpc_mismatches.append(' '.join([email, name]))

  if len(icpc_mismatches) == 0 and len(other_email) == 0:
    print('No mismatches.')

  for line in icpc_mismatches:
    print('I', line)

  for (email, name) in other_email.items():
    print('O', email, name)


if __name__ == '__main__':
  main()