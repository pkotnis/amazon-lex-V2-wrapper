from unittest.mock import Mock

from lex import Lex

lex = Lex()
mock = Mock()


@lex.dialog("available-intent")
def available_intent():
    mock.dialog_available_intent()


@lex.dialog("unavailable-intent")
def unavailable_intent():
    mock.dialog_unavailable_intent()


@lex.fulfillment("available-intent")
def available_intent():
    mock.fulfillment_available_intent()


@lex.fulfillment("unavailable-intent")
def unavailable_intent():
    mock.fulfillment_unavailable_intent()


handler = lex.handler()


def test_dialog():
    mock.reset_mock()

    input_event = {
        "messageVersion": "1.0",
        "invocationSource": "DialogCodeHook",
        "inputMode": "Text",
        "responseContentType": "PlainText",
        "sessionId": "string",
        "inputTranscript": "string",
        "bot": {
            "id": "string",
            "name": "string",
            "aliasId": "string",
            "localeId": "string",
            "version": "string",
        },
        "interpretations": [],
        "requestAttributes": {"string": "string"},
        "sessionState": {
            "activeContexts": [
                {
                    "name": "string",
                    "contextAttributes": {"string": "string"},
                    "timeToLive": {"timeToLiveInSeconds": 123, "turnsToLive": 33},
                }
            ],
            "sessionAttributes": {"string": "string"},
            "dialogAction": {"slotToElicit": "string", "type": "Close"},
            "intent": {
                "confirmationState": "Confirmed",
                "name": "available-intent",
                "slots": {
                    "string": {
                        "value": {
                            "interpretedValue": "string",
                            "originalValue": "string",
                            "resolvedValues": ["string"],
                        }
                    },
                },
                "state": "Fulfilled",
                "kendraResponse": {},
                "originatingRequestId": "string",
            },
        },
    }

    handler(input_event, {})
    mock.dialog_available_intent.assert_called_once()
    mock.dialog_unavailable_intent.assert_not_called()
    mock.fulfillment_available_intent.assert_not_called()
    mock.fulfillment_unavailable_intent.assert_not_called()


def test_fulfillment():
    mock.reset_mock()

    input_event = {
        "messageVersion": "1.0",
        "invocationSource": "FulfillmentCodeHook",
        "inputMode": "Text",
        "responseContentType": "PlainText",
        "sessionId": "string",
        "inputTranscript": "string",
        "bot": {
            "id": "string",
            "name": "string",
            "aliasId": "string",
            "localeId": "string",
            "version": "string",
        },
        "interpretations": [],
        "requestAttributes": {"string": "string"},
        "sessionState": {
            "activeContexts": [
                {
                    "name": "string",
                    "contextAttributes": {"string": "string"},
                    "timeToLive": {"timeToLiveInSeconds": 123, "turnsToLive": 33},
                }
            ],
            "sessionAttributes": {"string": "string"},
            "dialogAction": {"slotToElicit": "string", "type": "Close"},
            "intent": {
                "confirmationState": "Confirmed",
                "name": "available-intent",
                "slots": {
                    "string": {
                        "value": {
                            "interpretedValue": "string",
                            "originalValue": "string",
                            "resolvedValues": ["string"],
                        }
                    },
                },
                "state": "Fulfilled",
                "kendraResponse": {},
                "originatingRequestId": "string",
            },
        },
    }

    handler(input_event, {})
    mock.dialog_available_intent.assert_not_called()
    mock.dialog_unavailable_intent.assert_not_called()
    mock.fulfillment_available_intent.assert_called_once()
    mock.fulfillment_unavailable_intent.assert_not_called()
