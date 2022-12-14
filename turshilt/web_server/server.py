from aiohttp import web
from aiohttp import ClientSession
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


@routes.get('/weather/{city}')
async def weather(request):

    appid = '453f67309f0172f66cf2c3257af1ea55'
    parameter = {'q':request.match_info['city'], 'appid':appid}
    async with ClientSession().get('http://api.openweathermap.org/data/2.5/weather', params=parameter) as resp:
        print(resp.status)
        sda = await resp.json()
        weather = sda["coord"]
    
    return web.Response(text="In {} is now {}".format(request.match_info['city'],weather))

app = web.Application()
app.add_routes(routes)
web.run_app(app)
print("server down")