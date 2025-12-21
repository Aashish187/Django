from django.shortcuts import render,redirect
from .models import Room
from .forms import RoomForm
# from django.http import HttpResponse 
# now we can use render too

# Create your views here.
# info=[
#     {"id":1,"name":"Aashish"},
#     {"id":2,"name":"Mitul"},
#     {"id":3,"name":"Arsh"},
# ]
def home(request):
    # context={"info":info}
    info=Room.objects.all()
    context={"info":info}
    return render(request,"home.html",context)

def another(request,pk):
    # another= None
    # for i in info : 
    #     if i['id'] == int(pk):
    #         another= i
    another=Room.objects.get(id=pk)
    context={"another":another}
    # return HttpResponse("This is another page")
    return render(request,"another.html",context)

def create_room(request):
    form=RoomForm()
    if request.method == 'POST':
        # print(request.POST)
        form =RoomForm(request.POST)
        if form.is_valid() :
            form.save() # saves the form
            return redirect('home')
    context={'form':form}
    return render(request,'room_form.html',context)



def update_room(request,pk):
    room=Room.objects.get(id=pk)
    form=RoomForm(instance=room)
    context={"form":form}
    return render(request,'room_form.html',context)
