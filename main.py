import eel
from tradingview_ta import TA_Handler, Interval

def info_product_tv(ticket):
    info = {"valid" : True, "status":"Успешно"}
    try:
        output = TA_Handler(symbol=ticket,
                    screener="russia",
                    exchange="MOEX",
                    interval=Interval.INTERVAL_1_MONTH)
        info["oscillators"] = output.get_analysis().oscillators
        info["moving_averages"] = output.get_analysis().moving_averages

    except Exception as e:
        info["status"] = str(e)

    return info

@eel.expose
def info_product(type_product, ticket):
    if type_product == "stocks":
        info = info_product_tv(ticket)

    return info

eel.init("web")
eel.start("index.html")

output = TA_Handler(symbol="SBER",
                    screener="russia",
                    exchange="MOEX",
                    interval=Interval.INTERVAL_1_MONTH)
