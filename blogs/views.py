from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from .models import Blogs
from problems.models import Judge,Problem

def blogs(request):
    context = {"type":'','message':''}
    if request.method=="POST":
        pass
    else:
        all_blogs = Blogs.objects.all()
        context = {'blogs':[]}
        for b in all_blogs:
            related_problem = b.related_problem.all()
            blog = {'name':b.title,'link':b.link,
                    'description':b.description,'comment':b.additional_comment,
                    'contributor':b.user,'blog_id':b.id,'problems':[{'link':problem.link,'name':problem.name} for problem in related_problem]}
            
            context['blogs'].append(blog)
        print("context-----------\n",context)
        return render(request, 'blogs.html',context)

@login_required
def add_blogs(request):
    print("-------request method------")
    print(request.method)
    if request.method=="POST":
        blog_name = request.POST.get("blog_name")
        blog_link = request.POST.get("blog_link")
        description = request.POST.get("description")
        comment = request.POST.get("comment")
        user = request.user
        
        # print(blog_name)
        # print(blog_link)
        # print(description)
        # print(comment)
        context = {'type':'success','message':'Thanks for your contribution'}
        try:
            new_blog = Blogs(title=blog_name,link=blog_link,description=description,additional_comment=comment,user=user)
            new_blog.save()
        except Exception as e:
            context["type"]='error'
            context["message"]=f'Error with database {e}'
            print("error :",e)
        return render(request,'add_blogs.html',context)
            
    else:
        return render(request, 'add_blogs.html')
    
@login_required
def add_blog_related_problem(request):
    if request.method=="POST":
        number_of_problems = (int)(request.POST.get("number_of_problems"))
        blog_id = request.POST.get("blog_id")
        blog_object = Blogs.objects.get(id=blog_id)
        user = request.user
        
        for i in range(0,number_of_problems):
            problem_link = request.POST.get(f"problem{i}")
            if len(problem_link)>0:
                try:
                    problem = Problem.objects.get_or_create(link=problem_link,user=user)
                    blog_object.related_problem.add(problem[0])
                    problem = Problem.objects.get(link=problem_link,user=user)
                    problem.blog.add(blog_object)
                except Exception as e:
                    print("error ",e)
        return redirect('blogs')
    else:
        pass