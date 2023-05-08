import requests


class CoinGeckoAPI:
    def __init__(self) -> None:
        self._url = 'https://api.coingecko.com/api/v3/ping'

    def testar_conexao(self) -> int:
        req = requests.get(url=self._url)
        return req.status_code
