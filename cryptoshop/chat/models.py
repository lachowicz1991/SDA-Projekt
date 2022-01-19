from django.db.models import Model, CharField, TextField, DateTimeField


class Message(Model):
    username = CharField(max_length=255)
    room = CharField(max_length=255)
    content = TextField()
    date_added = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)