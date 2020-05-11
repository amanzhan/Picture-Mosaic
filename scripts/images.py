import requests
import os
import sys

#Get 1000 bb
for i in range(6,11):
    url = "https://pixabay.com/api/?key=16301324-61a8310fb58d44417389284dc&q=animals&image_type=photo&per_page=200&p=" + str(i)
    r = requests.get(url)
    filename = "file" + str(i) + ".json"
    fd = os.open(filename,os.O_CREAT|os.O_RDWR)
    os.write(fd, r.text.encode())
    os.close(fd)
