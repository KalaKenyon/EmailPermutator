# Email Permutator for OSINT

This script generates email address permutations based on a person's name, a known domain, and an email pattern (e.g., `first.last`, `f.last`, or `first`). It's useful for OSINT, red teaming, or recon workflows when you know an organization’s email format.

## 📄 Function Overview

```python
def generate_email(name, domain, pattern):
    first, last = name.lower().split()
    if pattern == "first.last":
        return f"{first}.{last}@{domain}"
    elif pattern == "f.last":
        return f"{first[0]}.{last}@{domain}"
    elif pattern == "first":
        return f"{first}@{domain}"
    return None
```

## 🚀 Usage

1. Save the function in a file named `generate_email.py` or include it in your project.
2. Call the function with a full name, domain, and desired pattern.

### 💡 Example:

```python
email = generate_email("Jane Doe", "example.com", "first.last")
print(email)  # Output: jane.doe@example.com
```

## 🎯 Supported Patterns

- `first.last` → `jane.doe@example.com`
- `f.last` → `j.doe@example.com`
- `first` → `jane@example.com`

## 🔐 Requirements

- Python 3+
- No external libraries required

## 🛡️ Disclaimer

This script is intended for educational, ethical, and legal use only. Use responsibly within the scope of OSINT, red teaming, or authorized testing engagements.

