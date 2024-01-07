def update_domain(email, new_domain, old_domain):
    if '@' + old_domain in email:
        index = email.index('@' + old_domain)
        new_email = email[:index] + '@' + new_domain
        return new_email
    return email

emails = ['james@olddomain.com', 'marycook@olddomain1.com', 'joseph@veryold.com', 'janedoe@gmail.com', 'johndoe@oldhotm.com']
new_emails = []

old_domains = ['olddomain', 'olddomain1', 'oldhotm.com', 'veryold.com']
for old_domain in old_domains:
    for email in emails:
        if old_domain in email:
            new_emails.append(update_domain(email, 'gmail.com', old_domain))
for email in new_emails:
    print(email)

