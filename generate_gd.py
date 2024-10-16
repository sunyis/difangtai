#import subprocess
from datetime import datetime
import requests
import os

def generate_m3u8_stream_with_info(urls, info_list):
    if len(urls) != len(info_list):
        raise ValueError("URLs and info list should have the same length")
    # 生成m3u文件
    m3u8_content = "#EXTM3U x-tvg-url=\"https://e.wztv.us.kg/e.xml\"\n"
    for index, (url, info) in enumerate(zip(urls, info_list)):
        tvg_id = info.get("tvg-id", "")
        tvg_name = info.get("tvg-name", "")
        tvg_logo = info.get("tvg-logo", "")
        m3u8_content += f'#EXTINF:-1 tvg-id="{tvg_id}" tvg-name="{tvg_name}" tvg-logo="{tvg_logo}" group-title=\"广东\",{tvg_name} \n{url}\n'
    with open("gdtv.m3u", "w") as file:
        file.write(m3u8_content)

    # 生成txt文件
    txt_content = '广东TV,#genre#\n'
    #m3u8_content = "x-tvg-url=\"https://e.wztv.us.kg/e.xml\"\n"
    for index, (url, info) in enumerate(zip(urls, info_list)):
        #tvg_id = info.get("tvg-id", "")
        tvg_name = info.get("tvg-name", "")
        #tvg_logo = info.get("tvg-logo", "")
        txt_content += f'{tvg_name},{url}\n'
    with open("gdtv.txt", "w", encoding="utf-8") as file:
        file.write(txt_content)
        now = datetime.now()
        file.write(f"更新时间,#genre#\n")
        file.write(f"{now.strftime("%Y-%m-%d %H:%M:%S")},url\n")


stream_info_list = [
    {
        "tvg-id": "43",
        "tvg-name": "广东卫视",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/hnjs.png",
        "filename": "gd43.m3u8",
    },
    {
        "tvg-id": "44",
        "tvg-name": "广东珠江",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/hnds.png",
        "filename": "gd44.m3u8",
    },
    {
        "tvg-id": "45",
        "tvg-name": "广东新闻",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/hndsj.png",
        "filename": "gd45.m3u8",
    },
    {
        "tvg-id": "48",
        "tvg-name": "广东民生",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/hngg.png",
        "filename": "gd48.m3u8",
    },
    {
        "tvg-id": "47",
        "tvg-name": "广东体育",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/hngj.png",
        "filename": "gd47.m3u8",
    },
    {
        "tvg-id": "51",
        "tvg-name": "大湾区卫视",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/hnyl.png",
        "filename": "gd51.m3u8",
    },
    {
        "tvg-id": "46",
        "tvg-name": "大湾区卫视 海外",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/hnklg.png",
        "filename": "gd46.m3u8",
    },
    {
        "tvg-id": "49",
        "tvg-name": "经济科教",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/cpd.png",
        "filename": "gd49.m3u8",
    },
    {
        "tvg-id": "53",
        "tvg-name": "广东影视",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/jyjs.png",
        "filename": "gd53.m3u8",
    },
    {
        "tvg-id": "16",
        "tvg-name": "4K超高清",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/jykt.png",
        "filename": "gd16.m3u8",
    },
    {
        "tvg-id": "54",
        "tvg-name": "广东少儿",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/klcd.png",
        "filename": "gd54.m3u8",
    },
    {
        "tvg-id": "66",
        "tvg-name": "嘉佳卡通",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/xfpy.png",
        "filename": "gd66.m3u8",
    },
    {
        "tvg-id": "16",
        "tvg-name": "岭南戏曲",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/csxw.png",
        "filename": "gd16.m3u8",
    },
    {
        "tvg-id": "13",
        "tvg-name": "现代教育",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/cszf.png",
        "filename": "gd13.m3u8",
    },
    {
        "tvg-id": "74",
        "tvg-name": "广东移动",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/csnx.png",
        "filename": "gd74.m3u8",
    },
    {
        "tvg-id": "100",
        "tvg-name": "荔枝台",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/hndy.png",
        "filename": "gd100.m3u8",
    },
    {
        "tvg-id": "94",
        "tvg-name": "纪录片",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/hndy.png",
        "filename": "gd94.m3u8",
    },
    {
        "tvg-id": "99",
        "tvg-name": "GRTN健康频道",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/csnx.png",
        "filename": "gd99.m3u8",
    },
    {
        "tvg-id": "75",
        "tvg-name": "GRTN文化频道",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/hndy.png",
        "filename": "gd75.m3u8",
    },   
    {
        "tvg-id": "102",
        "tvg-name": "GRTN生活频道",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/csnx.png",
        "filename": "gd102.m3u8",
    },
    {
        "tvg-id": "104",
        "tvg-name": "GRTN教育频道",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/hndy.png",
        "filename": "gd104.m3u8",
    },
]
def update_single_m3u8_file(url, filename):
    m3u8_dir = 'm3u8'
    filepath = os.path.join(m3u8_dir, filename)
    with open(filepath, 'r') as file:
        lines = file.readlines()
    with open(filepath, 'w') as file:
        for line in lines:
            if line.startswith('http'):
                file.write(url + '\n')
            else:
                file.write(line)
    print(f'更新{filepath}完毕！')

def get_live_url(channel_id):
    proxy= {
        'http': '221.231.13.198:1080',
    }
    url = f'https://www.gdtv.cn/tvChannelDetail/{channel_id}&node=$node'
    # print(channel_id, url)
    response = requests.get(url, proxies=proxy)
    data = response.json()
    return data.get('data', {}).get('url')

# 示例 URL 列表和信息列表
def generate_live_stream_urls(stream_info_list):
    live_stream_urls = []
    for stream_info in stream_info_list:
        tvg_id = stream_info.get("tvg-id")
        filename = stream_info.get("filename")
        # # 调用另一个脚本，传入 tvg-id 参数
        # process = subprocess.Popen(
        #     ["python", "./update_url.py", tvg_id, filename],
        #     stdout=subprocess.PIPE,
        # )
        # output, error = process.communicate()
        # 输出中应该包含直播流链接，你可以根据实际情况进行解析
        live_url = get_live_url(tvg_id)
        print(live_url)
        if live_url:
            update_single_m3u8_file(live_url, filename)
            # print('文件 {filename} 的URL已更新为：')
            # print(f'{live_url}\n')
        else:
            print('未能获取到直播URL, 请检查网络或参数设置。')

        #live_stream_url = output.decode("utf-8").strip()
        live_stream_urls.append(live_url)
    return live_stream_urls


# 示例调用
live_stream_urls = generate_live_stream_urls(stream_info_list)
print(live_stream_urls)

generate_m3u8_stream_with_info(live_stream_urls, stream_info_list)

print("gdtv.m3u8文件已生成。")
