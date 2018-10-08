from django.db import models

# Create your models here.
class Students(models.Model):
	class Meta:
		verbose_name_plural = "Students"

	USN = models.IntegerField(primary_key=True)
	Name = models.CharField(max_length=20)
	Department = models.CharField(max_length=4)
	Email = models.EmailField(null=True)
	Phone = models.CharField(max_length = 15,null=True)

	def __str__(self):
		return str(self.USN)


class Marks(models.Model):
	class Meta:
		verbose_name_plural = "Marks"
	
	USN = models.OneToOneField(Students, on_delete=models.CASCADE)
	MAT = models.IntegerField(null=True)
	CHE = models.IntegerField(null=True)
	PCD = models.IntegerField(null=True)
	CED = models.IntegerField(null=True)
	ELN = models.IntegerField(null=True)
	CIV = models.IntegerField(null=True)


	def __str__(self):
		return str(self.USN)

