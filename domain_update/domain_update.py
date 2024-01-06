def update_domain(email, new_domain, old_domain):
    if '@' + old_domain in email:
        index = email.index('@' + old_domain)
        new_email = email[:index] + '@' + new_domain
        return new_email
    return email

emails = ['james@outlook.com', 'marycook@outlook.com', 'joseph@outlook.com', 'janedoe@gmail.com']
new_emails = []

for email in emails:
    new_emails.append(update_domain(email, 'gmail.com', 'outlook.com'))

for email in new_emails:
    print(email)

