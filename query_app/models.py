from django.db import models


types=[
    ('student','Student'),
    ('employee','Employee'),
]
priority=[
    ('high','High'),
    ('low','Low'),
]
# Create your models here.
class register_data(models.Model):
    reg_user=models.CharField(max_length=20)
    reg_mail=models.EmailField(max_length=20)
    reg_type=models.CharField(max_length=10,choices=types)
    reg_pass=models.CharField(max_length=12)

    def __str__(self):
        return self.reg_mail

class new_query(models.Model):
    id_user=models.ForeignKey(register_data,on_delete=models.CASCADE)
    query_type=models.CharField(max_length=10,choices=types)
    query_priority=models.CharField(max_length=10,choices=priority)
    query_title=models.CharField(max_length=50)
    query_data=models.CharField(max_length=5000)
    query_date=models.DateField()
    query_sender=models.CharField(max_length=20)
    query_status=models.CharField(max_length=20)

    def _str_(self):
        return self.id_user
    
class response_queries(models.Model):
    res_id=models.ForeignKey(register_data,on_delete=models.CASCADE)
    res_typ=models.CharField(max_length=10,choices=types)
    res_priority=models.CharField(max_length=10,choices=priority)
    res_title=models.CharField(max_length=50)
    query_date=models.DateField()
    response_data=models.CharField(max_length=5000)
    resonded_date=models.DateField()
    query_sender=models.CharField(max_length=20)
    status=models.CharField(max_length=20)

    def __str__(self):
        return self.response_data



    

