import sys  # noqa: INP001
from os import getenv

from dotenv import load_dotenv
from requests import get

load_dotenv()
API_KEY = getenv("API_KEY")

print("Curency Converter v1.0\n")

try:
    while True:
        try:
            fromamount = float(input("Zadej množství pěnez: "))
        except ValueError:
            print("Zadali jste neplatnou hodnotu!\nHodnota musí být číslo!\n")
            continue
        fromcurrency = input("Zadej měnu ze které převádíš (EUR, CZK, USD, JPY): ")
        if not any(
            fromcurrency == currency for currency in ["EUR", "CZK", "USD", "JPY"]
        ):
            print("Měna je neplatná!\n")
            continue
        tocurrency = input("Zadej měnu do které převádíš (EUR, CZK, USD, JPY): ")
        if not any(tocurrency == currency for currency in ["EUR", "CZK", "USD", "JPY"]):
            print("Měna je neplatná!\n")
            continue
        res = get(
            f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{fromcurrency}/{tocurrency}",
            timeout=10,
        ).json()
        print(
            f"{fromamount} {fromcurrency} = {fromamount * res['conversion_rate']} {tocurrency}",  # noqa: E501
        )
except KeyboardInterrupt:
    sys.exit(0)
