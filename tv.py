from tradingview_ta import TA_Handler, Interval, Exchange

output = TA_Handler(symbol="fdf",
                    screener="russia",
                    exchange="MOEX",
                    interval=Interval.INTERVAL_1_MONTH)

print(output.get_analysis().oscillators)
print(output.get_analysis().moving_averages )