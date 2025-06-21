# AWS Lambda Functions

## Content

- `def lambda_handler(event, context):` This is the **main handler function** for the lambda function code.
- This contains the main application logic.
- When Lambda invokes the function handler, the lambda runtime passes two arguments to the function.
    - *event object*: that contains [data](https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html#python-handler-event) for function to process.
    - *context object*: that contains information about the [function invocation](https://docs.aws.amazon.com/lambda/latest/dg/python-context.html).

- The `context object` can be used to differentiate the task invocation using the trigger data.
- `invoked_function_arn` gives the ARN that's used to invoke the function.

- Example lambda event

```json
{
    "Location": "SEA",
    "WeatherData": {
        "TemperaturesC": {
            "MinTempC": -5.56,
            "MaxTempC": 25.56
        },
        "PressuresHPa": {
            "MinPresHPa": 1015,
            "MaxPresHPa": 1027
        }
    }
}
```

- The `event` object structure differes when triggered by different sources.

- *SNS Triggered event*
```json
{
  "Records": [
    {
      "EventSource": "aws:sns",
      "Sns": {
        "Message": "{\"Location\": \"SEA\", \"WeatherData\": {\"TemperaturesC\": {\"MinTempC\": -5.56, \"MaxTempC\": 25.56}, \"PressuresHPa\": {\"MinPresHPa\": 1015, \"MaxPresHPa\": 1027}}}"
      }
    }
  ]
}
```

- *EventBridge Triggered event*
```json
{
  "version": "0",
  "id": "event-id",
  "source": "your.custom.source",
  "detail-type": "Your Event Detail Type",
  "detail": {
    ...
  }
}
```