from django.shortcuts import render, redirect
from .models import Group, Message
from django.contrib import messages
from .forms import imageForm
def create_group(request):
    if request.method == 'POST':
        group_name = request.POST['group_name']
        description = request.POST['description']

        if Group.objects.filter(group_name=group_name).exists():
            messages.error(request, "Group name already exists!")
        else:
            Group.objects.create(group_name=group_name, description=description)
            messages.success(request, "Group created successfully.")
            return redirect('chat_list')
    return render(request, "create_chat.html")

def groups(request):
    groups = Group.objects.all()
    return render(request, "chat_list.html", {'groups': groups})

def group_chat(request, id):
    group = Group.objects.get(id=id)
    messages_list = Message.objects.filter(group=group)
    
    if request.method == 'POST':
        sender = request.POST.get('sender', 'Anonymous')
        content = request.POST.get('content')
        if content:
            Message.objects.create(group=group, sender=sender, content=content)
            return redirect('group_chat', id=id)
    
    return render(request, 'chat.html', {
        'group_chats': group,
        'messages': messages_list
    })



def imagePost(request):
    forms = imageForm(request.POST, request.FILES)
    if request.method== "POST":
        if forms.is_valid:
            forms.save()
            messages.success(request, 'upload successfully')
            return redirect('chat_list')
        else:
            messages.error(request, 'upload failed')
            return redirect('upload')
    return render(request, 'uploadPost.html', {'form':forms})
