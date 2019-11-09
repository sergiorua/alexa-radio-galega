# -*- coding: utf-8 -*-

import datetime
from typing import Dict, Optional
from ask_sdk_model import Request, Response
from ask_sdk_model.ui import StandardCard, Image
from ask_sdk_model.interfaces.audioplayer import (
    PlayDirective, PlayBehavior, AudioItem, Stream, AudioItemMetadata,
    StopDirective, ClearQueueDirective, ClearBehavior)
from ask_sdk_model.interfaces import display
from ask_sdk_core.response_helper import ResponseFactory
from ask_sdk_core.handler_input import HandlerInput
from . import data

def audio_data(request):
    # type: (Request) -> Dict
    default_locale = "en-US"
    if request.locale is None:
        locale = default_locale
    else:
        locale = request.locale

    if locale.startswith("en"):
        return data.en
    elif locale.startswith("fr"):
        return data.fr
    elif locale.startswith("it"):
        return data.it
    elif locale.startswith("es"):
        return data.es
    elif locale.startswith("pt"):
        return data.pt
    elif locale.startswith("jp"):
        return data.jp
    elif locale.startswith("de"):
        return data.de
    else:
        logger.info("Locale {} not found, falling back to EN".format(locale))
        return data.en


def play(url, offset, text, card_data, response_builder):
    """Function to play audio.

    Using the function to begin playing audio when:
        - Play Audio Intent is invoked.
        - Resuming audio when stopped / paused.
        - Next / Previous commands issues.

    https://developer.amazon.com/docs/custom-skills/audioplayer-interface-reference.html#play
    REPLACE_ALL: Immediately begin playback of the specified stream,
    and replace current and enqueued streams.
    """
    # type: (str, int, str, Dict, ResponseFactory) -> Response
    if card_data:
        response_builder.set_card(
            StandardCard(
                title=card_data["title"], text=card_data["text"],
                image=Image(
                    small_image_url=card_data["small_image_url"],
                    large_image_url=card_data["large_image_url"])
            )
        )

    # Using URL as token as they are all unique
    response_builder.add_directive(
        PlayDirective(
            play_behavior=PlayBehavior.REPLACE_ALL,
            audio_item=AudioItem(
                stream=Stream(
                    token=url,
                    url=url,
                    offset_in_milliseconds=offset,
                    expected_previous_token=None),
                metadata=add_screen_background(card_data) if card_data else None
            )
        )
    ).set_should_end_session(True)

    if text:
        response_builder.speak(text)

    return response_builder.response

def play_later(url, card_data, response_builder):
    """Play the stream later.

    https://developer.amazon.com/docs/custom-skills/audioplayer-interface-reference.html#play
    REPLACE_ENQUEUED: Replace all streams in the queue. This does not impact the currently playing stream.
    """
    # type: (str, Dict, ResponseFactory) -> Response
    if card_data:
        # Using URL as token as they are all unique
        response_builder.add_directive(
            PlayDirective(
                play_behavior=PlayBehavior.REPLACE_ENQUEUED,
                audio_item=AudioItem(
                    stream=Stream(
                        token=url,
                        url=url,
                        offset_in_milliseconds=0,
                        expected_previous_token=None),
                    metadata=add_screen_background(card_data)))
        ).set_should_end_session(True)

        return response_builder.response

def stop(text, response_builder):
    """Issue stop directive to stop the audio.

    Issuing AudioPlayer.Stop directive to stop the audio.
    Attributes already stored when AudioPlayer.Stopped request received.
    """
    # type: (str, ResponseFactory) -> Response
    response_builder.add_directive(StopDirective())
    if text:
        response_builder.speak(text)

    return response_builder.response

def clear(response_builder):
    """Clear the queue amd stop the player."""
    # type: (ResponseFactory) -> Response
    response_builder.add_directive(ClearQueueDirective(
        clear_behavior=ClearBehavior.CLEAR_ENQUEUED))
    return response_builder.response

def add_screen_background(card_data):
    # type: (Dict) -> Optional[AudioItemMetadata]
    if card_data:
        metadata = AudioItemMetadata(
            title=card_data["title"],
            subtitle=card_data["text"],
            art=display.Image(
                content_description=card_data["title"],
                sources=[
                    display.ImageInstance(
                        url="https://alexademo.ninja/skills/logo-512.png")
                ]
            )
            , background_image=display.Image(
                content_description=card_data["title"],
                sources=[
                    display.ImageInstance(
                        url="https://alexademo.ninja/skills/logo-512.png")
                ]
            )
        )
        return metadata
    else:
        return None
