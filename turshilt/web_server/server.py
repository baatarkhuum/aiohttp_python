from aiohttp import web

#request handler
# async def hello(request):
#     return web.Response(text="Hello Babu")


# #create an App Instance and register the request handler on a some http method and path
# app = web.Application()
# app.add_routes([web.get('/', hello)])
# print(type(app.add_routes))
# web.run_app(app)

# with route decorator

routes = web.RouteTableDef()

@routes.get('/')
async def hello(request):
    return web.Response(text="hello babu")

app = web.Application()
app.add_routes(routes)
web.run_app(app)
print("server down")