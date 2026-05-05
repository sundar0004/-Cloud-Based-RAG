import requests
import json
import time

# wait for server to start
time.sleep(5)

response = requests.post(
    "http://127.0.0.1:8000/ask",
    json={"query": "What is retrieval-augmented generation?", "mode": "rag"}
)
print("Status code:", response.status_code)
print("Response JSON:")
print(json.dumps(response.json(), indent=2))
