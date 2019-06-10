import time
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from multiprocessing import Process, Queue
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


def f_crawling(request):
    if request.is_ajax() or request.POST:
        f_username = request.POST.get('f_username')
        f_password = request.POST.get('f_password')

        if f_username != '' and f_password != '':
            f_data = facebook(1, f_username, f_password)
            # 로그인이나 보안으로 인하여 크롤링이 안됐을시
            if len(f_data) > 1:
                ctx = {
                    'facebook_info': f_data[0],
                    'facebook_friends': f_data[1],
                    'facebook_img': f_data[2]
                }
                return JsonResponse(ctx, content_type="application/json", json_dumps_params={'ensure_ascii': False})
            else:
                ctx = {
                    'facebook_info': f_data,
                }
                return JsonResponse(ctx, content_type="application/json", json_dumps_params={'ensure_ascii': False})
        else:
            return None
    return None


def i_crawling(request):
    if request.is_ajax() and request.POST:
        i_username = request.POST.get('i_username')
        i_password = request.POST.get('i_password')
        # 아이디 비밀번호 미입력시
        if i_username != '' and i_password != '':
            i_data = instagram(1, i_username, i_password)

            # 로그인이나 보안으로 인하여 크롤링이 안됐을시
            if len(i_data) > 1:
                ctx = {
                    'instagram_info': i_data[0],
                    'instagram_following': i_data[1],
                    'instagram_img': i_data[2]
                }
                return JsonResponse(ctx, content_type="application/json", json_dumps_params={'ensure_ascii': False})
            else:
                ctx = {
                    'instagram_info': i_data,
                }
                return JsonResponse(ctx, content_type="application/json", json_dumps_params={'ensure_ascii': False})
        else:
            return None
    return None


def t_crawling(request):
    if request.is_ajax() and request.POST:
        t_username = request.POST.get('t_username')
        t_password = request.POST.get('t_password')

        if t_username != '' and t_password != '':
            t_data = twitter(1, t_username, t_password)
            # 로그인이나 보안으로 인하여 크롤링이 안됐을시
            if len(t_data) > 1:
                ctx = {
                    'twitter_info': t_data[0],
                    'twitter_following': t_data[1],
                    'twitter_img': t_data[2]
                }
                return JsonResponse(ctx, content_type="application/json", json_dumps_params={'ensure_ascii': False})
            else:
                ctx = {
                    'twitter_info': t_data,
                }
                return JsonResponse(ctx, content_type="application/json", json_dumps_params={'ensure_ascii': False})
        else:
            return None
    return None


def y_crawling(request):
    if request.is_ajax() and request.POST:
        y_username = request.POST.get('g_username')
        y_password = request.POST.get('g_password')

        if y_username != '' and y_password != '':
            y_data = youtube(1, y_username, y_password)

            if len(y_data) > 1:
                ctx = {
                    'youtube_info': y_data[0],
                    'youtube_subscribe': y_data[1],
                    'youtube_img': y_data[2]
                }
                return JsonResponse(ctx, content_type="application/json", json_dumps_params={'ensure_ascii': False})
            else:
                ctx = {
                    'youtube_info': y_data,
                }
                return JsonResponse(ctx, content_type="application/json", json_dumps_params={'ensure_ascii': False})
        else:
            return None
    return None


def g_crawling(request):
    if request.is_ajax() and request.POST:
        g_username = request.POST.get('g_username')
        g_password = request.POST.get('g_password')

        if g_username != '' and g_password != '':
            g_data = gmail(1, g_username, g_password)
            if len(g_data) > 1:
                ctx = {
                    'gmail_info': g_data[0],
                    'gmail_list': g_data[1]
                }
                # print(ctx)
                return JsonResponse(ctx, content_type="application/json", json_dumps_params={'ensure_ascii': False})
            else:
                ctx = {
                    'gmail_info': g_data,
                }
                return JsonResponse(ctx, content_type="application/json", json_dumps_params={'ensure_ascii': False})
        else:
            return None
    return None
