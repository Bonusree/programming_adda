from django.shortcuts import render
from django.db.models import Count,Q

from problems.models import Problem
from blogs.models import Blogs
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
    return render(request, 'profile.html')

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
        