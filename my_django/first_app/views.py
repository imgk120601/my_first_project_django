from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect   #importing our home_made forms.py file  #from first_app.models import Topic,AccessRecord,Webpage
from first_app import forms  
from django.urls import reverse      
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

#def index(request):###------just to print the word-----####
#	return HttpResponse('<strong>Hello World</strong')


#def index(request):  #just to link to html page
#	return render(request,'index.html')
def index(request): #  ----Just to add a text----
	my_dict={'my_template_tag':'this is template_tag  value','num_template':1 }
	return render(request,'index.html',context=my_dict)

#def my_temp(request): ----Just to add a database table----
#	webpage_list=AccessRecord.objects.order_by('date')
#	date_dict={'access_records':webpage_list }
#	return render(request,'index.html',context=date_dict)

'''def my_temp(request):                             
	form=forms.FormName() #this will cheak in form

	if request.method=='POST':        #here to check whether request is is 'POST' or not by request.method
		form=forms.FormName(request.POST)    #here to make request = equal to POST request using request.POST

		if form.is_valid():                            #checking whether form is valid or not
			print('Validation Successful!!')
			print('Name : ' +form.cleaned_data['name'] )      #retriving user's input and print it to the console
			print('Email : ' + form.cleaned_data['email'])
			print('Text : ' + form.cleaned_data['text'])

	return render(request,'form_page.html',{'form':form})''' #form_dict={'form':form} will not work    -----   #return render(request,'form_page.html',context=form_dict)	

def registration(request):
	registered=False
	if request.method=='POST':
		user_form=forms.UserForm(data=request.POST)
		profile_form=forms.UserProfileInfoForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user=user_form.save()#profile_form modelform(UserForm) which has model=User and 
								#field=('username','email','password')

			user.set_password(user.password)#here in user.password user represent
			#this called password hashing go to settings.py#we have created password instance in UserForm (modelform) in form.py
			user.save()

			profile=profile_form.save(commit=False)#profile_form modelform(UserProfileInfoForm) which has model=UserProfileInfo and 
										#field=(portfolio_site,profile_pic)
			profile.user=user         #we have assign profile's user as user(in model.py)

			
			if 'profile_pic'in request.FILES:
				profile.profile_pic=request.FILES['profile_pic']
				print('its image here')
			print(request.FILES)

			profile.save()

			registered=True


		else:
			print(user_form.errors,profile_form.errors)
	else:
		user_form=forms.UserForm()
		profile_form=forms.UserProfileInfoForm()

	return render(request,'registration.html',{'registered':registered,'user_form':user_form,'profile_form':profile_form})

def user_login(request):
	if request.method=='POST':
		username=request.POST.get('username')				#after submit when you come here name column in input name='username'
		password=request.POST.get('password')  #after submit when you come here name column in input name='password'

		user=authenticate(username=	username,password= password)  #it will authenticate it is valid or not

		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect(reverse('index'))   #it will redirect it to the index.html
			else:
				return HttpResponse('Account is not active!!!!!')
		else:
			print('Some tried to login and failed')                   #printing in console
			print('Username: {} and Password: {}'.format(username,password))
			return HttpResponse('Invalid login details provided')
	else:
		return	render(request,'login.html',{})

@login_required        #inbuilt decorator that ensure you are logged in
def user_logout(request):
	logout(	request)
	return HttpResponseRedirect(reverse('index')) 

@login_required     #inbuilt decorator that ensure you are logged in
def special(request):
	return HttpResponse('You are logged in!!!!Yay!!!!!!')


def relative_url_template(request):  # --------
	return render(request,'relative_url_template.html')

def relative_url_template1(request):  # --------
	return render(request,'relative_url_template1.html')

def base(request):  # --------
	return render(request,'base.html')

def other(request):  # --------
	return render(request,'other.html')





	                                   

	
	
