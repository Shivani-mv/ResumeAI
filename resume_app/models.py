from django.db import models

class candidate_info(models.Model):
	id = models.BigAutoField(primary_key = True)
	name = models.CharField(max_length=20,default="")
	phno = models.CharField(max_length=10,default="")
	email = models.EmailField()
	dob = models.DateField()
	gender = models.CharField(max_length=5,default="")
	Add1 = models.CharField(max_length=100,default="")
	Add2 = models.CharField(max_length=100,default="")
	city = models.CharField(max_length=50,default="")
	state = models.CharField(max_length=50,default="")
	pin = models.CharField(max_length=50,default="")
	pType = models.CharField(max_length=20,default="")
	desig = models.CharField(max_length=20,default="")
	dept = models.CharField(max_length=30,default="")


	def __str__(self):
		return self.email


class technical_info(models.Model):
	id = models.BigAutoField(primary_key=True)
	perc_10 = models.CharField(max_length=100,default="")
	year_10 = models.CharField(max_length=100,default="")
	perc_12 = models.CharField(max_length=100,default="")
	year_12 = models.CharField(max_length=100,default="")
	ug_degree = models.CharField(max_length=100,default="")
	ug_uni = models.CharField(max_length=100,default="")
	ug_spec = models.CharField(max_length=100,default="")
	perc_ug = models.CharField(max_length=100,default="")
	year_ug = models.CharField(max_length=100,default="")  #new
	pg_degree = models.CharField(max_length=100,default="")
	pg_uni = models.CharField(max_length=100,default="")
	pg_spec = models.CharField(max_length=100,default="")
	pg_perc = models.CharField(max_length=100,default="")
	year_pg = models.CharField(max_length=100,default="") #new
	phd_uni = models.CharField(max_length=100,default="")
	year_phd = models.CharField(max_length=100,default="") 
	phd_spec = models.CharField(max_length=100,default="") #new
	status = models.CharField(max_length=100,default="")
	tot_work_exp = models.CharField(max_length=100,default="")
	teach_work_exp = models.CharField(max_length=100,default="")
	interest = models.CharField(max_length=500,default="")
	skill_set = models.CharField(max_length=500,default="")


class admin_login(models.Model):
	id = models.BigAutoField(primary_key=True)
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=20)

class recp_login(models.Model):
	id = models.BigAutoField(primary_key=True)
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=20)

class Document(models.Model):
	Phone_number= models.CharField(primary_key=True,max_length=10,default='')
	document = models.FileField(upload_to='Document',default='')
	image = models.ImageField(upload_to='Images',default='')

	def __str__(self):
		return self.Phone_number
 





	