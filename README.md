# Anomaly detection with isolation Forest

## How to

Insert data into the `/data` folder. It has to be in the JSON format.
A single log entry should look like this:

```json
{
    "timestamp": 211256,
    "action": "ALLOW",
    "httpRequest": {
      "clientIp": "172.6.20.69",
      "country": "PH",
      "uri": "/placeholder"
    },
    "host": "www.f81C.de"
  }
```
