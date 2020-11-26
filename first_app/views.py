import csv, io
from django.conf import settings 
from django.contrib import messages
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from first_app.forms import ProgramForm,UserForm
from first_app.models import Entity,Program,UserProfileInfo
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from My_portal.settings import SENDGRID_API_KEY
# Create your views here.

def index(request):
    return render(request,'first_app/index.html')

def base(request):
    return render(request,'first_app/base.html')

@login_required
def front(request):
    return render(request,'first_app/front.html')


@login_required
def entitys(request):
    entity_list = Entity.objects.order_by('entity_name')  
    return render(request,'first_app/entity_list.html',{'entity':entity_list})

@login_required
def prog(request,pk):
    if request.method == "GET":    
        prog_list = Program.objects.filter(entity=pk) 
        entity_list = Entity.objects.get(id=pk)  
        return render(request,'first_app/program_list.html',{'progrm':prog_list,'entity':entity_list})

@login_required
def users(request,pk):  
    if request.method == "GET":    
        user_list = UserProfileInfo.objects.filter(entity=pk) 
        entity_list = Entity.objects.get(id=pk)  
        return render(request,'first_app/userlist.html',{'users':user_list,'entity':entity_list})
"""
    if request.method == "GET":  
            user_list = UserProfileInfo.objects.filter(progrm=pk)
            prog_list=Program.objects.get(id=pk)  """


class EntityDetailView(LoginRequiredMixin,DetailView):
    model = Entity
    template_name = "first_app/entity_details.html"

class ProgramDetailView(LoginRequiredMixin,DetailView):
    model = Program
    template_name = "first_app/program_details.html"

class EntityCreateView(LoginRequiredMixin,CreateView):
    model = Entity
    template_name = "first_app/add_org.html"
    fields = '__all__'
    
"""  
class ProgramCreateView(CreateView):
    model = Program
    template_name = "first_app/add_prog.html"
    fields = ['programe_name','no_of_people','place','description']
    
"""
@login_required
def add_Program(request, pk):
    entity = get_object_or_404(Entity, pk=pk)
    if request.method == "POST":
        form = ProgramForm(request.POST)
        if form.is_valid():
            Program = form.save(commit=False)
            Program.entity = entity 
            Program.save()
            return redirect('prog', pk=entity.pk)
    else:
        form = ProgramForm()
    
    entity_list = Entity.objects.order_by('entity_name')  
    return render(request, 'first_app/add_prog.html', {'form': form})

@login_required
def add_User(request,pk):
    entity = get_object_or_404(Entity, pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST)
        
        if form.is_valid():
            UserProfileInfo = form.save(commit=False)
            UserProfileInfo.entity = entity
            UserProfileInfo.save()
            
            import pdb 
            pdb.set_trace()
            
            subject = 'Your Fafnir account is set!'

            message = "Hi, Testing"

            message = Mail(
                 from_email='vishnu.m@pacewisdom.com',
                 to_emails=["vishnu.m@pacewisdom.com"],
                 subject=subject,
                 html_content=message)
            
            sg = SendGridAPIClient(SENDGRID_API_KEY)
            response = sg.send(message)
            """  
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = f'Message from {form.cleaned_data["name"]}'
            message = "Welcome to My Portal"    
            sender =  "vishnu.m@pacewisdom.com"
            recipients = ['vishnu.m@pacewisdom.com',  "padmakshi.n@pacewisdom.com"]
           
            try:
                jj = send_mail(subject, message, sender, recipients, fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            """
            return redirect('users', pk=entity.pk)
    else:
        form = UserForm()
    
    entity_list = Entity.objects.order_by('entity_name')  
    return render(request, 'first_app/add_user.html', {'form': form})
    

    
class EntityUpdateView(LoginRequiredMixin,UpdateView):
    model = Entity
    template_name = "first_app/updatentity.html"
    fields = '__all__'
    
class ProgramUpdateView(LoginRequiredMixin,UpdateView):
    model = Program
    template_name = "first_app/updateprog.html"
    fields = ['programe_name','no_of_people','place','description']
    
    def get_queryset(self):
        return Program.objects.filter()
    
    
    
class EntityDeleteView(LoginRequiredMixin,DeleteView):
    model = Entity
    template_name = "first_app/deletentity.html"
    success_url = reverse_lazy(entitys)
"""  
class ProgramDeleteView(DeleteView):
    model = Program
    template_name = "first_app/deleteprogram.html"
    success_url = reverse_lazy(prog)
    """
    
@login_required   
def Program_remove(request, pk):
    program = get_object_or_404(Program, pk=pk)
    entity_pk = program.entity.pk
    program.delete()
    return redirect('prog', pk=entity_pk)

@login_required
def User_remove(request, pk):
    userss = get_object_or_404(UserProfileInfo, pk=pk)
    entity_pk = userss.entity.pk
    userss.delete()
    return redirect('users', pk=entity_pk)


@login_required
def Upload(request,pk):
    entitys = get_object_or_404(Entity, pk=pk)
    template = "first_app/userupload.html"
    
    prompt = {
        'order': 'Order of the CSV should be Name, email and password'
    }
    if request.method == "GET":
        return render(request,template,prompt)

    csv_file = request.FILES['file']
    
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Please upload a .csv file.')
        return redirect('upload', pk=entitys.pk)
    
    else:
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string,delimiter=',',quotechar="|"):
            _, created = UserProfileInfo.objects.update_or_create(
                entity = entitys,
                name = column[0],
                email = column[1]        
        )
        context = {}

        return redirect('users', pk=entitys.pk)