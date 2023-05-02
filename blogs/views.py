from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from .models import Blogs

def blogs(request):
    context = {"type":'','message':''}
    if request.method=="POST":
        pass
    else:
        all_blogs = Blogs.objects.all()
        context = {'blogs':[]}
        for b in all_blogs:
            blog = {'name':b.title,'link':b.link,
                    'description':b.description,'comment':b.additional_comment,
                    'contributor':b.user,'blog_id':b.id}
            
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