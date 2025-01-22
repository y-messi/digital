from django.contrib import admin
from .models import Student, Category, Product

# Register your models here.
try:
    admin.site.unregister(Student)
except admin.sites.NotRegistered:
    pass

# Define the custom StudentAdmin class
class StudentAdmin(admin.ModelAdmin):
    search_fields = ['title', 'author']  # Adjust the fields as needed

# Register the Student model with the custom StudentAdmin class
admin.site.register(Student, StudentAdmin)
admin.site.register(Category)
admin.site.register(Product)


