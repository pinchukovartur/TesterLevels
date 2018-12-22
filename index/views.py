"""
The script handles URL requests

created by: Pinchukov Artur
date: 13.10.17
"""

# frameworks
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.utils import timezone
# project libs
from .models import TestSecretKey, LevelFile
# standard libs
import datetime
import json
import os
import time


def index(request):
    """
    The method redirected index url on admin panel
    :return: admin url
    """
    time.sleep(5)
    return HttpResponseRedirect('/admin')


def get_files_name(request, secret_key):
    """
    The method return list file names by secret key
    :param request: framework object
    :param secret_key: tester secret key
    :return: json text with file names
    """
    data = {}

    #test_secret_key = get_object_or_404(TestSecretKey, pk=secret_key)
    test_secret_keys = TestSecretKey.objects.filter(pk=secret_key)

    if len(test_secret_keys) == 0:
        data["error"] = "Secret key not found!"
        return HttpResponse(json.dumps(data))

    test_secret_key = test_secret_keys[0]

    # read data in files
    if __check_secret_key_status__(test_secret_key):
        data["files"] = [level.level_name for level in test_secret_key.levels.all()]
    else:
        data["error"] = "The private key has expired!"

    return HttpResponse(json.dumps(data))


def get_file_name(request, secret_key, level_name):
    """
    The method return list file names by secret key
    :param level_name: name level file
    :param request: framework object
    :param secret_key: tester secret key
    :return: json text with file data
    """
    file = get_object_or_404(LevelFile, pk=level_name)
    test_secret_key = get_object_or_404(TestSecretKey, pk=secret_key)


    # read data in files
    if __check_secret_key_status__(test_secret_key):
        file_path = os.path.dirname(__file__) + "/download_files/" + file.level_file.name
        file = open(file_path, "rb")
        bytes = file.read()
        file.close()
        return HttpResponse(bytes, "application/octet-steam")
    else:
        return HttpResponse("Error check key")


def __check_secret_key_status__(test_secret_key):
    """
    The method check key access date
    :param secret_key: tester secret key
    :return: True if key active else False
    """
    if test_secret_key.status == "No active":
        test_secret_key.status = "Active"
        test_secret_key.key_active_date = timezone.now()
        test_secret_key.save()
        return True
    elif test_secret_key.status == "Active":
        if timezone.now() < (test_secret_key.key_active_date + datetime.timedelta(days=test_secret_key.lifetime)):
            return True
        else:
            test_secret_key.status = "Expired"
            test_secret_key.save()
            return False
    else:
        return False



"""
def __check_date__(finish_date):
    return int(time.time()) < finish_date


def __convert_to_unix_time__(date):

    return time.mktime(date.timetuple())


def __convert_to_datetime__(unix):
    return datetime.datetime.fromtimestamp(int(unix)).strftime('%Y-%m-%d %H:%M:%S')


def __add_day_unix_time__(unix_time, day):
    return unix_time + day * 60 * 60 * 24
"""