import requests

while(True):
    query = input("What type of news are you interested in? ")
    description = input("show description also?[y/n]: ")
    content = input("show content also?[y/n]: ")
        
    url = f"https://newsapi.org/v2/everything?q={query}&popularity&apiKey=d1f69ee125ac4256bf0c651883d3dafa"
    news = requests.get(url).json()
    # print(news, type(news))

    i = 1
    for article in news["articles"]:
        print("\n",f"{i}.",article["title"],":\n")
        print(article["description"],"\n") if description == "y" else ""
        print(article["content"]) if content == "y" else ""
        i = i + 1
        print("---------------------------------------------------------")
        
    exit = input("Exit? [y/n]: ")
    exit() if exit == "y" else ""        
        