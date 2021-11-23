from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from frontend.forms import SignUpForm, LoginForm
from api.models import deltaStatus
import datetime as datetime
import numpy as np

def indexView(request):
    if not request.user.is_anonymous:
        meting_ids = request.user.profile.meting_ids
        if meting_ids is not None:
            delta_ids_sep = split_meting_ids(meting_ids)
            selected_meting_id = get_selected_delta_id(request, delta_ids_sep)

            delta_statusses = deltaStatus.objects.filter(meting_id=selected_meting_id).order_by('time').reverse()
            if len(delta_statusses) > 0:
                args = {'page':'index.html', 'delta_status': delta_statusses[0], 'meting_id': selected_meting_id}
                return render(request, 'default.html', args)
            else:
                args = {'page': 'index.html', 'meting_id': meting_ids}
                return render(request, 'default.html', args)

    # args = {'page': 'index.html',}
    # return render(request, 'default.html', args)
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

def downloadsView(request):
    template_name = 'downloads.html'
    return render(request, 'default.html', {'page': template_name})

def logboekView(request):
    if not request.user.is_anonymous:
        meting_ids = request.user.profile.meting_ids

        # check if user has meting ids in profile
        if meting_ids is not None:
            # Sepperate meting ids
            meting_ids_sep = split_meting_ids(meting_ids)

            # Get querys from request
            selected_column_names_unf = request.GET.get('column_names')
            selected_meting_id = get_selected_meting_id(request, meting_ids_sep)
            selected_startDate_unf = request.GET.get("startDate")
            selected_endDate_unf = request.GET.get("endDate")

            # Check if user filtered on meting id else set selected meting id to first meting id in profile
            if selected_meting_id is None:
                selected_meting_id = meting_ids_sep[0]

            if (selected_startDate_unf is None) or (selected_endDate_unf is None):
                now = datetime.datetime.now()
                start_date = datetime.datetime(now.year, now.month, now.day, 0, 0)
                end_date = datetime.datetime(now.year, now.month, now.day, 23, 59)
            else:
                start_date = datetime.datetime.strptime(selected_startDate_unf, '%d/%m/%Y %H:%M')
                end_date = datetime.datetime.strptime(selected_endDate_unf, '%d/%m/%Y %H:%M')
            date = (start_date, end_date)

            meting_statusses = deltaStatus.objects.filter(meting_id=selected_meting_id, time__range=date).order_by('time').reverse()

            column_names_all_unf_unfilt = [f.name for f in deltaStatus._meta.get_fields()]
            arr = np.array(list(column_names_all_unf_unfilt))
            filter_arr = []
            for element in arr:
                if (element == "meting_id"):
                    filter_arr.append(False)
                else:
                    filter_arr.append(True)
            column_names_all_unf = arr[filter_arr]
            column_names_all = format_column_names(column_names_all_unf)

            # Check if there are statusses with selected meting id
            status_matrix, column_names_form = [],[]
            if len(meting_statusses) > 0:
                # Check if user filtered on columns else use all column names
                if selected_column_names_unf is None:
                    column_names = column_names_all
                else:
                    column_names_unf = selected_column_names_unf.split(",")
                    column_names = format_column_names(column_names_unf)

                # Create table matrix
                for status in meting_statusses:
                    row = []
                    dict = vars(status)
                    for name in column_names:
                        row.append(dict[name[0]])
                    status_matrix.append(row)

            else:
                column_names = None

            # Render template
            args = {'page':'logboek.html',
                    'meting_statusses': status_matrix,
                    'meting_ids': meting_ids_sep,
                    'column_names': column_names,
                    'meting_id': selected_meting_id,
                    'column_names_all': column_names_all,
                    'chart_date_range': get_chart_date_range(),
                    'start_date': start_date.strftime('%d/%m/%Y %H:%M'),
                    'end_date': end_date.strftime('%d/%m/%Y %H:%M'),
                    }
            return render(request, 'default.html', args)

    # Render template without statusses and without meting id
    args = {'page': 'logboek.html'}
    return render(request, 'default.html', args)


def dataAnalyticsView(request):
    if not request.user.is_anonymous:
        meting_ids = request.user.profile.meting_ids

        # check if user has meting ids in profile
        if meting_ids is not None:
            # Sepperate meting ids
            meting_ids_sep = meting_ids.replace(" ","").split(";")
            meting_ids_sep = [n for n in meting_ids_sep if len(n) > 0] # Filter spaces

            # Get querys from request
            selected_meting_id = request.GET.get('meting_id')
            selected_column_names_unf = request.GET.get('column_names')
            selected_startDate_unf = request.GET.get("startDate")
            selected_endDate_unf = request.GET.get("endDate")

            # Check if user filtered on meting id else set selected meting id to first meting id in profile
            if selected_meting_id is None:
                selected_meting_id = meting_ids_sep[0]

            if (selected_startDate_unf is None) or (selected_endDate_unf is None):
                now = datetime.datetime.now()
                start_date = datetime.datetime(now.year,now.month,now.day,0,0)
                end_date = datetime.datetime(now.year,now.month,now.day,23,59)
            else:
                start_date = datetime.datetime.strptime(selected_startDate_unf, '%d/%m/%Y %H:%M')
                end_date = datetime.datetime.strptime(selected_endDate_unf, '%d/%m/%Y %H:%M')
            date = (start_date, end_date)

            # Get all meting statusses with selected meting id and selected date range
            meting_statusses = deltaStatus.objects.filter(meting_id=selected_meting_id, time__range=date).order_by('time').reverse()

            # Get all possible variables in model
            column_names_all_unf_unfilt = [f.name for f in deltaStatus._meta.get_fields()]
            arr = np.array(list(column_names_all_unf_unfilt))
            filter_arr = []
            for element in arr:
                if ((element == "meting_id") or (element == "time") or (element == 'id')):
                    filter_arr.append(False)
                else:
                    filter_arr.append(True)
            column_names_all_unf = arr[filter_arr]
            column_names_all = format_column_names(column_names_all_unf)

            # Check if there are statusses with selected meting id
            status_matrix, column_names_form = [],[]
            if len(meting_statusses) > 0:
                # Check if user filtered on columns else use all column names
                if selected_column_names_unf is None:
                    column_names = column_names_all
                else:
                    column_names_unf = selected_column_names_unf.split(",")
                    column_names = format_column_names(column_names_unf)

                # Create table matrix
                for status in meting_statusses:
                    row = []
                    dict = vars(status)
                    for name in column_names:
                        row.append(dict[name[0]])
                    status_matrix.append(row)

                charts = []

                for i in range(len(column_names)):
                    name_list = column_names[i]
                    name = name_list[0]
                    x, y = [], []
                    for s in range(len(status_matrix)):
                        row = status_matrix[s]
                        valx = meting_statusses[s].time.strftime('%Y-%m-%dT%H:%M:%S')
                        valy = float(row[i])
                        x.append(valx)
                        y.append(valy)
                    chart = Chart(name, x, y)
                    charts.append(chart)
            else:
                column_names = None
                charts = None

            # Render template
            args = {'page':'data-analytics.html',
                    'meting_statusses': status_matrix,
                    'meting_ids': meting_ids_sep,
                    'column_names': column_names,
                    'meting_id': selected_meting_id,
                    'column_names_all': column_names_all,
                    'charts': charts,
                    'start_date': start_date.strftime('%d/%m/%Y %H:%M'),
                    'end_date': end_date.strftime('%d/%m/%Y %H:%M'),
                    }
            return render(request, 'default.html', args)

    # Render template without statusses and without meting id
    args = {'page': 'data-analytics.html'}
    return render(request, 'default.html', args)



# FUNCTIONS
def format_column_names(column_names_unf):
    column_names = [None] * len(column_names_unf)
    for i in range(len(column_names_unf)):
        unformatted = column_names_unf[i]
        formatted = unformatted.replace("_", " ").capitalize()
        column_names[i] = [unformatted, formatted]
    return column_names


def get_selected_meting_id(request, meting_ids_sep):
    # get query meting id
    selected_meting_id = request.GET.get('meting_id')

    # Check if user filtered on meting id else set selected meting id to first meting id in profile
    if selected_meting_id is None:
        selected_meting_id = meting_ids_sep[0]

    return selected_meting_id


def split_meting_ids(meting_ids):
    meting_ids_sep = meting_ids.replace(" ", "").split(";")
    meting_ids_sep = [m for m in meting_ids_sep if len(m) > 0]  # Filter spaces
    return meting_ids_sep


def get_chart_date_range():
    second_date = datetime.date.today()
    first_date = datetime.date(second_date.year,second_date.month-1,second_date.day)
    range_string = first_date.strftime('%m/%d/%Y') + " - " + second_date.strftime('%m/%d/%Y')

    return range_string


class Chart:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y


def liveData(request):
    context = {
        'countAss':'Hello World',
    }
    return render(request, 'ass.html', context)