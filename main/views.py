from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Internship, Company, Person


# Create your views here.
def index(request):
    return render(request, 'base.html')


def list_internships(request):
    internships = Internship.objects.all()
    return render(request, 'display_internships.html', {'internships': internships})


def add_internship(request):
    if request.method == 'POST':
        company_name = request.POST['company_name']
        position = request.POST['position']
        city = request.POST['city']
        description = request.POST['description']
        categories = request.POST['categories']
        company = Company.objects.get(name=company_name)
        ins = Internship(company=company, position=position, city=city,
                         description=description, categories=categories)
        ins.save()
        return HttpResponseRedirect('success/')
    companies = Company.objects.all()
    return render(request, 'form.html', {'companies': companies})


def added_success(request):
    internship = Internship.objects.latest('id')
    return render(request, 'success.html', {'internship': internship})


def register_company(request):
    if request.method == 'POST':
        name = request.POST['name']
        headquarters = request.POST['headquarters']
        description = request.POST['description']
        com = Company(name=name, headquarters=headquarters, description=description)
        com.save()
        return HttpResponseRedirect('registration-successful/')
    return render(request, 'register-company-form.html')


def register_successful(request):
    companies = Company.objects.all()
    return render(request, 'register-successful.html', {'companies': companies})


def apply(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        university = request.POST['university']
        company = request.POST['company_name']
        position = request.POST['position']

        com = Company.objects.get(name=company)
        ins = com.internship_set.get(position=position)
        person = Person(first_name=first_name, last_name=last_name, university=university, internship=ins)
        person.save()
        return HttpResponseRedirect('application-successful/')

    companies = Company.objects.all()
    return render(request, 'apply-form.html', {'companies': companies})


def application_successful(request):
    student = Person.objects.latest('id')
    internships = []
    people = Person.objects.all()
    for person in people:
        if person.first_name == student.first_name and person.last_name == student.last_name:
            internships.append(person.internship)
    context = {'student': student, 'internships': internships}
    return render(request, 'application-successful.html', context=context)


def delete_company(request):
    if request.method == 'POST':
        name = request.POST['company_name']
        company_to_delete = Company.objects.get(name=name)
        company_to_delete.delete()
        return HttpResponseRedirect('delete-successful/')

    companies = Company.objects.all()
    return render(request, 'delete-company.html', {'companies': companies})


def delete_successful(request):
    companies = Company.objects.all()
    return render(request, 'delete-successful.html', {'companies': companies})


def show_internships(request):
    if request.method == 'POST':
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']

        internships = []
        for p in Person.objects.all():
            if p.first_name == first_name and p.last_name == last_name:
                internships.append(p.internship)

        return render(request, 'show-internships.html', {'internships': internships, 'var': 1})

    return render(request, 'show-internships.html', {"var": 0})


def update_internship(request):
    if request.method == 'POST':
        company_name = request.POST['company_name']
        position = request.POST['position']
        new_description = request.POST['new_description']

        try:
            internship = Internship.objects.get(company__name=company_name, position=position)
            if internship:
                internship.description = new_description
                internship.save()
        except ObjectDoesNotExist:
            internship = None

        companies = Company.objects.all()
        return render(request, 'update-internship.html', {'companies': companies, 'internship': internship, 'var': 1})

    companies = Company.objects.all()
    return render(request, 'update-internship.html', {'companies': companies, 'var': 0})


def delete_internship(request):
    companies = Company.objects.all()
    if request.method == 'POST':
        company_name = request.POST['company_name']
        position = request.POST['position']

        try:
            internship = Internship.objects.get(company__name=company_name, position=position)
            if internship:
                internship.delete()
            deleted = 1
        except ObjectDoesNotExist:
            deleted = 0

        all_internships = Internship.objects.all()
        context = {'companies': companies, 'var': 1, 'deleted': deleted, 'internships': all_internships}
        return render(request, 'delete-internship.html', context=context)

    return render(request, 'delete-internship.html', {'companies': companies, 'var': 0})
