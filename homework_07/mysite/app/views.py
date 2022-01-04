from django.shortcuts import render
import json

from .conf import ALLURE
from .handlers import AllureProjectCoverage
from .api_coverage.models import CommonSwaggerCoverage
from .tools import get_allure_project_info, get_allure_token, get_coverage_count


def home(request, slug=''):
    projects = get_allure_project_info(get_allure_token())

    data = {}
    for project in projects:
        project = AllureProjectCoverage.parse_raw(json.dumps(project))
        product_url = f'{ALLURE}/project/{project.id}/dashboards'
        data[f'{project.name}'] = [product_url]

    context = {"data": data, }

    return render(request, 'base.html', context=context)


def allure(request, slug=''):
    projects = get_allure_project_info(get_allure_token())

    data = {}
    for project in projects:
        project = AllureProjectCoverage.parse_raw(json.dumps(project))
        allure_automated_test_count = project.automatedTestCasesCount
        allure_manual_test_count = project.manualTestCasesCount
        allure_coverage_count = get_coverage_count(allure_automated_test_count, allure_manual_test_count)
        data[f'{project.name}'] = [allure_automated_test_count, allure_manual_test_count, allure_coverage_count]

    context = {"data": data, }

    return render(request, 'allure.html', context=context)


def api(request, slug=''):
    projects = get_allure_project_info(get_allure_token())

    data = {}
    for project in projects:
        project = AllureProjectCoverage.parse_raw(json.dumps(project))
        api_coverage_project = CommonSwaggerCoverage.objects.filter(project=project.name).order_by('-created_at')
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
