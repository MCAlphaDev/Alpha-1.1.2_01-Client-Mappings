import urllib.request
import os

def download(file):
    loc = "./dontpush/" + file.split("/")[-1]
    if (not os.path.exists(loc)):
        urllib.request.urlretrieve(file, loc)
    else:
        print("File Already Exists: " + loc)


if not os.path.exists("./dontpush"):
    os.makedirs("./dontpush")

download("https://launcher.mojang.com/v1/objects/daa4b9f192d2c260837d3b98c39432324da28e86/client.jar")
