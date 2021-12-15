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
    "interpretations": [
        {
            "intent": {
                "confirmationState": "Confirmed",
                "name": "SampleIntent",
                "slots": {
                    "string": {
                        "value": {
                            "interpretedValue": "string",
                            "originalValue": "string",
                            "resolvedValues": ["string"],
                        }
                    },
                    "string": {
                        "shape": "List",
                        "value": {
                            "interpretedValue": "string",
                            "originalValue": "string",
                            "resolvedValues": ["string"],
                        },
                        "values": [
                            {
                                "shape": "Scalar",
                                "value": {
                                    "originalValue": "string",
                                    "interpretedValue": "string",
                                    "resolvedValues": ["string"],
                                },
                            },
                            {
                                "shape": "Scalar",
                                "value": {
                                    "originalValue": "string",
                                    "interpretedValue": "string",
                                    "resolvedValues": ["string"],
                                },
                            },
                        ],
                    },
                },
                "state": "Fulfilled",
                "kendraResponse": {},
            },
            "nluConfidence": {"score": 0.98},
            "sentimentResponse": {
                "sentiment": "POSITIVE",
                "sentimentScore": {
                    "mixed": 0.12,
                    "negative": 0.2,
                    "neutral": 0.4,
                    "positive": 0.5,
                },
            },
        }
    ],
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
            "name": "SampleIntent",
            "slots": {
                "string1": {
                    "value": {
                        "interpretedValue": "string",
                        "originalValue": "string",
                        "resolvedValues": ["string"],
                    }
                },
                "string2": {
                    "shape": "List",
                    "value": {
                        "interpretedValue": "string",
                        "originalValue": "string",
                        "resolvedValues": ["string"],
                    },
                    "values": [
                        {
                            "shape": "Scalar",
                            "value": {
                                "originalValue": "string",
                                "interpretedValue": "string",
                                "resolvedValues": ["string"],
                            },
                        },
                        {
                            "shape": "Scalar",
                            "value": {
                                "originalValue": "string",
                                "interpretedValue": "string",
                                "resolvedValues": ["string"],
                            },
                        },
                    ],
                },
            },
            "state": "Fulfilled",
            "kendraResponse": {},
            "originatingRequestId": "string",
        },
    },
}

response_event = {
    "sessionState": {
        "activeContexts": [
            {
                "name": "string",
                "contextAttributes": {"key": "value"},
                "timeToLive": {"timeToLiveInSeconds": 123, "turnsToLive": 22},
            }
        ],
        "sessionAttributes": {"string": "string"},
        "dialogAction": {
            "slotElicitationStyle": "Default",
            "slotToElicit": "string",
            "type": "Close",
        },
        "intent": {
            "confirmationState": "Confirmed",
            "name": "string",
            "slots": {
                "string": {
                    "value": {
                        "interpretedValue": "string",
                        "originalValue": "string",
                        "resolvedValues": ["string"],
                    }
                },
                "string": {
                    "shape": "List",
                    "value": {
                        "originalValue": "string",
                        "interpretedValue": "string",
                        "resolvedValues": ["string"],
                    },
                    "values": [
                        {
                            "shape": "Scalar",
                            "value": {
                                "originalValue": "string",
                                "interpretedValue": "string",
                                "resolvedValues": ["string"],
                            },
                        },
                        {
                            "shape": "Scalar",
                            "value": {
                                "originalValue": "string",
                                "interpretedValue": "string",
                                "resolvedValues": ["string"],
                            },
                        },
                    ],
                },
            },
        },
        "state": "Fulfilled",
    },
    "messages": [
        {
            "contentType": "PlainText",
            "content": "string",
            "imageResponseCard": {
                "title": "string",
                "subtitle": "string",
                "imageUrl": "string",
                "buttons": [{"text": "string", "value": "string"}],
            },
        }
    ],
    "requestAttributes": {"string": "string"},
}
