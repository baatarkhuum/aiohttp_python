import aiohttp
import asyncio

# try to get a web page
# async def main():
#     async with aiohttp.ClientSession() as session:
#         async with session.get('http://httpbin.org/get') as resp:
#             print(resp.status)
#             print(await resp.text())
# asyncio.run(main())

#We can get all the information we need from the response

# session.post('http://httpbin.org/post', data=b'data')
# session.put('http://httpbin.org/put', data=b'data')
# session.delete('http://httpbin.org/delete')
# session.head('http://httpbin.org/get')
# session.options('http://httpbin.org/get')
# session.patch('http://httpbin.org/patch', data=b'data')

# Oder es ist noch simpler

# async with aiohttp.ClientSession('http://httpbin.org') as session:
#     async with session.get('/get')
#         pass
#     async with session.post('/post', data=b'data')
#         pass
#     async with session.put('/put', data=b'data')


 # you need a session per application which performs all requests altogether.

#http://api.openweathermap.org/data/2.5/
# weather?q=Aachen&appid=453f67309f0172f66cf2c3257af1ea55

async def main():

    session = aiohttp.ClientSession()
    city = input()
    appid = '453f67309f0172f66cf2c3257af1ea55'
    params = {'q':city, 'appid':'453f67309f0172f66cf2c3257af1ea55'}
    resp = session.get('http://api.openweathermap.org/data/2.5/weather', params=params)
    print(resp)
    print("hallo")
asyncio.run(main())  