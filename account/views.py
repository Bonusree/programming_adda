from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.db.utils import DatabaseError

from django.utils.safestring import mark_safe

from problems.models import Problem
from blogs.models import Blogs
from contestants.models import Profile
# Create your views here.

@csrf_protect
def loginPage(request):
    
    # check session context 
    context = request.session.get('context', None)
    if context!=None:
        del request.session['context']
        
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        print(user)
        if user is not None:
            login(request,user)
            context = {'type':'success','message':'Successfully you are logged in.'}
            request.session['context'] = context
            return redirect('home')
        else:
            context = {'type':'error','message':'Username or Password is incorrect!'}
            return render (request,'login.html', context=context)
        
    return render (request,'login.html',context=context)

def SignupPage(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('cpassword')
        context={'type':'error','message':''}
        
        # check password and confirm password
        if pass1!=pass2:
            context['message']='Password does not match'
            return render(request,'register.html',context=context)
        
        # check duplicate username
        if User.objects.filter(username=name).exists():
            context['message']='Duplicate username'
            return render(request,'register.html',context=context)
        
        # check duplicate email address 
        if User.objects.filter(email=email).exists():
            context['message']='Duplicate email address'
            return render(request,'register.html',context=context)

        try:
            my_user=User.objects.create_user(email, email,pass1)
            my_user.save()
        except DatabaseError as e:
            context['message']=f'Sorry something error with database. Error: {e}'
            return render(request,'register.html',context=context)
        except Exception as e:
            context['message']=f'Sorry something error. Error: {e}'
            return render(request,'register.html',context=context)
        
        context['type']='success'
        context['message']='Your registration successfully completed.'
        request.session['context']=context
        return redirect('login')
    return render (request,'register.html')

def homePage(request):
    context = request.session.get('context', None)
    if context!=None:
        del request.session['context']
    else:
        context = {}
    context['problems']=Problem.objects.count()
    context['blogs']=Blogs.objects.count()
    context['contributors']=Profile.objects.count()
    context['editorials']=0
    return render (request,'home.html',context=context)

def LogoutPage(request):
    logout(request)
    context = {'type':'success','message':'You are logout'}
    return redirect('login')


def DDA_1(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1

    step = max(abs(dx),abs(dy))
    xinc = dx / step
    yinc = dy / step

    context = {'type':'dda_1','headings':['Step',mark_safe('X<sub>i</sub>'),mark_safe('Y<sub>i</sub>'),mark_safe(f'X<sub>i+1</sub>=X<sub>i</sub>+{round(xinc,2)}'),
                mark_safe(f'Y<sub>i+1</sub>=Y<sub>i</sub>+{yinc}'),mark_safe('(X<sub>i+1</sub>,Y<sub>i+1</sub>)'),'Pixel'],
        'x_inc':round(xinc,2),'y_inc':round(yinc,2),'result':[],
            'x1_x2':f'{x1}-{x2}','y1_y2':f'{y1}-{y2}','dx':dx,'dy':dy,
            'step':step,'x1':x1,'y1':y1,'x2':x2,'y2':y2,'x_values':[x for x in range(max(x1-1,0),x2+2)],'y_values':[y for y in range(max(y1-1,0),y2+2)],'points':[{'x':x1,'y':y1}],
            'figure_title':f'Fig: Drawing line from ({x1},{y1}) to {x2,y2}'}
    print(context['points'])
    # Set initial point
    x = x1
    y = y1

    # Draw line
    for i in range(step):
        cur = {'step':i+1,'xi':round(x,2),'yi':round(y,2),
                'xi_1':f'{round(x,2)}+{round(xinc,2)}={round(x+xinc,2)}',
                'yi_1':f'{round(y,2)}+{round(yinc,2)}={round(y+yinc,2)}',
                'x_y':f'({round(x+xinc,2)},{round(y+yinc,2)})',
                'plot_x_y':f'({round(x+xinc)},{round(y+yinc)})'}
        context['points'].append({'x':round(x+xinc),'y':round(y+yinc)})
        x += xinc
        y += yinc
        context['result'].append(cur)
    print(context)
    return context
    
def bresenham(x1,y1,x2,y2):
    print(x1,y1,x2,y2)
    dx = x2-x1
    dy = y2-y1
    m = round(dy/dx,2)
    
    ctx = {'type':'bresenham','headings':[mark_safe('X<sub>i</sub>'),mark_safe('Y<sub>i</sub>'),'Plot','Check p<0 or p>=0'],
            'dx':dx,'dy':dy,'m':m,'result':[],'points':[{'x':x1,'y':y1}],'x_values':[x for x in range(max(x1-1,0),x2+2)],'y_values':[y for y in range(max(y1-1,0),y2+2)],
            'figure_title':f'Fig: Drawing line from ({x1},{y1}) to {x2,y2}'}
    ctx['description']=[mark_safe('First calculate the followings:<br>'),
        f'dx = x2-x1 = {x2}-{x1}={x2-x1}',
        f'dy = y2-y1={y2}-{y1}={y2-y1}',
        f'm = dy/dx = {dy}/{dx} = {m}']
    
    if m>=1:
        c1 = 2*dx
        c2 = 2*(dx-dy)
        p = c1-dy
        ctx['description'].append('Since m>=1, so we have to calculate-')
        ctx['description'].append(f'c1 = 2*dx= 2*{dx}={2*dx}')
        ctx['description'].append(f'c2 = 2*(dx-dy) =2({dx}-{dy})= {2*(dx-dy)}')
        ctx['description'].append(f'p = c1 - dy= {c1}-{dy}={c1-dy}')
    else:
        c1 = 2*dy
        c2 = 2*(dy-dx)
        p = c1-dx
        ctx['description'].append('Since m<1, so we have to calculate-')
        ctx['description'].append(f'c1 = 2*dy= 2*{dy}={2*dy}')
        ctx['description'].append(f'c2 = 2*(dy-dx) =2({dy}-{dx})= {2*(dy-dx)}')
        ctx['description'].append(f'p = c1 - dx= {c1}-{dx}={c1-dx}')
        
    ctx['p']=p;ctx['c1']=c1;ctx['c2']=c2
    result = []
    got=0
    while got<2:
        row={'x1':x1,'y1':y1}
        print(row)
        if p<0:
            row['f_l']=mark_safe(f'Here p={p} i.e. p<0<br>So p=p+c1={p}+({c1})={p+c1}')
            p += c1
            if m >= 1:
                row['l_l']=f'Hence, next y= y+1={y1}+1={y1+1} and x will be same as previous i.e., x={x1}'
                y1 += 1
            else:
                row['l_l']=f'Hence, next y will be same as previous i.e., y={y1} and x=x+1={x1}+1={x1+1}'
                x1 += 1
        else:
            row['f_l']=mark_safe(f'Here p={p} i.e. p>=0<br>So p=p+c2={p}+({c2})={p+c2}')
            p += c2
            row['l_l']=f'Hence, next y= y+1={y1}+1={y1+1} and x=x+1={x1}+1={x1+1}'
            y1+=1;x1+=1
        result.append(row)
        if got>0:
            got+=1
        if(x1==x2 and y1==y2):
            got=1
        if x1-2>x2 and y1-2>y2:
            result.clear()
            ctx.clear()
            ctx['type']='bresenham'
            ctx['description']=['Please swap coordinate']
            break
        if(x1<=x2 and y1<=y2):
            ctx['points'].append({'x':x1,'y':y1})
    try:
        result[-1]['l_l']=mark_safe(f'Since x= x<sub>end</sub> i.e., x={x2} and y=y<sub>end</sub> i.e., y={y2} so the process is to be stopped.')
    except:
        pass
    ctx['result']=result
    
    print(ctx)
    return ctx

def graphics(request):
    if request.method=="POST":
        type = request.POST.get("type")
        x1 = (int)(request.POST.get("x1"))
        y1 = (int)(request.POST.get("y1"))
        x2 = (int)(request.POST.get("x2"))
        y2 = (int)(request.POST.get("y2"))
        
        if type=='dda_1':
            return render(request,'graphics.html',context=DDA_1(x1,y1,x2,y2))
        # elif type=='dda_2':
        #     return render(request,'graphics.html',context=DDA_2(x1,y1,x2,y2))
        else:
            return render(request,'graphics.html',context=bresenham(x1,y1,x2,y2))
    else:
        return render(request,'graphics.html')