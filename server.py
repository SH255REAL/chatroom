import asyncio
import websockets

# Dictionary to hold connected clients
connected = set()

async def chat_server(websocket, path):
    # Add client to the connected set
    connected.add(websocket)
    try:
        async for message in websocket:
            # Broadcast the message to all connected clients
            await asyncio.wait([client.send(message) for client in connected])
    finally:
        # Remove client from the connected set when they disconnect
        connected.remove(websocket)

# Start the server
start_server = websockets.serve(chat_server, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
