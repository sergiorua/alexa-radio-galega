from botocore.vendored import requests
import os
import json
import re
import time
import datetime
from dateutil import tz, utils, parser

cardUrlSmall = 'http://www.crtvg.es/static/v2_img/rg/logo-rg.png'
cardUrlLarge = 'http://www.crtvg.es/static/v2_img/rg/logo-rg.png'
streamURL = "http://wecast-b03-03.flumotion.com/radiogalega/live.mp3"
#streamURL = "http://crtvg-radiogalega.stream.flumotion.com/radiogalega/live.mp3.m3u"
# http://dir.xiph.org/listen/808250/listen.m3u

def format_response(message, status_code):
    return {
        'statusCode': str(status_code),
        'body': json.dumps(message, default=decimal_default),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
            },
        }


def _do_get(uri):
    url = baseUrl + uri
    print(url)
    try:
        ret = requests.get(url, headers=headers)
    except Exception as e:
        print(str(e))
        return {}
    return ret.json()


def play_radio(intent, session):
    radioName = 'Radio Galega'
    session_attributes = {}
    return build_response(session_attributes, build_audioplayer_play_response(streamURL, radioName))

def stop_audioplayer(intent, session):
    session_attributes = {}
    return build_response(session_attributes, build_audioplayer_stop_response())

######################
######################

def build_speechlet_response(output, should_end_session, ssml=False):
    o = {
        'outputSpeech': {
            'type': 'SSML' if ssml is True else 'PlainText',
            'text': output,
            'ssml': "<speak>"+output+"</speak>"
        },
        'shouldEndSession': should_end_session
    }
    print(o)
    return o

def build_audioplayer_play_response(streamURL, radioName):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': 'Playing ' + radioName + ' Radio'
        },
        "card": {
            "type": "Standard",
            "title": "Radio Galega",
            "text": 'Playing ' + radioName + ' Radio',
            "image": {
                "smallImageUrl": cardUrlSmall,
                "largeImageUrl": cardUrlLarge
            }
        },
        "directives": [
            {
                "type": "AudioPlayer.Play",
                "playBehavior": "REPLACE_ALL",
                "audioItem": {
                    "stream": {
                        "token": "33|fdd9052a-717f-414f-a438-1072a64d0f49|831",
                        "url": streamURL,
                        "offsetInMilliseconds": 0
                    }
                }
            }
        ],
        'shouldEndSession': True
    }

def build_audioplayer_stop_response():
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': 'OK. Thanks for listening'
        },
        "directives": [
            {
                "type": "AudioPlayer.Stop"
            }
        ],
        'shouldEndSession': True
    }

def session_end():
    card_title = "Radio Galega"
    speech_output = "Goodbye "
    should_end_session = True
    return build_response({}, build_speechlet_response(speech_output, should_end_session))

def build_response(session_attributes, speechlet_response):
    print("In build_response")
    resp = {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }
    print(resp)
    return resp

def alexa_msg(intent, session, message):
    session_attributes = {}
    card_title = "Radio Galega"
    speech_output = str(message)
    reprompt_text = None
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(speech_output, should_end_session))    

def help():
    session_attributes = {}
    reprompt_text = None
    helptext = ["Unknown intent"]
    speech_output = 'You can ask me about todays top bets, or about the next race at a particular racecourse. I can also play horse racing and greyhounds radio.'
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(speech_output, should_end_session))

def unknown_intent():
    session_attributes = {}
    reprompt_text = None
    helptext = ["Unknown intent"]
    # TODO: We should really be logging what people are asking here, so we can build in functionality later on!!! ---------------
    speech_output = 'Im not too sure on that one. You can ask for help to hear some example of what you can ask me'
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(speech_output, should_end_session))

def on_intent(intent_request, session):
    print("on_intent requestId=" + intent_request['requestId'] + ", sessionId=" + session['sessionId'])
    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    print(intent_name + 'is intent invoked...')
    if intent_name == "HelloIntent":
        return alexa_msg(intent, session, "Hello there!")
    elif intent_name == 'PlayRadioIntent':
        return play_radio(intent, session)
    elif intent_name == 'AMAZON.NextIntent' or intent_name == 'AMAZON.PreviousIntent' or intent_name == 'AMAZON.RepeatIntent' or intent_name == 'AMAZON.StartOverIntent':
        return alexa_msg(intent, session, "This is a live stream. There is no next but track.")
    elif intent_name == "AMAZON.HelpIntent":
        return help()
    elif intent_name == "AMAZON.FallbackIntent":
        return unknown_intent()
    elif intent_name == "AMAZON.CancelIntent":
        return session_end()
    elif intent_name == "AMAZON.StopIntent" or intent_name == "AMAZON.PauseIntent":
        return stop_audioplayer(intent, session)
    else:
        raise ValueError("Invalid intent")

# --------------- Generic Events ------------------

def on_session_started(session_started_request, session):
    print("on_session_started requestId=" + session_started_request['requestId']+ ", sessionId=" + session['sessionId'])

def on_launch(launch_request, session):
    #return play_radio(None, None)
    return alexa_msg(None, None, "Welcome to Radio Galega")

def on_session_ended(session_ended_request, session):
    print("on_session_ended requestId=" + session_ended_request['requestId'] + ", sessionId=" + session['sessionId'])

def lambda_handler(event, context):
    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']}, event['session'])
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])


