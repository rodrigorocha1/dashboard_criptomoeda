from datetime import datetime


class OHLC:

    @staticmethod
    def _converter_timestamp(timestamp: int) -> str:
        """Converte timestamp para hora no formato dd-mm-AAAA

        Args:
            timestamp (int): timestamp

        Returns:
            str: data e hora Ex: 10-08-2020 20:00:00
        """

        timestamp = timestamp // 1000
        data = datetime.fromtimestamp(timestamp)
        # data_str_formato = '%d-%m-%Y %H:%M:%S'
        # data = data.strftime(data_str_formato)
        return data

    def __init__(self, timestamp: int, open_hc: float, hight: float, low: float, close: float) -> None:
        """Contrutor OHLC

        Args:
            timestamp (int): Timestamp
            open_hc (float): preço abertura
            hight (float): preço alta
            low (float): preço baixa
            close (float): preço fechamento
        """

        self._data_hora = self._converter_timestamp(timestamp)
        self._open = open_hc
        self._high = hight
        self._low = low
        self._close = close

    @property
    def data_hora(self):
        return self._data_hora

    @property
    def open(self):
        return self._open

    @property
    def high(self):
        return self._high

    @property
    def low(self):
        return self._low

    @property
    def close(self):
        return self._close
