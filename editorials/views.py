from django.shortcuts import render,redirect

# all decorators
from django.contrib.auth.decorators import login_required

# models import here 
from .models import Editorials
from problems.models import Tag,Judge

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
    

@login_required    
def add_editorial(request):
    print("current here ",request.method)
    if request.method=="POST":
        problem_name = request.POST.get("problem_name")
        problem_link = request.POST.get("problem_link")
        editorial_link = request.POST.get("editorial_link")
        problem_judge = request.POST.get("judge")
        problem_tags = request.POST.get("searchTags")
        comment = request.POST.get("comment")
        editorial_description = request.POST.get("editorial_description")
        source_code = request.POST.get("source_code")
        
        print(" >>> ",problem_name)
        print(" >>> ",problem_link)
        print(" >>> ",editorial_link)
        print(" >>> ",problem_judge)
        print(" >>> ",problem_tags)
        print(" >>> ",comment)
        print(" >>> ",editorial_description)
        print(" >>> ",source_code)
        pass
    else:
        tags = Tag.objects.filter(valid=1)
        judges = Judge.objects.filter(valid=1)
        context = {'tags':[tag.name for tag in tags],'judges':[judge.name for judge in judges]}
        return render(request, 'add_editorial.html', context=context)
    

def search_editorial(request):
    pass
    # if request.method=="POST":
    #     searchText=request.POST.get('searchText')
    #     data=Editorials.objects.filter(Q(name=searchText) | Q(link=searchText))
    #     problems=[]
    #     for p in data:
    #         problem = {'name': p.name, 'link': p.link, 'tags':[],'code': p.code, 'solution':p.tutorial,
    #                     'oj': p.judge, 'contributor': p.user}
    #         for t in p.tags.all():
    #             problem['tags'].append(t.name)
    #         problems.append(problem)
    #     return render(request, "editorials.html", {"problems": problems})
        
    # else:
    #     return render(request, 'home.html')