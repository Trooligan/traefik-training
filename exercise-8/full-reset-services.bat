@ECHO OFF 

TITLE Full-reset Swarm Services

ECHO Please wait... Leaving swarm.

docker swarm leave -f

ECHO.
ECHO =================
ECHO.

ECHO Please wait... Re-initalizing swarm.
ECHO.

docker swarm init

ECHO.

docker network create -d overlay inbound

ECHO.
ECHO =================
ECHO.

ECHO Deploying core services to the swarm...
ECHO.

docker stack deploy myswarm -c ./services/traefik/docker-compose.yml

docker stack deploy myswarm -c ./services/prometheus/docker-compose.yml
docker stack deploy myswarm -c ./services/grafana/docker-compose.yml

docker stack deploy myswarm -c ./services/catapp/docker-compose.yml
docker stack deploy myswarm -c ./services/error/docker-compose.yml
docker stack deploy myswarm -c ./services/whoami/docker-compose.yml



::docker stack deploy myswarm -c ./services/scaler/docker-compose.yml

ECHO.
ECHO Deploys completed!

PAUSE