import json
from typing import Dict, List

import websockets
from hexbytes import HexBytes

from hubble_exchange.eip712 import get_ioc_order_hash, get_limit_order_hash
from hubble_exchange.eth import get_async_web3_client, get_websocket_endpoint
from hubble_exchange.models import (AsyncOrderBookDepthCallback,
                                    AsyncOrderStatusCallback,
                                    AsyncPlaceOrdersCallback,
                                    AsyncPositionCallback,
                                    AsyncSubscribeToOrderBookDepthCallback,
                                    ConfirmationMode, IOCOrder, LimitOrder,
                                    MarketFeedUpdate,
                                    OrderBookDepthUpdateResponse,
                                    OrderStatusResponse, TraderFeedUpdate,
                                    WebsocketResponse)
from hubble_exchange.order_book import OrderBookClient, TransactionMode
from hubble_exchange.utils import (float_to_scaled_int,
                                   get_address_from_private_key, get_new_salt)


class HubbleClient:
    def __init__(self, private_key: str):
        if not private_key:
            raise ValueError("Private key is not set")
        self.trader_address = get_address_from_private_key(private_key)
        if not self.trader_address:
            raise ValueError("Cannot determine trader address from private key")

        self.web3_client = get_async_web3_client()
        self.websocket_endpoint = get_websocket_endpoint()
        self.order_book_client = OrderBookClient(private_key)

    def set_transaction_mode(self, mode: TransactionMode):
        self.order_book_client.set_transaction_mode(mode)

    async def get_markets(self):
        return await self.order_book_client.get_markets()

    async def get_order_book(self, market: int, callback: AsyncOrderBookDepthCallback):
        order_book_depth = await self.web3_client.eth.get_order_book_depth(market)
        return await callback(order_book_depth)

    async def get_margin_and_positions(self, callback: AsyncPositionCallback):
        response = await self.web3_client.eth.get_margin_and_positions(self.trader_address)
        return await callback(response)

    async def get_order_status(self, order_id: HexBytes, callback: AsyncOrderStatusCallback):
        response = await self.web3_client.eth.get_order_status(order_id.hex()) # type: ignore
        return await callback(response)

    async def get_open_orders(self, market_id: int, callback: AsyncOrderStatusCallback):
        response = await self.web3_client.eth.get_open_orders(self.trader_address, market_id)
        return await callback(response)
    
    async def get_trades(self, market, start_time, end_time, callback):
        if start_time is None or end_time is None:
            raise ValueError("Start and end time must be specified")

        response = await self.order_book_client.get_trades(self.trader_address, market, start_time, end_time)
        return await callback(response)
    
    async def place_limit_orders(self, orders: List[LimitOrder], wait_for_response: bool, callback: AsyncPlaceOrdersCallback, tx_options = None, mode=None):
        if len(orders) > 75:
            raise ValueError("Cannot place more than 75 orders at once")

        for order in orders:
            if order.amm_index is None:
                raise ValueError("Order AMM index is not set")
            if order.base_asset_quantity is None:
                raise ValueError("Order base asset quantity is not set")
            if order.price is None:
                raise ValueError("Order price is not set")
            if order.reduce_only is None:
                raise ValueError("Order reduce only is not set")

            # trader and salt can be set automatically
            if order.trader in [None, "0x", ""]:
                order.trader = self.trader_address
            if order.salt in [None, 0]:
                order.salt = get_new_salt()

        order_ids = set()  # stores all the order ids
        for order in orders:
            order_hash = get_limit_order_hash(order)
            order.id = order_hash
            order_ids.add(order_hash.hex())  # add each order id to the set

        # if the response if requested then we'll have to wait for the transaction to be mined
        # This is because the receipt is generated only after the transaction is mined(accepted)
        if wait_for_response:
            mode = TransactionMode.wait_for_accept

        tx_hash = await self.order_book_client.place_limit_orders(orders, tx_options, mode)
        if wait_for_response:
            receipt = await self.web3_client.eth.get_transaction_receipt(tx_hash)

            events = self.order_book_client.get_events_from_receipt(receipt, "OrderPlaced")
            event_order_ids = set()  # stores order ids present in events
            response = []
            for event in events:
                order_id = event.args.orderHash
                event_order_ids.add('0x' + order_id.hex())
                response.append({
                    "order_id": '0x' + order_id.hex(),
                    "success": True
                })

            missing_order_ids = order_ids - event_order_ids  # order ids not present in events

            for missing_id in missing_order_ids:
                response.append({
                    "order_id": missing_id,
                    "success": False
                })

            return await callback(response)
        else:
            return await callback(orders)

    async def place_ioc_orders(self, orders: List[IOCOrder], wait_for_response: bool, callback: AsyncPlaceOrdersCallback, tx_options = None, mode=None):
        if len(orders) > 75:
            raise ValueError("Cannot place more than 75 orders at once")

        for order in orders:
            if order.amm_index is None:
                raise ValueError("Order AMM index is not set")
            if order.base_asset_quantity is None:
                raise ValueError("Order base asset quantity is not set")
            if order.price is None:
                raise ValueError("Order price is not set")
            if order.reduce_only is None:
                raise ValueError("Order reduce only is not set")
            if order.expire_at is None:
                raise ValueError("Order expiry is not set")

            # trader and salt can be set automatically
            if order.trader in [None, "0x", ""]:
                order.trader = self.trader_address
            if order.salt in [None, 0]:
                order.salt = get_new_salt()

        order_ids = set()  # stores all the order ids
        for order in orders:
            order_hash = get_ioc_order_hash(order)
            order.id = order_hash
            order_ids.add(order_hash.hex())  # add each order id to the set

        # if the response if requested then we'll have to wait for the transaction to be mined
        # This is because the receipt is generated only after the transaction is mined(accepted)
        if wait_for_response:
            mode = TransactionMode.wait_for_accept

        tx_hash = await self.order_book_client.place_ioc_orders(orders, tx_options, mode)
        if wait_for_response:
            receipt = await self.web3_client.eth.get_transaction_receipt(tx_hash)

            events = self.order_book_client.get_events_from_receipt(receipt, "OrderPlaced", contract_name="ioc")
            event_order_ids = set()  # stores order ids present in events
            response = []
            for event in events:
                order_id = event.args.orderHash
                event_order_ids.add('0x' + order_id.hex())
                response.append({
                    "order_id": '0x' + order_id.hex(),
                    "success": True
                })

            missing_order_ids = order_ids - event_order_ids  # order ids not present in events

            for missing_id in missing_order_ids:
                response.append({
                    "order_id": missing_id,
                    "success": False
                })

            return await callback(response)
        else:
            return await callback(orders)

    async def cancel_limit_orders(self, orders: List[LimitOrder], atomic: bool, wait_for_response: bool, callback, tx_options = None, mode=None):
        if len(orders) > 100:
            raise ValueError("Cannot cancel more than 100 orders at once")

        if atomic is None:
            atomic = True  # default mode

        # if the response if requested then we'll have to wait for the transaction to be mined
        # This is because the receipt is generated only after the transaction is mined(accepted)
        if wait_for_response:
            mode = TransactionMode.wait_for_accept

        order_ids = set()  # stores all the order ids
        for order in orders:
            order_hash = get_limit_order_hash(order)
            order.id = order_hash
            order_ids.add(order_hash.hex())  # add each order id to the set

        tx_hash = await self.order_book_client.cancel_orders(orders, atomic, tx_options, mode)

        if wait_for_response:
            receipt = await self.web3_client.eth.get_transaction_receipt(tx_hash)

            response = []
            event_order_ids = set()
            cancelled_events = self.order_book_client.get_events_from_receipt(receipt, "OrderCancelled")
            for event in cancelled_events:
                event_order_ids.add('0x' + event.args.orderHash.hex())
                response.append({
                    "order_id": '0x' + event.args.orderHash.hex(),
                    "success": True
                })
            skipped_events = self.order_book_client.get_events_from_receipt(receipt, "SkippedCancelOrder")
            for event in skipped_events:
                event_order_ids.add('0x' + event.args.orderHash.hex())
                response.append({
                    "order_id": '0x' + event.args.orderHash.hex(),
                    "success": False,
                })

            missing_order_ids = order_ids - event_order_ids  # order ids not present in events

            for missing_id in missing_order_ids:
                response.append({
                    "order_id": missing_id,
                    "success": False
                })

            return await callback(response)
        else:
            return await callback(orders)

    async def cancel_order_by_id(self, order_id: HexBytes, wait_for_response: bool, callback, tx_options = None, mode=None):
        async def order_status_callback(response: OrderStatusResponse) -> LimitOrder:
            position_side_multiplier = 1 if response.positionSide == "LONG" else -1
            return LimitOrder(
                id=order_id,
                amm_index=response.symbol,
                trader=self.trader_address,
                base_asset_quantity=float_to_scaled_int(float(response.origQty) * position_side_multiplier, 18),
                price=float_to_scaled_int(float(response.price), 6),
                salt=int(response.salt),
                reduce_only=response.reduceOnly,
            )
        order = await self.get_order_status(order_id, order_status_callback)
        return await self.cancel_limit_orders([order], True, wait_for_response, callback, tx_options, mode)

    async def get_order_fills(self, order_id: str) -> List[Dict]:
        return await self.order_book_client.get_order_fills(order_id)

    async def subscribe_to_order_book_depth(
        self, market: int, callback: AsyncSubscribeToOrderBookDepthCallback
    ) -> None:
        async with websockets.connect(self.websocket_endpoint) as ws:
            msg = {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "trading_subscribe",
                "params": ["streamDepthUpdateForMarket", market]
            }
            await ws.send(json.dumps(msg))

            async for message in ws:
                message_json = json.loads(message)
                if message_json.get('result'):
                    # ignore because it's a subscription confirmation with subscription id
                    continue
                response = WebsocketResponse(**message_json)
                if response.method and response.method == "trading_subscription":
                    response = OrderBookDepthUpdateResponse(
                        T=response.params['result']['T'],
                        symbol=response.params['result']['s'],
                        bids=response.params['result']['b'],
                        asks=response.params['result']['a'],
                    )
                    await callback(ws, response)

    async def subscribe_to_trader_updates(
        self, update_type: ConfirmationMode, callback
    ) -> None:
        async with websockets.connect(self.websocket_endpoint) as ws:
            msg = {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "trading_subscribe",
                "params": ["streamTraderUpdates", self.trader_address, update_type.value]
            }
            await ws.send(json.dumps(msg))

            async for message in ws:
                message_json = json.loads(message)
                if message_json.get('result'):
                    # ignore because it's a subscription confirmation with subscription id
                    continue
                response = WebsocketResponse(**message_json)
                if response.method and response.method == "trading_subscription":
                    response = TraderFeedUpdate(**response.params['result'])
                    await callback(ws, response)

    async def subscribe_to_market_updates(
        self, market, update_type: ConfirmationMode, callback
    ) -> None:
        async with websockets.connect(self.websocket_endpoint) as ws:
            msg = {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "trading_subscribe",
                "params": ["streamMarketTrades", market, update_type.value]
            }
            await ws.send(json.dumps(msg))

            async for message in ws:
                message_json = json.loads(message)
                if message_json.get('result'):
                    # ignore because it's a subscription confirmation with subscription id
                    continue
                response = WebsocketResponse(**message_json)
                if response.method and response.method == "trading_subscription":
                    response = MarketFeedUpdate(**response.params['result'])
                    await callback(ws, response)
