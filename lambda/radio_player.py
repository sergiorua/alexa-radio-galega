#!/usr/bin/env python

radioUrl = "http://195.10.10.213/radiogalega/live.mp3"
radioToken = "1234"

def play_radio():
    return {
        "response": {
            "directives": [
                {
                    "type": "AudioPlayer.Play",
                    "playBehavior": "REPLACE_ALL",
                    "audioItem": {
                        "stream": {
                            "token": radioToken,
                            "url": radioUrl,
                            "offsetInMilliseconds": 0
                        }
                    }
                }
            ],
            "shouldEndSession": True
        }
    }

def handle_session_end_request():
    return {
        "version": "1.0",
        "response": {
            "shouldEndSession": True
        }
    }

def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    if intent_name == "PlayMusic":
        return play_radio()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")

def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest":
        return {
            "version": "1.0",
            "response": {
                "shouldEndSession": False
            }
        }
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return handle_session_end_request()
