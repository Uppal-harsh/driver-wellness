import asyncio
import websockets
import json
from aiohttp import web

class MonitoringServer:
    def __init__(self):
        self.clients = set()
        self.app = web.Application()
        self.setup_routes()

    def setup_routes(self):
        self.app.router.add_static('/static', 'static')
        self.app.router.add_get('/', self.handle_index)

    async def handle_index(self, request):
        return web.FileResponse('./static/index.html')

    async def websocket_handler(self, websocket, path):
        self.clients.add(websocket)
        try:
            async for message in websocket:
                # Broadcast message to all clients
                await self.broadcast(message)
        finally:
            self.clients.remove(websocket)

    async def broadcast(self, message):
        if self.clients:
            await asyncio.wait([client.send(message) for client in self.clients])

    def run(self):
        # Start websocket server
        start_server = websockets.serve(self.websocket_handler, 'localhost', 8765)
        
        # Start web server
        runner = web.AppRunner(self.app)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(runner.setup())
        site = web.TCPSite(runner, 'localhost', 8080)
        
        # Run both servers
        loop.run_until_complete(site.start())
        loop.run_until_complete(start_server)
        loop.run_forever()

if __name__ == '__main__':
    server = MonitoringServer()
    server.run()
