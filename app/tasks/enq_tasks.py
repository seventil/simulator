import time

import numpy as np
from celery import shared_task

from .models import CalcResult, Params


@shared_task
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    if int(task_type) == 0:
        sim_calculations()
    return True


def sim_calculations():
    all_params = list(Params.objects.all().values())
    param = "_".join(list(map(str, all_params[0].values())))

    ms = [a for a in range(10000)]
    length = len(ms)
    t = np.eye(length)
    for i in range(length):
        t[i, i] = ms[i]

    beta = -6.24e-12
    gamma = 1.97e-19

    r = ((-3 * beta) / (4 * gamma)) / 1e6
    d = t - (1 / length) * (np.trace(t)) * np.eye(length)
    b = np.array([[0 for _ in range(length)]])
    b[0, 0] = 1
    b = b.T
    tmA = np.sqrt(b.T @ (((r * np.eye(length)) - (3 / 2) * d) ** 2) @ b)

    if b.T @ d @ b <= (2 * r) / 3:
        teq = r - tmA
    else:
        teq = r + tmA

    time.sleep(1)
    teq = 42

    CalcResult.objects.create(param=param, answer=teq)
    return None
