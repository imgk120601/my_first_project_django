#usec to create fake data 
#it also give an idea how fully fetch site looks like see the '/admin' in browser using a faker librery
import os
os.environ.setdefault('DJANGO_SETTINGs_MODULE','my_django.settings')

import django
django.setup()

#fake pop script
import random 
from first_app.models import Topic, AccessRecord,Webpage
from faker import Faker

fakegen=Faker() 

topics=['Search','Social','Markerplace','News','Games']

def add_topic():
	t=Topic.objects.get_or_create(top_name=random.choice(topics))[0] #get_or_create method either retrive if name already is added to the Topic or...create it automatically
	t.save() #just like we do in shell
	return t 

def populate(N=5):
	for entry in range (N):
		top=add_topic() #get the topic for entry

		#creating fake data for the entry	
		fake_url=fakegen.url()
		fake_date=fakegen.date()
		fake_name=fakegen.company()# fake company name

		#create the new webpage entry
		webpg=Webpage.objects.get_or_create(topic=top,url=fake_url ,name=fake_name)[0]

		#create fake AcessRecord
		acc_rec=AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]


if __name__=='__main__':
	print('populating script!!')
	populate(20)
	print('populating complete!!!')

#run this code 
#run python manage.py runserver

  