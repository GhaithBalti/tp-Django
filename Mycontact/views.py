from django.shortcuts import render

from django.http import HttpResponse

from Mycontact.forms import contactform2
from .models import Contact
# Create your views here.
def controleform1 (request):
    if request.method=='POST':
        f=request.POST['firstname']# firstname c'est name dans page html
        l=request.POST['lastname']
        e=request.POST['email']
        m=request.POST['message']
        contact=Contact.objects.create(firstname=f,lastname=l,Email=e,message=m)
#contact=Contact(firstname=f,lastname=l,Email=e,msg=m)
#contact.save()
        return HttpResponse(' <h2> Data has been submitted </h2>')
    return render(request,"Mycontact/myform1.html")


    
def controleform2 (request):
    if request.method == 'POST': # S'il s'agit d'une requête POST
        form = contactform2(request.POST) # Nous reprenons les données
        if form.is_valid(): # Nous vérifions que les données envoyées sont valides
# Ici nous pouvons traiter les données du formulaire
            f = form.cleaned_data['firstname']
            l = form.cleaned_data['lastname']
            e = form.cleaned_data['Email']
            m = form.cleaned_data['msg']
# Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer
            contact=Contact.objects.create(firstname=f,lastname=l,Email=e,message=m)
        return HttpResponse(' <h2> Data has been submitted </h2>')
    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = contactform2() # Nous créons un formulaire vide
    return render(request,"Mycontact/myform2.html",{'mycontactform2':form})


def controleform3 (request):
    if request.method == 'POST': # S'il s'agit d'une requête POST
        form = contactform3(request.POST) # Nous reprenons les données
        if form.is_valid(): # Nous vérifions que les données envoyées sont valides
            form.save()
            return HttpResponse(' <h2> Data has been submitted </h2>')
    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = contactform3() # Nous créons un formulaire vide
    return render(request,"myform3.html",{'mycontactform3':form})

    
