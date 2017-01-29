from slackbot.bot import respond_to
from slackbot_settings import DARKSKY_API
from slackbot_settings import SKHU_LOCATION
from datetime import datetime
from datetime import timedelta
import forecastio

last_forecast = None
forecast = None


@respond_to('온도')
@respond_to('날씨')
def weather(message):
    global last_forecast
    global forecast
    dt = timedelta(hours=1)
    tz = timedelta(hours=9)

    if last_forecast is None or last_forecast < datetime.now() - dt:
        forecast = forecastio.load_forecast(
            DARKSKY_API,
            SKHU_LOCATION['lat'],
            SKHU_LOCATION['lng'],
        )

    string = "날씨 예보 입니다. " + forecast.daily().summary
    message.reply(string)
    data = forecast.currently()
    last_forecast = data.time + tz
    string = "지금 학교의 날씨 입니다! " +\
             "\n온도: " + str(data.temperature) + '℃' +\
             "\n기상: " + data.summary +\
             "\n풍속: " + str(round(data.windSpeed, 1)) + 'm/s'
    message.reply(string)
