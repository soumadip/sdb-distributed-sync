import requests
import sys
from pathlib import Path

SERVER_URL = "http://127.0.0.1:8000"

def upload(filepath):
    with open(filepath, "rb") as f:
        files = {"file": f}
        r = requests.post(f"{SERVER_URL}/upload/", files=files)
        print(r.json())

def download_file(filename: str, save_dir="downloads"):
    url = f"{SERVER_URL}/download/{filename}"
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        Path(save_dir).mkdir(exist_ok=True)
        file_path = Path(save_dir) / filename
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded {filename} -> {file_path}")
    else:
        print(f"Error: {response.json()}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python client.py upload <filepath>")
    elif sys.argv[1] == "upload":
        upload(sys.argv[2])
    elif sys.argv[1] == "download":
        download_file(sys.argv[2])
