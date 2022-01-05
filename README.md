# Lex wrapper

Amazon Lex V2 uses only one lambda to handle all intents. This can lead to a lot of if statements around
invocation sources as well as intents.

A regular lambda handler for Lex V2 could look something like this:

```python
def handler(event, context):
  invocation_source = event["invocationSource"]
  intent_name = event["sessionState"]["intent"]["name"]
  slots = event["sessionState"]["intent"]["slots"]
  session_attributes = event["sessionState"]["sessionAttributes"]

  if invocation_source == "DialogCodeHook":
    if intent_name == "OrderPizza":
      return order_pizza(slots)
    elif intent_name == "OrderDrinks":
      return order_drinks(slots)

  elif invocation_source == "FulfillmentCodeHook":
    if intent_name == "Confirmation":
      return finish_order(session_attributes)
```

Lex wrapper allows you to make this code much more readable:

```python
lex = Lex()

@lex.dialog("OrderPizza")
def order_pizza(slots):
  return order_pizza(slots)

@lex.dialog("OrderDrinks")
def order_drink(slots):
  return order_drinks(slots)

@lex.fulfillment("Confirmation")
def confirmation(session_attributes):
  return finish_order(session_attributes)

handler = lex.handler()
```

Each method, can optionally ask for `slots`, `session_attributes` or `request_attributes`, each one represented as a
`dict`. For slots, the values inside the dict are Lex's interpreted values.

```python
@lex.dialog("OrderPizza")
def dialog_order_pizza_handler(slots, session_attributes, request_attributes):
  for slot_name, slot_value in input.sessionState.intent.slots.items():
    print(f"{slot_name} was interpreted as {slot_value}")

  return order_pizza(session_attributes, request_attributes)
```
