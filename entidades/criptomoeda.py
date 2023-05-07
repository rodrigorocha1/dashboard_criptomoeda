import datetime


import datetime


class Crypto:
    def __init__(self, id: str, symbol: str, name: str, image: str, current_price: float, market_cap: float, market_cap_rank: int,
                 fully_diluted_valuation: int, total_volume: int, high_24h: float, low_24h: float, price_change_24h: float,
                 price_change_percentage_24h: float, market_cap_change_24h: float, market_cap_change_percentage_24h: float,
                 circulating_supply: float, total_supply: float,  max_supply: float, ath: float, ath_change_percentage: float,
                 ath_date: datetime.datetime, roi, last_updated: datetime.datetime, price_change_percentage_1h_in_currency: float,
                 price_change_percentage_1y_in_currency: float, price_change_percentage_24h_in_currency: float, price_change_percentage_30d_in_currency: float,
                 price_change_percentage_7d_in_currency: float
                 ) -> None:
        self._id = id
        self._symbol = symbol
        self._name = name
        self._image = image
        self._current_price = current_price
        self._market_cap = market_cap
        self._market_cap_rank = market_cap_rank
        self._fully_diluted_valuation = fully_diluted_valuation
        self._total_volume = total_volume
        self._high_24h = high_24h
        self._low_24h = low_24h
        self._price_change_24h = price_change_24h
        self._price_change_percentage_24h = price_change_percentage_24h
        self._market_cap_change_24h = market_cap_change_24h
        self._market_cap_change_percentage_24h = market_cap_change_percentage_24h
        self._circulating_supply = circulating_supply
        self._total_supply = total_supply
        self._max_supply = max_supply
        self._ath = ath
        self._ath_change_percentage = ath_change_percentage
        self._ath_date = ath_date
        self._roi = roi
        self._last_updated = last_updated
        self._price_change_percentage_1h_in_currency = price_change_percentage_1h_in_currency
        self._price_change_percentage_1y_in_currency = price_change_percentage_1y_in_currency
        self._price_change_percentage_24h_in_currency = price_change_percentage_24h_in_currency
        self._price_change_percentage_30d_in_currency = price_change_percentage_30d_in_currency
        self._price_change_percentage_7d_in_currency = price_change_percentage_7d_in_currency

    @property
    def id(self):
        return self._id

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
