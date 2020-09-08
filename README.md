Red-DiscordBot Docker Image
---

# Example 

## Command

```bash
docker build -t redbot .

docker run --rm \
    -e REDBOT_NAME=redbot \
    -e REDBOT_STORAGE_TYPE=JSON \
    -e REDBOT_TOKEN=${REDBOT_TOKEN} \
    -e REDBOT_PREFIX=! \
    -v $PWD/data:/data \
    -it redbot
```

## docker-compose.yml
```yaml
version: "3.8"

services:
  redbot:
    build: .
    environment:
      REDBOT_NAME: redbot
      REDBOT_STORAGE_TYPE: POSTGRES
      REDBOT_TOKEN: ${REDBOT_TOKEN}
      REDBOT_PREFIX: !
      REDBOT_DB_HOST: postgres
      REDBOT_DB_USER: redbot
      REDBOT_DB_PASS: redbot
      REDBOT_DB_NAME: redbot
    depends_on:
      - postgres

  postgres:
    image: postgres
    environment:
      POSTGRES_PASSWORD: redbot
      POSTGRES_USER: redbot
      POSTGRES_DB: redbot
```

# Environments

- **REDBOT_NAME** - App Name
- **REDBOT_STORAGE_TYPE** - JSON / POSTGRES / MONGOV1 / MONGO (default: JSON)

### if Postgres / MonoDB / MongoDBV2

- **REDBOT_DB_HOST** - If blank : PGHOST or localhost
- **REDBOT_DB_PORT** - If blank : PGPORT or 5432
- **REDBOT_DB_USER** - If blank : PGUSER or The OS name of the user running Red 
- **REDBOT_DB_PASS** - If blank : PGPASSWORD or Looking up the password in the passfile or No password
- **REDBOT_DB_NAME** - If blank : PGDATABASE or The OS name of the user running Red