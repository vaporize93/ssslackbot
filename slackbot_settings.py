# Need ENV : SLACKBOT_API_TOKEN, DARKSKY_API
import os

DEFAULT_REPLY = "몰라"

ERROR_TO = 'junsu'

PLUGINS = [
    'plugins.example',
    'plugins.weather',
    'plugins.reactions',
    'plugins.geo',
]

try:
    DARKSKY_API = os.environ['DARKSKY_API']
except KeyError:
    pass
