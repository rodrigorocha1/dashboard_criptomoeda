from entidades.transacoes import Transacao
from service.coingecko_ping import CoinGeckoAPI
import requests
from entidades.criptomoeda import Cryptomoeda
from service.transacao_service import TransacaoService


class CoinMarket:
    def __init__(self) -> None:
        self._ping = CoinGeckoAPI()
        self._url = 'https://api.coingecko.com/api/v3/coins/markets?'

    def obter_mercado(self, ids: str, days: str, intervalo: str):
        """Método para obter o mercado da criptomoeda

        Args:
            ids (str): id da criptomoeda
            days (str): dias 
            intervalo (str): day, monthy year

        Returns:
            _type_: Objeto criptomoeda
        """

        url = f'{self._url}vs_currency=brl&ids={ids}&order=market_cap_desc&price_change_percentage=1h,24h,7d,30d,1y&locale=pt'
        if self._ping.testar_conexao() == 200:
            req = requests.get(url)
            criptomoeda = Cryptomoeda(req.json())
            transacao_service = TransacaoService()
            transacoes = transacao_service.obter_transacoes(
                ids, days, intervalo)
            for transacao in transacoes:
                criptomoeda.adicionar_trancacoes(
                    Transacao(timestamp=transacao[0], preco=transacao[1]))
            return criptomoeda
