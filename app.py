import logging; logging.basicConfig(level = logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body = b'<h1>Awesome, You find the job today</h1>', content_type = 'text/html')

@asyncio.coroutine
def init(loop):
    app = web.Application()
    # app = web_runner.AppRunner(app = app).app()
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app._make_handler(), '127.0.0.1', 9000)
    logging.info('Server started at http://127.0.0.1: 9000')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
