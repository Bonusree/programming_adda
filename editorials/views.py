from cmath import rect
from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import add_editorials
from problems.models import Tag,Judge
import json
from django.db.models import Q
# @login_required
def editorials(request):
    
    data= add_editorials.objects.all()
    problems=[]
    for p in data:
        problem = {'name': p.name, 'link': p.link, 'tags':[],'code': p.code, 'solution':p.tutorial,
                       'oj': p.judge, 'contributor': p.user}
        for t in p.tags.all():
            problem['tags'].append(t.name)
        problems.append(problem)
    return render(request, "editorials.html", {"problems": problems})

def search_editorial(request):
    if request.method=="POST":
        searchText=request.POST.get('searchText')
        data=add_editorials.objects.filter(Q(name=searchText) | Q(link=searchText))
        problems=[]
        for p in data:
            problem = {'name': p.name, 'link': p.link, 'tags':[],'code': p.code, 'solution':p.tutorial,
                        'oj': p.judge, 'contributor': p.user}
            for t in p.tags.all():
                problem['tags'].append(t.name)
            problems.append(problem)
        return render(request, "editorials.html", {"problems": problems})
        
    else:
        return render(request, 'home.html')
@login_required    
def add_editorial(request):
    # judges=Judge.objects.all()
    # tags=Tag.objects.all()
    # j=[]
    # t=[]
    # context ={'judge':[], 'tag':[]}
    # for ju in judges:
    #     context['judge'].append(ju.name)
    # for ta in tags:
    #     context['tag'].append(ta.name)
    return render(request, 'add_editorial.html')

def after_add_editorial(request):
    if request.method=="POST":
        problem_name = request.POST.get('problemName')
        problem_link = request.POST.get('problemLink')
        problem_judge = request.POST.get('judge')
        problem_tags = json.loads(request.POST.get('searchTags'))
        tutorial = request.POST.get('tutorial')
        code = request.POST.get('code')
        user = request.user
        try:
            judge= Judge.objects.filter(name=problem_judge).last()
            print(judge)
            try:
                editorial=add_editorials(name=problem_name, link=problem_link,
                                    judge=judge, tutorial=tutorial, code=code, user=user)
                editorial.save()
                for tag_name in problem_tags:
                    # print("tag_name",tag_name)
                    tag, _ = Tag.objects.get_or_create(name=tag_name,valid=1)
                    editorial.tags.add(tag)
            except Exception as e:
                print(e)       
            
            return render(request, 'profile.html')
        except Exception as e:
            print(e)
            
        
        
    else:
        return render(request, 'add_editorials.html')
    

