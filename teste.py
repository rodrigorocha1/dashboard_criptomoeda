import requests

# substitua "nome_do_jogo" pelo nome do jogo que você quer procurar
jogo = "Genshin Impact"

url = f"https://api.twitch.tv/helix/games?name={jogo}"
headers = {"Client-ID": "mgmjyzbawewj49w7z46t343o6xkb26",
           "Authorization": "Bearer bdmpjydl7tq0q9g3img94al6sf3gw5"}

response = requests.get(url, headers=headers)

data = response.json()
if data["data"]:
    box_art_url = data["data"][0]["box_art_url"].format(width=285, height=380)
    print(box_art_url)
else:
    print("Jogo não encontrado.")
