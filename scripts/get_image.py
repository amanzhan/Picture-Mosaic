import requests
from PIL import Image
from io import BytesIO
import os
import json
import uuid

counter = 1
for i in range(6,11):
    filename = "file" + str(i) + ".json"
    with open(filename) as json_file:
        data = json.load(json_file)
        for hit in data["hits"]:
            url = hit["previewURL"]
            r = requests.get(url)
            try:
                i = Image.open(BytesIO(r.content))
                u = uuid.uuid4().hex
                i.save("output/" + str(u) + ".jpg")
            except:
                #woop
                continue

