# Securing the Docker API and usage with Traefik

By default if you mount the dockerAPI to the service, this service is granted full access to the dockerAPI. This is going to be security issue if the service is exposed to the public network (outside of the docker internal network).
<br>

## How to start?

1. `docker-compose up --build`
2. http://localhost:8080 & http://whoami.localhost

<br>

---

<br>


## 1. Securing dockerAPI with proxy

> Dockerproxy is simple and easy to setup, so I'm not documenting the usage, look docker-socket-proxy Github page.

If multiple services need different access to the dockerAPI, it seems that we create another dockerproxy service dedicated to that service or access group. For example Traefik only needs the dockerAPIs */api/container* access, so we have a dockerproxy that has this api path enabled and traefik is connected to the same network as the dockerproxy.

1. Make a private network between the service and dockerproxy (watch *docker-compose.yml*)
2. All other public services should be connected to traefik with different network, in this project it is called "*public*"
3. Configure *treafik.yml* to use dockerproxy service
    ```yml
    providers:
    docker:
        exposedByDefault: false
        endpoint: "tcp://traefik-dockerproxy:2375"
    ```

<br>

---

## Materials
- https://doc.traefik.io/traefik/v3.0/providers/docker/#docker-api-access
- https://docs.docker.com/engine/security/
- https://chriswiegman.com/2019/11/protecting-your-docker-socket-with-traefik-2/
- [Securing The Docker Daemon (YT VIDEO)](https://www.youtube.com/watch?v=70QOBVwLyC0)
- [Docker Security Essentials | How To Secure Docker Containers (YT VIDEO)](https://www.youtube.com/watch?v=KINjI1tlo2w)
- https://github.com/Tecnativa/docker-socket-proxy



