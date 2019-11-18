# -*- coding: utf-8 -*-
from gettext import gettext as _
import os

WELCOME_MSG = _("Welcome to {}")
HELP_MSG = _("Welcome to {}. You can play, stop, resume listening.  How can I help you ?")
UNHANDLED_MSG = _("Sorry, I could not understand what you've just said.")
CANNOT_SKIP_MSG = _("This is radio, you have to wait for previous or next track to play.")
RESUME_MSG = _("Resuming {}")
NOT_POSSIBLE_MSG = _("This is radio, you can not do that.  You can ask me to stop or pause to stop listening.")
STOP_MSG = _("Goodbye.")
DEVICE_NOT_SUPPORTED = _("Sorry, this skill is not supported on this device")

TEST = _("test english")
TEST_PARAMS = _("test with parameters {} and {}")

ASSETS_URL = os.environ.get('ASSETS_URL', 'https://alexa-radio-galega-assets.s3-eu-west-1.amazonaws.com')
STREAM_URL = os.environ.get('STREAM_URL', 'https://wecast-b02-01.flumotion.com/radiogalega/live.mp3')

en = {
    "card": {
        "title": 'Galega Radio',
        "name": "Radio Galega",
        "text": 'The best radio in the best language',
        "large_image_url": os.path.join(ASSETS_URL, 'Radio_Galega_Large.jpg'),
        "small_image_url": os.path.join(ASSETS_URL, 'Radio_Galega_Small.jpg')
    },
    "url": STREAM_URL
}

fr = {
    "card": {
        "title": 'Galega Radio',
        "name": "Radio Galega",
        "text": 'La meilleure radio dans la meilleure langue',
        "large_image_url": os.path.join(ASSETS_URL, 'Radio_Galega_Large.jpg'),
        "small_image_url": os.path.join(ASSETS_URL, 'Radio_Galega_Small.jpg')
    },
    "url": STREAM_URL
}

it = {
    "card": {
        "title": 'Galega Radio',
        "name": "Radio Galega",
        "text": 'La migliore radio nella migliore lingua',
        "large_image_url": os.path.join(ASSETS_URL, 'Radio_Galega_Large.jpg'),
        "small_image_url": os.path.join(ASSETS_URL, 'Radio_Galega_Small.jpg')
    },
    "url": STREAM_URL
}

es = {
    "card": {
        "title": 'Galega Radio',
        "name": "Radio Galega",
        "text": 'A millor radio na millor lingua',
        "large_image_url": os.path.join(ASSETS_URL, 'Radio_Galega_Large.jpg'),
        "small_image_url": os.path.join(ASSETS_URL, 'Radio_Galega_Small.jpg')
    },
    "url": STREAM_URL
}

pt = {
    "card": {
        "title": 'Galega Radio',
        "name": "Radio Galega",
        "text": 'A millor radio na millor lingua',
        "large_image_url": os.path.join(ASSETS_URL, 'Radio_Galega_Large.jpg'),
        "small_image_url": os.path.join(ASSETS_URL, 'Radio_Galega_Small.jpg')
    },
    "url": STREAM_URL
}

ja = {
    "card": {
        "title": 'Galega Radio',
        "name": "Radio Galega",
        "text": 'ガリシアのラジオ',
        "large_image_url": os.path.join(ASSETS_URL, 'Radio_Galega_Large.jpg'),
        "small_image_url": os.path.join(ASSETS_URL, 'Radio_Galega_Small.jpg')
    },
    "url": STREAM_URL
}

de = {
    "card": {
        "title": 'Galega Radio',
        "name": "Radio Galega",
        "text": 'Das beste Radio in der besten Sprache',
        "large_image_url": os.path.join(ASSETS_URL, 'Radio_Galega_Large.jpg'),
        "small_image_url": os.path.join(ASSETS_URL, 'Radio_Galega_Small.jpg')
    },
    "url": STREAM_URL
}
