from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from frontend.forms import SignUpForm, LoginForm
from api.models import deltaStatus

def indexView(request):
    template_name = 'index.html'
    return render(request, 'default.html', {'page': template_name})

def registerView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('Login')
    else:
        form = SignUpForm()
    return render(request, 'default.html', {'page': 'registration/register.html', 'form': form})

def loginView(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('Home')
                else:
                    form = LoginForm
                    return render(request, 'default.html', {'page': 'registration/login.html', 'form': form, 'error': 'Account is not activated'})
            else:
                form = LoginForm
                return render(request, 'default.html', {'page': 'registration/login.html', 'form': form, 'error': 'Your username and password were incorrect.'})
        except:
            form = LoginForm
            return render(request, 'default.html', {'page': 'registration/login.html', 'form': form, 'error': 'Invalid Form'})

    else:
        form = LoginForm
        return render(request, 'default.html', {'page': 'registration/login.html', 'form': form, 'error': ''})

def logoutView(request):
    logout(request)
    return redirect('Home')

def profielView(request):
    if not request.user.is_anonymous:
        meting_id = request.user.profile.meting_ids
        if meting_id != None:
            delta_statusses = deltaStatus.objects.filter(meting_id=meting_id).order_by('time').reverse()
            args = {'page': 'profiel.html', 'delta_statusses': delta_statusses, 'meting_id': meting_id}

            return render(request, 'default.html', args)
        else:
            args = {'page': 'profiel.html', 'delta_statusses': None, 'meting_id': meting_id}
            return render(request, 'default.html', args)
    else:
        args = {'page': 'profiel.html', 'delta_statusses': None}
        return render(request, 'default.html', args)

def dashboardView(request):
    if not request.user.is_anonymous:
        meting_ids = request.user.profile.meting_ids
        if meting_ids is not None:
            delta_ids_sep = split_meting_ids(meting_ids)
            selected_meting_id = get_selected_delta_id(request, delta_ids_sep)

            delta_statusses = deltaStatus.objects.filter(meting_id=selected_meting_id).order_by('time').reverse()
            if len(delta_statusses) > 0:
                args = {'page':'dashboard.html', 'delta_status': delta_statusses[0], 'meting_id': selected_meting_id}
                return render(request, 'default.html', args)
            else:
                args = {'page': 'dashboard.html', 'meting_id': meting_ids}
                return render(request, 'default.html', args)

    args = {'page': 'dashboard.html',}
    return render(request, 'default.html', args)

def split_meting_ids(delta_ids):
    delta_ids_sep = delta_ids.replace(" ", "").split(";")
    delta_ids_sep = [n for n in delta_ids_sep if len(n) > 0]  # Filter spaces
    return delta_ids_sep

def get_selected_delta_id(request, delta_ids_sep):
    # get query delta id
    selected_delta_id = request.GET.get('delta_id')

    # Check if user filtered on delta id else set selected delta id to first delta id in profile
    if selected_delta_id is None:
        selected_delta_id = delta_ids_sep[0]

    return selected_delta_id