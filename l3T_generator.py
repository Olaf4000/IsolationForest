import pandas as pd

logs = pd.read_csv('data/logs.csv')
all_client_ips = logs['clientIp'].unique()
all_hosts = logs['host'].unique()

l3T = pd.DataFrame({
    'host': [],
    'clientIp': [],
    'timestamp_min': [],
    'timestamp_max': [],
    'time_active': [],
    'count': []
})

for host in all_hosts:
    logs_hosts = logs[logs['host'] == host]
    print("|", end="")

    for client in logs_hosts['clientIp'].unique():
        logs_host_client = logs_hosts[logs_hosts['clientIp'] == client]
        line = {
            'host': host,
            'clientIp': client,
            'timestamp_min': logs_host_client['timestamp'].min(),
            'timestamp_max': logs_host_client['timestamp'].max(),
            'time_active': logs_host_client['timestamp'].max() - logs_host_client['timestamp'].min(),
            'count': len(logs_host_client)
        }
        l3T.loc[len(l3T)] = line
        print("-", end="")
    print("|")

l3T.to_csv('data/l3T.csv', index=False)
print("Done")
