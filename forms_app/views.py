from django.shortcuts import render, get_object_or_404, redirect
from .models import NPModel
from .forms import NPForm

def index(request):
    form_list = NPModel.objects.all()
    context = {'form_list': form_list}
    return render(request, 'forms_app/index.html', context)

def detail(request, pk):
    theModel = get_object_or_404(NPModel, pk=pk)
    return render(request, 'forms_app/detail.html', {'theModel':theModel})


def create(request):
    if request.method == "POST":
        form = NPForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = NPForm()
    return render(request, 'forms_app/create.html', {'form': form})

def edit(request, pk):
    theModel = get_object_or_404(NPModel, pk=pk)
    if request.method == 'POST':
        form = NPForm(request.POST, instance=theModel)
        if form.is_valid():
            form.save(commit=False)
        return redirect('index')

    else:
        form = NPForm(instance=theModel)

    return render(request,'forms_app/edit.html', {'form':form})

def about(request):
    form_list = NPModel.objects.all()
    context = {'form_list': form_list}
    return render(request, 'forms_app/about.html',context)