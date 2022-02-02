import re

pattern = r'([\w+.-]+)@([\w.]+)'
emails = []
with open('text.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        email = re.findall(pattern, line)
        emails.append(email[0])


if emails:
    print(emails)

with open('emails.txt', 'w') as f:
    for email in emails:
        f.write(f"Username: {email[0]}   Host: {email[1]}")
        f.write("\n")
