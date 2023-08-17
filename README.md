# Prometheuzdy-Status

[![Deployment Status](https://github.com/CarelessDev/Prometheuzdy-Status/actions/workflows/deploy.yml/badge.svg)](https://github.com/CarelessDev/Prometheuzdy-Status/actions/workflows/deploy.yml)


This repository hosts a webpage that displays the status of the `prometheuzdy.cloud` service using the `wasinuddy/prometheuzdy-pingpong` tool. The status information is obtained by pinging endpoints specified in the `IPs.json` file.

## Usage

Follow these steps to set up the status page:

### 1. Adding Services to IPs

Edit the `IPs.json` file to add the services you want to monitor. For each service, provide the following information:

- `"name"`: The name of the service.
- `"pingEndpoint"`: The endpoint to ping for checking the status.

Example `IPs.json`:

```json
[
  {
    "name": "Service 1",
    "pingEndpoint": "https://service1.example.com/ping"
  },
  {
    "name": "Service 2",
    "pingEndpoint": "https://service2.example.com/ping"
  }
]

```

### 2. Adding Pingpong service to VM

Run the [wasinuddy/prometheuzdy-pingpong]("https://hub.docker.com/repository/docker/wasinuddy/prometheuzdy-pingpong") so the status page can ping the services. Map your desire port to the container's port `5000`.

```bash
docker run -d -p 100:5000 wasinuddy/prometheuzdy-pingpong
```

