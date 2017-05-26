import requests
from bs4 import BeautifulSoup
import os, time
import re

#模拟登陆知乎
# import http.cookiejar as cookielib

# 构造 Request headers
agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
headers = {
    "Host": "issues.apache.org",
    "Referer": "https://issues.apache.org/jira/login.jsp",
    'User-Agent': agent
}

######### 构造用于网络请求的session
session = requests.Session()
# session.cookies = cookielib.LWPCookieJar(filename='zhihucookie')
# try:
#     session.cookies.load(ignore_discard=True)
# except:
#     print('cookie 文件未能加载')

########### 开始登陆
headers['X-Requested-With'] = 'XMLHttpRequest'
loginurl = 'https://issues.apache.org/jira/login.jsp'
postdata = {
    'login': 'Log In',
    'os_username': 'kongcheng',
    'os_password': 'xy521521'
}
loginresponse = session.post(url=loginurl, headers=headers, data=postdata)
print('服务器端返回响应码：', loginresponse.status_code)
#print(loginresponse.json())


##########################保存登陆后的cookie信息
#session.cookies.save()
############################判断是否登录成功
profileurl = 'https://issues.apache.org/jira/secure/ViewProfile.jspa'
profileresponse = session.get(url=profileurl, headers=headers)
print('profile页面响应码：', profileresponse.status_code)
profilesoup = BeautifulSoup(profileresponse.text, 'html.parser')
div = profilesoup.find('span', {'id': 'up-user-title-name'})
print(div)

check = 'https://issues.apache.org/jira/issues/?jql=project%20in%20(YARN%2C%20HDFS%2C%20HADOOP%2C%20MAPREDUCE)%20AND%20status%20%3D%20Resolved&startIndex='



def getOnepage(url):
    checkresponse = session.get(url=url, headers=headers)
    soup = BeautifulSoup(checkresponse.text, 'html.parser')
    #print(soup.prettify())
    div = soup.find_all('span', {'class': 'issue-link-key'})
    for i in div:
        f.write(i.string+',')
    #print(s)
#d=0
#while (d < 293):
#    getOnepage(check+str(d*50))
#    d=d+1

#html = requests.get('https://issues.apache.org/jira/browse/YARN-6627?jql=project%20in%20(YARN%2C%20HDFS%2C%20HADOOP%2C%20MAPREDUCE)%20AND%20status%20%3D%20Resolved')
#print(html.text)
f = open('ppp.txt', 'r')
a=f.read()
f.close()
b=a.split(',')
s=set()
for i in b:
    s.add(i)

#p=open('ppp.txt','a')
def getpage(u):
    cs = session.get(url=u, headers=headers)
    sp = BeautifulSoup(cs.text, 'html.parser')
    #print(soup.prettify())
    dd=sp.find_all('ul', {'id': 'peopledetails'})
    if len(dd)!=0:
        m = re.search(r'rel="(.+)"', str(dd[0]))
        if len(m.groups())==1:
            print(m.groups()[0])
            p.write(m.groups()[0]+',')
        elif len(m.groups())==2:
            print(m.groups()[0]+','+m.groups()[1])
            p.write(m.groups()[0]+','+m.groups()[1] + ',')



onepage = 'https://issues.apache.org/jira/browse/'
#getpage(onepage+'YARN-6618')
#for num in s:
#    getpage(onepage+num)

pag='https://issues.apache.org/jira/secure/ViewProfile.jspa?name='
pera=open('result111.txt','a')
def getOneperson(ur):
    cs = session.get(url=ur, headers=headers)
    sp = BeautifulSoup(cs.text, 'html.parser')
    # print(soup.prettify())
    dic={}
    dd = sp.find_all('dd', {'id': 'up-d-username'})
    ddfullname=sp.find_all('dd', {'id': 'up-d-fullname'})
    ddemail = sp.find_all('dd', {'id': 'up-d-email'})
    if len(dd)!=0 and len(ddfullname)!=0 and len(ddemail)!=0:
        dic['username']=dd[0].string.strip()
        dic['fullname']=ddfullname[0].string
        dic['email']=ddemail[0].string
        print(dd[0].string.strip())
        print(dic)
        pera.write(str(dic)+',')

for nn in s:
    getOneperson(pag+nn)
