from urllib.parse import urlparse, urlunparse


def validate_url(url):
    parsed_url = urlparse(url)

    # Check if scheme is missing
    if not parsed_url.scheme:
        url = 'http://' + url

    # Check if "https://www." is present at the beginning of the string
    if not url.startswith('https://www.'):
        url = url.replace('http://', 'https://www.')

    # Check if top-level domain is already included
    top_level_domains = ['.com', '.net', '.org', '.edu', '.gov', 'co', 'io']
    domain = parsed_url.netloc.lower()

    if any(domain.endswith(tld) for tld in top_level_domains):
        # Check if a "/" is present after the top-level domain
        if parsed_url.path and parsed_url.path != '/':
            # Fix the "https://www." prefix
            url = 'https://www.' + domain + parsed_url.path

    else:
        # Check if ".com" is missing at the end of the string
        if not any(url.endswith(tld) for tld in top_level_domains):
            url = url.rstrip('/') + '.com'

    corrected_url = urlunparse(urlparse(url))
    return corrected_url


user_input = input("Enter a Domain name: ")
validated_url = validate_url(user_input)
print("Validated URL:", validated_url)
