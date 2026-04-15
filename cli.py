import argparse
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_input
from bot.logging_config import setup_logging

#  Initialize logging
setup_logging()

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    #  Required arguments
    parser.add_argument("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"], help="Order side")
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT", "STOP"], help="Order type")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")

    #  Optional arguments
    parser.add_argument("--price", type=float, help="Price (required for LIMIT & STOP)")
    parser.add_argument("--stop_price", type=float, help="Stop price (required for STOP)")

    args = parser.parse_args()

    try:
        #  Validate inputs
        validate_input(args.symbol, args.side, args.type, args.quantity, args.price)

        #  Extra validation for STOP order
        if args.type == "STOP":
            if not args.price or not args.stop_price:
                raise ValueError("STOP order requires both --price and --stop_price")

        #  Get Binance client
        client = get_client()

        #  Place order
        order = place_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price,
            args.stop_price
        )

        #  Print clean output
        print("\n Order Summary:")
        print(f"Symbol      : {args.symbol}")
        print(f"Side        : {args.side}")
        print(f"Type        : {args.type}")
        print(f"Quantity    : {args.quantity}")
        if args.price:
            print(f"Price       : {args.price}")
        if args.stop_price:
            print(f"Stop Price  : {args.stop_price}")

        print("\n Order Response:")
        print(order)

        #  Success / failure message
        if "error" in order:
            print("\n Order Failed")
        else:
            print("\n Order Placed Successfully")

    except Exception as e:
        print("\n Error:", str(e))


if __name__ == "__main__":
    main()