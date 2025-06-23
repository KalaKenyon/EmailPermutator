def generate_email(name, domain, pattern):
    first, last = name.lower().split()
    if pattern == "first.last":
        return f"{first}.{last}@{domain}"
    elif pattern == "f.last":
        return f"{first[0]}.{last}@{domain}"
    elif pattern == "first":
        return f"{first}@{domain}"
    return None
