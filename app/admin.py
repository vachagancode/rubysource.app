from django.contrib import admin

from .models import Courses, Resources, CopyrightRules, CourseCategory, CoursesOfCategory

admin.site.register(Courses)
admin.site.register(CourseCategory)
admin.site.register(CoursesOfCategory)
admin.site.register(Resources)
admin.site.register(CopyrightRules)
