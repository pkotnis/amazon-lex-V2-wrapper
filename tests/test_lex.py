from unittest.mock import Mock

from lex import Lex

lex = Lex()
mock = Mock()


@lex.dialog("unavailable-intent")
def dialog_unavailable_intent():
    mock.dialog_unavailable_intent()


@lex.dialog("available-intent")
def dialog_available_intent():
    mock.dialog_available_intent()


@lex.fulfillment("unavailable-intent")
def fulfillment_unavailable_intent():
    mock.fulfillment_unavailable_intent()


@lex.fulfillment("available-intent")
def fulfillment_available_intent(slots, session_attributes, request_attributes):
    mock.fulfillment_available_intent(slots, session_attributes, request_attributes)


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
        "requestAttributes": {"request_1": "request_value"},
        "sessionState": {
            "activeContexts": [
                {
                    "name": "string",
                    "contextAttributes": {"string": "string"},
                    "timeToLive": {"timeToLiveInSeconds": 123, "turnsToLive": 33},
                }
            ],
            "sessionAttributes": {"session_1": "session_value"},
            "dialogAction": {"slotToElicit": "string", "type": "Close"},
            "intent": {
                "confirmationState": "Confirmed",
                "name": "available-intent",
                "slots": {
                    "slot_1": {
                        "value": {
                            "interpretedValue": "slot_value",
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
    mock.dialog_unavailable_intent.assert_not_called()
    mock.dialog_available_intent.assert_called_once()
    mock.fulfillment_unavailable_intent.assert_not_called()
    mock.fulfillment_available_intent.assert_not_called()


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
        "requestAttributes": {"request_1": "request_value"},
        "sessionState": {
            "activeContexts": [
                {
                    "name": "string",
                    "contextAttributes": {"string": "string"},
                    "timeToLive": {"timeToLiveInSeconds": 123, "turnsToLive": 33},
                }
            ],
            "sessionAttributes": {"session_1": "session_value"},
            "dialogAction": {"slotToElicit": "string", "type": "Close"},
            "intent": {
                "confirmationState": "Confirmed",
                "name": "available-intent",
                "slots": {
                    "slot_1": {
                        "value": {
                            "interpretedValue": "slot_value",
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
    mock.dialog_unavailable_intent.assert_not_called()
    mock.dialog_available_intent.assert_not_called()
    mock.fulfillment_unavailable_intent.assert_not_called()
    mock.fulfillment_available_intent.assert_called_once_with(
        {"slot_1": "slot_value"},
        {"session_1": "session_value"},
        {"request_1": "request_value"},
    )
