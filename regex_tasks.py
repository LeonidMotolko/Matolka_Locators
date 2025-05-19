import re

# Task 1: Username & Password
username_pattern = re.compile(r'^[a-zA-Z0-9]+$')
password_pattern = re.compile(r'^[a-zA-Z0-9]{8}$')

print(bool(username_pattern.match("user123")))  # True
print(bool(password_pattern.match("pass1234"))) # True

# Task 2: Email validation
email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.(com|net|org)$')
print(bool(email_pattern.match("test@example.com")))  # True
print(bool(email_pattern.match("user@domain")))       # False

# Task 3: Extract timestamps
log_text = """
[2024-09-01 14:32:00] ERROR: NullPointerException at line 23
[2024-09-01 14:33:15] WARN: Memory usage high
[2024-09-01 14:35:47] INFO: System started
"""
timestamps = re.findall(r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]', log_text)
print(timestamps)

# Task 4: Phone numbers
phone_pattern = re.compile(r'^(\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4})$')
print(bool(phone_pattern.match("(555) 555-5555")))  # True
print(bool(phone_pattern.match("1234567890")))      # False

# Task 5: URLs
url_pattern = re.compile(r'^https?://[\w.-]+\.(com|net|org)')
domain_extractor = re.compile(r'https?://(www\.[\w.-]+)')

print(bool(url_pattern.match("https://example.com")))
print(domain_extractor.search("https://www.test.com/page?param=value").group(1))  # paste youre links

# Task 6: Extract from HTML
html_content = """
<div class="product" data-id="101">
    <span class="product-name">Laptop</span>
    <span class="price">$1200</span>
</div>
<div class="product" data-id="102">
    <span class="product-name">Smartphone</span>
    <span class="price">$800</span>
</div>
"""
products = re.findall(r'data-id="(\d+)".*?<span class="price">(\$\d+)</span>', html_content, re.DOTALL)
for pid, price in products:
    print(f"Product ID: {pid}, Price: {price}")

# Task 7: Date validation
date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
print(bool(date_pattern.match("2024-09-01")))  # True
print(bool(date_pattern.match("01-09-2024")))  # False

# Task 8: Complex password
complex_password_pattern = re.compile(
    r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$]).{8,}$'
)
print(bool(complex_password_pattern.match("Passw0rd@123")))  # True
print(bool(complex_password_pattern.match("password")))       # False

# Task 9: Split string
text = "apple, banana; orange,grape;pear"
parts = re.split(r'\s*[,;]\s*', text)
print(parts)
