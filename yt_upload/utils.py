import os
import re
import datetime as dt

from typing import Tuple, Union

from .exceptions import YTVideoError


def to_abs_path(path: str) -> str:
    if not os.path.isabs(path):
        path = os.path.join(os.getcwd(), path)

    if not os.path.exists(path):
        raise IOError(f"File does not exists: {path}")
    
    return path

def datetime_to_yt_date(date: Union[dt.datetime, dt.date])\
        -> Tuple[str, str]:
    if isinstance(date, dt.datetime):
        time = date.time().strftime(r"%H:%M")
        date = date.date().strftime(r"%b %d, %Y")
        return date, time
    else:
        date = date.strftime(r"%b %d, %Y")
        return date

def get_all_files(path: str):
    queue = list(map(lambda item: os.path.join(path, item), os.listdir(path)))
    files = []

    while queue:
        path = queue.pop()

        if os.path.isdir(path):
            queue.extend(list(
                map(
                    lambda item: os.path.join(path, item),
                    os.listdir(path)
                )
            ))
        else:
            files.append(path)

    return files

def remove_indexddb_cache_files(profile_path: str):    
    db = os.path.join(profile_path, "IndexedDB")
    studio_blob = re.compile(r".*studio.youtube.com.*.blob")
    target_dir = list(filter(lambda item: studio_blob.search(item), os.listdir(db)))

    if len(target_dir) == 0:
        return None

    if len(target_dir) != 1:
        folders = "\n".join([f"{i}. {p}" for i, p in enumerate(target_dir)])
        raise YTVideoError(f"{len(target_dir)} studio.youtube folders was found:"
                           f"\n{folders}\nleave one folder studio.youtube")
    
    files = get_all_files(os.path.join(db, target_dir[0]))
    
    for file in files:
        os.remove(file)
