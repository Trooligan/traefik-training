# Learn the basics of Traefik. - Traefik v2.5 Basics

https://github.com/56kcloud/traefik-training

Inside every *exercise-#* folder, there is file *docker-compose.yml*, so initalization is in most cases: (There's README.md otherwise if something else is needed.)
- `docker swarm init`
- `docker stack deploy -c docker-compose.yml myswarm` *except *exercise-1*


## exercise-1 - Traefik Basic Functionality and Setting up Services

`docker-compose up --build`

### Contents:
- Adding service to traefik (traefik labels)
- Automatic + custom port routing
- Path prefixes + some middlewares

## exercise-2 - Docker Swarm / Static configuration file

### Contents:
- Adding services to swarm
- traefik.yml (entryPoints, certificateResolvers...)
- Scaling services + sticky session cookie

## exercise-3 - HTTPS / TLS / Let's Encrypt

This section is a little unfinished because I don't have a domain address and too complicated for me.


### Contents:
- Let's Encrypt HTTP Challenge
- Let's Encrypt TLS Challenge
- Let's Encrypt DNS Challenge
- Wildcard Let's Encrypt Certificate

## exercise-4 - Middlewares

### Contents:
- Basicauth
- Compression
- HTTP status code error handler (404-page...)
- Rate limit
- RedirectScheme (HTTP -> HTTPS)


## exercise-5 - Metrics, Logs, Prometheus&Grafana

### Contents:
- Logging (DEBUG, INFO, ERROR...)
- Access Logs + filters
- Traefik Metrics (using prometheus)
- Grafana (plot metrics get from prometheus)


## exercise-6 - Portainer, Docker&Portainer API

> :information_source:  **./exercise-6/README.md**

### Contents:
- Portainer + Trafik + Swarm
- PortainerAPI -> DockerAPI
- Palvelun skaalaus käyttäen PortainerAPI


## exercise-7 - Docker-container auto-scaler + other tests

> :information_source:  **./exercise-7/README.md**

### Contents:
- Prometheus + Traefik metrics
- A Python container that retrieves data from Prometheus and scales the docker service using the Docker API
- Other not documented tests

## exercise-8 Traefik Plugins & Traefik V2->V3 migration

> :information_source:  **./exercise-8/README.md**

### Contents:
- Traefik Plugins
    - Maintenance-page plugin
    - Theme.park plugin
- Traefik V3
- Different Project/Folder Structure

## exercise-9 Good practice with DockerAPI

> :information_source:  **./exercise-9/README.md**

### Contents:
- docker-api-proxy
- Exposing dockerAPI to public service through proxy-service