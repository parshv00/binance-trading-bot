import time
import logging

def place_order(client, symbol, side, order_type, quantity, price=None, stop_price=None):
    try:
        #  Sync time with Binance server
        server_time = client.futures_time()
        client.timestamp_offset = server_time['serverTime'] - int(time.time() * 1000)

        logging.info(f"Placing order: {symbol} {side} {order_type} {quantity} {price} {stop_price}")

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        #  BONUS: STOP-LIMIT ORDER
        elif order_type == "STOP":
            if not stop_price or not price:
                raise ValueError("STOP order requires both price and stop_price")

            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP",
                quantity=quantity,
                price=price,
                stopPrice=stop_price,
                timeInForce="GTC"
            )

        else:
            raise ValueError("Invalid order type")

        logging.info(f"Order success: {order}")

        return {
            "orderId": order.get("orderId"),
            "status": order.get("status"),
            "executedQty": order.get("executedQty"),
            "avgPrice": order.get("avgPrice", "N/A")
        }

    except Exception as e:
        logging.error(f"Order failed: {str(e)}")
        return {"error": str(e)}