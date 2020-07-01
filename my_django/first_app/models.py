from django.db import models
from django.contrib.auth.models import User



class UserProfileInfo(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE) #in this usename,first name,last name etc...is already in included
	
	#Additional
	portfolio_site=models.URLField(blank=True)
	profile_pic=models.ImageField(upload_to='profile_pic',blank=True) #Upload_to -- profile_pics--is a folder in media
																		#for the ImageField pip install pillow
	def __str__(self):
		return self.user.username

'''class Topic(models.Model):
	top_name=models.CharField(max_length=264,unique=True )
	
	def __str__(self):
		return self.top_name

class Webpage(models.Model):
	topic=models.ForeignKey(Topic,on_delete=models.CASCADE) #artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
	name=models.CharField(max_length=264,unique=True)
	url=models.URLField(unique=True)

	def __str__(self):
		return self.name

class AccessRecord(models.Model):
	name=models.ForeignKey(Webpage,on_delete=models.CASCADE) #artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
	date=models.DateField()

	def __str__(self):
		return str(self.date)'''

#after creating models in models.py or after using modelform use --python manage.py migrate
#python manage.py makemigrations firs_app(your app in which models.py is in)
#python manage.py migrate

#you can add to modela(Topic,Webpage,AccessRecord) using python manage.py shell
#from first_app.models import Topic
#t=Topic(top_name='Social Network')
#t.save()		
#print(t.objects.all())#added
#quit()
#but to add to the model better way is to use admin feature
# go to admin