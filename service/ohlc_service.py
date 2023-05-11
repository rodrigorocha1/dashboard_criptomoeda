from service.coingecko_ping import CoinGeckoAPI
import requests
from entidades.ohlc import OHLC


class OHLCService:
    def __init__(self) -> None:
        self._ping = CoinGeckoAPI()
        self._url = 'https://api.coingecko.com/api/v3/coins'

    def obter_ohlc(self, id_cripto: str, days: int):
        """Obtem as transações da criptomoeda

        Args:
            id_cripto (str): id Ex bitcoin
            days (int): intervalo de dias 1/7/14/30/90/180/365/max

        Returns:
            _type_: json de preços
        """
        url = f'{self._url}/{id_cripto}/ohlc?vs_currency=brl&days={days}'
        if self._ping.testar_conexao() == 200:
            req_ohlc = requests.get(url)

            ohcl = OHLC(req_ohlc.json())
            return ohcl
