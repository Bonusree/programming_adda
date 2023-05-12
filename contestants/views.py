from django.shortcuts import render
from django.db.models import Count,Q

from problems.models import Problem
from blogs.models import Blogs
from contestants.models import Profile,User_sites
from django.contrib.auth.models import User

# @login_required
def contestants(request):
    if request.method=="POST":
        pass
    else:
        users = User.objects.all()
        contestants_info = []
        for user in users:
            num_problems = Problem.objects.filter(user=user).count()
            num_blogs = Blogs.objects.filter(user=user).count()
            contestants_info.append({'username':user.username,'problems':num_problems,'editorials':0,'blogs':num_blogs,'others':0})
        context = {'contestants_info':contestants_info}
        return render(request, 'contestants.html',context=context)

def profile(request):
    context={}
    if request.method == "POST":
        type = request.POST.get("type")
        if type=='addsite':
            try:
                user = Profile.objects.get(user=request.user)
                title = request.POST.get("website_title")
                url = request.POST.get("website_url")
                social_site = User_sites.objects.create(title=title,url=url)
                user.url.add(social_site)
            except Profile.DoesNotExist:
                print("-------------error")
                context = {'type':'info','message':'Before add your social site please add your full name or bio.'}
            except Exception as e:
                context = {'type':'error','message':f'Something wrong! Error = {e}'}
            
            
        elif type=='updateprofile':
            name = request.POST.get("name")
            bio = request.POST.get("bio")

            user = Profile.objects.filter(user=request.user)
            if user.exists()==False:
                user = Profile(user=request.user,full_name=name,bio=bio)
                user.save()
            else:
                user = Profile.objects.get(user=request.user)
                if len(bio)>0:
                    user.bio = bio
                if len(name)>0:
                    user.full_name = name
                user.save()
        else:
            context={'type':'error','message':'তুমি মানুষ ভালা না। উল্টাপালটা কাজ করো 😢'}
    user = Profile.objects.filter(user=request.user)
    if user.exists():
        user = user.first()
        if len(user.full_name)>0:
            context['full_name']=user.full_name
        if len(user.bio)>0:
            context['bio']=user.bio
        social_sites = user.url.all()
        if social_sites.exists():
            context['social_sites']=[]
            for site in social_sites:
                context['social_sites'].append({
                    'title':site.title,
                    'url':site.url
                })
    user_problems = Problem.objects.filter(user=request.user)
    if user_problems.exists():
        context['problems'] = []
        for problem in user_problems:
            context['problems'].append({'title':problem.name,'url':problem.link})
    user_blogs = Blogs.objects.filter(user=request.user)
    if user_blogs.exists():
        context['blogs'] = []
        for blog in user_blogs:
            context['blogs'].append({'title':blog.title,'url':blog.link})
            
    return render(request, 'profile.html',context=context)

def single_user_info(request):
    username = request.POST.get('searchText')
    ctx = {}
    try:
        user = User.objects.get(username=username)
        contestants_info = []
        num_problems = Problem.objects.filter(user=user).count()
        num_blogs = Blogs.objects.filter(user=user).count()
        contestants_info.append({'username':username,'problems':num_problems,'editorials':0,'blogs':num_blogs,'others':0})
        ctx['contestants_info']=contestants_info
    except User.DoesNotExist:
        ctx['type'] = 'info'
        ctx['message'] = f'No data for {username}'
    return render(request, 'contestants.html',context=ctx)
        