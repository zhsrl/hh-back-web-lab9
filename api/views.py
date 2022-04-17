from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse

from django.core.serializers import serialize

from .serializers import VacancySerializer
from .models import Company, Vacancy


class CompanyView(View):

    def get(self, request):
        all_companies = Company.objects.all()
        companies_count = Company.objects.count()

        companies_serialized = VacancySerializer

        companies = {
            'companies': companies_serialized,
            'count': companies_count
        }

        return JsonResponse(companies)

    def get_single(request, id):
        single_company = Company.objects.get(id=id)

        return JsonResponse(single_company.to_json())


class VacancyView(View):

    def get(self, request):
        all_vacancy = Vacancy.objects.all()
        vacany_count = Vacancy.objects.count()

        vacancies_serialized = serialize('python', all_vacancy)

        vacancies = {
            'vacancies': vacancies_serialized,
            'count': vacany_count
        }

        return JsonResponse(vacancies)

    def get_single(request, id):
        single_vacancy = Vacancy.objects.get(id=id)

        return JsonResponse(single_vacancy.to_json())
