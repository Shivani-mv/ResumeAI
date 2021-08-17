from django import forms
from django.db.models import fields
from django.db.models.fields.files import FieldFile
from django.forms import ModelForm, widgets
from .models import *
from django.forms import TextInput,EmailInput

from django import forms
from django.forms import ModelForm, FileField,ImageField


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('Phone_number','document','image')
        widgets = {
            'Phone_number': TextInput(attrs={
                'class': "form-control",
                'style': 'font-size:20px;border-radius:5px;border-width:thin;padding-left:20px;width: 250px;height: 45px;position: relative;left:155px;top:80px;border: 1px solid lightgrey;margin-bottom:20px;margin-top:20px;'
                })

        }


class technicalForm(forms.ModelForm):
    class Meta:
        model = technical_info
        fields = ('perc_10','year_10','perc_12','year_12','ug_degree','ug_uni','ug_spec','perc_ug','year_ug','pg_degree','pg_uni','pg_spec','pg_perc','year_pg','phd_uni','year_phd','phd_spec','status','tot_work_exp','teach_work_exp','interest','skill_set')
        widgets = {
            'perc_10': TextInput(attrs={
                'class': "form-control",
                'label': 'font-size:250px',
                'style': "font-size:18px;border-radius:5px;border-width:thin;padding-left:20px;width:400px;height: 45px;position: relative;left:100px;top:50px;border: 1px solid lightgrey;"
                }),
            'year_10': TextInput(attrs={
                'class': "form-control",
                'style': "font-size:20px;border-radius:5px;border-width:thin;padding-left:20px;width:400px;height: 45px;position: relative;left:342px;top:70px;border: 1px solid lightgrey;"
                }),
            'perc_12': TextInput(attrs={
                'class': "form-control",
                'style': 'font-size:20px;border-radius:5px;border-width:thin;padding-left:10px;width: 400px;height: 45px;position: relative;left:343px;bottom:-75px;border: 1px solid lightgrey;margin-top:20px;'
                }),
            'year_12': TextInput(attrs={
                'class': "form-control",
                'style': 'font-size:20px;border-radius:5px;border-width:thin;padding-left:10px;width: 400px;height: 45px;position: relative;left:343px;bottom:-74px;border: 1px solid lightgrey;margin-top:20px;'
                }),
            'ug_degree': TextInput(attrs={
                'class': "form-control",
                'style': 'font-size:20px;border-radius:5px;border-width:thin;padding-left:10px;width: 400px;height: 45px;position: relative;left:-182px;bottom:-140px;border: 1px solid lightgrey;margin-top:20px;'
                }),
            'ug_uni': TextInput(attrs={
                'class': "form-control",
                'style': 'font-size:20px;border-radius:5px;border-width:thin;padding-left:10px;width: 400px;height: 45px;position: relative;left:343px;bottom:-140px;border: 1px solid lightgrey;margin-top:20px;'
                }),
            'ug_spec': TextInput(attrs={
                'class': "form-control",
                'style': 'font-size:20px;border-radius:5px;border-width:thin;padding-left:10px;width: 400px;height: 45px;position: relative;left:-250px;bottom:-208px;border: 1px solid lightgrey;margin-top:20px;'
                }),
            'perc_ug': TextInput(attrs={
                'class': "form-control",
                'style': 'font-size:20px;border-radius:5px;border-width:thin;padding-left:10px;width: 400px;height: 45px;position: relative;left:111px;bottom:-212px;border: 1px solid lightgrey;margin-top:20px;'
                }),
            'year_ug': TextInput(attrs={
                'class': "form-control",
                'style': 'font-size:20px;border-radius:5px;border-width:thin;padding-left:10px;width: 400px;height: 45px;position: relative;left:342px;bottom:-215px;border: 1px solid lightgrey;margin-top:20px;'
                }),
            'pg_degree': TextInput(attrs={
                'class': "form-control",
                'style': 'font-size:20px;border-radius:5px;border-width:thin;padding-left:10px;width: 400px;height: 45px;position: relative;left:-180px;bottom:-285px;border: 1px solid lightgrey;margin-top:20px;'
                }),
            'pg_uni': TextInput(attrs={
                'class': "form-control",
                'style': 'font-size:20px;border-radius:5px;border-width:thin;padding-left:10px;width: 400px;height: 45px;position: relative;left:342px;bottom:-290px;border: 1px solid lightgrey;margin-top:20px;'
                }),
            'pg_spec': TextInput(attrs={
                'class': "form-control",
                'style': 'font-size:20px;border-radius:5px;border-width:thin;padding-left:10px;width: 400px;height: 45px;position: relative;left:-250px;bottom:-360px;border: 1px solid lightgrey;margin-top:20px;'
                }),
            'pg_perc': TextInput(attrs={
                'class': "form-control",
                'style': 'font-size:20px;border-radius:5px;border-width:thin;padding-left:10px;width: 400px;height: 45px;position: relative;left:112px;bottom:-365px;border: 1px solid lightgrey;margin-top:20px;'
                }),
            'year_pg': TextInput(attrs={
                'class': "form-control",
                'style': 'font-size:20px;border-radius:5px;border-width:thin;padding-left:10px;width: 400px;height: 45px;position: relative;left:344px;bottom:-373px;border: 1px solid lightgrey;margin-top:20px;'
                }),
            'phd_uni': TextInput(attrs={
                'class': "form-control",
                'style': 'font-size:20px;border-radius:5px;border-width:thin;padding-left:10px;width: 400px;height: 45px;position: relative;left:343px;bottom:-380px;border: 1px solid lightgrey;margin-top:20px;'
                }),
            'year_phd': TextInput(attrs={
                'class': "form-control",
                'style': 'font-size:20px;border-radius:5px;border-width:thin;padding-left:10px;width: 400px;height: 45px;position: relative;left:342px;bottom:-385px;border: 1px solid lightgrey;margin-top:20px;'
                }),
            'phd_spec': TextInput(attrs={
                'class': "form-control",
                'style': 'font-size:20px;border-radius:5px;border-width:thin;padding-left:10px;width: 400px;height: 45px;position: relative;left:343px;bottom:-390px;border: 1px solid lightgrey;margin-top:20px;'
                }),
            'status': TextInput(attrs={
                'class': "form-control",
                'style': 'font-size:20px;border-radius:5px;border-width:thin;padding-left:10px;width: 400px;height: 45px;position: relative;left:-185px;bottom:-460px;border: 1px solid lightgrey;margin-top:20px;'
                }),
            'tot_work_exp': TextInput(attrs={
                'class': "form-control",
                'style': 'font-size:20px;border-radius:5px;border-width:thin;padding-left:10px;width: 400px;height: 45px;position: relative;left:342px;bottom:-330px;border: 1px solid lightgrey;margin-top:20px;'
                }),
            'teach_work_exp': TextInput(attrs={
                'class': "form-control",
                'style': 'font-size:20px;border-radius:5px;border-width:thin;padding-left:10px;width: 400px;height: 45px;position: relative;left:63px;bottom:-540px;border: 1px solid lightgrey;margin-top:20px;'
                }),
            'interest': widgets.Textarea(attrs={'rows':10,
                'class': "form-control",
                'style': 'font-size:20px;border-radius:5px;border-width:thin;padding-left:10px;width: 400px;height: 100px;position: relative;left:-163px;bottom:-550px;border: 1px solid lightgrey;margin-top:20px;'
                
                }),
            'skill_set': widgets.Textarea(attrs={'rows':10,
                'class': "form-control",
                'style': 'font-size:20px;border-radius:5px;border-width:thin;padding-left:10px;width: 400px;height: 100px;position: relative;left:343px;bottom:-560px;border: 1px solid lightgrey;margin-top:20px;'
                }),

        }
    

class adminForm(forms.ModelForm):
    class Meta:
        model = admin_login
        fields = ('username','password')

class recpForm(forms.ModelForm):
    class Meta:
        model = recp_login
        fields = ('username','password')


class candidateForm(forms.ModelForm):
    class Meta:
        model = candidate_info
        fields = ('name','phno','email','dob','gender','Add1','Add2','city','state','pin','pType','desig','dept')
        

