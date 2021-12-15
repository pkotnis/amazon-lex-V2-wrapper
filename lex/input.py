from typing import Dict, List, Optional

from pydantic import BaseModel

from lex.enums import *


class Bot(BaseModel):
    id: str
    name: str
    aliasId: str
    localeId: str
    version: str


class SlotValue(BaseModel):
    interpretedValue: str
    originalValue: Optional[str]
    resolvedValues: Optional[List[str]]


class Slot(BaseModel):
    shape: Optional[SlotShape]
    value: SlotValue
    # values: Optional[List[Slot]] # multi-valued slots currently not supported


class Intent(BaseModel):
    confirmationState: Optional[ConfirmationState]
    name: str
    slots: Optional[Dict[str, Slot]]
    state: Optional[IntentState]


class ConfidenceScore(BaseModel):
    score: Optional[float]


class SentimentScore(BaseModel):
    mixed: Optional[float]
    negative: Optional[float]
    neutral: Optional[float]
    positive: Optional[float]


class SentimentResponse(BaseModel):
    sentiment: Optional[Sentiment]
    sentimentScore: Optional[SentimentScore]


class Interpretation(BaseModel):
    intent: Optional[Intent]
    nluConfidence: Optional[ConfidenceScore]
    sentimentResponse: Optional[SentimentResponse]


class TimeToLive(BaseModel):
    timeToLiveInSeconds: int
    turnsToLive: int


class ActiveContext(BaseModel):
    name: str
    contextAttributes: Dict[str, str]
    timeToLive: TimeToLive


class DialogAction(BaseModel):
    slotElicitationStyle: Optional[SlotElicitationStyle]
    slotToElicit: Optional[str]
    type: DialogActionType


class SessionState(BaseModel):
    activeContexts: Optional[List[ActiveContext]]
    dialogAction: Optional[DialogAction]
    intent: Optional[Intent]
    originatingRequestId: Optional[str]
    sessionAttributes: Dict[str, str] = {}


class Input(BaseModel):
    messageVersion: str
    invocationSource: InvocationSource
    inputMode: InputMode
    responseContentType: ContentType
    sessionId: str
    inputTranscript: str
    bot: Bot
    interpretations: List[Interpretation]
    requestAttributes: Dict[str, str]
    sessionState: SessionState
