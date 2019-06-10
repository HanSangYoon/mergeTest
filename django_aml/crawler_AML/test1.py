import time
import json
from django.http import HttpResponse
from django.shortcuts import render
from multiprocessing import Process, Pool, Queue
from crawler_AML.crawler.user_db import user_tbl_select_AML
from crawler_AML.crawler.facebook.facebookCrawlerBot_AML import start as facebook
from crawler_AML.crawler.instagram.instagramCrawlerBot_AML import start as instagram
from crawler_AML.crawler.youtube.youtubeCrawlerBot_AML import start as youtube
from crawler_AML.crawler.twitter.twitterCrawlerBot_AML import start as twitter
from crawler_AML.crawler.gmail.gmailCrawlerBot_AML import start as gmail


def home(request):
    ctx = {

    }
    return render(request, 'home.html', ctx)


def crawling(request):
    if request.method == "POST":
        f_username = request.POST.get('f_username')
        f_password = request.POST.get('f_password')
        i_username = request.POST.get('i_username')
        i_password = request.POST.get('i_password')
        t_username = request.POST.get('t_username')
        t_password = request.POST.get('t_password')
        g_username = request.POST.get('g_username')
        g_password = request.POST.get('g_password')

        # 데이터 담을 객체
        f_data = Queue()
        i_data = Queue()
        y_data = Queue()
        t_data = Queue()
        g_data = Queue()

        # 프로세스 시작
        start_time_all = time.time()
        if f_username != '' and f_password != '':
            p1 = Process(target=facebook, args=(1, f_username, f_password, f_data,))
            p1.start()

        else:
            p1 = ''

        if i_username != '' and i_password != '':
            p2 = Process(target=instagram, args=(1, i_username, i_password, i_data,))
            p2.start()
        else:
            p2 = ''

        if g_username != '' and g_password != '':
            p3 = Process(target=youtube, args=(1, g_username, g_password, y_data,))
            p3.start()
        else:
            p3 = ''

        if t_username != '' and t_password != '':
            p4 = Process(target=twitter, args=(1, t_username, t_password, t_data,))
            p4.start()
        else:
            p4 = ''

        if g_username != '' and g_password != '':
            p5 = Process(target=gmail, args=(1, g_username, g_password, g_data,))
            p5.start()
        else:
            p5 = ''

        # 프로세스 종료
        if type(p1) == Process:
            p1.join()
        if type(p2) == Process:
            p2.join()
        if type(p3) == Process:
            p3.join()
        if type(p4) == Process:
            p4.join()
        if type(p5) == Process:
            p5.join()

        # 데이터 가져오기
        try:
            f_data = f_data.get(timeout=1)
        except Exception as e:
            f_data = ''
        try:
            i_data = i_data.get(timeout=1)
        except Exception as e:
            i_data = ''
        try:
            y_data = y_data.get(timeout=1)
        except Exception as e:
            y_data = ''
        try:
            t_data = t_data.get(timeout=1)
        except Exception as e:
            t_data = ''
        try:
            g_data = g_data.get(timeout=1)
        except Exception as e:
            g_data = ''

        print('멀티 프로세스 :', time.time() - start_time_all)

        ctx = {
            'facebook': f_data,
            'instagram': i_data,
            'youtube': y_data,
            'twitter': t_data,
            'gamil': g_data,
        }
        return render(request, 'crawling.html', ctx)

    ctx = {

    }
    return render(request, 'crawling.html', ctx)
