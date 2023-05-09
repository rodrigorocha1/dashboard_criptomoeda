from service.coingecko_ping import CoinGeckoAPI
import requests
from entidades.transacoes import Transacao


class TransacaoService:
    def __init__(self) -> None:
        self._ping = CoinGeckoAPI()
        self._url = 'https://api.coingecko.com/api/v3/coins'

    def obter_transacoes(self, id_cripto: str, days: int, interval: str):
        """Obtem as transações da criptomoeda

        Args:
            id_cripto (str): id Ex bitcoin
            days (int): intervalo de dias 2
            interval (str): days, month, year

        Returns:
            _type_: json de preços
        """
        url = f'{self._url}/{id_cripto}/market_chart?vs_currency=brl&days={days}&interval={interval}'
        if self._ping.testar_conexao() == 200:
            prices = requests.get(url)
            return prices.json()['prices']
