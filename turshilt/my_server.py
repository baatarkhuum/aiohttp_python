from aiohttp import web

async def hello(request): # request handler
    return web.Response(text="Hello, World")

app = web.Application() # App Instance

# Route / ruu get request yavuulahad hello (register handler) duudagdana.
app.add_routes([web.get('/',hello)]) 

web.run_app(app)