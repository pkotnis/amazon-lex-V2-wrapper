import inspect
from enum import Enum


class Lex:
    def __init__(self):
        self.functions = []

    # Methods decorated with `dialog` will be called only as the Dialog Code Hook
    def dialog(self, intent_name):
        return self._get_function("DialogCodeHook", intent_name)

    # Methods decorated with `fulfillment` will be called only as the Fulfillment Code Hook
    def fulfillment(self, intent_name):
        return self._get_function("FulfillmentCodeHook", intent_name)

    # Returns a ready to use lambda handler for this Lex object
    def handler(self):
        def inner(event, context):
            request_attributes = event.get("requestAttributes", {})
            session_attributes = event["sessionState"].get("sessionAttributes", {})
            original_slots = event["sessionState"]["intent"]["slots"]
            slots = {
                slot_name: slot_value["value"]["interpretedValue"] for slot_name, slot_value in original_slots.items()
            }

            for function, invocation_source, intent_name in self.functions:
                if (
                    event["invocationSource"] == invocation_source
                    and event["sessionState"]["intent"]["name"] == intent_name
                ):

                    mapping = {
                        "request_attributes": request_attributes,
                        "session_attributes": session_attributes,
                        "slots": slots,
                    }

                    kwargs = {
                        paremeter_name: mapping[paremeter_name]
                        for paremeter_name in inspect.signature(function).parameters.keys()
                        if paremeter_name in mapping
                    }

                    return function(**kwargs)

        return inner

    def _get_function(self, invocation_source, intent_name):
        def inner(func):
            self.functions.append((func, invocation_source, intent_name))

        return inner
