# encoding=utf-8
import os
import time


def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)


def get_FileSize(filePath):
    # filePath = str(filePath, 'utf8')
    fsize = os.path.getsize(filePath)
    return round(fsize, 2)


def get_FileAccessTime(filePath):
    # filePath = str(filePath, 'utf8')
    t = os.path.getatime(filePath)
    return TimeStampToTime(t)


def get_FileCreateTime(filePath):
    # filePath = str(filePath, 'utf8')
    t = os.path.getctime(filePath)
    return TimeStampToTime(t)


def get_FileModifyTime(filePath):
    # filePath = str(filePath, 'utf8')
    t = os.path.getmtime(filePath)
    return TimeStampToTime(t)


jsons = []


def scan_dir(dir):
    import re
    if os.path.isdir(dir) and re.match('\..*',dir):
        return
    try:
        for file in os.listdir(dir):
            file_path = os.path.join(dir, file)

            size = get_FileSize(file_path)
            create_time = get_FileCreateTime(file_path)
            acces_time = get_FileAccessTime(file_path)
            modify_time = get_FileModifyTime(file_path)

            file_info = {
                'path': file_path,
                'name': file,
                'create_time': create_time,
                'acces_time': acces_time,
                'modify_time': modify_time
            }

            jsons.append(file_info)


            print (file_path)

            """
            print (file)
            print (size)
            print (create_time)
            print (acces_time)
            print (modify_time)
            """

            if os.path.isdir(file_path):
                scan_dir(file_path)
    except Exception as e:
        print (e)


scan_dir('/home')

import pickle

pickle.dump(jsons, open('all_files.pickle', 'wb'))
