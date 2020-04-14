from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
### Codes for Home Page ###
def home(request):
    colors=('red', 'blue', 'yellow', 'green', 'black', 'pink', 'purple', 'violet')
    output = ''
    for i in range(1,7):
        color=random.choice(colors)
        output += '<div class="shadow-lg p-3 mb-5 bg-white rounded" style="color:{}"><H{}> This is a HTML Template with Passing Data</H{}></div>'.format(color,i,i)
    select_data = ''
    for i in range(6,21):
        select_data += '<option value={}>Password Length: {}</option>'.format(i,i)

    return render(request, 'generator/home.html',{'output':output, 'select_data':select_data, 'title': 'Main Page'})

### Codes for Generated Password ###
def password(request):
    created_password = ''
    length = request.GET.get('length')
    uppercase = request.GET.get('Uppercase')
    lowercase = request.GET.get('Lowercase')
    numbers = request.GET.get('Numbers')
    special_charecters = request.GET.get('Special_Charecters')
    password_pattern = ''
    if uppercase:
        for i in range(ord('A'), ord('Z')+1):
            password_pattern += chr(i)
    if lowercase:
        for i in range(ord('a'), ord('z')+1):
            password_pattern += chr(i)
    if numbers:
        for i in range(0, 10):
            password_pattern += str(i)
    if special_charecters:
        password_pattern += '~!@#$%^&*()_+'
    created_password = ''
    for i in range(int(length)):
        created_password += random.choice(password_pattern)
    return render(request, 'generator/password.html', {'password': created_password, 'title': 'Generated Password'})
