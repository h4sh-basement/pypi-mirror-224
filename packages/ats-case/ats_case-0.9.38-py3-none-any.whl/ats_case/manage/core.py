import psutil

from multiprocessing import Process

from ats_base.service import mm
from ats_base.log.logger import logger
from ats_case.manage.start import run


def start(data):
    """
    启动测试进程
    :param data:
    :return:
    """
    # 判断测试终端是否可以连接
    p = Process(target=run, kwargs=data)
    p.start()

    logger.info('TEST PROCESS[{}] START - DATA: {}...'.format(p.pid, data))
    return p.pid


def suspend(data):
    """
    暂停测试进程
    :param data:
    :return:
    """
    pid = data.get('pid')
    logger.info('TEST PROCESS[{}] SUSPEND...'.format(pid))

    p = psutil.Process(pid)
    p.suspend()


def resume(data):
    """
    恢复暂停测试进程
    :param data:
    :return:
    """
    pid = data.get('pid')
    logger.info('TEST PROCESS[{}] RESUME...'.format(pid))

    p = psutil.Process(pid)
    p.resume()


def cancel(data):
    """
    结束测试进程
    :param data:
    :return:
    """
    pid = data.get('pid')
    logger.info('TEST PROCESS[{}] CANCEL...'.format(pid))

    p = psutil.Process(pid)
    p.kill()


def callback(host: str, csn: str, data):
    """
    回调
    :param host:
    :param csn:
    :param data:
    :return:
    """
    mm.Dict.put(host, csn, data.get('data'))
    logger.info('CALLBACK HOST[{}] CSN[{}] - DATA: {}...'.format(host, csn, data))

