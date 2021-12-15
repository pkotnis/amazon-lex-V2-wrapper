from typing import Dict, List, Optional

from pydantic import BaseModel

from lex.enums import *
from lex.input import ActiveContext, DialogAction, Intent


class SessionState(BaseModel):
    activeContexts: Optional[List[ActiveContext]]
    dialogAction: Optional[DialogAction]
    intent: Optional[Intent]
    state: RequestState
    sessionAttributes: Optional[Dict[str, str]]


class Button(BaseModel):
    text: str
    value: str


class ImageResponseCard(BaseModel):
    Buttons: Optional[List[Button]]
    imageUrl: Optional[str]
    subtitle: Optional[str]
    title: str


class Message(BaseModel):
    content: Optional[str]
    contentType: ContentType
    imageResponseCard: Optional[ImageResponseCard]


class Response(BaseModel):
    # sessionId: str  Do we need that?
    sessionState: SessionState
    messages: Optional[List[Message]]  # Optional not entirely true :(
    requestAttributes: Optional[Dict[str, str]]
