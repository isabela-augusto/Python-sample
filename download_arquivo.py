# coding: utf-8

import io
import sys
import urllib.request as request

BUFF_SIZE = 1024

def download_length(response, output, lenght):
    times = lenght // BUFF_SIZE
    if lenght % BUFF_SIZE > 0:
        times += 1
    for time in range(times):
        output.write(response.read(BUFF_SIZE))
        print("Downloaded {}".format((((time * BUFF_SIZE)/lenght)*100)))

def download(response, output):
    total_downloaded = 0
    while True:
        data = response.read(BUFF_SIZE)
        total_downloaded += len(data)
        if not data
            break