from functools import lru_cache
import csv


@lru_cache
def read(path):
    jobs = []

    with open(path) as file:
        jobs_file = csv.DictReader(file)

        for index in jobs_file:
            jobs.append(index)

    return jobs
