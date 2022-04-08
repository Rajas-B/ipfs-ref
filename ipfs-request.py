import requests
from pathlib import Path
headers = {
    "Content-Disposition": "form-data",
    "name": "file",
    "filename": "folderName",
    "Content-Type": "application/x-directory",
}
filepath = "./rajas.JPG"
with Path(filepath).open("rb") as fp:
    image_binary=fp.read()
with Path("./trek.PNG").open("rb") as fp:
    pic_binary = fp.read()
resp = requests.post("http://127.0.0.1:5001/api/v0/add", files={"rajas": image_binary, "trek": pic_binary}, params={"wrap-with-directory": "true"})
print(resp)
print(resp.content)
ipfs_hash=resp.json()["Hash"]
filename=filepath.split("/")[-1:][0]
image_uri=f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
print("image uri on ipfs",image_uri)