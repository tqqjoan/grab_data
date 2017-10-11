# -*- coding:UTF-8 -*-
import re
import urllib

def gethtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist
def getconment(html):
    reg = r'"rateContent":"(.+?)",'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist
if __name__ == '__main__':
    html = gethtml("https://rate.tmall.com/list_detail_rate.htm?itemId=521534875164&spuId=348759693&sellerId=1644880265&order=3&currentPage=1&append=0&content=1&tagId=&posi=&picture=&ua=098#E1hvvvv7vOOvUvCkvvvvvjiPP2SOtjtjPLFUAjnEPmPOsjYRPFLZljYVRsLwsjimdphvhkphvQULhQpPIkeS8oxLiXcasLyCvvpvvvvvRphvCvvvvvmCvpvW7DQMmmFw7Di4NG5N9phv2HiwjMwVzHi47eQ1zsyCvvpvvvvv3QhvCvvhvvm5vpvhvvmv99GCvvpvvPMMKphv8vvvvvCvpvvvvvvCJZCvmUyvvUUdphvWvvvv9krvpv3FvvmCvhCvmVRivpvUvvmvd65y+YJEvpvV2vvC9jxvmphvLCCxFvvjWfmxfwpOd5lPARm+D404jLVxfwLhdigDNKBleE7rejvr+Exr08gcWhcnI4mxdX31b8oQD70wd5lPARm+D404jLVxfaBl5dUCvpvVvvpvvhCvRphvCvvvvvmCvpvW7DQcz1dw7Di4ObzNRphvCvvvvvmrvpvEvv2k9SMMCHIldphvhovUD9UNjQBeXoeS8kH2mOcE9phvV0Df2NMszHi47MiBzAcjKGqRsRDdm8e/ubSjvQwCvva47rMNMCjF9phvHHifvSMjzHi471y4tMQv7er4srYO&isg=AtracYgkVwidYtvLMMYgAywRKoM8o16CmfDsKORTBG04V3iRzZrr9bVlURm0&needFold=0&_ksTS=1507696030857_1603&callback=jsonp1604")
    print html
    content = getconment(html)
    for i in content:
        print i.decode("gbk")