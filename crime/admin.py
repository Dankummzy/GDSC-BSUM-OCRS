from django.contrib import admin
from .models import Post, Report, Student, Security


class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'post_body', 'post_author', 'post_date')


class ReportAdmin(admin.ModelAdmin):
    list_display = ('report_title', 'report_body', 'report_author', 'report_date', 'report_location')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'student_username', 'student_email', 'student_mat_no', 'student_phone_no')


class SecurityAdmin(admin.ModelAdmin):
    list_display = ('user', 'security_username', 'security_email', 'security_phone_no')


admin.site.register(Post, PostAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Security, SecurityAdmin)
