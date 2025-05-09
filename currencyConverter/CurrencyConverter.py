from os import getenv
from requests import get
from dotenv import load_dotenv

load_dotenv()
API_KEY = getenv("API_KEY")

print("Curency Converter v1.0\n")

try:
    while True:
        try:
            fromAmount = float(input("Zadej množství pěnez: "))
        except ValueError:
            print("Zadali jste neplatnou hodnotu!\nHodnota musí být číslo!\n")
            continue
        fromCurrency = input("Zadej měnu ze které převádíš (EUR, CZK, USD, JPY): ")
        if not any(fromCurrency == currency for currency in ["EUR", "CZK", "USD", "JPY"]):
            print("Měna je neplatná!\n")
            continue
        toCurrency = input("Zadej měnu do které převádíš (EUR, CZK, USD, JPY): ")
        if not any(toCurrency == currency for currency in ["EUR", "CZK", "USD", "JPY"]):
            print("Měna je neplatná!\n")
            continue
        res = get(f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{fromCurrency}/{toCurrency}").json()
        print(f"{fromAmount} {fromCurrency} = {fromAmount * res["conversion_rate"]} {toCurrency}")
except KeyboardInterrupt:
    exit(0)

