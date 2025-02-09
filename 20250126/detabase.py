from peewee import *

db = SqliteDatabase('Todo.db')

class memo(Model):
    name = CharField()

    class Meta:
        database = db

db.create_tables([memo])
