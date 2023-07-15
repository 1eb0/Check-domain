# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name
# pylint: disable=missing-function-docstring
# pylint: disable=import-error
# pylint: disable=missing-timeout

from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from url_validation import validated_url

# Specify the URL of the website you want to inspect
url = validated_url

# Send a GET request to retrieve the webpage content
response = requests.get(url)


# Check if the request was successful (status code 200 indicates success)
if response.status_code == 200:
    # Get the HTML content of the webpage
    html_content = response.text

    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(html_content, "html.parser")

    # Find all the links on the webpage
    links = soup.find_all("a")

    # Extract and print the links
    for link in links:
        href = link.get("href")

        # Create an absolute URL by joining the relative URL with the base URL
        absolute_url = urljoin(url, href)
        print(absolute_url)
else:
    print("Error:", response.status_code)
