my venv path: C:\Users\User\.virtualenvs\src-LEnh2ho0
my activation path: C:\Users\User\.virtualenvs\src-LEnh2ho0\Scripts\activate

"""
>>> p = Provider.objects.get(id=1)
>>> t.name
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 't' is not defined
>>> p.name
'mtn'
>>> p.image
<ImageFieldFile: mtn/2.png>
>>> p.updated
datetime.datetime(2019, 4, 28, 14, 50, 14, 621910, tzinfo=<UTC>)
>>> p.services.all()
<QuerySet [<Service: MTN Lumos boost tarrif plan>, <Service: MTN Lumos boost tarrif plan.>, <Service: What is MTN PLC and where is it located?>]>

"""