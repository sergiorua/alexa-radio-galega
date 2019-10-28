#!/usr/bin/env python3

import gettext
import os


def process():
    for locale in ('es', 'pt', 'jp', 'en'):
        print("Locale is {}".format(locale))
        if locale.startswith("es"):
            locale_file_name = "es-ES"
        elif locale.startswith("jp"):
            locale_file_name = "ja-JP"
        elif locale.startswith("pt"):
            locale_file_name = "pt-BR"
        else:
            locale_file_name = locale

        print("Loading locale file: {}".format(locale_file_name))

        i18n = gettext.translation(
            'data', localedir='locales', languages=[locale_file_name],
            fallback=True)

        print("\t{}".format(i18n.lgettext("Welcome to {}")))

process()
