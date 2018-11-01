from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Students(models.Model):
	class Meta:
		verbose_name_plural = "Students"

	USN = models.IntegerField(primary_key=True)
	Name = models.CharField(max_length=20)
	Department = models.CharField(max_length=4)
	Email = models.EmailField(null=True, blank=True)
	Phone = models.CharField(max_length = 15,null=True, blank=True)

	def __str__(self):
		return str(self.USN)


class Marks(models.Model):
	class Meta:
		verbose_name_plural = "Marks"
	
	USN = models.OneToOneField(Students, on_delete=models.CASCADE)
	MAT = models.IntegerField(blank=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
	CHE = models.IntegerField(blank=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
	PCD = models.IntegerField(blank=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
	CED = models.IntegerField(blank=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
	ELN = models.IntegerField(blank=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
	CIV = models.IntegerField(blank=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])


	def __str__(self):
		return str(self.USN)


