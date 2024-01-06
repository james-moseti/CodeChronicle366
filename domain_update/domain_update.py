def update_domain(email, new_domain, old_domain):
    if '@' + old_domain in email:
        index = email.index('@' + old_domain)
        new_email = email[:index] + '@' + new_domain
        return new_email
    return email

emails = ['james@outlook.com', 'marycook@yahoo.com', 'joseph@outlook.com', 'janedoe@gmail.com', 'johndoe@hotmail.com']
new_emails = []

old_domains = ['outlook.com', 'yahoo.com', 'hotmail.com', 'aol.com']
for old_domain in old_domains:
    for email in emails:
        if old_domain in email:
            new_emails.append(update_domain(email, 'gmail.com', old_domain))
for email in new_emails:
    print(email)

