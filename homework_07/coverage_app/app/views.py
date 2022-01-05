from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Project, APICoverage, E2ECoverage, UnitCoverage


def index(request):
    return render(request, 'e2e.html')


class E2EListView(ListView):
    model = E2ECoverage
    p_title = 'E2E coverage'


class E2EDetailView(DetailView):
    model = E2ECoverage
    p_title = 'E2E detail coverage'


class APIListView(ListView):
    model = APICoverage
    p_title = 'API coverage'


class UNITListView(ListView):
    model = UnitCoverage
    p_title = 'UNIT coverage'


class ProjectListView(ListView):
    model = Project
    p_title = 'Projects'


class ProjectDetailView(DetailView):
    model = Project
    p_title = 'Project detail'


def e2e(request, slug=''):
    projects = Project.objects.order_by('-name')

    data = {}
    for project in projects:
        e2e_tests = E2ECoverage.objects.filter(project=project.id).order_by('-created_at')
        automated_test_count = e2e_tests[0].automated if len(e2e_tests) else 0
        manual_test_count = e2e_tests[0].manual if len(e2e_tests) else 0
        coverage_count = e2e_tests[0].get_coverage_count() if len(e2e_tests) else 0
        data[f'{project.name}'] = [automated_test_count, manual_test_count, coverage_count]

    context = {"data": data, }

    return render(request, 'e2e.html', context=context)


def api(request, slug=''):
    projects = Project.objects.order_by('-name')

    data = {}
    for project in projects:
        api_coverage_project = APICoverage.objects.filter(project=project.id).order_by('-created_at')
        exist_coverage_in_db = bool(len(api_coverage_project))

        full_api_coverage = api_coverage_project[0].full_coverage if exist_coverage_in_db else 0
        full_cnt = api_coverage_project[0].full_cnt if exist_coverage_in_db else 0
        actual_cnt = api_coverage_project[0].actual_cnt if exist_coverage_in_db else 0

        partial_api_coverage_count = api_coverage_project[0].partial_coverage if exist_coverage_in_db else 0
        partial_cnt = api_coverage_project[0].partial_cnt if exist_coverage_in_db else 0

        empty_api_coverage = api_coverage_project[0].empty_coverage if exist_coverage_in_db else 0
        empty_cnt = api_coverage_project[0].empty_cnt if exist_coverage_in_db else 0

        data[f'{project.name}'] = [full_api_coverage, full_cnt, actual_cnt,
                                   partial_api_coverage_count, partial_cnt,
                                   empty_api_coverage, empty_cnt]

    context = {"data": data, }

    return render(request, 'api.html', context=context)


def unit(request, slug=''):
    projects = Project.objects.order_by('-name')

    data = {}
    for project in projects:
        unit_coverage_project = UnitCoverage.objects.filter(project=project.id).order_by('-created_at')
        exist_coverage_in_db = bool(len(unit_coverage_project))
        code_coverage = unit_coverage_project[0].code_coverage if exist_coverage_in_db else 0
        data[f'{project.name}'] = [code_coverage, 100-code_coverage]
    context = {"data": data, }

    return render(request, 'unit.html', context=context)
