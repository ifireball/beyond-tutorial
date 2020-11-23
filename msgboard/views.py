from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm


def board(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('board')
    else:
        form = MessageForm()
    messages = Message.main_feed()
    return render(request, 'msgboard/board.html', {
        'messages': messages,
        'form': form,
    })
