import argparse

from colorama import Fore

from trading_bot.bot.orders import place_order

from trading_bot.bot.validators import *


parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)

parser.add_argument("--side", required=True)

parser.add_argument("--type", required=True)

parser.add_argument("--quantity", required=True)

parser.add_argument("--price")

args = parser.parse_args()

try:

    symbol = args.symbol.upper()

    side = validate_side(args.side)

    order_type = validate_order_type(args.type)

    quantity = validate_quantity(args.quantity)

    price = validate_price(args.price)

    if order_type == "LIMIT" and price is None:

        raise Exception("LIMIT order requires price.")

    print("=" * 40)

    print("ORDER SUMMARY")

    print("=" * 40)

    print("Symbol :", symbol)

    print("Side :", side)

    print("Type :", order_type)

    print("Quantity :", quantity)

    if price:

        print("Price :", price)

    print()

    response = place_order(

        symbol,
        side,
        order_type,
        quantity,
        price
    )

    print(Fore.GREEN)

    print("Order Placed Successfully")

    print()

    print("Order ID :", response["orderId"])

    print("Status :", response["status"])

    print("Executed Qty :", response["executedQty"])

    print("Average Price :", response.get("avgPrice"))

except Exception as e:

    print(Fore.RED)

    print("Failed")

    print(e)