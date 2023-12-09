from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contacts(request):
    contact = {'list': ['My phone number: +7 992 221 07 99', 'My Telegram: @Anidab_cuba77', 'My email: at987217@gmail.com']}
    return render(request, 'contacts.html', contact)
