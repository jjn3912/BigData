from bs4 import BeautifulSoup

html = """
<html>
<head>
<title>스크레이핑 실습</title>
</head>
<body>
<a href="https://www.daelim.ac.kr">대림대학교</a><br>
<a href="http://www.harvard.edu">하버드대학교</a><br>
</body>
</html>
"""
soup = BeautifulSoup(html, 'html.parser')
urls = soup.find_all('a')
print(urls)
#하버드대학교 rl주소는 http://www.harvard.edu 입니다.
for url in urls:
    print("{0}의 주소는 {1}입니다.".format(url.string, url.attrs['href']))
