from trading_bot.bot.client import client
from trading_bot.bot.logging_config import logger


def place_order(symbol,
                side,
                order_type,
                quantity,
                price=None):

    try:

        logger.info(
            f"Request: {symbol} {side} {order_type} Qty={quantity} Price={price}"
        )

        if order_type == "MARKET":

            order = client.futures_create_order(

                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        else:

            order = client.futures_create_order(

                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logger.info(order)

        return order

    except Exception as e:

        logger.error(str(e))

        raise