from functools import lru_cache
import csv


@lru_cache
def read():
    jobs = []

    with open("src/jobs.csv") as file:
        csv.DictReader(file)

        for index in file:
            jobs.append(index)

    return jobs
