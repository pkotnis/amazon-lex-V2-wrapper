# Lex wrapper

Amazon Lex V2 uses only one lambda to handle all intents. This can lead to a lot of if statements around
invocation sources as well as intents.

A regular lambda handler for Lex V2 could look something like this:

```python
def handler(event, context):
  invocation_source = event["invocationSource"]
  intent_name = event["sessionState"]["intent"]["name"]

  if invocation_source == "DialogCodeHook":
    if intent_name == "OrderPizza":
      return order_pizza(event)
    elif intent_name == "OrderDrinks":
      return order_drinks(event)

  elif invocation_source == "FulfillmentCodeHook":
    if intent_name == "Confirmation":
      return finish_order(event)
```

Lex wrapper allows you to make this code much more readable:

```python
lex = Lex()

@lex.dialog("OrderPizza")
def order_pizza(event: Input):
  return order_pizza(event)

@lex.dialog("OrderDrinks")
def order_drink(event: Input):
  return order_drinks(event)

@lex.fulfillment("Confirmation")
def confirmation(event: Input):
  return finish_order(event)
```

On top of that, the `Input` object that you can optionally request in the parameters of a handler makes it much
easier to access internals of the input

```python
@lex.dialog("OrderPizza")
def dialog_order_pizza_handler(input: Input):
  for slot in input.sessionState.intent.slots.values():
    print(f"{slot.value.originalValue} was interpreted as {slot.value.interpretedValue}")

  return order_pizza(event)
```

You can also optionally ask for a `Request` object, but I don't think it is functional yet :)

```python
@lex.dialog("OrderPizza")
def dialog_order_pizza_handler(response: Response):
  response.messages.append('Hello')
  return response
```
