import requests
import requests_unixsocket
import sys
import time
import json

session = requests_unixsocket.Session()

data_url = "http://prometheus:9090/api/v1/query?query=traefik_service_requests_total"
docker_url = "http+unix://%2Fvar%2Frun%2Fdocker.sock/v1.41"

# Loopin kierrosten laskentaan
counter=1

total_activity_old = 0
total_activity_new = 0

# Ajastin
timer = time.time() + 10
timer2 = time.time() + 30


# FILL THESE
swarm_name='myswarm'
service_name='whoami'

# Paljonko pavelua skaalataan yhdellä kertaa
scale_factor=1


while True:
    print("\n----------------\nIteration:", counter, file=sys.stderr)

    # 10 sekunttia mennyt niin suoritaa
    if time.time() > timer:

        print("Timer expired. Reset values", file=sys.stderr)
        
        
        # Resetoi ajastimen
        ajastin = time.time() + 10
        
        # Päivittää vanhan aktiivisuus muuttujan
        total_activity_old = total_activity_new


    # Noutaa metriikat
    try:
        r = requests.get(data_url)

        if r:
            data = r.json()['data']['result']

            total_activity_temp = 0
            
            # Etsii datasta "*service_name*@docker" palvelut ja summaa ne yhteen
            for obj in data:
                if obj['metric']['service'] == "{}@docker".format(service_name):
                    total_activity_temp += int(obj['value'][1])

            total_activity_new = total_activity_temp
            
            print('\nACTIVITY',total_activity_new, file=sys.stderr)
            print('new-activity:',total_activity_new, file=sys.stderr)
            print('old-activity:',total_activity_old, file=sys.stderr)

            counter += 1
            
        else:
            print("Metrics fetch failed 2", file=sys.stderr)
        
    except:
        print("Metrics fetch failed 1", file=sys.stderr)


    # Koska spagetti on jees
    if counter == 2:
        total_activity_old = total_activity_new

    # Tarkistaa onko 10s aikana tullut yli 10 muutosta aktiviteettiin
    else:
        if int(total_activity_new) - int(total_activity_old) > 10:
            print("Scaling {} service".format(service_name), file=sys.stderr)
            total_activity_old = total_activity_new


            # Hakee palveluista *service_name*-palvelun tiedot, joita tarvitaan skaalaukseen
            try:
                r = session.get(docker_url+'/services')
                data = r.json()
                for i in range(len(data)):
                    if data[i]['Spec']['Name'] == '{}_{}'.format(swarm_name, service_name):
                        container_ID = data[i]['ID']
                        container_version = data[i]['Version']['Index']
                        container_spec = data[i]['Spec']
                        container_replicas = data[i]['Spec']['Mode']['Replicated']['Replicas']
                        container_spec['Mode']['Replicated']['Replicas'] = int(container_replicas) + 1
                        break
                try:
                    container_spec_json = json.dumps(container_spec, indent = 4) 
                    r = session.post(docker_url+'/services/{}/update?version={}'.format(container_ID, container_version), data=container_spec_json)
                    print(r.json(), file=sys.stderr)

                except:
                    print("failed to update whoami")
            
            except:
                print("No connection to docker api", file=sys.stderr)
            
            print("POG SCALED WHOAMI from {} -> {}".format(container_replicas, int(container_replicas)+1))

    time.sleep(2)

