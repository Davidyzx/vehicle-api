# vehicle-api
Vehicle API for 17-648 IoT project milestone 1
# Vehicle API

This project implements a Vehicle API for the 17-648 IoT project (Milestone 1).

## Features
- Provides simulated vehicle sensor data
- REST API endpoint: `/vehicle`
- Runs in Docker

## How to Run

```bash
docker build -t vehicle-api .
docker run -p 5000:5000 vehicle-api
