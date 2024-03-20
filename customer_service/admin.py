from django.contrib import admin
from customer_service.models import AllCustomerData,WebCustomersData,ServiceRequestData


class AllCustomerDataAdmin(admin.ModelAdmin):
    list_display=('bill_number','cust_name','cust_address','cust_number','cust_email')

class WebCustomersDataAdmin(admin.ModelAdmin):
    list_display=('bill_number','user_name','user_address','user_number','user_email','user_pass')

class ServiceRequestDataAdmin(admin.ModelAdmin):
    list_display=('bill_number','user_name','user_address','user_number','status','req_date','req_title','req_description')


admin.site.register(AllCustomerData,AllCustomerDataAdmin)
admin.site.register(WebCustomersData,WebCustomersDataAdmin)
admin.site.register(ServiceRequestData,ServiceRequestDataAdmin)
