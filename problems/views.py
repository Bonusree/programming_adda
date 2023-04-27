from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Problem
from .models import Tag

def problems(request):
    if request.method=="POST":
        pass
    else:
        return render(request, 'problems.html')
    
@login_required
def addproblem(request):
    if request.method=="POST":
        problem_name = request.POST.get('problemName')
        problem_link = request.POST.get('problemLink')
        problem_tags = request.POST.get('searchTags').split(',')
        comment = request.POST.get('comment')
        user = request.user
        
        print(problem_name)
        print(problem_link)
        print(problem_tags)
        print(comment)
        print("user :",user)
        
        # Create a new problem object
        problem = Problem(name=problem_name, link=problem_link, comment=comment, user=user)
        problem.save()

        # Add tags to the problem object
        for tag_name in problem_tags:
            print("tag_name",tag_name)
            tag, _ = Tag.objects.get_or_create(name=tag_name.strip())
            problem.tags.add(tag)
            
    return render(request,'add_problem.html')