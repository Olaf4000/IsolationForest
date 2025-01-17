# Anomaly detection with isolation Forest

## How to

Insert data into the `/data/logs.json` folder. It has to be in the JSON format.
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

## Data

### input data

| name | usage                                          |
|:-----|:-----------------------------------------------|
|logs  |raw log files as JSON list                      |
|l3T   |noramized and augmented log files as a CSV file |

## sample results

### first attempt of isolation forest

The input data of the first attempt looked like this:

|   | host        | clientIp        | timestamp\_min | timestamp\_max | time\_active | count |
|:--|:------------|:----------------|:---------------|:---------------|:-------------|:------|
| 0 | www.f81C.de | 104.215.18.178  | 48295          | 286809         | 238514       | 4     |
| 1 | www.f81C.de | 110.193.215.48  | 189303         | 228127         | 38824        | 2     |
| 2 | www.f81C.de | 110.251.240.42  | 51088          | 51088          | 0            | 1     |
| 3 | www.f81C.de | 115.147.226.201 | 34296          | 104285         | 69989        | 6     |
| 4 | www.f81C.de | 115.239.140.6   | 225932         | 225932         | 0            | 1     |
| 5 | www.f81C.de | 118.45.72.40    | 42878          | 218826         | 175948       | 8     |
| 6 | www.f81C.de | 120.6.48.216    | 40880          | 255223         | 214343       | 5     |
| 7 | www.f81C.de | 122.164.48.164  | 31119          | 263515         | 232396       | 6     |
| 8 | www.f81C.de | 123.215.134.210 | 50191          | 297878         | 247687       | 4     |
| 9 | www.f81C.de | 127.199.221.38  | 25508          | 28981          | 3473         | 2     |

after training the model and predicting the anomaly score the result looked like this:

|   | host        | clientIp        | timestamp\_min | timestamp\_max | time\_active | count | anomaly | anomaly\_score |
|:--|:------------|:----------------|:---------------|:---------------|:-------------|:------|:--------|:---------------|
| 0 | www.f81C.de | 104.215.18.178  | 48295          | 286809         | 238514       | 4     | 1       | 0.093002       |
| 1 | www.f81C.de | 110.193.215.48  | 189303         | 228127         | 38824        | 2     | 1       | 0.055464       |
| 2 | www.f81C.de | 110.251.240.42  | 51088          | 51088          | 0            | 1     | 1       | 0.033778       |
| 3 | www.f81C.de | 115.147.226.201 | 34296          | 104285         | 69989        | 6     | -1      | -0.058396      |
| 4 | www.f81C.de | 115.239.140.6   | 225932         | 225932         | 0            | 1     | 1       | 0.017611       |
| 5 | www.f81C.de | 118.45.72.40    | 42878          | 218826         | 175948       | 8     | -1      | -0.021464      |
| 6 | www.f81C.de | 120.6.48.216    | 40880          | 255223         | 214343       | 5     | 1       | 0.097059       |
| 7 | www.f81C.de | 122.164.48.164  | 31119          | 263515         | 232396       | 6     | 1       | 0.076642       |
| 8 | www.f81C.de | 123.215.134.210 | 50191          | 297878         | 247687       | 4     | 1       | 0.060956       |
| 9 | www.f81C.de | 127.199.221.38  | 25508          | 28981          | 3473         | 2     | -1      | -0.020290      |

visualisation of the time_active against the count of requests:

![](/sample_diagrams/count_timeActive.png)

if calculate the mean anomaly_score of each clientIp you get the following scatter:

![](/sample_diagrams/meanAnomalyScore_clientIp.png)

due to the generated sample date the results aren´t very realistic
