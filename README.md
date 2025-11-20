# Truck Signs API
Truck Signs API is a backend service for managing truck signs in a transport fleet.
The project is containerized using Docker and uses PostgreSQL for persistent storage.

---

## Table of Contents
- [Quickstart](#quickstart)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Volumes](#volumes)
- [Restarting and Stopping Containers](#restarting-and-stopping-containers)
- [Security](#security)

---



## Quickstart
Prerequisites:
- Docker
- Docker network for DB

Steps:

1. Create your .env file:
```bash
cp .env.example .env
```

2. Create the Docker network (if not existing):
```bash
docker network create trucknet
```
3. Start PostgreSQL:
```bash
docker run -d \
  --name db \
  --network trucknet \
  -v postgres_data:/var/lib/postgresql/data \
  -e POSTGRES_USER=user \
  -e POSTGRES_PASSWORD=password \
  -e POSTGRES_DB=trucksigns \
  postgres:15
```
4. Build and run the Truck Signs API:
```bash
docker build -t truck-signs-api .
docker run -d \
  --name truckapi \
  --network trucknet \
  -p 8020:8020 \
  --env-file .env \
  truck-signs-api
```
5. Access the API:
```bash
http://<your-vm-ip>:8020
```

## Usage

* Navigate to the above URL to use the API.
* Admin panel available at /admin/.
* Entrypoint handles migrations, collectstatic, and superuser creation automatically.
* API runs on Gunicorn at port 8020.


### Environment Variables
You can configure the project by modifying .env.example:

| Variable                     | Description                          | Example                 |
|-------------------------------|--------------------------------------|-------------------------|
| DJANGO_SUPERUSER_USERNAME     | Username for Django superuser        | admin                   |
| DJANGO_SUPERUSER_EMAIL        | Email for Django superuser           | admin@example.com       |
| DJANGO_SUPERUSER_PASSWORD     | Password for Django superuser        | changeme                |
| POSTGRES_USER                 | PostgreSQL username                  | user                    |
| POSTGRES_PASSWORD             | PostgreSQL password                  | password                |
| POSTGRES_DB                   | PostgreSQL database name             | trucksigns              |
| POSTGRES_HOST                 | PostgreSQL host (container name)     | db                      |
| POSTGRES_PORT                 | PostgreSQL port                      | 5432                    |
| DEBUG                         | Django debug mode                    | False                   |



## Superuser Access (Admin Panel):
1. **Automatic creation (recommended)**  
   The entrypoint script automatically creates a superuser on the first container start if the following environment variables are set in your `.env` file:
   - `DJANGO_SUPERUSER_USERNAME`
   - `DJANGO_SUPERUSER_EMAIL`
   - `DJANGO_SUPERUSER_PASSWORD`

2. **Manual creation**  
 If you need to create a superuser manually:
 ```bash
   docker exec -it truckapi python manage.py createsuperuser
```
  
  
After the superuser is created, log in to the Django admin panel at /admin/ using the credentials you set. From the admin panel, you can:

* Manage users and permissions
* View and edit trucks, signs, or other models
* Monitor API-related data
* The API runs on Gunicorn at port 8020.
* Entrypoint also handles migrations and collectstatic automatically.


### Volumes
* postgres_data: Stores PostgreSQL database files to persist data between container restarts.

### Restarting and Stopping Containers

1. Stop and start containers:
```bash
docker stop truckapi db
docker start db truckapi
```

### Security
* Do not commit .env files, passwords, SSH keys, or other sensitive information to the repository.
* Containers communicate over Docker networks; use hostnames instead of IP addresses.
* Critical configuration is provided via environment variables only.

