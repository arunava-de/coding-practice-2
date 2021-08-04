def normalize(email):

    local, domain = email.split('@')
    norm_local = ''

    for i in range(len(local)):
        if local[i] == '.':
            continue
        elif local[i] == '+':
            break 
        else:
            norm_local += local[i]

    return norm_local + '@' + domain 

def num_unique_emails(emails):

    emails = [normalize(e) for e in emails]

    return len(set(emails))
