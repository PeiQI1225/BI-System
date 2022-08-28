import requests
import datetime
import time
import threading


class test_login002:
    times = []
    error = []

    def login(self):
        mytest = test_login002
        url = "http://127.0.0.1:8001/api/v1.datasource/list?host=139.224.74.8&port=9000&user=default&password=2001G1225"
        headers = {'Host': '127.0.0.1:8001',
                   'Connection': 'keep-alive',
                   'Cache-Control': 'max-age=0',
                   'Upgrade-Insecure-Requests': '1',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/59.0.3071.115 Safari/537.36',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',

                   'Accept-Encoding': 'gzip, deflate',
                   'Accept-Language': 'zh-CN,zh;q=0.8'
                   }

        data = {
            '__RequestVerificationToken': '_d2CRXnYwB2-C-lyxSox2yG3kXccfDiKgZCKOOwnXHeyC_VNcByNaCthXXB7C_T22BnWAdjyZEcM347UbyuYgZimAbY1',
            '.ASPXAUTH': 'E40162DB50A8AC96D74418EB0DEC828780B2E067638C596A9B16E51237E9EE0483F1686AA4407A6ABC276DA7FE2539CC4212148844B564E2D013D7575F0DA0F58975516CF5494E3680D7F333252F3597DDE55D1EC9731897B88DCB7B0E5B9884E03904BF67EF158514A48CEFAE16B4613817E6A4F7CB992A18B983E1CC1C928925DF99EACCEBC6E3B9B12AC2DCC23B1BF509DDDDF43C9F9509666FD771946D66608B92D8B63D5FBD8713E0DC220E710367FE6E393AA8E5BD69821E6AED9DEEC8BDC62B8ED8EB6D3040325AAEEF720B248BA53FF044B746C264C3B360C7BEECA8E7CBA4332B6335BA66F26F68666524FA2BEB195636E72138F3074AAD90F7AC3C12BE9FE70CE40A614C79F1E41EED77A6C21DE1B432EE8E0D999DFC4502D57BAB168B29995588CF7D795383040BD9AFCEB4E11A70181634E5B0A1FECD28CBBAEEA80F4CB5D6BDE50A6D125B08514552326AE38832749B5A69FFEB8426CEBD4B0F714D53E59356A70321BB9B4B220F0E3C27C84950'}
        r = requests.post(url=url, headers=headers, data=data)
        ResponseTime = float(r.elapsed.microseconds) / 1000
        mytest.times.append(ResponseTime)
        if r.status_code != 200:
            mytest.error.append("0")


if __name__ == "__main__":
    mytest = test_login002()
    threads = []
    starttime = datetime.datetime.now()
    print("request start time %s " % starttime)
    nub = 10
    ThinkTime = 0.1
    for i in range(1, nub + 1):
        t = threading.Thread(target=mytest.login, args='')
        threads.append(t)
    for t in threads:
        time.sleep(ThinkTime)
        # t.setDaemon(True)
        t.daemon = True
        t.start()
    t.join()
    endtime = datetime.datetime.now()
    print("request end time %s" % endtime)
    time.sleep(0.1)
    AverageTime = "{:.3f}".format(float(sum(mytest.times)) / float(len(mytest.times)))
    print("Average Response Time %s ms" % AverageTime)
    usertime = str(endtime - starttime)
    hour = usertime.split(':').pop(0)
    minute = usertime.split(':').pop(1)
    second = usertime.split(':').pop(2)
    totaltime = float(hour) * 60 * 60 + float(minute) * 60 + float(second)
    print("Concurrent processing %s" % nub)
    print("use total time %s s" % (totaltime - float(nub * ThinkTime)))
    print("fail request %s" % mytest.error.count("0"))
