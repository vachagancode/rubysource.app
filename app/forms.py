from django.forms import ModelForm

from .models import Courses, Resources, CopyrightRules, CourseCategory, CoursesOfCategory

class CourseCreationForm(ModelForm):
    class Meta:
        model = Courses
        fields = ['title']

class ResourceCreationForm(ModelForm):
    class Meta:
        model = Resources
        fields = ['resource_name', 'resource_link']

class CopyrightRuleCreationForm(ModelForm):
    class Meta:
        model = CopyrightRules
        fields = ['copyright_rule']
class CategoryCreationForm(ModelForm):
    class Meta:
        model = CourseCategory
        fields = ['title', 'parent']

class CategoryCoursesCreationForm(ModelForm):
    class Meta:
        model = CoursesOfCategory
        fields = ['title', 'description', 'course_creator', 'course_link', 'thumbnail', 'parent']