from service.coingecko_ping import CoinGeckoAPI
import requests


class CoinMarket:
    def __init__(self) -> None:
        self._ping = CoinGeckoAPI()
        self._url = 'https://api.coingecko.com/api/v3/coins/markets?'

    def obter_mercado(self, ids: str):
        """Obtem as informações do mercado de acordo com a criptomoeda

        Args:
            ids (str): id da criptomoeda EX: bitcoin

        Returns:
            _type_: _description_
        """
        url = f'{self._url}vs_currency=brl&ids={ids}&order=market_cap_desc&price_change_percentage=1h,24h,7d,30d,1y&locale=pt'
        if self._ping.testar_conexao() == 200:
            req = requests.get(url)
            return req.json()
