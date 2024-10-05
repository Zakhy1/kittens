# Запуск

1. Необходимо создать файл .env по следующему формату:

```dotenv
TZ=UTC
POSTGRES_PASSWORD=password
POSTGRES_USER=user
POSTGRES_DB=db
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

SECRET_KEY=izr*z9=%fidp7p2cueju7iulv$u$cav3m2=^!2h!c=uhjb^%^^
DEBUG=0
```

2. Запустить `docker-compose.yml`

```bash
docker-compose up -d
```

# Описание программы

* swagger находится по пути `http://localhost:8000/api/v1/swagger/`
* Авторизация приведена в группе `token`. Для выполнения некоторых действий необходим токен авторизации.
* Получение токена происходит по пути `http://localhost:8000/api/v1/token/`. Полученный `access_token` необходимо
  использовать при запросах.
* При запуске будут загружены тестовые данные.
    * Учетная запись администратора по умолчанию:
        * Логин: `admin`
        * Пароль: `admin`