from aiohttp import web

# async def hello(request):
#     return web.Response(text = "Hello World")

# app.router.add_get('/',hello)
class Handler:

    def __init__(self):
        pass
    async def handle_intro(self, request):
        return web.Response(text = "Hello, World")

    async def handle_greeting(self, request):
        name = request.match_info.get('name',"Anonymous")
        txt = "Hello, {}".format(name)
        return web.Resource(text = txt)
handler = Handler()
app = web.Application()
app.add_routes([web.get('/intro', handler.handle_intro),
web.get('/greet/{name}', handler.handle_greeting)])
web.run_app(app)
print("server down")