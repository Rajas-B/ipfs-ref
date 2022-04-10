import requests
from pathlib import Path

filepath = "./rajas.JPG"
with Path(filepath).open("rb") as fp:
    rajas_binary=fp.read()
with Path("./trek.PNG").open("rb") as fp:
    trek_binary = fp.read()
print(type(rajas_binary))
# resp = requests.post("http://127.0.0.1:5001/api/v0/add", files={"rajas": rajas_binary, "trek": trek_binary}, params={"wrap-with-directory": "true"})
resp = requests.post("http://127.0.0.1:5001/api/v0/add", files={"rajas": rajas_binary})
# 
# print(resp)
print(resp.content)
ipfs_hash=resp.json()["Hash"]
print(ipfs_hash)
# filename=filepath.split("/")[-1:][0]
# image_uri=f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
# print("image uri on ipfs",image_uri)