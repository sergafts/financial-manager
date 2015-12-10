# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render


# @login_required
def index(request):
    return render(request, 'manager/login.html', {})


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return render(request, 'manager/login.html', {'message': 'login successful'})
            # Redirect to a success page.
        else:
            # Return a 'disabled account' error message
            return render('manager/login.html', {'message': 'you are not yet active'})
    else:
        return render(request, 'manager/login.html', {'message': 'credentials are wrong'})
