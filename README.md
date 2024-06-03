# Dasturni yurguzish
```bash
docker compose up -d --build
```
# Super user qo'shish

```bash
docker container exec -it task_web bash
```

```bash
python3 manage.py createsuperuser
```
# Malumotlar indexini yasash
```bash
python3 manage.py search_index --rebuild
```

# Swagger URL
[http://127.0.0.1:8000/swagger](http://127.0.0.1:8000/swagger)
