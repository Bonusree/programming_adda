from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Problem
from .models import Tag
import json

def problems(request):
    if request.method=="POST":
        pass
    else:
        print("----------- now get request ---------- ")
        allProblems = Problem.objects.all()
        context = {'problems':[]}
        for p in allProblems:
            problem = {'name':p.name,'link':p.link,
                    'tags':[],'comment':p.comment,
                    'oj':p.judge, 'contributor':p.user}
            for t in p.tags.all():
                problem['tags'].append(t.name)
            context['problems'].append(problem)
        print("context-----------\n",context)
        return render(request, 'problems.html',context=context)
    
@login_required
def addproblem(request):
    if request.method=="POST":
        print("----------- now post request ---------- ")
        problem_name = request.POST.get('problemName')
        problem_link = request.POST.get('problemLink')
        problem_judge = request.POST.get('judge')
        problem_tags = json.loads(request.POST.get('searchTags'))
        comment = request.POST.get('comment')
        user = request.user
        
        print(problem_name)
        print(problem_link)
        print(problem_judge)
        print(problem_tags)
        print(comment)
        print("user :",user)
        
        # Create a new problem object
        problem = Problem(name=problem_name, link=problem_link,judge=problem_judge, comment=comment, user=user)
        problem.save()

        # Add tags to the problem object
        for tag_name in problem_tags:
            print("tag_name",tag_name)
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            problem.tags.add(tag)
            
    return render(request,'add_problem.html')