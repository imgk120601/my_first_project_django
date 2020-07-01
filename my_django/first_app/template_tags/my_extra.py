from django import template
{% load template%}#in filter we need to load template!!!!
register=template.Library()##making of filter we are using it in {{template tag}} in index.html

@register.filter(name='cut')   #decorator it is like function which take entry as a function just below the decorator and overall 
                               #overall name of function is definec in name='***'.
def cut(value,arg):
	return value.replace(arg,'')#this will cut all 'arg' from string