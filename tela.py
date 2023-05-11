from service.coin_market import CoinMarket
from service.ohlc_service import OHLCService

cm = CoinMarket()
criptomoeda = cm.obter_mercado('bitcoin', 7, 'hour')
print(criptomoeda.id_cripto, criptomoeda.name, criptomoeda.image)
print()


for ohlc in criptomoeda.mostrar_ohlc:
    print(ohlc.timestamp, ' ',  ohlc.open,
          ' ', ohlc.close, ' ', ohlc.high, ' ', ohlc.low)

for t in criptomoeda.listar_transacoes:
    print(t.preco, '-', t.timestamp)
