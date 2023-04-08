import os
import requests
import json

url = "http://127.0.0.1:8000/query"
headers = {"Authorization": "Bearer " + os.getenv("BEARER_TOKEN"), "Content-Type": "application/json"}

data = {
    "queries": [
        {
            "query": "was there any evidence of malfeasance in the management behaviour of enron",  #"who was the ceo of enron",  #"revenue generating services", #"customer names",
            # "filter": {
            #     "document_id": "string",
            #     "source": "email",
            #     "source_id": "string",
            #     "author": "string",
            #     "start_date": "string",
            #     "end_date": "string",
            # },
            "top_k": 3,
        }
    ]
}

response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.json())