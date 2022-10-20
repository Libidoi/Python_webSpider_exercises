import urllib.request
import urllib.parse


# 下载豆瓣前15页数据

# 1、请求对象定制
# 2、获取请求request
# 3、获取相应
# 4、下载数据
# 入口
def create_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&'

    data = {
        'start': (page - 1) * 20,
        'limit': 20
    }
    data = urllib.parse.urlencode(data)

    url = base_url + data

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'}

    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_context(request):
    response = urllib.request.urlopen(request)
    context = response.read().decode('utf8')
    return context


def download(page, context):
    with open('douban_' + str(page) + '.json', 'w', encoding='utf8') as fp:
        fp.write(context)


if __name__ == '__main__':
    start_page = int(input('起始页码：'))
    end_page = int(input('结束页码'))

    for page in range(start_page, end_page + 1):
        # 因为每面的url不同,所以每个页面的请求对象都不同
        request = create_request(page)
        # 获取响应的数据
        context = get_context(request)
        # 下载
        download(page, context)
