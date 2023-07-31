# Swarm commands cheatsheet

## Init Swarm
`docker swarm init`

## Deploy (and update) services from docker-compose file
`docker stack deploy -c <compose file name> <user provided stack name>`

## Update spesific service
`docker service update <service_name>`

## Check service names
`docker service ls`

## Inspect service
`docker inspect <service id>`

## Check service logs
`docker service logs <service name>`

## Scale service
`docker service scale <swarm_container_name>=<#>`

## Stop and remove stack from swarm

`docker stack rm <swarm_name>`

## Leave swarm
`docker swarm leave -f`