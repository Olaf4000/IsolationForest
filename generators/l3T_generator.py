import pandas as pd

def generate_l3T():
    logs = pd.read_csv('../data/logs.csv')
    all_hosts = logs['host'].unique()

    client_counter = 0
    host_counter = 0

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
        print(str(host) + ": |", end="")

        counter = 0
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
            client_counter += 1

            counter += 1
            if counter % 10 == 0:
                print("-", end="")
        print("|")
        host_counter += 1

    l3T.to_csv('../data/l3T.csv', index=False)
    print("--------------- generated l3T ---------------")
    print(" Hosts generated: " + str(host_counter))
    print(" Clients generated: " + str(client_counter))
    print("---------------------------------------------")

generate_l3T()
