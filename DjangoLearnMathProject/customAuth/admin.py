from django.contrib import admin
from customAuth.models import OTP, User

# Register your models here.



# admin.site.register(OTP)
# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'is_active')
    readonly_fields = ('created_at', 'updated_at')

    


@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    list_display = ('content', 'verification_token', 'timeout', 'type', 'used')
    readonly_fields = ('created_at', 'updated_at')