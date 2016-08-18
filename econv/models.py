from django.db.models import Model
from django.db.models import CharField

class Codec(Model):
	name = CharField(max_length=20)
	alias = CharField(max_length=100)
	language = CharField(max_length=100)
