import datetime
import hashlib
import re
import time

import requests

#友爱社id
union_id = 000

def CurrentTime():
    current_time = int(time.mktime(datetime.datetime.now().timetuple()))
    return str(current_time)


class Friendly_society:
    def __init__(self, cookie):
        self.cookie = cookie
        self.csrf = re.findall(r'bili_jct=(\S+)', cookie)[0].split(";")[0]
        self.sid = re.findall(r'sid=(\S+);', cookie)[0]
        self.access_key = re.findall(r'access_token=(\S+);', cookie)[0].split(";")[0]

    # 获取sign
    def calc_sign(self, str):
        str += '560c52ccd288fed045859ed18bffd973'
        #获取一个md5加密算法对象
        hash = hashlib.md5()
        hash.update(str.encode('utf-8'))
        sign = hash.hexdigest()
        return sign

    # 加入友爱社
    def Join_friendly_society(self):
        url = f'https://api.live.bilibili.com/activity/v1/UnionFans/apply'
        data = {
            'union_id': union_id,
            'csrf_token': self.csrf,
            'csrf': self.csrf
        }
        headers = {
            'Cookie': self.cookie,
            'Host': 'api.live.bilibili.com',
            'Origin': 'https://link.bilibili.com',
            'Referer': 'https://link.bilibili.com/p/center/index',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
        }
        response = requests.request("post", url=url, headers=headers, data=data,timeout=4).json()
        print(response)

    # 获取友爱社申请列表 + 同意 副社以上有权限  不使用代理
    def getApplyList(self):
        try:
            url = 'https://api.live.bilibili.com/activity/v1/UnionFans/getApplyList?page=1'
            data = {
                'page': 1
            }
            headers = {
                'Cookie': self.cookie,
                'Host': 'api.live.bilibili.com',
                'Origin': 'https://link.bilibili.com',
                'Referer': 'https://link.bilibili.com/p/center/index',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
            }
            while True:
                response = requests.request('get', url, params=data, headers=headers,timeout=3).json()
                # 判断列表里面有成员
                list_len = int(len(response['data']['list']))
                if list_len != 0:
                    for i in range(0, list_len):
                        apply_id = response['data']['list'][i]['apply_id']
                        uname = response['data']['list'][i]['uname']
                        print(uname, end=' ')
                        self.verify(apply_id)

                else:
                    print('没检测到有申请,休息5s')
                    time.sleep(5)
        except Exception as e:
            print("异常了,休息3秒后继续",e)
            time.sleep(3)
            self.getApplyList()
    # 同意进入
    def verify(self, apply_id):
        url = 'https://api.live.bilibili.com/activity/v1/UnionFans/verify'
        data = {
            'apply_id': apply_id,
            'status': 1,   #1 通过  2拒绝
            'csrf_token': self.csrf,
            'csrf': self.csrf
        }
        headers = {
            'Cookie': self.cookie,
            'Host': 'api.live.bilibili.com',
            'Origin': 'https://link.bilibili.com',
            'Referer': 'https://link.bilibili.com/p/center/index',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
        }
        re = requests.request('post', url, data=data, headers=headers,timeout=3).json()
        print(re)

    # 每日签到
    def doSign(self):
        url = 'https://api.live.bilibili.com/sign/doSign'
        headers = {
            'Cookie': self.cookie,
            'Host': 'api.live.bilibili.com',
            'Origin': 'https://link.bilibili.com',
            'Referer': 'https://link.bilibili.com/p/center/index',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
        }
        response = requests.request("get", url, headers=headers).json()
        print(response)

    # 进入房间
    def JoinRoom(self):
        url = 'https://api.live.bilibili.com/room/v1/Room/playUrl?cid=23058'
        headers = {
            'Cookie': self.cookie,
            'Host': 'api.live.bilibili.com',
            'Origin': 'https://live.bilibili.com',
            'Referer': f'https://live.bilibili.com/23058',
            'Referer': 'https://link.bilibili.com/p/center/index',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
        }
        response = requests.request('get', url, headers=headers).json()
        print(response)

    # Pc心跳
    def PcHearbeat(self):
        url = 'https://api.live.bilibili.com/User/userOnlineHeart'
        data = {
            'csrf_token': self.csrf,
            'csrf': self.csrf
        }
        headers = {
            'Cookie': self.cookie,
            'Host': 'api.live.bilibili.com',
            'Origin': 'https://live.bilibili.com',
            'Referer': f'https://live.bilibili.com/3',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
        }
        response = requests.request('post', url, headers=headers, data=data).json()
        print('Pc心跳', response)

    # App心跳
    def AppHearbeat(self):
        time = CurrentTime()
        temp_params = 'access_key=' + self.access_key + '&actionKey=appkey&appkey=1d8b6e7d45233436&build=520001' \
                                                        '&device=android&mobi_app=android&platform=android&ts=' + time
        sign = self.calc_sign(temp_params)
        url = 'https://api.live.bilibili.com/mobile/userOnlineHeart?' + \
              temp_params + '&sign=' + sign
        data = {'roomid': 23058, 'scale': 'xhdpi'}
        headers = {
            'User-Agent': 'bili-universal/6570 CFNetwork/894 Darwin/17.4.0',
            'Accept-encoding': 'gzip',
            'Buvid': '000ce0b9b9b4e342ad4f421bcae5e0ce',
            'Display-ID': '146771405-1521008435',
            'Accept-Language': 'zh-CN',
            'Accept': 'text/html,application/xhtml+xml,*/*;q=0.8',
            'Connection': 'keep-alive',
            'Host': 'api.live.bilibili.com',
            'cookie': self.sid,
        }
        response = requests.request('post', url, data=data, headers=headers).json()
        print('App心跳', response)

    # 一起跳
    def Pc_AppHearbeat(self):
        self.PcHearbeat()
        self.AppHearbeat()

    # 领取双端奖励
    def receive_award(self):
        url = 'https://api.live.bilibili.com/activity/v1/task/receive_award'
        data = {
            'task_id': 'double_watch_task',
            'csrf_token': self.csrf,
            'csrf': self.csrf
        }
        headers = {
            'Cookie': self.cookie,
            'Host': 'api.live.bilibili.com',
            'Origin': 'https://link.bilibili.com',
            'Referer': f'https://link.bilibili.com/p/center/index',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
        }
        response = requests.request('post', url, data=data, headers=headers,timeout=3).json()
        print('领取双端奖励:',response)
    #退出友爱社
    def quit(self):
        url = 'https://api.live.bilibili.com/activity/v1/UnionFans/quit'
        data = {
            'csrf_token': self.csrf,
            'csrf': self.csrf
        }
        headers = {
            'Cookie': self.cookie,
            'Host': 'api.live.bilibili.com',
            'Origin': 'https://link.bilibili.com',
            'Referer': f'https://link.bilibili.com/p/center/index',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
        }
        response = requests.request('post', url, data=data, headers=headers,timeout=3).json()
        print('退出友爱社:', response)
if __name__ == '__main__':
    Ck = ''
    Ck_function = Friendly_society(Ck)
    while True:
        Ck_function.PcHearbeat()
        time.sleep(300)
