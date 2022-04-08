import requests
from pathlib import Path
from PIL import Image
import io

headers = {
    "Content-Disposition": "form-data",
    "name": "file",
    "filename": "folderName",
    "Content-Type": "application/x-directory",
}
# resp = requests.post("http://127.0.0.1:5001/api/v0/object/get?arg=QmSau2JosdfFiWpxn2KjZNG55QihfQzGKSaXUcceF5p5iF&encoding=json")
# resp = requests.post("http://127.0.0.1:5001/api/v0/dag/get?arg=QmSau2JosdfFiWpxn2KjZNG55QihfQzGKSaXUcceF5p5iF&output-codec=dag-json")
# resp = requests.post("http://127.0.0.1:5001/api/v0/files/read?arg=/ipfs/QmSau2JosdfFiWpxn2KjZNG55QihfQzGKSaXUcceF5p5iF")
resp = requests.post("http://127.0.0.1:5001/api/v0/cat?arg=QmSau2JosdfFiWpxn2KjZNG55QihfQzGKSaXUcceF5p5iF")
image_file = io.BytesIO(resp.content)
image = Image.open(image_file)
file_path = "./best.png"

with open(file_path, "wb") as f:
    image.save(f, "png")