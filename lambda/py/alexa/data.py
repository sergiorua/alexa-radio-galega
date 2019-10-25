# -*- coding: utf-8 -*-
import gettext

_ = gettext.gettext

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


en = {
    "card": {
        "title": 'Radio Galega',
        "text": 'The best radio in the best language',
        "large_image_url": 'https://alexademo.ninja/skills/logo-512.png',
        "small_image_url": 'https://alexademo.ninja/skills/logo-108.png'
    },
    "url": 'https://wecast-b02-01.flumotion.com/radiogalega/live.mp3'
}

fr = {
    "card": {
        "title": 'Radio Galega',
        "text": 'Moins de bla bla bla, plus de la la la',
        "large_image_url": 'https://alexademo.ninja/skills/logo-512.png',
        "small_image_url": 'https://alexademo.ninja/skills/logo-108.png'
    },
    "url": 'https://wecast-b02-01.flumotion.com/radiogalega/live.mp3'
}

it = {
    "card": {
        "title": 'Radio Galega',
        "text": 'Meno parlare, più musica',
        "large_image_url": 'https://alexademo.ninja/skills/logo-512.png',
        "small_image_url": 'https://alexademo.ninja/skills/logo-108.png'
    },
    "url": 'https://wecast-b02-01.flumotion.com/radiogalega/live.mp3'
}

es = {
    "card": {
        "title": 'Radio Galega',
        "text": 'A millor radio no millor idioma',
        "large_image_url": 'https://alexademo.ninja/skills/logo-512.png',
        "small_image_url": 'https://alexademo.ninja/skills/logo-108.png'
    },
    "url": 'https://wecast-b02-01.flumotion.com/radiogalega/live.mp3'
}