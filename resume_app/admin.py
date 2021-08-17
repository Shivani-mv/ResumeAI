from resume_app.forms import adminForm
from django.contrib import admin
from .models import *

admin.site.register(candidate_info)
admin.site.register(technical_info)
admin.site.register(admin_login)
admin.site.register(recp_login)
admin.site.register(Document)




