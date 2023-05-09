from typing import Dict, List
from entidades.transacoes import Transacao


class Cryptomoeda:

    """Classe que representa uma criptomoeda
    """

    def __init__(self, json: Dict) -> None:

        self._id_cripto = json[0]['id']
        self._symbol = json[0]['symbol']
        self._name = json[0]['name']
        self._image = json[0]['image']
        self._current_price = json[0]['current_price']
        self._market_cap = json[0]['market_cap']
        self._market_cap_rank = json[0]['market_cap_rank']
        self._fully_diluted_valuation = json[0]['fully_diluted_valuation']
        self._total_volume = json[0]['total_volume']
        self._high_24h = json[0]['high_24h']
        self._low_24h = json[0]['low_24h']
        self._price_change_24h = json[0]['price_change_24h']
        self._price_change_percentage_24h = json[0]['price_change_percentage_24h']
        self._market_cap_change_24h = json[0]['market_cap_change_24h']
        self._market_cap_change_percentage_24h = json[0]['market_cap_change_percentage_24h']
        self._circulating_supply = json[0]['circulating_supply']
        self._total_supply = json[0]['total_supply']
        self._max_supply = json[0]['max_supply']
        self._ath = json[0]['ath']
        self._ath_change_percentage = json[0]['ath_change_percentage']
        self._ath_date = json[0]['ath_date']
        self._roi = json[0]['roi']
        self._last_updated = json[0]['last_updated']
        self._price_change_percentage_1h_in_currency = json[
            0]['price_change_percentage_1h_in_currency']
        self._price_change_percentage_1y_in_currency = json[
            0]['price_change_percentage_1y_in_currency']
        self._price_change_percentage_24h_in_currency = json[
            0]['price_change_percentage_24h_in_currency']
        self._price_change_percentage_30d_in_currency = json[
            0]['price_change_percentage_30d_in_currency']
        self._price_change_percentage_7d_in_currency = json[
            0]['price_change_percentage_7d_in_currency']
        self._transacoes = []

    @property
    def id_cripto(self):
        return self._id_cripto

    @property
    def symbol(self):
        return self._symbol

    @property
    def name(self):
        return self._name

    @property
    def image(self):
        return self._image

    @property
    def current_price(self):
        return self._current_price

    @property
    def market_cap(self):
        return self._market_cap

    @property
    def market_cap_rank(self):
        return self._market_cap_rank

    @property
    def fully_diluted_valuation(self):
        return self._fully_diluted_valuation

    @property
    def total_volume(self):
        return self._total_volume

    @property
    def high_24h(self):
        return self._high_24h

    @property
    def low_24h(self):
        return self._low_24h

    @property
    def price_change_24h(self):
        return self._price_change_24h

    @property
    def price_change_percentage_24h(self):
        return self._price_change_percentage_24h

    @property
    def market_cap_change_24h(self):
        return self._market_cap_change_24h

    @property
    def market_cap_change_percentage_24h(self):
        return self._market_cap_change_percentage_24h

    @property
    def circulating_supply(self):
        return self._circulating_supply

    @property
    def total_supply(self):
        return self._total_supply

    @property
    def max_supply(self):
        return self._max_supply

    @property
    def ath(self):
        return self._ath

    @property
    def ath_change_percentage(self):
        return self._ath_change_percentage

    @property
    def ath_date(self):
        return self._ath_date

    @property
    def roi(self):
        return self._roi

    @property
    def last_updated(self):
        return self._last_updated

    @property
    def price_change_percentage_1h_in_currency(self):
        return self._price_change_percentage_1h_in_currency

    @property
    def price_change_percentage_1y_in_currency(self):
        return self._price_change_percentage_1y_in_currency

    @property
    def price_change_percentage_24h_in_currency(self):
        return self._price_change_percentage_24h_in_currency

    @property
    def price_change_percentage_30d_in_currency(self):
        return self._price_change_percentage_30d_in_currency

    @property
    def price_change_percentage_7d_in_currency(self):
        return self._price_change_percentage_7d_in_currency

    def adicionar_trancacoes(self, transacao: Transacao):
        """Adiciona uma transação

        Args:
            transacao (Transacao): Um objeto trancacao
        """
        self._transacoes.append(transacao)

    @property
    def listar_transacoes(self) -> List[Transacao]:
        return self._transacoes
