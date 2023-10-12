import urllib.request

from bs4 import BeautifulSoup

html ="""
<html>
<head>
<title>스크레이핑 실슴</title>
</head>
<body>
<a href="http://www.daelim.ac.kr">대림대학교</a><br>
<a href="http://www.harvard.edu">하버드대학교</a>
</body>
</html>
"""
api ='https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'
urls = urllib.request.urlopen(api).read()
soup= BeautifulSoup(urls, 'html.parser')


cities = soup.find_all("city")
data = soup.find_all("data")


for i in range(len(cities)):
    print(f'{cities[i].string}의 날씨는 {data[i*13].find("wf").string}입니다.')
print(len(cities), len(data))
# print(urls)
# for url in urls:
#     print(f'{url.string}의 url주소는 {url.attrs["href"]}입니다.')
    # univ = url.string
    # link = url.attrs['href']
    # print(univ)
    # print(link)
