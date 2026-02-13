from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm


def about_me(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()
    
    # Create an instance of the form
    collaborate_form = CollaborateForm()
    
    # Handle form submission
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Collaboration request received! I will respond soon."
            )

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form,
        },
    )
