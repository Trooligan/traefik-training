# Portainer->Docker API + Traefik + Swarm

## Description

This guide explains how to use the Portainer API to control the Docker API in combination with Traefik and Swarm. Portainer provides powerful management tools for swarms, making it an ideal tool to use in conjunction with Docker API and Traefik.


## Requirements:
- External overlay networks
- Portainer API-KEY


## Setup

### 1. Init swarm
`docker swarm init`

### 2. Create overlay networks for the swarm
- `docker network create -d overlay traefik-public`
- `docker network create -d overlay agent-network`

### 3. Deploy stack
`docker stack deploy -c docker-compose.yml myswarm`

You can test the deployment by visiting http://portainer.localhost

### 4. Deploy additional services (whoami-container in *services.yml*)

`docker stack deploy -c services.yml myswarm`

<br>

---

## Portainer API KEY

### 1. Login or create Portainer account

### 2. Add a new access token

1. Navigate to *My Account* by clicking on the profile icon in the upper-right corner.
2. In the *Access Tokens* section, click on + *Add Access Token*.
3. Provide a *Description* for the access token and copy the created token.

### 3. Test the API key
`curl -k -H "Host: portainer.localhost" -H "X-API-Key:<api-key-here>" https://portainer.localhost/api/system/info`

*Expected output*: `{"platform":"","edgeAgents":0,"edgeDevices":0,"agents":1}`

<br>

---

## Scaling docker swarm services using Portainer->Docker API

> There must be a better way to do this.

### 1. Find serviceID

Easiest way -> `docker service ls`

### 2. Inspect service and create json file

Easiest way -> `docker service inpect <serviceID>`

-> Grab "Version":  {"index": **95**" value from json (needed from step 3.)

Not sure what is needed just grapped the whole crab.

-> Create .json file from these:

```json
//data.json
{
"Name": "portainer_whoami",
            "Labels": {
                "com.docker.stack.image": "traefik/whoami",
                "com.docker.stack.namespace": "portainer",
                "traefik.enable": "true",
                "traefik.http.routers.whoami.entrypoints": "web",
                "traefik.http.routers.whoami.rule": "Host(`whoami.localhost`)",
                "traefik.http.services.whoami.loadbalancer.server.port": "80"
            },
            "TaskTemplate": {
                "ContainerSpec": {
                    "Image": "traefik/whoami:latest@sha256:615ee4ae89e143eb4d8261a2699ad4659b5bcc70156928e1a721e088f458a38d",
                    "Labels": {
                        "com.docker.stack.namespace": "portainer"
                    },
                    "Privileges": {
                        "CredentialSpec": null,
                        "SELinuxContext": null
                    },
                    "Isolation": "default"
                },
                "Resources": {},
                "Placement": {
                    "Platforms": [
                        {
                            "Architecture": "386",
                            "OS": "linux"
                        },
                        {
                            "Architecture": "amd64",
                            "OS": "linux"
                        },
                        {
                            "OS": "linux"
                        },
                        {
                            "OS": "linux"
                        },
                        {
                            "Architecture": "arm64",
                            "OS": "linux"
                        }
                    ]
                },
                "Networks": [
                    {
                        "Target": "7l1dejvg89s9p3unxt8xiuprc",
                        "Aliases": [
                            "whoami"
                        ]
                    }
                ],
                "ForceUpdate": 0,
                "Runtime": "container"
            },
            "Mode": {
                "Replicated": {
                    "Replicas": 1
                }
            },
            "EndpointSpec": {
                "Mode": "vip"
            }
}
```


### 3. Scale up service using Curl

Change **Replicas** value from **data.json**

```json
// data.json
...
  "Mode": {
    "Replicated": {
      "Replicas": 2
    }
...
```

Delete <> and fill fields **SERVICE_ID**,**VERSION** and **API-KEY**:

`curl https://localhost/api/endpoints/2/docker/services/<SERVICE_ID>/update?version=<VERSION> -k -H "Host: portainer.localhost" -H "X-API-Key:<API-KEY>" -d @data.json`

Success returns:
```json
{"Warnings":null}
```




