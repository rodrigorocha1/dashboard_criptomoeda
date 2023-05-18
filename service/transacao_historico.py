from service.coingecko_ping import CoinGeckoAPI
import requests
from entidades.transacoes import Transacao


class TransacaoHistorico:
    def __init__(self) -> None:
        self._ping = CoinGeckoAPI()
        self._url = 'https://api.coingecko.com/api/v3/coins'

    def obter_transacoes_historico(self, id_cripto: str, timestamp_inicial: int, timestamp_final: str):
        """Obtem as transações da criptomoeda

        Args:
            id_cripto (str): id Ex bitcoin
            days (int): intervalo de dias 2
            interval (str): days, month, year

        Returns:
            _type_: json de preços
        """
        url = f'{self._url}/{id_cripto}/market_chart?vs_currency=brl&from={timestamp_inicial}&to={timestamp_final}'
        if self._ping.testar_conexao() == 200:
            prices = requests.get(url)
            return prices.json()['prices']
