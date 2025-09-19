import requests
import sys

SERVER_URL = "http://127.0.0.1:8000"

def upload(filepath):
    with open(filepath, "rb") as f:
        files = {"file": f}
        r = requests.post(f"{SERVER_URL}/upload/", files=files)
        print(r.json())

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python client.py upload <filepath>")
    elif sys.argv[1] == "upload":
        upload(sys.argv[2])
