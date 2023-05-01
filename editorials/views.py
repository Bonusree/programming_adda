from cmath import rect
from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Editorials
from problems.models import Tag,Judge
import json
from django.db.models import Q
# @login_required
def editorials(request):
   
        
        data=Editorials.objects.all()
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
        data=Editorials.objects.filter(Q(name=searchText) | Q(link=searchText))
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
    tags = Tag.objects.filter(valid=1)
    judges = Judge.objects.filter(valid=1)
    context = {'tags':[tag.name for tag in tags],'judges':[judge.name for judge in judges]}
    return render(request, 'add_editorial.html', context=context)


def after_add_editorial(request):
    if request.method=="POST":
        problem_name = request.POST.get('problemName')
        problem_link = request.POST.get('problemLink')
        problem_judge = request.POST.get('judge')
        problem_tags = json.loads(request.POST.get('searchTags'))
        tutorial = request.POST.get('tutorial')
        code = request.POST.get('code')
        user = request.user
        judge,_ = Judge.objects.get_or_create(name=problem_judge,valid=1)
        try:
           
            try:
                editorial=Editorials(name=problem_name, link=problem_link,
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
    

