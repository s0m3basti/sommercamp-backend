# Database Migration

Tool used : alembic

```
docker exec -it lagerwebsite-server alembic revision --autogenerate -m "added test field"   # add a new autogenerated migration

docker exec -it lagerwebsite-server alembic upgrade head # push the migrations to the database
```

To add more data models to alembic go to env.py and import data models and give base.metatdata to target metadata

Config alembic: alembic.ini -> change sqlalchemy.url