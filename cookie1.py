import urllib.request
import urllib.parse
import urllib.error
import http.cookiejar
import time

# cookie_filename = 'cookie1.txt'
# cookie = http.cookiejar.MozillaCookieJar(cookie_filename)
# #Netscape HTTP Cookie File
# cookie.load(cookie_filename, ignore_discard=True, ignore_expires=True)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# get_url1 = 'https://testv2.pandai.cn/home/get_captcha_text'  # 利用cookie请求访问另一个网址
# get_url = 'https://testv2.pandai.cn/registers/new'
# get_request = urllib.request.Request(get_url)
# header1 = {
#     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#     "Accept-Encoding":"utf-8",
#     "Accept-Language":"zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
#     "Connection":"keep-alive",
#     "Host":"testv2.pandai.cn",
#     "Referer":"https://testv2.pandai.cn/registers/new",
#     "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:50.0) Gecko/20100101 Firefox/50.0"
#     "Cookie":"Hm_lvt_efb73549c2150380afb7c447a533af55=1483528539,1483600178,1483672350,1483681155;
#              "CNZZDATA1260093310=581429397-1479777324-http%253A%252F%252Fuat.soopay.net%252F%7C1483959132;
#              "_p2plending_v2_session=L3pBQ1J5RXRIWVNjY2I0KzdLR2dhajRtSk43a3R5WU1XblJrUElDdkVHM2VYS3FnbFp4Q3EvZVNKd2I0RnRzcGd2bnFwTGFOdXkzZ1Zvdmx5SnV5S05LZlB2ckxpQmtMaG54VUNJQjRSeEZ6Wm4waXlCZENLN05rLzNjQlFSSFdsWUYrcDlSOXBYR2VaWmhiZ1crcThPWHMrVnFFVUNscVlhUzN2VFNiUUdRZVRPaVR1OWFwU0REUC9DU1FZaHNBSFozcUYwdzFnbllIQnV0Ui83eDZGUT09LS11MVBsUE1Fa21VSkNkZUxSN2tXMlNRPT0%3D--be03a98830d4b25c25bb305568f5a0432965f5d0; Hm_lpvt_efb73549c2150380afb7c447a533af55=1483960186; cn_1260093310_dplus=%7B%22distinct_id%22%3A%20%2215828f574f1a-02540fb974bb0b-485960-13c680-15828f574f241e%22%2C%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201483960188%2C%22initial_view_time%22%3A%20%221478152780%22%2C%22initial_referrer%22%3A%20%22%24direct%22%2C%22initial_referrer_domain%22%3A%20%22%24direct%22%2C%22%24recent_outside_referrer%22%3A%20%22%24direct%22%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201483960188%7D"
# }

header1={
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding":"utf-8",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Host":"h.highpin.cn",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "Referer":"http://h.highpin.cn/ManageJob/PubNewJob",


    "Cookie":"K2h5TUYrc3FOQXNlOEhQWEFSc0NIaEErRXpvMGV1SWduKzM2ZEV5cElyVFhrWk9GZEF1RDR0M3p6ZFFpa3NMSGhoZUkrYk13ZnBybG9ZYUhvYXNRQTk5emt1RTc2T1d2VDlnNnZkbU9vMjJyTGlYRkxDakF2VUVHTXl3L3lEaGh5ZG0wcnppdFdUMlpFNU9NckhtVWhJMVJkc0MxNU5RQjJodkpucjZUa3ZkY0NOckw5V2R3blBRWEVaMy9iRUVIZlppeVpGUURVTmdRbjdkQ3dpNGxXQT09LS1HdzA4UC9DSkprMm92dVgvb3poSWJnPT0=--a9556f0fdcf753d655c738684e4bee2e89e3442a",
    "Connection":"keep-alive"
    }


time.sleep(2)


url = 'https://testv2.pandai.cn/home/get_captcha_text'
get_request2 = urllib.request.Request(url,header1)
# get_response = get_request2.open(get_request2)
r = urllib.request.urlopen(url)
print(r.read().decode('utf-8'))

# cookie.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中
# for item in cookie:
#     print('Name = ' + item.name)
#     print('Value = ' + item.value)