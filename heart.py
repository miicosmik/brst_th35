from aiohttp import web
import asyncio

async def handle(request):
    return web.Response(text="Viva!")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8080)
    await site.start()
    print("[OK] Web service iniciado na porta 8080")
