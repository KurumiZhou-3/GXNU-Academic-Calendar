import pprint
import datetime

STANDARD_OUTPUT_SYMBOL = "#"
WARNING_SYMBOL = "?"
ERROR_SYMBOL = "!"

NET_PART_NAME = "net"
DATASTORE_PART_NAME = "data"


# Base colorful print out
def green_print(output_text: str):
    print("\033[1;32m%s\033[0m" % output_text)


def yellow_print(output_text: str):
    print('\033[5;33m%s\033[0m' % output_text)


def red_print(output_text: str):
    print('\033[1;31m%s\033[0m' % output_text)


# Base std print out

def slog(output_text: str, front_symbol: str, front_text: str, mode: str = "withtime"):
    """
    Print out the text with a format style and the color of GREEN.\n
    ex( mode = "withtime" ): \n
    [#net 2020-04-13 17:09:49.015911] The text here you want to print out.

    ex( mode != "withtime" ): \n
    [#net] The text here you want to print out.

    :param output_text:
    :param front_symbol:
    :param front_text:
    :param mode:
    :return: None
    """
    if mode == "withtime":
        green_print(f"[{front_symbol}{front_text} {datetime.datetime.now()}] {output_text}")
    else:
        green_print(f"[{front_symbol}{front_text}] {output_text}")


def wlog(output_text: str, front_symbol: str, front_text: str, mode: str = "withtime"):
    """
    Print out the text with a format style and the color of YELLOW.\n
    ex( mode = "withtime" ): \n
    [#net 2020-04-13 17:09:49.015911] The text here you want to print out.

    ex( mode != "withtime" ): \n
    [#net] The text here you want to print out.

    :param output_text:
    :param front_symbol:
    :param front_text:
    :param mode:
    :return: None
    """
    if mode == "withtime":
        yellow_print(f"[{front_symbol}{front_text} {datetime.datetime.now()}] {output_text}")
    else:
        yellow_print(f"[{front_symbol}{front_text}] {output_text}")


def elog(output_text: str, front_symbol: str, front_text: str, mode: str = "withtime"):
    """
    Print out the text with a format style and the color of RED.\n
    ex( mode = "withtime" ): \n
    [#net 2020-04-13 17:09:49.015911] The text here you want to print out.

    ex( mode != "withtime" ): \n
    [#net] The text here you want to print out.

    :param output_text:
    :param front_symbol:
    :param front_text:
    :param mode:
    :return: None
    """
    if mode == "withtime":
        red_print(f"[{front_symbol}{front_text} {datetime.datetime.now()}] {output_text}")
    else:
        red_print(f"[{front_symbol}{front_text}] {output_text}")


# Print out but use pprint

class Proprint:
    @staticmethod
    def slog(output_text: str, front_symbol: str, front_text: str, mode: str = "withtime"):
        if mode == "withtime":
            green_print(f"[{front_symbol}{front_text} {datetime.datetime.now()}]")
            pprint.pprint(output_text)
        else:
            green_print(f"[{front_symbol}{front_text}]")
            pprint.pprint(output_text)

    @staticmethod
    def wlog(output_text: str, front_symbol: str, front_text: str, mode: str = "withtime"):
        if mode == "withtime":
            yellow_print(f"[{front_symbol}{front_text} {datetime.datetime.now()}]")
            pprint.pprint(output_text)
        else:
            yellow_print(f"[{front_symbol}{front_text}]")
            pprint.pprint(output_text)

    @staticmethod
    def elog(output_text: str, front_symbol: str, front_text: str, mode: str = "withtime"):
        if mode == "withtime":
            red_print(f"[{front_symbol}{front_text} {datetime.datetime.now()}]")
            pprint.pprint(output_text)
        else:
            red_print(f"[{front_symbol}{front_text}]")
            pprint.pprint(output_text)


# 2 Base print styles

class Net:
    @staticmethod
    def slog(output_text: str, mode: str = "withtime"):
        slog(output_text, STANDARD_OUTPUT_SYMBOL, NET_PART_NAME, mode)

    @staticmethod
    def wlog(output_text: str, mode: str = "withtime"):
        wlog(output_text, WARNING_SYMBOL, NET_PART_NAME, mode)

    @staticmethod
    def elog(output_text: str, mode: str = "withtime"):
        elog(output_text, ERROR_SYMBOL, NET_PART_NAME, mode)


class Data:
    @staticmethod
    def slog(output_text: str, mode: str = "withtime"):
        slog(output_text, STANDARD_OUTPUT_SYMBOL, DATASTORE_PART_NAME, mode)

    @staticmethod
    def wlog(output_text: str, mode: str = "withtime"):
        wlog(output_text, WARNING_SYMBOL, DATASTORE_PART_NAME, mode)

    @staticmethod
    def elog(output_text: str, mode: str = "withtime"):
        elog(output_text, ERROR_SYMBOL, DATASTORE_PART_NAME, mode)


if __name__ == "__main__":
    slog("ni hao nigger", "!", "human", "withtime")
    # red_print("nigger")
    # Net.slog("no nigger herr")
    pass
