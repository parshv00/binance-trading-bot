def validate_input(symbol, side, order_type, quantity, price):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Invalid order type")

    if order_type == "LIMIT" and not price:
        raise ValueError("Price required for LIMIT order")