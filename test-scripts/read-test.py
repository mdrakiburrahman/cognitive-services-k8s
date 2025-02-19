import requests
import json
import time

external_ip = "20.121.145.67"

# Sync
print("####################### SYNC #######################")

endpoint = 'http://'+ external_ip +':5000/vision/v3.2/read/syncAnalyze'

file = 'https://raw.githubusercontent.com/mdrakiburrahman/cognitive-services-k8s/main/test-files/mortgage.pdf'
response = requests.post(endpoint, \
                         headers={'accept': 'application/json'
                         , 'Content-Type': 'application/json'},
                         json={'url': file
                         })

print(json.dumps(json.loads(response.content), indent=4, sort_keys=True))

# Async
print("####################### ASYNC #######################")

endpoint = 'http://'+ external_ip +':5000/vision/v3.2/read/analyze'

response = requests.post(endpoint, headers={"accept": "application/json", 
                        "Content-Type" : "application/json"},  
                        json={'url': file
                        })

print(response)
print(response.headers)

# Get Async response back
response_url = response.headers["Operation-Location"]
succeeded = 0

while succeeded != 1:
  response = requests.get(response_url)
  print(response.content)
  j = response.json() 
  
  print("Status: " + j["status"])
  
  if j["status"] == "succeeded":
    succeeded = 1

  time.sleep(5)