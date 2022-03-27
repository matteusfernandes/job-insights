from src.jobs import read


def get_unique_job_types(path):
    types_of_jobs = []

    data_of_jobs = read(path)
    for obj in data_of_jobs:
        if obj["job_type"] not in types_of_jobs:
            types_of_jobs.append(obj["job_type"])

    return types_of_jobs


def filter_by_job_type(jobs, job_type):
    filtered_job_type = []

    for obj in jobs:
        if obj["job_type"] == job_type:
            filtered_job_type.append(obj)

    return filtered_job_type


def get_unique_industries(path):
    industries = []

    data_of_jobs = read(path)
    for obj in data_of_jobs:
        if obj["industry"] not in industries and obj["industry"] != '':
            industries.append(obj["industry"])

    return industries


def filter_by_industry(jobs, industry):
    filtered_industry = []

    for obj in jobs:
        if obj["industry"] == industry:
            filtered_industry.append(obj)

    return filtered_industry


def get_max_salary(path):
    max_salary = 0

    data_jobs = read(path)
    for obj in data_jobs:
        if (obj["max_salary"] != "invalid" and obj["max_salary"] != ''
                and float(obj["max_salary"]) > max_salary):
            max_salary = float(obj["max_salary"])

    return max_salary


def get_min_salary(path):
    data_of_jobs = read(path)

    min_salary = float(data_of_jobs[3]["min_salary"])

    for obj in data_of_jobs:
        if (obj["min_salary"] != "invalid" and obj["min_salary"] != ''
                and float(obj["min_salary"]) < min_salary):
            min_salary = float(obj["min_salary"])

    return min_salary


def matches_salary_range(job, salary):
    if "max_salary" not in job or "min_salary" not in job:
        raise ValueError()

    if (type(job["max_salary"]) is not int
            or type(job["min_salary"]) is not int):
        raise ValueError()

    if job["min_salary"] > job["max_salary"]:
        raise ValueError()

    if job["min_salary"] <= salary and salary <= job["max_salary"]:
        return True

    return False


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
