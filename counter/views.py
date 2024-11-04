from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1
    context = {
        'count' : request.session['count']
    }
    return render(request , "index.html" , context)

def reset(request):
    request.session['count'] = 0
    return redirect('/')