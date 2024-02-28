import requests

url = "https://wallpapercave.com/wp/wp6806679.jpg"

r = requests.get(url)

with open("file.jpg", "wb") as f:
    f.write(r.content)