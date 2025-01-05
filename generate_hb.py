#import subprocess
from datetime import datetime
import requests
import os

def generate_m3u8_stream_with_info(urls, info_list):
    if len(urls) != len(info_list):
        raise ValueError("URLs and info list should have the same length")
    # 生成m3u文件
    m3u8_content = "#EXTM3U x-tvg-url=\"https://mirror.ghproxy.com/https://raw.githubusercontent.com/mlzlzj/hbtv/main/hbtv.xml\"\n"
    for index, (url, info) in enumerate(zip(urls, info_list)):
        tvg_id = info.get("tvg-id", "")
        tvg_name = info.get("tvg-name", "")
        tvg_logo = info.get("tvg-logo", "")
        m3u8_content += f'#EXTINF:-1 tvg-id="{tvg_id}" tvg-name="{tvg_name}" tvg-logo="{tvg_logo}" group-title=\"河北\",{tvg_name} \n{url}\n'
    with open("hbtv.m3u", "w") as file:
        file.write(m3u8_content)

    # 生成txt文件
    txt_content = '河北TV,#genre#\n'
    #m3u8_content = "x-tvg-url=\"https://mirror.ghproxy.com/https://raw.githubusercontent.com/mlzlzj/mgtv/main/mgtv.xml\"\n"
    for index, (url, info) in enumerate(zip(urls, info_list)):
        #tvg_id = info.get("tvg-id", "")
        tvg_name = info.get("tvg-name", "")
        #tvg_logo = info.get("tvg-logo", "")
        txt_content += f'{tvg_name},{url}\n'
    with open("hbtv.txt", "w", encoding="utf-8") as file:
        file.write(txt_content)
        now = datetime.now()
        file.write(f"更新时间,#genre#\n")
        file.write(f"{now.strftime("%Y-%m-%d %H:%M:%S")},url\n")


stream_info_list = [
  {
    "tvg-id": "280",
    "tvg-name": "河北卫视",
    "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/hbtv@main/logo/hebtv.png",
    "filename": "hb01.m3u8",
    "urls": [
      "https://www.hebtv.com/19/19js/st/xdszb/index.shtml?index=0"
    ]
  },
  {
    "tvg-id": "281",
    "tvg-name": "河北经济",
    "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/hbtv@main/logo/hebtv.png", 
    "filename": "hb02.m3u8",
    "urls": [
      "https://www.hebtv.com/19/19js/st/xdszb/index.shtml?index=1"
    ]
  },
  {
    "tvg-id": "282",
    "tvg-name": "农民频道",
    "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/hbtv@main/logo/hebtv.png",
    "filename": "hb03.m3u8",
    "urls": [
      "https://www.hebtv.com/19/19js/st/xdszb/index.shtml?index=2"
    ]
  },
  {
    "tvg-id": "283",
    "tvg-name": "河北都市",
    "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/hbtv@main/logo/hebtv.png", 
    "filename": "hb04.m3u8",
    "urls": [
      "https://www.hebtv.com/19/19js/st/xdszb/index.shtml?index=3"
    ]
  },
  {
    "tvg-id": "284",
    "tvg-name": "河北影视剧",
    "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/hbtv@main/logo/hebtv.png",
    "filename": "hb05.m3u8",
    "urls": [
      "https://www.hebtv.com/19/19js/st/xdszb/index.shtml?index=4"
    ]
  },
  {
    "tvg-id": "285",
    "tvg-name": "少儿科教",
    "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/hbtv@main/logo/hebtv.png", 
    "filename": "hb06.m3u8",
    "urls": [
      "https://www.hebtv.com/19/19js/st/xdszb/index.shtml?index=5"
    ]
  },
  {
    "tvg-id": "286",
    "tvg-name": "文旅公共",
    "tvg-logo": "https://cdn.jsdelivr.net/gh/mlzlzj/hbtv@main/logo/hebtv.png",
    "filename": "hb07.m3u8",
    "urls": [
      "https://www.hebtv.com/19/19js/st/xdszb/index.shtml?index=6"
    ]
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
    
    url = f'https://api.cmc.hebtv.com/spidercrms/api/live/liveShowSet/findNoPage}'
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

print("hbtv.m3u8文件已生成。")
