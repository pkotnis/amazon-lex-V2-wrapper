import inspect

from lex.enums import InvocationSource
from lex.input import Input
from lex.response import Response


class Lex:
    def __init__(self):
        self.functions = []

    # Methods decorated with `dialog` will be called only as the Dialog Code Hook
    def dialog(self, intent_name):
        return self._get_function(InvocationSource.DIALOG_CODE_HOOK, intent_name)

    # Methods decorated with `fulfillment` will be called only as the Fulfillment Code Hook
    def fulfillment(self, intent_name):
        return self._get_function(InvocationSource.FULFILLMENT_CODE_HOOK, intent_name)

    # Returns a ready to use lambda handler for this Lex object
    def handler(self):
        def inner(event, context):
            input_event: Input = Input.parse_obj(event)

            for function, invocation_source, intent_name in self.functions:
                if (
                    input_event.invocationSource == invocation_source
                    and input_event.sessionState.intent.name == intent_name
                ):

                    # Build a response
                    response_event: Response = Response.construct()
                    response_event.sessionState = input_event.sessionState.copy()
                    response_event.messages = []
                    response_event.requestAttributes = input_event.requestAttributes

                    class_to_value_mapping = {
                        Input: input_event,
                        Response: response_event,
                    }

                    kwargs = {}
                    function_signature = inspect.signature(function).parameters

                    for paremeter_name, parameter_object in function_signature.items():
                        if parameter_object.annotation in class_to_value_mapping:
                            kwargs[paremeter_name] = class_to_value_mapping[parameter_object.annotation]

                    return function(**kwargs)

        return inner

    def _get_function(self, invocation_source, intent_name):
        def inner(func):
            self.functions.append((func, invocation_source, intent_name))

        return inner
