import json
import requests


url = "http://ikigaitestbucket.s3-website-eu-west-1.amazonaws.com/"
filename = "required_files.json"

print (f"\nEl link es: {url}{filename}")

#download file from url as json
response = requests.get(url+filename)

if response.status_code == 200:
    data = response.json()
else:
    print("Failed to retrieve the JSON file.")

print(data)

# for i in file:
#      print(file[i]['url'])
#     # print(file[i]['protocol'])
#     # print(file[i]['output'])
#     # print(f"\n")


# # Load the JSON data from a file
# with open('file.json', 'r') as json_file:
#     data = json.load(json_file)

# # Loop through the JSON objects and download the files
# for item in data:
#     protocol = item['protocol']
#     url = item['url']
#     filename = item.get('output', url.split('/')[-1])  # Use the last part of the URL as the default filename
#     try:
#         if protocol == 'https':
#             url = f"https://{url}"  
#             if 'insecure' in item and item['insecure'].lower() == 'true':
#                 response = requests.get(url, verify=False,timeout=2)
#             else:
#                 response = requests.get(url,timeout=2)
#         elif protocol == 'http':
#             url = "http://{url}"  
#             response = requests.get(url,timeout=2)
#         else:
#             print(f"Unsupported protocol: {protocol}")
#             continue
#         print(f"Downloaded {filename}")
#     except requests.exceptions.Timeout:
#         print(f"Timeout error while trying to download {url}")
        
# print("All downloads completed.")
