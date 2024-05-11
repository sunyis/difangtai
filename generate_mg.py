#import subprocess
from datetime import datetime
import requests
import os

def generate_m3u8_stream_with_info(urls, info_list):
    if len(urls) != len(info_list):
        raise ValueError("URLs and info list should have the same length")
    # 生成m3u文件
    m3u8_content = "#EXTM3U x-tvg-url=\"https://mirror.ghproxy.com/https://raw.githubusercontent.com/mlzlzj/mgtv/main/mgtv.xml\"\n"
    for index, (url, info) in enumerate(zip(urls, info_list)):
        tvg_id = info.get("tvg-id", "")
        tvg_name = info.get("tvg-name", "")
        tvg_logo = info.get("tvg-logo", "")
        m3u8_content += f'#EXTINF:-1 tvg-id="{tvg_id}" tvg-name="{tvg_name}" tvg-logo="{tvg_logo}" group-title=\"湖南\",{tvg_name} \n{url}\n'
    with open("mgtv.m3u", "w") as file:
        file.write(m3u8_content)

    # 生成txt文件
    txt_content = ''
    #m3u8_content = "x-tvg-url=\"https://mirror.ghproxy.com/https://raw.githubusercontent.com/mlzlzj/mgtv/main/mgtv.xml\"\n"
    for index, (url, info) in enumerate(zip(urls, info_list)):
        #tvg_id = info.get("tvg-id", "")
        #tvg_name = info.get("tvg-name", "")
        #tvg_logo = info.get("tvg-logo", "")
        txt_content += f'{tvg_name},{url}\n'
    with open("mgtv.txt", "w", encoding="utf-8") as file:
        file.write(txt_content)
        now = datetime.now()
        file.write(f"更新时间,#genre#\n")
        file.write(f"{now.strftime("%Y-%m-%d %H:%M:%S")},url\n")


stream_info_list = [
    {
        "tvg-id": "280",
        "tvg-name": "湖南经视",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/hnjs.png",
        "filename": "hn01.m3u8",
    },
    {
        "tvg-id": "346",
        "tvg-name": "湖南都市",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/hnds.png",
        "filename": "hn02.m3u8",
    },
    {
        "tvg-id": "484",
        "tvg-name": "湖南电视剧",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/hndsj.png",
        "filename": "hn03.m3u8",
    },
    {
        "tvg-id": "261",
        "tvg-name": "湖南公共",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/hngg.png",
        "filename": "hn04.m3u8",
    },
    {
        "tvg-id": "229",
        "tvg-name": "湖南国际",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/hngj.png",
        "filename": "hn05.m3u8",
    },
    {
        "tvg-id": "344",
        "tvg-name": "湖南娱乐",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/hnyl.png",
        "filename": "hn06.m3u8",
    },
    {
        "tvg-id": "267",
        "tvg-name": "快乐购",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/hnklg.png",
        "filename": "hn07.m3u8",
    },
    {
        "tvg-id": "578",
        "tvg-name": "茶频道",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/cpd.png",
        "filename": "hn08.m3u8",
    },
    {
        "tvg-id": "316",
        "tvg-name": "金鹰纪实",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/jyjs.png",
        "filename": "hn09.m3u8",
    },
    {
        "tvg-id": "287",
        "tvg-name": "金鹰卡通",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/jykt.png",
        "filename": "hn10.m3u8",
    },
    {
        "tvg-id": "218",
        "tvg-name": "快乐垂钓",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/klcd.png",
        "filename": "hn11.m3u8",
    },
    {
        "tvg-id": "329",
        "tvg-name": "先锋乒羽",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/xfpy.png",
        "filename": "hn12.m3u8",
    },
    {
        "tvg-id": "269",
        "tvg-name": "长沙新闻",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/csxw.png",
        "filename": "hn13.m3u8",
    },
    {
        "tvg-id": "254",
        "tvg-name": "长沙政法",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/cszf.png",
        "filename": "hn14.m3u8",
    },
    {
        "tvg-id": "230",
        "tvg-name": "长沙女性",
        "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/mgtv@main/logo/csnx.png",
        "filename": "hn15.m3u8",
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
        'http': '47.114.101.57:8888',
    }
    url = f'http://mpp.liveapi.mgtv.com/v1/epg/turnplay/getLivePlayUrlMPP?version=PCweb_1.0&platform=1&buss_id=2000001&channel_id={channel_id}'
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

print("mgtv.m3u8文件已生成。")
