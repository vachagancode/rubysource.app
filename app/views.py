from django.shortcuts import render, redirect
from .models import Courses, Resources, CopyrightRules, CourseCategory, CoursesOfCategory
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

# Forms
from .forms import CourseCreationForm, ResourceCreationForm, CopyrightRuleCreationForm, CategoryCreationForm, CategoryCoursesCreationForm

def index(request):
    courses = Courses.objects.all()
    resources =  Resources.objects.all()
    copyright_rules = CopyrightRules.objects.all()
    context = {
        'title': 'Rubysource',
        'courses': courses,
        'resources': resources,
        'rules': copyright_rules,
    }
    return render(request, 'app/index.html', context)

def new_course(request):
    title = 'New Course'
    if request.method != 'POST':
        form = CourseCreationForm()
    else:
        form = CourseCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:course')
    context = {
        'title': title,
        'form': form,
    }

    return render(request, 'app/new_course.html', context)

def new_resource(request):
    title = 'Resource'
    if request.method != 'POST':
        form = ResourceCreationForm()
    else:
        form = ResourceCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:resource')
    context = {
        'title': title,
        'form': form,
    }

    return render(request, 'app/new_resource.html', context)

def new_copyright(request):
    title = 'Copyright'
    if request.method != 'POST':
        form = CopyrightRuleCreationForm()
    else:
        form = CopyrightRuleCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:copyright')
    context = {
        'title': title,
        'form': form,
    }

    return render(request, 'app/new_copyright.html', context)

def category_check(request, parameter):
    object = Courses.objects.get(title=parameter)
    try:
        categories = CourseCategory.objects.filter(parent=object)

        context = {
                'title': 'Categories',
                'object': object,
                'categories': categories,
        }
        return render(request, 'app/categories.html', context)
    except CourseCategory.DoesNotExist:
        raise Http404
    
def new_category(request):
    title = 'New Category'
    if request.method != 'POST':
        form = CategoryCreationForm()
    else:
        form = CategoryCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:new_category')
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'app/new_category.html', context)

def course_check(request, parameter , course_id):
    object = Courses.objects.get(title=parameter)
    try:
        category = CourseCategory.objects.get(id=course_id)
        courses = CoursesOfCategory.objects.filter(parent=category)

        context = {
            'courses':courses
        }

        return render(request, 'app/courses.html', context)
    except CourseCategory.DoesNotExist:
        raise Http404
    
def new_category_course(request):
    title = 'New Course'
    if request.method != 'POST':
        form = CategoryCoursesCreationForm()
    else:
        form = CategoryCoursesCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:new_cat_course')
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'app/new_category_course.html', context)


def admin(request):
    if request.user.username != "rubysource_admin_only":
        return redirect('app:index')
    else:
        return render(request, 'app/admin.html')