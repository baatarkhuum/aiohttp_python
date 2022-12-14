import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        city = input()
        appid = '453f67309f0172f66cf2c3257af1ea55'
        parameter = {'q':city, 'appid':appid}
        async with session.get('http://api.openweathermap.org/data/2.5/weather', params=parameter) as resp:

            print(resp.status)
            sda = await resp.json()

            #if the request is successful
            if resp.status == 200: 
                position = sda['coord']
                position['city'] = city
                position['country'] = sda['sys']['country']

                temp = sda['main']['temp'] -273.5
                humidity = sda['main']['humidity']
                wind_speed = sda['wind']['speed']
                weather = {'temp' : temp, "humidity" : humidity, "wind_speed" : wind_speed}
                print('Position: {}'.format(position))
                print('Weather: {}'.format(weather))
            else:    
                print(sda)

asyncio.run(main())