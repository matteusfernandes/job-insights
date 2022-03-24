from functools import lru_cache
import csv


@lru_cache
def read(path):
    jobs = []

    with open(path) as file:
        csv.DictReader(file)

        for index in file:
            jobs.append(index)

    return jobs
