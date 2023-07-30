from django.shortcuts import render,HttpResponse

# Create your views here.
#from Diseasepredictor.models import disease
def home(request):
    #return HttpResponse("this is the home sandeep")
    #context={'name':"sandeep",'course':"django"}
    return render(request,"home.html")
def reportanalysis(request):
    return render(request,"data.html")
def contact(request):
    if (request.method=="POST"):
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        desc = request.POST['desc']
        print(name,email,number,desc)
        lns = contact(name=name, email=email, phone=number, desc=desc)
        lns.save()
        print("the  data has been written to the db ")
    return render(request,"contact.html")