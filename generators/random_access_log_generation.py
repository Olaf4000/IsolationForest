import random
import string

from urllib3 import request

# input variables
min_amount = 600
max_amount = 1100
average_amount = 500 #TODO: do dis shit
amount_of_anomaly = 4
amount_of_client = 500
amount_of_hoste = 5
timestamp_min = 100000
timestamp_max = 400000

# functions
def random_timestamp():
    return random.randint(timestamp_min, timestamp_max)

def random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_random_host():
    random_host = 'www.' + str(random_string(4)) + '.pl'
    random_number = random.randint(1, 100)

    if random_number > 1 & random_number < 50:
        random_host = 'www.' + str(random_string(4)) + '.de'
        return random_host

    if random_number > 50 & random_number < 75:
        random_host = 'www.' + str(random_string(4)) + '.com'
        return random_host

    if random_number > 75 & random_number < 100:
        random_host = 'www.' + str(random_string(4)) + '.co.uk'
        return random_host

    return random_host

def generate_multiple_random_hosts(amount_of_hosts):
    random_hosts = []

    for i in range(amount_of_hosts):
        random_hosts.append(generate_random_host())

    return random_hosts

def generate_random_ip():
    ip_byts = []

    for i in range(1, 5):
        ip_byts.append(random.randint(2, 254))

    return str(ip_byts[0]) + '.' + str(ip_byts[1]) + '.' + str(ip_byts[2]) + '.' + str(ip_byts[3])

def generate_multiple_random_ips(amount_of_ips):
    ip_list = []

    for i in range(amount_of_ips):
        ip_list.append(generate_random_ip())

    return ip_list

# generation
def generate_random_logs():
    host_counter = 0
    client_counter = 0
    request_counter = 0

    with open("../data/logs.csv", mode="w") as file:
        file.write('timestamp,action,host,clientIp,country,uri' + '\n')

        for i in range(amount_of_hoste):
            host = str(generate_random_host())
            host_counter += 1
            print('-------------- ' + str(host) + ' --------------')

            #generate_noise
            print('Generating noise for: ' + str(host))
            for j in range(amount_of_client):
                client_ip = str(generate_random_ip())
                client_counter += 1
                amount_of_requests = int(random.uniform(min_amount, max_amount))

                for k in range(amount_of_requests):
                    timestamp = random_timestamp()
                    request_counter += 1
                    file.write(
                        str(timestamp) + ',' +
                        'ALLOW' + ',' +
                        str(host) + ',' +
                        str(client_ip) + ',' +
                        'DE' + ',' +
                        '/placeholder' + '\n'
                    )

            #generate high request anomaly
            print('Generating high anomaly for: ' + str(host))
            for j in range(int(amount_of_anomaly / 2)):
                client_ip = str(generate_random_ip())
                amount_of_requests = int((random.uniform(min_amount, max_amount)) + max_amount)

                for k in range(amount_of_requests):
                    timestamp = random_timestamp()
                    file.write(
                        str(timestamp) + ',' +
                        'ALLOW' + ',' +
                        str(host) + ',' +
                        str(client_ip) + ',' +
                        'DE' + ',' +
                        '/placeholder' + '\n'
                    )

            #generate low request anomaly
            print('Generating low amount for: ' + str(host))
            for j in range(int(amount_of_anomaly / 2)):
                client_ip = str(generate_random_ip())
                amount_of_requests = int((random.uniform(min_amount, max_amount)) - min_amount)

                for k in range(amount_of_requests):
                    timestamp = int(random_timestamp() / 3)
                    file.write(
                        str(timestamp) + ',' +
                        'ALLOW' + ',' +
                        str(host) + ',' +
                        str(client_ip) + ',' +
                        'DE' + ',' +
                        '/placeholder' + '\n'
                    )
            print('-----------------------------------------')
    print("Successfully generated random logs")
    print("Hosts generated: " + str(host_counter))
    print("Clients generated: " + str(client_counter))
    print("Requests generated: " + str(request_counter))

generate_random_logs()