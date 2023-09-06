from django.contrib import admin

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name')
