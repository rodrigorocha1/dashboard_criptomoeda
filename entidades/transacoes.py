from datetime import datetime


class Transacao:
    """Classe que representa uma transacao

    """

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

    def __init__(self,  timestamp: int, preco: float,) -> None:
        """Construtor da classe 

        Args:
            preco (float): preço da criptomoeda
            timestamp (int): timestamp da transacao
        """

        self._preco = preco
        self._timestamp = self._converter_timestamp(timestamp)

    @property
    def timestamp(self) -> str:
        """retorna o valor sem modificar

        Returns:
            str: data e hora Ex: 10-08-2020 20:00:00 
        """
        return self._timestamp

    @property
    def preco(self) -> str:
        """retorna o valor sem modificar

        Returns:
            str: data e hora Ex: 10-08-2020 20:00:00 
        """
        return self._preco
