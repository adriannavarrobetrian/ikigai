import requests
import sys
import os

folder_name = "./files"
base_url = "http://ikigaitestbucket.s3-website-eu-west-1.amazonaws.com/"
filename = "required_files.json"

try:
    data = requests.get(base_url + filename).json()
except requests.exceptions.RequestException as e:
    print("Failed to retrieve the JSON file.")
    sys.exit(1)

if not os.path.exists(folder_name):
    os.makedirs(folder_name)

for item in data:
    file = item.get('output', base_url.split('/')[-1])
    protocol = item.get('protocol')
    base_url = item.get('url')

    if item.get('output') is not None:
        file_path = os.path.join(folder_name, item.get('output'))
    else:
        file_path = os.path.join(folder_name, file)

    try:
        response = requests.get(item.get('protocol') + '://' + item.get('url'), verify=True, timeout=3)
    except requests.exceptions.RequestException as e:
        print(e)

    if response.status_code == 200:
        with open(file_path, "wb") as file:
            file.write(response.content)
        print("File written.")

print("All downloads completed.")