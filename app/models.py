from django.db import models

class Courses(models.Model):
    title = models.TextField()

    class Meta:
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.title
    
class Resources(models.Model):
    resource_name = models.TextField()
    resource_link = models.TextField()

    class Meta:
        verbose_name_plural = "Resources"

    def __str__(self):
        return self.resource_name
    
class CopyrightRules(models.Model):
    copyright_rule = models.TextField()

    class Meta:
        verbose_name_plural = "CopyrightRules"

    def __str__(self):
        return self.copyright_rule
    
class CourseCategory(models.Model):
    title = models.TextField()
    parent = models.ForeignKey(Courses, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "CourseCategories"
    def __str__(self):
        return self.title
    
class CoursesOfCategory(models.Model):
    title = models.TextField()
    description = models.TextField()
    course_creator = models.TextField(max_length=255)
    course_link = models.TextField()
    thumbnail = models.ImageField()
    parent = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'CoursesOfCategories'

    def __str__(self):
        return self.title
    


