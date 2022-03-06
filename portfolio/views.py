from django.shortcuts import render, get_object_or_404
from .models import home, about, service, project, contact, experience
# Create your views here.


def portfolio(request):
    Home = home.objects.all()
    About = about.objects.all()
    Experience = experience.objects.all()
    Service = service.objects.all()
    Project = project.objects.all()
    Contact = contact.objects.all()
    return render(request, 'lib/portfolio.html', {'home': Home, 'about': About,
                                                    'experience':Experience,
                                                  'service': Service,
                                                  'project': Project,
                                                  'contact': Contact})


def Project(request, project_id):
    Project = get_object_or_404(project, pk=project_id)
    return render(request, 'lib/project.html', {'Project': Project})
