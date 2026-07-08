import re
import aiocache
from bs4 import BeautifulSoup
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler, CallbackContext
import logging
import aiohttp
import tracemalloc
<<<<<<< HEAD
import os
from dotenv import load_dotenv
=======
>>>>>>> 7da8da2224b06529d5730a3525e587eeaa23937b

tracemalloc.start()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;'
                      ' Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

##################################################################################################################
####################      РУССКИЙ ЯЗЫК     ##########################


@aiocache.cached(ttl=60)
async def ALMATY_parse_weather():
    url = "https://www.gismeteo.kz/weather-almaty-5205/now/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                temperature_div = soup.find('div', class_='weather-value')
                weather = soup.find("div", class_="now-desc").text.strip()
                if temperature_div:
                    temperature_value = temperature_div.find('temperature-value')
                    if temperature_value:
                        temperature = temperature_value.get('value')
                        return f"Погода сейчас в Алматы: {temperature}, {weather}"
                    else:
                        print('Temperature value not found')
                else:
                    print('Weather value div not found')
            else:
                return "Не удалось получить данные о погоде для Алматы"


@aiocache.cached(ttl=60)
async def ALMATY_parse_weather_ten_days():
    url = "https://yandex.kz/pogoda/almaty?lat=43.273564&lon=76.914851"
<<<<<<< HEAD

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:

            if response.status != 200:
                return "Не удалось получить данные о погоде."

            html = await response.text()
            soup = BeautifulSoup(html, "html.parser")

            container = soup.find(
                "div",
                class_=lambda c: c and "AppShortForecastContainer_days" in c
            )

            if container is None:
                return "Не удалось найти прогноз на странице."

            days = container.find_all(
                "div",
                class_=lambda c: c and "AppShortForecastDay_container" in c
            )

            weekdays = {
                "пн": "Понедельник",
                "вт": "Вторник",
                "ср": "Среда",
                "чт": "Четверг",
                "пт": "Пятница",
                "сб": "Суббота",
                "вс": "Воскресенье",
            }

            weather_list = []

            for i, day in enumerate(days[:10]):

                title = day.find(
                    "span",
                    class_=lambda c: c and "AppShortForecastDay_title" in c
                )

                subtitle = day.find(
                    "span",
                    class_=lambda c: c and "AppShortForecastDay_subtitle" in c
                )

                temps = day.find_all(
                    "span",
                    class_=lambda c: c and "AppShortForecastDay_temperature" in c
                )

                if len(temps) < 2:
                    continue

                weekday = title.get_text(strip=True)
                date = subtitle.get_text(strip=True)

                day_temp = temps[0].get_text(strip=True)
                night_temp = temps[1].get_text(strip=True)

                if date.lower() == "сегодня":
                    header = f"📅 Сегодня ({weekday})"
                else:
                    header = f"📅 {weekdays.get(weekday, weekday)} ({date})"

                weather_list.append(
                    f"{header}\n"
                    f"🌡 Днем: {day_temp}\n"
                    f"🌙 Ночью: {night_temp}"
                )

            return (
                    "🌤 Прогноз погоды на 10 дней (Алматы)\n\n"
                    + "\n\n━━━━━━━━━━━━━━━━━━━━\n\n".join(weather_list)
            )
=======
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                containers = soup.find("div", class_="forecast-briefly__days").text.strip()
                matches = re.findall(r'(\d+\s\w+)\D+(\d+)\D+(\d+)', containers)

                weather_list = []

                for match in matches[:10]:
                    day_weather = f"{match[0]} днем: {match[1]} {choose_degree_suffix(match[1])}, ночью: {match[2]} {choose_degree_suffix(match[2])}"
                    weather_list.append(day_weather)

                line = '☁' * 5

                return '\n'.join([f"{line}\n{weather}" for weather in weather_list])
            else:
                return "Не удалось получить данные о погоде для Алматы"
>>>>>>> 7da8da2224b06529d5730a3525e587eeaa23937b


@aiocache.cached(ttl=60)
async def ASTANA_parse_weather():
    url = "https://www.gismeteo.kz/weather-astana-5164/now/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                temperature_div = soup.find('div', class_='weather-value')
                weather = soup.find("div", class_="now-desc").text.strip()
                if temperature_div:
                    temperature_value = temperature_div.find('temperature-value')
                    if temperature_value:
                        temperature = temperature_value.get('value')
                        return f"Погода сейчас в Астане: {temperature}, {weather}"
                    else:
                        print('Temperature value not found')
                else:
                    print('Weather value div not found')
            else:
                return "Не удалось получить данные о погоде для Астаны"


@aiocache.cached(ttl=60)
async def ASTANA_parse_weather_ten_days():
<<<<<<< HEAD
    url = "https://yandex.kz/pogoda/ru?lat=51.12820053&lon=71.43042755"

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:

            if response.status != 200:
                return "Не удалось получить данные о погоде."

            html = await response.text()
            soup = BeautifulSoup(html, "html.parser")

            container = soup.find(
                "div",
                class_=lambda c: c and "AppShortForecastContainer_days" in c
            )

            if container is None:
                return "Не удалось найти прогноз на странице."

            days = container.find_all(
                "div",
                class_=lambda c: c and "AppShortForecastDay_container" in c
            )

            weekdays = {
                "пн": "Понедельник",
                "вт": "Вторник",
                "ср": "Среда",
                "чт": "Четверг",
                "пт": "Пятница",
                "сб": "Суббота",
                "вс": "Воскресенье",
            }

            weather_list = []

            for i, day in enumerate(days[:10]):

                title = day.find(
                    "span",
                    class_=lambda c: c and "AppShortForecastDay_title" in c
                )

                subtitle = day.find(
                    "span",
                    class_=lambda c: c and "AppShortForecastDay_subtitle" in c
                )

                temps = day.find_all(
                    "span",
                    class_=lambda c: c and "AppShortForecastDay_temperature" in c
                )

                if len(temps) < 2:
                    continue

                weekday = title.get_text(strip=True)
                date = subtitle.get_text(strip=True)

                day_temp = temps[0].get_text(strip=True)
                night_temp = temps[1].get_text(strip=True)

                if date.lower() == "сегодня":
                    header = f"📅 Сегодня ({weekday})"
                else:
                    header = f"📅 {weekdays.get(weekday, weekday)} ({date})"

                weather_list.append(
                    f"{header}\n"
                    f"🌡 Днем: {day_temp}\n"
                    f"🌙 Ночью: {night_temp}"
                )

            return (
                    "🌤 Прогноз погоды на 10 дней (Астана)\n\n"
                    + "\n\n━━━━━━━━━━━━━━━━━━━━\n\n".join(weather_list)
            )
=======
    url = "https://yandex.kz/pogoda?lat=51.12820053&lon=71.43042755"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                text = await response.text()
                soup = BeautifulSoup(text, 'html.parser')
                containers = soup.find("div", class_="forecast-briefly__days").text.strip()

                matches = re.findall(r'(\d+\s\w+)\D+(\d+)\D+(\d+)', containers)

                weather_list = []

                for match in matches[:10]:
                    day_weather = f"{match[0]} днем: {match[1]} {choose_degree_suffix(match[1])}, ночью: {match[2]} {choose_degree_suffix(match[2])}"
                    weather_list.append(day_weather)

                line = '☁' * 5

                return '\n'.join([f"{line}\n{weather}" for weather in weather_list])
            else:
                return "Не удалось получить данные о погоде на 10 дней для Астаны"
>>>>>>> 7da8da2224b06529d5730a3525e587eeaa23937b


@aiocache.cached(ttl=60)
async def AKTAU_parse_weather():
    url = "https://www.gismeteo.kz/weather-aktau-5320/now/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                temperature_div = soup.find('div', class_='weather-value')
                weather = soup.find("div", class_="now-desc").text.strip()
                if temperature_div:
                    temperature_value = temperature_div.find('temperature-value')
                    if temperature_value:
                        temperature = temperature_value.get('value')
                        return f"Погода сейчас в Актау: {temperature}, {weather}"
                    else:
                        print('Temperature value not found')
                else:
                    print('Weather value div not found')
            else:
                return "Не удалось получить данные о погоде для Актау"


@aiocache.cached(ttl=60)
async def AKTAU_parse_weather_ten_days():
<<<<<<< HEAD
    url = "http://yandex.kz/pogoda/ru?lat=43.6355896&lon=51.16824341"

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:

            if response.status != 200:
                return "Не удалось получить данные о погоде."

            html = await response.text()
            soup = BeautifulSoup(html, "html.parser")

            container = soup.find(
                "div",
                class_=lambda c: c and "AppShortForecastContainer_days" in c
            )

            if container is None:
                return "Не удалось найти прогноз на странице."

            days = container.find_all(
                "div",
                class_=lambda c: c and "AppShortForecastDay_container" in c
            )

            weekdays = {
                "пн": "Понедельник",
                "вт": "Вторник",
                "ср": "Среда",
                "чт": "Четверг",
                "пт": "Пятница",
                "сб": "Суббота",
                "вс": "Воскресенье",
            }

            weather_list = []

            for i, day in enumerate(days[:10]):

                title = day.find(
                    "span",
                    class_=lambda c: c and "AppShortForecastDay_title" in c
                )

                subtitle = day.find(
                    "span",
                    class_=lambda c: c and "AppShortForecastDay_subtitle" in c
                )

                temps = day.find_all(
                    "span",
                    class_=lambda c: c and "AppShortForecastDay_temperature" in c
                )

                if len(temps) < 2:
                    continue

                weekday = title.get_text(strip=True)
                date = subtitle.get_text(strip=True)

                day_temp = temps[0].get_text(strip=True)
                night_temp = temps[1].get_text(strip=True)

                if date.lower() == "сегодня":
                    header = f"📅 Сегодня ({weekday})"
                else:
                    header = f"📅 {weekdays.get(weekday, weekday)} ({date})"

                weather_list.append(
                    f"{header}\n"
                    f"🌡 Днем: {day_temp}\n"
                    f"🌙 Ночью: {night_temp}"
                )

            return (
                    "🌤 Прогноз погоды на 10 дней (Актау)\n\n"
                    + "\n\n━━━━━━━━━━━━━━━━━━━━\n\n".join(weather_list)
            )
=======
    url = "https://yandex.kz/pogoda?lat=43.6355896&lon=51.16824341"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                text = await response.text()
                soup = BeautifulSoup(text, 'html.parser')
                containers = soup.find("div", class_="forecast-briefly__days").text.strip()

                matches = re.findall(r'(\d+\s\w+)\D+(\d+)\D+(\d+)', containers)

                weather_list = []

                for match in matches[:10]:
                    day_weather = f"{match[0]} днем: {match[1]} {choose_degree_suffix(match[1])}, ночью: {match[2]} {choose_degree_suffix(match[2])}"
                    weather_list.append(day_weather)

                line = '☁' * 5

                return '\n'.join([f"{line}\n{weather}" for weather in weather_list])
            else:
                return "Не удалось получить данные о погоде на 10 дней для Актау"
>>>>>>> 7da8da2224b06529d5730a3525e587eeaa23937b


@aiocache.cached(ttl=60)
async def ATYRAU_parse_weather():
    url = "https://www.gismeteo.kz/weather-atyrau-11945/now/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                temperature_div = soup.find('div', class_='weather-value')
                weather = soup.find("div", class_="now-desc").text.strip()
                if temperature_div:
                    temperature_value = temperature_div.find('temperature-value')
                    if temperature_value:
                        temperature = temperature_value.get('value')
                        return f"Погода сейчас в Атырау: {temperature}, {weather}"
                    else:
                        print('Temperature value not found')
                else:
                    print('Weather value div not found')
            else:
                return "Не удалось получить данные о погоде для Атырау"

@aiocache.cached(ttl=60)
async def ATYRAU_parse_weather_ten_days():
<<<<<<< HEAD
    url = "https://yandex.kz/pogoda/ru?lat=47.10680008&lon=51.91687393"

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:

            if response.status != 200:
                return "Не удалось получить данные о погоде."

            html = await response.text()
            soup = BeautifulSoup(html, "html.parser")

            container = soup.find(
                "div",
                class_=lambda c: c and "AppShortForecastContainer_days" in c
            )

            if container is None:
                return "Не удалось найти прогноз на странице."

            days = container.find_all(
                "div",
                class_=lambda c: c and "AppShortForecastDay_container" in c
            )

            weekdays = {
                "пн": "Понедельник",
                "вт": "Вторник",
                "ср": "Среда",
                "чт": "Четверг",
                "пт": "Пятница",
                "сб": "Суббота",
                "вс": "Воскресенье",
            }

            weather_list = []

            for i, day in enumerate(days[:10]):

                title = day.find(
                    "span",
                    class_=lambda c: c and "AppShortForecastDay_title" in c
                )

                subtitle = day.find(
                    "span",
                    class_=lambda c: c and "AppShortForecastDay_subtitle" in c
                )

                temps = day.find_all(
                    "span",
                    class_=lambda c: c and "AppShortForecastDay_temperature" in c
                )

                if len(temps) < 2:
                    continue

                weekday = title.get_text(strip=True)
                date = subtitle.get_text(strip=True)

                day_temp = temps[0].get_text(strip=True)
                night_temp = temps[1].get_text(strip=True)

                if date.lower() == "сегодня":
                    header = f"📅 Сегодня ({weekday})"
                else:
                    header = f"📅 {weekdays.get(weekday, weekday)} ({date})"

                weather_list.append(
                    f"{header}\n"
                    f"🌡 Днем: {day_temp}\n"
                    f"🌙 Ночью: {night_temp}"
                )

            return (
                    "🌤 Прогноз погоды на 10 дней (Атырау)\n\n"
                    + "\n\n━━━━━━━━━━━━━━━━━━━━\n\n".join(weather_list)
            )
=======
    url = "https://yandex.kz/pogoda?lat=47.10680008&lon=51.91687393"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                text = await response.text()
                soup = BeautifulSoup(text, 'html.parser')
                containers = soup.find("div", class_="forecast-briefly__days").text.strip()

                matches = re.findall(r'(\d+\s\w+)\D+(\d+)\D+(\d+)', containers)

                weather_list = []

                for match in matches[:10]:
                    day_weather = f"{match[0]} днем: {match[1]} {choose_degree_suffix(match[1])}, ночью: {match[2]} {choose_degree_suffix(match[2])}"
                    weather_list.append(day_weather)

                line = '☁' * 5

                return '\n'.join([f"{line}\n{weather}" for weather in weather_list])
            else:
                return "Не удалось получить данные о погоде на 10 дней для Атырау"
>>>>>>> 7da8da2224b06529d5730a3525e587eeaa23937b


##################################################################################################################
####################      ENGLISH    ##########################


@aiocache.cached(ttl=60)
async def ALMATY_parse_weather_english():
    url = "https://weather.com/weather/today/l/a944f87f387a92bc4718ec1bf6f06b1c03217976fc96db720be23e8ba0d954bb"
<<<<<<< HEAD

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:

            if response.status != 200:
                return "Failed to get weather data for Almaty."

            html = await response.text()
            soup = BeautifulSoup(html, "html.parser")

            temp = soup.find("span", attrs={"data-testid": "TemperatureValue"})
            weather = soup.find(
                "p",
                class_=lambda c: c and "font-bold" in c
            )

            if temp is None or weather is None:
                return "Failed to parse weather data."

            temperature = temp.contents[0].strip()
            description = weather.get_text(strip=True)

            return (
                "🌤 <b>Current Weather in Almaty</b>\n\n"
                f"🌡 Temperature: <b>{temperature}°F</b>\n"
                f"☁ Conditions: <b>{description}</b>"
            )
=======
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                container = soup.find("span", class_="CurrentConditions--tempValue--MHmYY").text.strip()
                weather = soup.find("div", class_="CurrentConditions--phraseValue--mZC_p").text.strip()

                return f'The weather now in Almaty is: {container}F, {weather}'
            else:
                return "Failed to get weather data for Almaty"
>>>>>>> 7da8da2224b06529d5730a3525e587eeaa23937b


@aiocache.cached(ttl=60)
async def ALMATY_parse_weather_ten_days_english():
    url = "https://weather.com/weather/tenday/l/a944f87f387a92bc4718ec1bf6f06b1c03217976fc96db720be23e8ba0d954bb"
<<<<<<< HEAD

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:

            if response.status != 200:
                return "Failed to get weather data."

            html = await response.text()
            soup = BeautifulSoup(html, "html.parser")

            # Каждый день прогноза
            days = soup.find_all(
                "div",
                attrs={"data-slot": "accordion-item"}
            )

            print(len(days))

            weather_list = []

            for day in days[:10]:

                # День недели
                day_name = day.find(
                    "span",
                    class_=lambda c: c and "font-bold text-gray-900" in c
                )

                if not day_name:
                    continue

                day_name = day_name.get_text(strip=True)

                # Вероятность осадков
                rain = day.find(
                    "span",
                    attrs={"data-testid": "PercentageValue"}
                )

                rain = rain.get_text(strip=True) if rain else "0%"

                # Описание погоды
                description = day.find(
                    "span",
                    class_=lambda c: c and "hidden w-44" in c
                )

                description = description.get_text(strip=True) if description else "Unknown"

                # Температуры
                temps = day.find_all(
                    "span",
                    attrs={"data-testid": "TemperatureValue"}
                )

                if len(temps) < 2:
                    continue

                low = temps[0].contents[0].strip()
                high = temps[1].contents[0].strip()

                # Ветер
                wind = day.find(
                    "span",
                    attrs={"data-testid": "Wind"}
                )

                wind = wind.get_text(" ", strip=True) if wind else "N/A"

                weather_list.append(
                    f"📅 <b>{day_name}</b>\n"
                    f"☁ <b>{description}</b>\n"
                    f"🌡 High: <b>{high}°F</b>\n"
                    f"🌙 Low: <b>{low}°F</b>\n"
                    f"🌧 Rain: <b>{rain}</b>\n"
                    f"💨 Wind: <b>{wind}</b>"
                )

            return (
                "🌤 <b>10-Day Weather Forecast (Almaty)</b>\n\n"
                + "\n\n━━━━━━━━━━━━━━━━━━━━\n\n".join(weather_list)
            )
=======
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                daypart_elements = soup.find_all("h2", class_="DetailsSummary--daypartName--kbngc")[1:10]
                temperature_elements = soup.find_all("div", class_="DetailsSummary--temperature--1kVVp")[1:10]

                weather_list = []

                for day_element, temp_element in zip(daypart_elements, temperature_elements):
                    day = day_element.text.strip()
                    high_temp_f = temp_element.find("span", class_="DetailsSummary--highTempValue--3PjlX").text.strip()
                    low_temp_f = temp_element.find("span", class_="DetailsSummary--lowTempValue--2tesQ").text.strip()

                    day_weather = f"{day}: during the day: {high_temp_f}F / at night: {low_temp_f}F"
                    weather_list.append(day_weather)

                return '\n'.join(weather_list)

            else:
                return "Failed to get weather data for Almaty"
>>>>>>> 7da8da2224b06529d5730a3525e587eeaa23937b


async def ASTANA_parse_weather_english():
    url = "https://weather.com/weather/tenday/l/a53972e14c64e70bca39cfe9ba0568d951b70605ca314dc9b3aeec8fac43acb6"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                container = soup.find("span", class_="DailyContent--temp--1s3a7 DailyContent--tempN--33RmW").text.strip()
                weather = soup.find("p", class_="DailyContent--narrative--3Ti6_").text.strip()

                return f'The weather now in Astana is: {container}F, {weather}'
            else:
                return "Failed to get weather data for Astana"


async def ASTANA_parse_weather_ten_days_english():
    url = "https://weather.com/weather/tenday/l/a53972e14c64e70bca39cfe9ba0568d951b70605ca314dc9b3aeec8fac43acb6"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                daypart_elements = soup.find_all("h2", class_="DetailsSummary--daypartName--kbngc")[1:10]
                temperature_elements = soup.find_all("div", class_="DetailsSummary--temperature--1kVVp")[1:10]

                weather_list = []

                for day_element, temp_element in zip(daypart_elements, temperature_elements):
                    day = day_element.text.strip()
                    high_temp_f = temp_element.find("span", class_="DetailsSummary--highTempValue--3PjlX").text.strip()
                    low_temp_f = temp_element.find("span", class_="DetailsSummary--lowTempValue--2tesQ").text.strip()

                    day_weather = f"{day}: during the day: {high_temp_f}F / at night: {low_temp_f}F"
                    weather_list.append(day_weather)

                return '\n'.join(weather_list)

            else:
                return "Failed to get weather data for Astana"


async def ATYRAU_parse_weather_english():
    url = "https://weather.com/weather/tenday/l/Atyrau+Kazakhstan?canonicalCityId=70d4b322c82adff9be01070fa49aff9c78b4d5a931602abb1218d91825707c4a"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                container = soup.find("span",
                                      class_="DailyContent--temp--1s3a7 DailyContent--tempN--33RmW").text.strip()
                weather = soup.find("p", class_="DailyContent--narrative--3Ti6_").text.strip()

                return f'The weather now in Atyrau is: {container}F, {weather}'
            else:
                return "Failed to get weather data for Atyrau"



async def ATYRAU_parse_weather_ten_days_english():
    url = "https://weather.com/weather/tenday/l/Atyrau+Kazakhstan?canonicalCityId=70d4b322c82adff9be01070fa49aff9c78b4d5a931602abb1218d91825707c4a"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                daypart_elements = soup.find_all("h2", class_="DetailsSummary--daypartName--kbngc")[1:10]
                temperature_elements = soup.find_all("div", class_="DetailsSummary--temperature--1kVVp")[1:10]

                weather_list = []

                for day_element, temp_element in zip(daypart_elements, temperature_elements):
                    day = day_element.text.strip()
                    high_temp_f = temp_element.find("span", class_="DetailsSummary--highTempValue--3PjlX").text.strip()
                    low_temp_f = temp_element.find("span", class_="DetailsSummary--lowTempValue--2tesQ").text.strip()

                    day_weather = f"{day}: during the day: {high_temp_f}F / at night: {low_temp_f}F"
                    weather_list.append(day_weather)

                return '\n'.join(weather_list)

            else:
                return "Failed to get weather data for Atyrau"


async def AKTAU_parse_weather_english():
    url = "https://weather.com/weather/tenday/l/7d5a51416f97db234962bb5774ae0736677b4db7e3d9fc3593701909b7cf2df3"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                container = soup.find("span",
                                      class_="DailyContent--temp--1s3a7 DailyContent--tempN--33RmW").text.strip()
                weather = soup.find("p", class_="DailyContent--narrative--3Ti6_").text.strip()

                return f'The weather now in Atyrau is: {container}F, {weather}'
            else:
                return "Failed to get weather data for Aktau"


async def AKTAU_parse_weather_ten_days_english():
    url = "https://weather.com/weather/tenday/l/7d5a51416f97db234962bb5774ae0736677b4db7e3d9fc3593701909b7cf2df3"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                daypart_elements = soup.find_all("h2", class_="DetailsSummary--daypartName--kbngc")[1:10]
                temperature_elements = soup.find_all("div", class_="DetailsSummary--temperature--1kVVp")[1:10]

                weather_list = []

                for day_element, temp_element in zip(daypart_elements, temperature_elements):
                    day = day_element.text.strip()
                    high_temp_f = temp_element.find("span", class_="DetailsSummary--highTempValue--3PjlX").text.strip()
                    low_temp_f = temp_element.find("span", class_="DetailsSummary--lowTempValue--2tesQ").text.strip()

                    day_weather = f"{day}: during the day: {high_temp_f}F / at night: {low_temp_f}F"
                    weather_list.append(day_weather)

                return '\n'.join(weather_list)

            else:
                return "Failed to get weather data for Aktau"


##################################################################################################################

def choose_degree_suffix(number):
    last_digit = int(number) % 10
    if last_digit in [1] and int(number) not in [11, 12, 13]:
        return "градус"
    elif last_digit in [2, 3, 4] and int(number) not in [11, 12, 13]:
        return "градуса"
    else:
        return "градусов"

##################################################################################################################

async def language1(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Русский", callback_data="ru")],
        [InlineKeyboardButton("Казахский", callback_data="kk")],
        [InlineKeyboardButton("Английский", callback_data="en")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выберите язык:", reply_markup=reply_markup)

##################################################################################################################


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    list1 = ["Русский язык", "English"]
    keyboard = []
    for i in list1:
        new_button = [InlineKeyboardButton(i, callback_data=i)]
        keyboard.append(new_button)

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выберите ваш язык: ", reply_markup=reply_markup)


##################################################################################################################

async def button(update, context):
    query = update.callback_query
    await query.answer()
    message = ""

    if query.data == "Русский язык":
        keyboard = [
            [InlineKeyboardButton("Алмата", callback_data="Алматы")],
            [InlineKeyboardButton("Астана", callback_data="Астана")],
            [InlineKeyboardButton("Актау", callback_data="Актау")],
            [InlineKeyboardButton("Атырау", callback_data="Атырау")],
            [InlineKeyboardButton("Дополнительно", callback_data="Дополнительно")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Выберите ваш город:",
                                       reply_markup=reply_markup)

##################################################################################################################

    if query.data == "English":
        keyboard = [
            [InlineKeyboardButton("Almaty", callback_data="Almaty")],
            [InlineKeyboardButton("Astana", callback_data="Astana")],
            [InlineKeyboardButton("Aktau", callback_data="Aktau")],
            [InlineKeyboardButton("Atyrau", callback_data="Atyrau")],
            [InlineKeyboardButton("Additionally", callback_data="Additionally")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Choose your city:",
                                       reply_markup=reply_markup)

##################################################################################################################
####################      ENGLISH    ##########################

    elif query.data == "Almaty":
        keyboard = [
            [InlineKeyboardButton("Weather for now", callback_data="Weather for now in Almaty")],
            [InlineKeyboardButton("Weather for 10 days", callback_data="Weather for 10 days in Almaty")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Choose the type of weather in Almaty(Please click once and wait a little bit):",
                                       reply_markup=reply_markup)
    elif query.data == "Astana":
        keyboard = [
            [InlineKeyboardButton("Weather for now", callback_data="Weather for now in Astana")],
            [InlineKeyboardButton("Weather for 10 days", callback_data="Weather for 10 days in Astana")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Choose the type of weather in Astana(Please click once and wait a little bit):",
                                       reply_markup=reply_markup)
    elif query.data == "Atyrau":
        keyboard = [
            [InlineKeyboardButton("Weather for now", callback_data="Weather for now in Atyrau")],
            [InlineKeyboardButton("Weather for 10 days", callback_data="Weather for 10 days in Atyrau")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Choose the type of weather in Atyrau(Please click once and wait a little bit):",
                                       reply_markup=reply_markup)
    elif query.data == "Aktau":
        keyboard = [
            [InlineKeyboardButton("Weather for now", callback_data="Weather for now in Aktau")],
            [InlineKeyboardButton("Weather for 10 days", callback_data="Weather for 10 days in Aktau")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Choose the type of weather in Aktau(Please click once and wait a little bit):",
                                       reply_markup=reply_markup)

    elif query.data == "Weather for now in Almaty":
        message_now_almaty_english = await ALMATY_parse_weather_english()
        if message_now_almaty_english:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=message_now_almaty_english)

    elif query.data == "Weather for 10 days in Almaty":
        message_10_days_almaty_english = await ALMATY_parse_weather_ten_days_english()
        if message_10_days_almaty_english:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=message_10_days_almaty_english)

    elif query.data == "Weather for now in Astana":
        message_now_astana_english = await ASTANA_parse_weather_english()
        if message_now_astana_english:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=message_now_astana_english)

    elif query.data == "Weather for 10 days in Astana":
        message_10_days_astana_english = await ASTANA_parse_weather_ten_days_english()
        if message_10_days_astana_english:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=message_10_days_astana_english)

    elif query.data == "Weather for now in Atyrau":
        message_now_atyrau_english = await ATYRAU_parse_weather_english()
        if message_now_atyrau_english:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=message_now_atyrau_english)

    elif query.data == "Weather for 10 days in Atyrau":
        message_10_days_atyrau_english = await ATYRAU_parse_weather_ten_days_english()
        if message_10_days_atyrau_english:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=message_10_days_atyrau_english)

    elif query.data == "Weather for now in Aktau":
        message_now_aktau_english = await AKTAU_parse_weather_english()
        if message_now_aktau_english:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=message_now_aktau_english)

    elif query.data == "Weather for 10 days in Aktau":
        message_10_days_aktau_english = await AKTAU_parse_weather_ten_days_english()
        if message_10_days_aktau_english:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=message_10_days_aktau_english)

    elif query.data == "Additionally":
        keyboard = [
            [InlineKeyboardButton("Download the video from Tiktok", callback_data="Скачать видео с Тиктока")],
            [InlineKeyboardButton("About us", callback_data="About us")]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Choose: ",
                                       reply_markup=reply_markup)

##################################################################################################################
####################      РУССКИЙ ЯЗЫК     ##########################

    elif query.data == "Алматы":
        keyboard = [
            [InlineKeyboardButton("Погода сейчас", callback_data="Погода_сейчас_в_Алматы")],
            [InlineKeyboardButton("Погода на 10 дней", callback_data="Погода_на_10_дней_в_Алматы")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
<<<<<<< HEAD
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Алматы (Пожалуйста нажмите один раз и немного подождите):",
=======
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Выберите тип погоды в Алмате(Пожалуйста нажмите один раз и немного подождите):",
>>>>>>> 7da8da2224b06529d5730a3525e587eeaa23937b
                                       reply_markup=reply_markup)
    elif query.data == "Астана":
        keyboard = [
            [InlineKeyboardButton("Погода сейчас", callback_data="Погода_сейчас_в_Астане")],
            [InlineKeyboardButton("Погода на 10 дней", callback_data="Погода_на_10_дней_в_Астане")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
<<<<<<< HEAD
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Астана (Пожалуйста нажмите один раз и немного подождите):",
=======
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Выберите тип погоды в Астане(Пожалуйста нажмите один раз и немного подождите):",
>>>>>>> 7da8da2224b06529d5730a3525e587eeaa23937b
                                       reply_markup=reply_markup)
    elif query.data == "Атырау":
        keyboard = [
            [InlineKeyboardButton("Погода сейчас", callback_data="Погода_сейчас_в_Атырау")],
            [InlineKeyboardButton("Погода на 10 дней", callback_data="Погода_на_10_дней_в_Атырау")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
<<<<<<< HEAD
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Атырау (Пожалуйста нажмите один раз и немного подождите):",
=======
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Выберите тип погоды в Атырау(Пожалуйста нажмите один раз и немного подождите):",
>>>>>>> 7da8da2224b06529d5730a3525e587eeaa23937b
                                       reply_markup=reply_markup)
    elif query.data == "Актау":
        keyboard = [
            [InlineKeyboardButton("Погода сейчас", callback_data="Погода_сейчас_в_Актау")],
            [InlineKeyboardButton("Погода на 10 дней", callback_data="Погода_на_10_дней_в_Актау")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
<<<<<<< HEAD
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Актау (Пожалуйста нажмите один раз и немного подождите):",
=======
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Выберите тип погоды в Актау(Пожалуйста нажмите один раз и немного подождите):",
>>>>>>> 7da8da2224b06529d5730a3525e587eeaa23937b
                                       reply_markup=reply_markup)

    elif query.data == "Погода_сейчас_в_Алматы":
        message_now_almaty = await ALMATY_parse_weather()
        if message_now_almaty:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=message_now_almaty)

    elif query.data == "Погода_на_10_дней_в_Алматы":
        message_10_days_almaty = await ALMATY_parse_weather_ten_days()
        if message_10_days_almaty:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=message_10_days_almaty)

    elif query.data == "Погода_сейчас_в_Астане":
        message_now_astana = await ASTANA_parse_weather()
        if message_now_astana:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=message_now_astana)

    elif query.data == "Погода_на_10_дней_в_Астане":
        message_10_days_astana = await ASTANA_parse_weather_ten_days()
        if message_10_days_astana:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=message_10_days_astana)

    elif query.data == "Погода_сейчас_в_Атырау":
        message_now_atyrau = await ATYRAU_parse_weather()
        if message_now_atyrau:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=message_now_atyrau)

    elif query.data == "Погода_на_10_дней_в_Атырау":
        message_10_days_atyrau = await ATYRAU_parse_weather_ten_days()
        if message_10_days_atyrau:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=message_10_days_atyrau)

    elif query.data == "Погода_сейчас_в_Актау":
        message_now_aktau = await AKTAU_parse_weather()
        if message_now_aktau:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=message_now_aktau)

    elif query.data == "Погода_на_10_дней_в_Актау":
        message_10_days_aktau = await AKTAU_parse_weather_ten_days()
        if message_10_days_aktau:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=message_10_days_aktau)

    elif query.data == "Дополнительно":
        keyboard = [
            [InlineKeyboardButton("Скачать видео с Тиктока", callback_data="Скачать видео с Тиктока")],
            [InlineKeyboardButton("О нас", callback_data="О нас")]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Выберите: ",
                                       reply_markup=reply_markup)
##################################################################################################################

    elif query.data == "Скачать видео с Тиктока":
        message_tiktok = "@FreeBotWithoutSubscriptions_bot"
        if message_tiktok:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=message_tiktok)

##################################################################################################################

    elif query.data == "О нас":
        message_o_nas = "Просто скучно было и сделал"
        if message_o_nas:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=message_o_nas)

    elif query.data == "About us":
        message_about_us = "I was just bored and did it"
        if message_about_us:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=message_about_us)

##################################################################################################################

<<<<<<< HEAD
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
=======

if __name__ == '__main__':
    application = ApplicationBuilder().token('7021129537:AAHnm5XFjtHrrCbcf_NYThUnVFK0NukeJOM').build()
>>>>>>> 7da8da2224b06529d5730a3525e587eeaa23937b

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()
