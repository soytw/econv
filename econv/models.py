from django.db.models import Model
from django.db.models import CharField

class Codec(Model):
	name = CharField(max_length=20)
	aliases = CharField(max_length=100, blank=True, null=True)
	languages = CharField(max_length=100, blank=True, null=True)
