from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import *
# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def trigerpreferencepage(request):
    if request.method == "POST":
        username = request.POST['username']
        age = float(request.POST['age'])
        height = float(request.POST['height'])
        weight = float(request.POST['weight'])
        water = float(request.POST['water'])
        protein = float(request.POST['protein'])
        carbs = float(request.POST['carbs'])
        fats = float(request.POST['fats'])
        dicti = {'username': username, 'age': age, 'height': height, 'weight': weight, 'water': water, 'protein': protein, 'carbs': carbs, 'fats': fats}
        dicti['select_trigger'] = True
        request.session['dicti'] = dicti
        return render (request, 'prefselect.html', dicti)
    else:
        dicti = request.session['dicti']
        print(dicti)
        dicti['select_trigger'] = True
        return render (request, 'prefselect.html', dicti)



def analysehelpfunction(request,condition, value, param):
    currentvalue = int(request.session['dicti'][param])
    if (condition == 1):
            if (currentvalue >= value): #Here I should give that param value
                return False
            else:
                return True
    elif condition == 2:
        if (currentvalue <= value):
            return False
        else:
            return True
    elif condition == 3:
        if (currentvalue == value):
            return True
        else:
            return False;


def analysereq(request):
    if request.method == "POST":
        param = request.POST['param']
        value = int(request.POST['value'])
        condition = int(request.POST['condition'])
        dicti = request.session['dicti']
        if (analysehelpfunction (request,condition, value, param)):
            dicti['analyse_repost'] = True
            dicti['select_trigger'] = False
            return render (request, 'prefselect.html', dicti)
        else:
            #Give a message
            dicti['select_trigger'] = True
            messages.info (request, 'Seems your current value is well with in your desired range')
            return render (request, 'prefselect.html', dicti)
        #Like wise I have to write for all functions
    else:
        dicti = request.session['dicti']
        dicti['analyse_repost'] = True
        print("came here")
        dicti['select_trigger'] = False
        return render (request, 'prefselect.html', dicti)


def functionality(request):
    param = int(request.POST['param'])
    dicti = request.session['dicti']
    dicti['analyse_repost'] = False
    dicti['select_trigger'] = False
    dicti['copynumber'] = False
    dicti['arthematic'] = False
    dicti['graphanalysis'] = False
    if (param == 1):
        dicti['copynumber'] = True
        return render (request, 'prefselect.html', dicti)
    elif (param == 2):
        dicti['arthematic'] = True
        return render (request, 'prefselect.html', dicti)
    elif (param == 3):
        dicti['graphanalysis'] = True
    return render (request, 'prefselect.html', dicti)

def copynumber(request):
    copyfrom = request.POST['copyfromparam']
    copyto = request.POST['copytoparam']
    request.session['dicti'][copyto] = request.session['dicti'][copyfrom]
    request.session.modified = True
    dicti = request.session['dicti']
    print(dicti)
    dicti['show_values'] = 1
    return render(request, 'details.html', dicti) 

def arthematic(request):
    param = request.POST['param']
    operation = int(request.POST['arthematic'])
    refvalue = int(request.POST['refvalue'])

    if (operation == 1):
        request.session['dicti'][param] += refvalue
    elif (operation == 2):
        request.session['dicti'][param] -= refvalue
    elif (operation == 3):
        request.session['dicti'][param] *= refvalue
    elif (operation == 4):
        if (refvalue == 0):
            dicti = request.session['dicti']
            dicti['select_trigger'] = False
            dicti['analyse_repost'] = True
            messages.info (request, 'Division with 0 is not possible')
            return render (request, "prefselect.html", dicti )
        else:
            request.session['dicti'][param] /= refvalue
    request.session.modified = True

    dicti = request.session['dicti']
    dicti['show_values'] = 1
    return render(request, 'details.html', dicti) 

def expression (request):
    param1 = request.POST['param1']
    param2 = request.POST['param2']
    y2coeff = int(request.POST['y2coeff'])
    ycoeff = int(request.POST['ycoeff'])
    constant = int(request.POST['constant'])

    ind_variable = list(range(0,100))
    res = []
    for i in ind_variable:
        t = y2coeff * i * i + ycoeff * i + constant
        #t = ycoeff * i + constant
        res.append(t)

    dicti = request.session['dicti']
    dicti['show_graph'] = 1
    dicti['show_values'] = False
    dicti['xaxis'] = ind_variable
    dicti['xaxis_name'] = param1
    dicti['yaxis_name'] = param2
    dicti['yaxis'] = res
    return render(request, 'details.html', dicti) 
        





    