from enum import Enum


class InvocationSource(Enum):
    DIALOG_CODE_HOOK = "DialogCodeHook"
    FULFILLMENT_CODE_HOOK = "FulfillmentCodeHook"


class InputMode(Enum):
    DTFM = "DTMF"
    SPEECH = "Speech"
    TEXT = "Text"


class ContentType(Enum):
    CUSTOM_PAYLOAD = "CustomPayload"
    IMAGE_RESPONSE_CARD = "ImageResponseCard"
    PLAIN_TEXT = "PlainText"
    SSML = "SSML"


class ConfirmationState(Enum):
    CONFIRMED = "Confirmed"
    DENIED = "Denied"
    NONE = "None"


class IntentState(Enum):
    FAILED = "Failed"
    FULFILLED = "Fulfilled"
    IN_PROGRESS = "InProgress"
    READY_FOR_FULFILLMENT = "ReadyForFulfillment"
    WAITING = "Waiting"
    FULFILLMENT_IN_PROGRESS = "FulfillmentInProgress"


class SlotShape(Enum):
    SCALAR = "Scalar"
    LIST = "List"


class Sentiment(Enum):
    MIXED = "MIXED"
    NEGATIVE = "NEGATIVE"
    NEUTRAL = "NEUTRAL"
    POSITIVE = "POSITIVE"


class SlotElicitationStyle(Enum):
    DEFAULT = "Default"
    SPELL_BY_LETTER = "SpellByLetter"
    SPELL_BY_WORD = "SpellByWord"


class DialogActionType(Enum):
    CLOSE = "Close"
    CONFIRMINTENT = "ConfirmIntent"
    DELEGATE = "Delegate"
    ELICITINTENT = "ElicitIntent"
    ELICITSLOT = "ElicitSlot"
    NONE = "None"


class RequestState(Enum):
    FAILED = "Failed"
    FULFILLED = "Fulfilled"
    FULFILLMENT_IN_PROGRESS = "FulfillmentInProgress"
    IN_PROGRESS = "InProgress"
    READY_FOR_FULFILLMENT = "ReadyForFulfillment"
    WAITING = "Waiting"
