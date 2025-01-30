# Anomaly detection with isolation Forest

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
## Data

### input for the machine learning algorithm

The aggregated data for the ml algorithm has to be inserted under `IsolationForest/data/l3T.csv`. This is not the
raw input data!

| host | clientIp | timestamp_min | timestamp_max | time_active | count |
|:-----|:---------|:--------------|:--------------|:------------|:------|
| ...  | ...      | ...           | ...           | ...         | ...   |

### use generated data

To generate sample date to try out the project you can use the the `IsolationForest/generators/`.

First execute the `IsolationForest/generators/random_access_log_generation.py` script.

If the script has run successfully execute the `IsolationForest/generators/l3T_generator.py.py` script

All file should be placed in the correct location by default.