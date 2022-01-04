from django.shortcuts import render
from .models import Project, APITest, E2ETest, UnitTest


def index(request):
    return render(request, 'e2e.html')


def e2e(request, slug=''):
    projects = Project.objects.order_by('-name')

    data = {}
    for project in projects:
        project = AllureProjectCoverage.parse_raw(json.dumps(project))
        e2e_tests = E2ETest.objects.filter(project=project.name).order_by('-created_at')
        automated_test_count = e2e_tests.automated
        manual_test_count = e2e_tests.manual
        coverage_count = get_coverage_count(automated_test_count, manual_test_count)
        data[f'{project.name}'] = [automated_test_count, manual_test_count, coverage_count]

    context = {"data": data, }

    return render(request, 'e2e.html', context=context)


def api(request, slug=''):
    projects = Project.objects.order_by('-name')

    data = {}
    for project in projects:
        api_coverage_project = APITest.objects.filter(project=project.name).order_by('-created_at')
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

    data = []
    context = {"data": data, }

    return render(request, 'unit.html', context=context)
