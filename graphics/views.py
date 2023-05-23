from django.shortcuts import render
from django.utils.safestring import mark_safe

# Create your views here.
def DDA_1(x1,y1,x2,y2):
    if x1>x2 or y1>y2:
        x1,x2=x2,x1
        y1,y2=y2,y1
    dx = x2 - x1
    dy = y2 - y1
    m = dy/dx
    if m<0:
        ctx = {'type':'info','message':f'Slope is {m}, we can not process for negative slope.'}
        return ctx;
    step = max(abs(dx),abs(dy))
    xinc = dx / step
    yinc = dy / step

    context = {'type':'dda_1','headings':['Step',mark_safe('X<sub>i</sub>'),mark_safe('Y<sub>i</sub>'),mark_safe(f'X<sub>i+1</sub>=X<sub>i</sub>+{round(xinc,2)}'),
                mark_safe(f'Y<sub>i+1</sub>=Y<sub>i</sub>+{yinc}'),mark_safe('(X<sub>i+1</sub>,Y<sub>i+1</sub>)'),'Pixel'],
        'x_inc':round(xinc,2),'y_inc':round(yinc,2),'result':[],
            'x1_x2':f'{x1}-{x2}','y1_y2':f'{y1}-{y2}','dx':dx,'dy':dy,
            'step':step,'x1':x1,'y1':y1,'x2':x2,'y2':y2,'x_values':[x for x in range(max(x1-1,0),x2+2)],'y_values':[y for y in range(max(y1-1,0),y2+2)],'points':[{'x':x1,'y':y1}],
            'figure_title':f'Fig: Drawing line from ({x1},{y1}) to {x2,y2}'}
    context['chart_width']=f"{len(context['x_values'])*50}px"
    context['chart_height']=f"{len(context['y_values'])*50}px"
    context['problem_description']=f"Draw line from ({x1},{y1}) to ({x2},{y2}) using DDA line drawing algorithm"
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
    if x1>x2 or y1>y2:
        x1,x2=x2,x1
        y1,y2=y2,y1
    dx = x2-x1
    dy = y2-y1
    m = round(dy/dx,2)
    if m<0:
        ctx = {'type':'error','message':f'Slope is {m}, we can not process for negative slope.'}
        return ctx;
    ctx = {'type':'bresenham','headings':[mark_safe('X<sub>i</sub>'),mark_safe('Y<sub>i</sub>'),'Plot','Check p<0 or p>=0'],
            'dx':dx,'dy':dy,'m':m,'result':[],'points':[{'x':x1,'y':y1}],'x_values':[x for x in range(max(x1-1,0),x2+2)],'y_values':[y for y in range(max(y1-1,0),y2+2)],
            'figure_title':f'Fig: Drawing line from ({x1},{y1}) to {x2,y2}'}
    ctx['description']=[mark_safe('First calculate the followings:<br>'),
        f'dx = x2-x1 = {x2}-{x1}={x2-x1}',
        f'dy = y2-y1={y2}-{y1}={y2-y1}',
        f'm = dy/dx = {dy}/{dx} = {m}']
    ctx['chart_width']=f"{len(ctx['x_values'])*50}px"
    ctx['chart_height']=f"{len(ctx['y_values'])*50}px"
    ctx['problem_description']=f"Draw line from ({x1},{y1}) to ({x2},{y2}) using Bresenham line drawing algorithm"
    
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
    context = {}
    if request.method=="POST":
        type = request.POST.get("type")
        x1 = (int)(request.POST.get("x1"))
        y1 = (int)(request.POST.get("y1"))
        x2 = (int)(request.POST.get("x2"))
        y2 = (int)(request.POST.get("y2"))
        chart_type = request.POST.get("chart_type")
        context = {}
        if type=='dda_1':
            context=DDA_1(x1,y1,x2,y2)
        elif type=='bresenham':
            context=bresenham(x1,y1,x2,y2)
        context['chart_type'] = chart_type
    return render(request,'graphics.html',context)


def bresenham_circle(h,k,r):
    if h!=k:
        ctx = {'type':'info','message':f'h and k is not same'}
        return ctx
    
    x, y = 0,r
    p = 3-2*r
    ctx = {'type':'circle','headings':['Step',mark_safe('X<sub>i</sub>'),mark_safe('Y<sub>i</sub>'),'Plot(x,y)','Plot(y,x)','Plot(-x,y)','Plot(y,-x)','Plot(-x,-y)','Plot(-y,-x)','Plot(x,-y)','Plot(-y,x)','Check p<0 or p>=0'],
            'h':h,'k':k,'r':r,'result':[],'points':[{'x':h,'y':k}],'x_values':[x for x in range(h-r-1,h+r+2)],'y_values':[y for y in range(k-r-1,k+r+2)],
            'figure_title':f'Fig: Drawing circle',}
    ctx['description']=[mark_safe('First calculate the followings:<br>'),
        f'P = 3-2r = 3-2*{r}={3-2*r}',
        f'x = 0',
        f'x = {r}']
    ctx['chart_width']=f"{len(ctx['x_values'])*50}px"
    ctx['chart_height']=f"{len(ctx['y_values'])*50}px"
    ctx['problem_description']=f"Draw circle, which center ({h},{k}) and radius {r} using Bresenham circle drawing algorithm."
    
    step=1
    while(x<=y):
        if p<0:
            p_update = f'p<0 so p = {p}+4*{x}+6 = {p+4*x+6}'
        else:
            p_update = f'p>=0 so p = {p}+4*({x}-{y})+10 = {p+4*(x-y)+10}'
        ctx['result'].append({
            'step':step,
            'x':x,
            'y':y,
            'plot1':f'({x+h},{y+k})',
            'plot2':f'({y+k},{x+h})',
            'plot3':f'({-x+h},{y+k})',
            'plot4':f'({y+k},{-x+h})',
            'plot5':f'({-x+h},{-y+k})',
            'plot6':f'({-y+k},{-x+h})',
            'plot7':f'({x+h},{-y+k})',
            'plot8':f'({-y+k},{x+h})',
            'p_update':p_update
        })
        ctx['points'].append({'x':x+h,'y':y+k})
        ctx['points'].append({'x': y+k,'y':x+h})
        ctx['points'].append({'x': -x+h,'y':y+k})
        ctx['points'].append({'x': y+k,'y':-x+h})
        ctx['points'].append({'x': -x+h,'y':-y+k})
        ctx['points'].append({'x': -y+k,'y':-x+h})
        ctx['points'].append({'x': x+h,'y':-y+k})
        ctx['points'].append({'x': -y+k,'y':x+h})
        step += 1
        if p<0:
            p = p+4*x+6
        else:
            p = p+4*(x-y)+10
            y-=1
        x+=1
    return ctx

def midpoint_circle(h,k,r):
    if h!=k:
        ctx = {'type':'info','message':f'h and k is not same'}
        return ctx
    
    x, y = 0,r
    p = 1-r
    ctx = {'type':'circle','headings':['Step',mark_safe('X<sub>i</sub>'),mark_safe('Y<sub>i</sub>'),'Plot(x,y)','Plot(y,x)','Plot(-x,y)','Plot(y,-x)','Plot(-x,-y)','Plot(-y,-x)','Plot(x,-y)','Plot(-y,x)','Check p<0 or p>=0'],
            'h':h,'k':k,'r':r,'result':[],'points':[{'x':h,'y':k}],'x_values':[x for x in range(h-r-1,h+r+2)],'y_values':[y for y in range(k-r-1,k+r+2)],
            'figure_title':f'Fig: Drawing circle',}
    ctx['description']=[mark_safe('First calculate the followings:<br>'),
        f'P = 1-r = 1-{r}={1-r}',
        f'x = 0',
        f'x = {r}']
    ctx['chart_width']=f"{len(ctx['x_values'])*50}px"
    ctx['chart_height']=f"{len(ctx['y_values'])*50}px"
    ctx['problem_description']=f"Draw circle, which center ({h},{k}) and radius {r} using Bresenham circle drawing algorithm."
    
    step=1
    while(x<=y):
        if p<0:
            p_update = f'p<0 so p = {p}+2*{x}+6 = {p+2*x+3}'
        else:
            p_update = f'p>=0 so p = {p}+2*({x}-{y})+10 = {p+2*(x-y)+5}'
        ctx['result'].append({
            'step':step,
            'x':x,
            'y':y,
            'plot1':f'({x+h},{y+k})',
            'plot2':f'({y+k},{x+h})',
            'plot3':f'({-x+h},{y+k})',
            'plot4':f'({y+k},{-x+h})',
            'plot5':f'({-x+h},{-y+k})',
            'plot6':f'({-y+k},{-x+h})',
            'plot7':f'({x+h},{-y+k})',
            'plot8':f'({-y+k},{x+h})',
            'p_update':p_update
        })
        ctx['points'].append({'x':x+h,'y':y+k})
        ctx['points'].append({'x': y+k,'y':x+h})
        ctx['points'].append({'x': -x+h,'y':y+k})
        ctx['points'].append({'x': y+k,'y':-x+h})
        ctx['points'].append({'x': -x+h,'y':-y+k})
        ctx['points'].append({'x': -y+k,'y':-x+h})
        ctx['points'].append({'x': x+h,'y':-y+k})
        ctx['points'].append({'x': -y+k,'y':x+h})
        step += 1
        if p<0:
            p = p+2*x+3
        else:
            p = p+2*(x-y)+5
            y-=1
        x+=1
    return ctx

def graphics_circle(request):
    context = {}
    if request.method=='POST':
        type = request.POST.get("type")
        h = (int)(request.POST.get("h"))
        k = (int)(request.POST.get("k"))
        r = (int)(request.POST.get("r"))
        chart_type = request.POST.get("chart_type")
        print("chart ===== ",chart_type)
        context = {}
        if type=='midpoint':
            context = midpoint_circle(h,k,r)
        elif type=='bresenham':
            context = bresenham_circle(h,k,r)
        context['chart_type'] = chart_type
    return render(request,'graphics.html',context)