from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from .models import Project, ContactMessage
from .forms import ContactForm # Form ကို အောက်မှာ ဆက်ရေးပေးပါ့မယ်

# Index Page View (Search + Category Filter ပါဝင်သည်)
def index(request):
    query = request.GET.get('q')
    category_filter = request.GET.get('category')
    
    projects = Project.objects.all()

    # Search Logic
    if query:
        projects = projects.filter(
            Q(title__icontains=query) | 
            Q(technology__icontains=query) |
            Q(description__icontains=query)
        )

    # Category Filter Logic
    if category_filter:
        projects = projects.filter(category=category_filter)

    categories = Project.CATEGORY_CHOICES # Button များအတွက် category စာရင်းယူခြင်း

    context = {
        'projects': projects,
        'categories': categories,
        'query': query,
        'selected_category': category_filter,
    }
    return render(request, 'app/index.html', context)

# Project Detail View
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'app/project.html', {'project': project})

# Contact Page View
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() # Database ထဲ သိမ်းလိုက်ခြင်း
            messages.success(request, 'သင့် Message ပေးပို့မှု အောင်မြင်ပါသည်။ ကျေးဇူးတင်ပါတယ်။')
            return redirect('index')
    else:
        form = ContactForm()
    
    return render(request, 'app/contact.html', {'form': form})

def cv_detail(request):
    return render(request, 'app/cv_detail.html')

def about(request):
    return render(request, 'app/about.html')