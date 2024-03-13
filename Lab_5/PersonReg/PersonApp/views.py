from django.shortcuts import render, redirect

people = []

class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return self.username

def add_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        new_person = Person(username=username, password=password)
        people.append(new_person)

        return redirect('list_view')

    return render(request, 'PersonApp/add.html')

def list_view(request):
    return render(request, 'PersonApp/list.html', {'people': people})

