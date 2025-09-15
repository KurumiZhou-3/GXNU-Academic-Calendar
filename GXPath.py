# -*- coding: utf-8 -*
import os, sys, platform


def get_local_path() -> str:
    """
    Get the app local file path
    :return:
    """
    return os.path.dirname(os.path.realpath(sys.argv[0]))


def end_with_slash(path: str) -> str:
    """
    If given path is ending with slash, return directly without any operation,
    if not, return path ended with slash
    :param path:
    :return:
    """
    if platform.system() == "Windows":
        return path + "\\" if path[-1] != "\\" else path
    else:
        return path + "/" if path[-1] != "/" else path


if __name__ == '__main__':
    print(end_with_slash(get_local_path()))
