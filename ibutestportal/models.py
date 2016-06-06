from django.db import models


class ApiInfo(models.Model):
    request_name=models.CharField(max_length=100,null=True)
    request_url=models.CharField(max_length=1000)
    request_content=models.CharField(max_length=999999999999)
    response_content=models.CharField(max_length=999999999999)
    create_date=models.DateTimeField()

    def __str__(self):
        return self.request_name

