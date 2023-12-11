import html
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
from django.views import View


# Create your views here.

def dumpdata(place, data):
    return_val = ""
    if len(data) > 0:
        return_val += '<p>Incoming ' + place + ' data:<br/>\n'
        for key, value in data.items():
            return_val += html.escape(key) + '=' + html.escape(value) + '</br>\n'
        return_val += '</p>\n'
    return return_val


# call as
# dumpdata('GET', request.GET)


def checkguess(value):
    msg = False
    if value:
        try:
            if int(value) < 0:
                msg = 'Negative Value'
            elif int(value) > 500:
                msg = 'Positive : High Value'
            elif int(value) == 42:
                msg = 'Congratulations!'
            else:
                msg = 'Positive : Low Value'
        except:
            msg = 'Bad format for guess: ' + html.escape(value)
    return msg


def index(request):
    return render(request, 'getpost/index.html')


def getForm(request):
    response = """<p>Impossible GET guessing game...</p>
        <form>
        <p><label for='guess'>Input Guess</label>
        <input type='text' name='guess' size='40' id='guess'/></p>
        <input type='submit'/>
        </form>"""

    response += dumpdata('GET', request.GET)
    return HttpResponse(response)


@csrf_exempt
def postForm(request):
    response = """<p>Impossible GET guessing game...</p>
        <form method='POST'>
        <p><label for='guess'>Input Guess</label>
        <input type='text' name='guess' size='40' id='guess'/></p>
        <input type='submit'/>
        </form>"""

    response += dumpdata('POST', request.POST)
    return HttpResponse(response)


@csrf_exempt
def submitForm(request):
    response = dumpdata('POST', request.POST)
    return render(request, 'getpost/submitForm.html', {'data': response})


@csrf_exempt
def studentForm(request):
    response = dumpdata('POST', request.POST)
    return render(request, 'getpost/studentdetails.html', {'data': response})


def csrfForm(request):
    response = """<p>CSRF guessing game...</p>
        <form method="POST">
        <p><label for="guess">Input Guess</label>
        <input type="text" name="guess" size="40" id="guess"/></p>
        <input type="hidden" name="csrfmiddlewaretoken" value="__token__"/>
        <input type="submit"/>
        </form>"""

    token = get_token(request)
    response = response.replace('__token__', html.escape(token))
    response += dumpdata('POST', request.POST)
    return HttpResponse(response)


class ClassyView(View):
    def get(self, request):
        return render(request, 'getpost/guess.html')

    def post(self, request):
        guess = request.POST.get('guess')
        msg = checkguess(guess)
        return render(request, 'getpost/guess.html', {'message': msg})
