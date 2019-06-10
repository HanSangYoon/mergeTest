# from multiprocessing import Process, freeze_support
# import time
# from crawler_AML.crawler.facebook.facebookCrawlerBot_AML import start as facebook
# from crawler_AML.crawler.instagram.instagramCrawlerBot_AML import start as instagram
# from crawler_AML.crawler.youtube.youtubeCrawlerBot_AML import start as youtube
# from crawler_AML.crawler.twitter.twitterCrawlerBot_AML import start as twitter
# from crawler_AML.crawler.gmail.gmailCrawlerBot_AML import start as gmail
#
#
# def home():
#     start_time_all = time.time()
#     facebook_user_id = '01053474109'
#     facebook_user_pw = 'xhdtls*03'
#     google_user_id = 'yifi1004@gmail.com'
#     google_user_pw = 'xhdtls*0#'
#     twitter_user_id = 'yifi1004@gmail.com'
#     twitter_user_pw = '4109121z'
#     insta_user_id = 'hj.vw'
#     insta_user_pw = '4109121z#!'
#
#     p1 = Process(target=facebook, args=(1, facebook_user_id, facebook_user_pw))
#     p2 = Process(target=instagram, args=(1, insta_user_id, insta_user_pw))
#     p3 = Process(target=youtube, args=(1, google_user_id, google_user_pw))
#     p4 = Process(target=twitter, args=(1, twitter_user_id, twitter_user_pw))
#     p5 = Process(target=gmail, args=(1, google_user_id, google_user_pw))
#
#     p1.start()
#     p2.start()
#     p3.start()
#     p4.start()
#     p5.start()
#
#     p1.join()
#     p2.join()
#     p3.join()
#     p4.join()
#     p5.join()
#     print('멀티 프로세스 :', time.time() - start_time_all)
#
# freeze_support()
# home()
i = dict()
j = list()

i['a'] = '3'
i['b'] = '3'
for j in i:
    print(j)
