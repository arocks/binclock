from django.http import HttpResponse
from django.utils.timezone import localtime, now

char_one = chr(0x25CF)
char_zero = chr(0x25CB)


def bcd_digit(x):
    return [(x & 8) >> 3, (x & 4) >> 2, (x & 2) >> 1, x & 1]


def bcd_2digits(x):
    return [bcd_digit(x // 10), bcd_digit(x % 10)]


def bcd_hhmmss(dt):
    return bcd_2digits(dt.hour) + bcd_2digits(dt.minute) + \
        bcd_2digits(dt.second)


def disp_unicode(clock_matrix):
    return "\n".join(" ".join(char_one if p == 1 else char_zero for p in line
                              ) for line in list(zip(*clock_matrix)))


def home(request):
    clock = disp_unicode(bcd_hhmmss(localtime(now())))
    return HttpResponse(clock, content_type="text/plain; charset=utf-8")




















