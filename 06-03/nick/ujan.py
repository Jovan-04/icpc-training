from sys import stdin

cased1 = {}
db1_names = {}
db1_emails = {}
for line in stdin:
    if not line.strip():
        break
    
    first, last, cased_email = line.split()
    cased_name = last + ' ' + first
    
    name = cased_name.casefold()
    email = cased_email.casefold()
    
    cased1[name] = cased_name
    cased1[email] = cased_email

    db1_names[name] = email
    db1_emails[email] = name

cased2 = {}
db2_names = {}
db2_emails = {}
for line in stdin:
    skip = False

    first, last, cased_email = line.split()
    cased_name = last + ' ' + first
    
    name = cased_name.casefold()
    email = cased_email.casefold()
    
    if name in db1_names:
        skip = True
        email1 = db1_names[name]
        del db1_emails[email1]
        del db1_names[name]
    
    if email in db1_emails:
        skip = True
        name1 = db1_emails[email]
        del db1_names[name1]
        del db1_emails[email]
    
    if not skip:
        cased2[name] = cased_name
        cased2[email] = cased_email
        db2_names[name] = email
        db2_emails[email] = name

if db1_emails or db2_emails:
    for email in sorted(db1_emails):
        print('I', cased1[email], cased1[db1_emails[email]])
    for email in sorted(db2_emails):
        print('O', cased2[email], cased2[db2_emails[email]])
else:
    print('No mismatches.')
