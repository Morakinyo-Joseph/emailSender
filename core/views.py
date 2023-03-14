from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def index(request):
    message = ""
    if request.method == "POST":
        receiver = request.POST.get("receiver")

        if receiver != None:
                
            print(receiver)

            from_email = "jmoraks03@gmail.com"
            recipient_list = [receiver]
            subject = "Just sending message"
            message = "If you are seeing this then this possibly worked"

            send_mail(subject, message, from_email, recipient_list, fail_silently=True)


            if send_mail:
                message = "SENT"
            else:
                message = "FAIL"

    return render(request, 'index.html', {"info": message})