from pprint import pp

from lex import Lex
from lex.input import Input
from lex.response import Response
from samples import input_event

lex = Lex()


@lex.dialog("SampleIntent")
def dialog_sample_intent(input: Input, response: Response):
    print("dialog for SampleInput")
    for slot in input.sessionState.intent.slots.values():
        print(f"{slot.value.originalValue} was interpreted as {slot.value.interpretedValue}")


@lex.fulfillment("SampleIntent")
def fulfillment_sample_intent():
    print("fulfillment for SampleIntent")


handler = lex.handler()
handler(input_event, None)
