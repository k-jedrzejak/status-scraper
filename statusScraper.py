import requests
from bs4 import BeautifulSoup
import subprocess
import os

login_url = 'website/url'

# make sure your payload keys are the same as the keys on the website you logged in to
payload = {
    'UserLoginID': 'Your User ID',
    'UserPassword': 'Your Password'
}

session = requests.Session()

response = session.get(login_url)
soup = BeautifulSoup(response.content, 'html.parser')

hidden_inputs = soup.find_all("input", type="hidden")
for hidden_input in hidden_inputs:
    payload[hidden_input['name']] = hidden_input['value']

login_response = session.post(login_url, data=payload)

if login_response.url != login_url:
    print("You have logged in successfully")
    
    secured_page_url = 'website/url'
    secured_page_response = session.get(secured_page_url)
    secured_page_content = secured_page_response.content
    html_content = secured_page_content.decode('utf-8')

    soup = BeautifulSoup(html_content, 'html.parser')

    # match the item you want to get information from
    status_div = soup.find('div', class_='media-account-pending-status')
    pending_status = status_div.get_text(separator='\n').strip()  
    lines = [line.strip() for line in pending_status.splitlines() if line.strip()]
    formatted_text = "\n".join(lines) 

    
    # Path to the file with the previous state
    status_file_path = '/path/to/checkStatus/previous_status.txt'
    
    if os.path.exists(status_file_path):
        with open(status_file_path, 'r') as file:
            previous_status = file.read().strip()
    else:
        previous_status = ""
    
    
    if formatted_text != previous_status:
        with open(status_file_path, 'w') as file:
            file.write(formatted_text)
            subprocess.run(['osascript', '/path/to/checkStatus/notify.scpt', formatted_text])
    else:
        print("The status has not changed")

else:
    print("Login error")