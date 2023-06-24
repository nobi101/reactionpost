import random
import requests, os, sys, threading
from time import sleep
from datetime import datetime
os.system('cls')
os.system('title TOOL REACTION POST')

def loading(dl):
   for x in range(dl , 0, -1):
    print(f'LOADING .',end='\r')
    sleep(0.8)
    print(f'LOADING ..',end='\r')
    sleep(0.8)
    print(f'LOADING ...',end='\r')
    sleep(0.8)
def hat_delay(dl):
   for x in range(int(dl) , 0, -1):
    print(f'[WAITING][|][x....][{x}]      ',end='\r')
    sleep(0.200)
    print(f'[WAITING][/][xX...][{x}]      ',end='\r')
    sleep(0.200)
    print(f'[WAITING][-][xxX..][{x}]      ',end='\r')
    sleep(0.200)
    print(f'[WAITING][\][xxxX.][{x}]      ',end='\r')
    sleep(0.200)
    print(f'[WAITING][|][xxxxx][{x}]      ',end='\r')
    sleep(0.200)
list_id = []
os.system('cls')
thanh()
cookie = input('Nhập Cookie: ')
thanh()
loading(2)
headers_check_live = {
    'authority': 'mbasic.facebook.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'origin': 'https://mbasic.facebook.com',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://mbasic.facebook.com/',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': cookie
}
try:
    find_data = requests.get("https://mbasic.facebook.com/", headers=headers_check_live).text
    fb_dtsg = find_data.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
    jazoest = find_data.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
except:
    thanh()
    print('KHÔNG GET ĐƯỢC THÔNG TIN - KIỂM TRA COOKIE')
    thanh()
    exit()
headers_id = {
    'cookie': cookie, 
}
data = {
    'fb_dtsg': fb_dtsg,
    'jazoest': jazoest,
    'variables': '{"showUpdatedLaunchpointRedesign":true,"useAdminedPagesForActingAccount":false,"useNewPagesYouManage":true}',
    'doc_id': '5300338636681652'
}
datapr = requests.post('https://www.facebook.com/api/graphql/', headers = headers_id, data = data).json()['data']['viewer']['actor']['profile_switcher_eligible_profiles']['nodes']
for o in datapr:
    uid_page = o['profile']['id']
    name_page = o['profile']['name']
    gomlist = f'{uid_page}|{name_page}'
    list_id.append(gomlist)
os.system('cls')
print(f'ĐÃ TÌM THẤY | '+ str(len(list_id)) + f' | PAGE')
thanh()
uid_post = input('VUI LÒNG NHẬP UID POST: ')
thanh()
loading(2)
link_post = f'https://www.facebook.com/{uid_post}'
dem = 0
amount = int(input('VUI LÒNG NHẬP SỐ LƯỢNG THẢ CẢM XÚC: '))
thanh()
delay_send_like = int(input('VUI LÒNG NHẬP DELAY THẢ CẢM XÚC: '))
list_random_reaction = ['1635855486666999', '1678524932434102', '613557422527858', '115940658764963', '478547315650144', '908563459236466', '444813342392137']
camxuc_can_buff = random.choice(list_random_reaction)
thanh()
print('')
loading(2)
def Sent_Reaction(x, cookie, link_post, uid_post):
    name = list_id[x].split('|')[1].upper()
    time = datetime.now().strftime("%H:%M:%S")
    uid_page = list_id[x].split('|')[0]
    list1 = (f'i_user={uid_page};')
    cookie9 = (f'{cookie}{list1}')
    head = {
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'vi',
            'cookie': cookie9,
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'viewport-width': '1366',
    }
    url = requests.get('https://www.facebook.com/'+uid_post, headers=head).url
    dataurl = requests.get(url, headers=head).text
    feed = dataurl.split('{"__typename":"CommentComposerLiveTypingBroadcastPlugin","feedback_id":"')[1].split('","')[0]
    headers_sent_ = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-length': '1971',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': cookie9,
        'origin': 'https://www.facebook.com',
        'referer': link_post,
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 ',
        'viewport-width': '917',
        'x-fb-friendly-name': 'CometUFIFeedbackReactMutation',
        'x-fb-lsd': 'qKMhU6_CR-RCDufzv-6t0H',
    }
    data_sent_ = {
        'fb_dtsg': fb_dtsg,
        'jazoest': jazoest,
        'lsd': 'qKMhU6_CR-RCDufzv-6t0H',
        '__aaid': '891806128653375',
        '__spin_r': '1006793176',
        '__spin_b': 'trunk',
        '__spin_t': '1672999475',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'CometUFIFeedbackReactMutation',
        'variables': '{"input":{"attribution_id_v2":"CometSinglePostRoot.react,comet.post.single,via_cold_start,1672999477085,30003,,","feedback_id":"'+feed+'","feedback_reaction_id":"'+ str(camxuc_can_buff) + '","feedback_source":"OBJECT","is_tracking_encrypted":true,"tracking":["AZWSQEESA1Ys6e9kswLNKqYWc0_ssxcQRJuuNBAX7xyuKjDFds_KNu2SuYSPwODMzCnpiThRlBy6FuqQWDdLKvbiY8qs-IF6Qv_C7Ly-tmBLqJAx2rZadB5fLX54jzkNlp7-YED61F6MN7crd1ibw9eh5wk8KfdrfExSnrViN4UGQbqoEZwYP4OVHaWhJ0YIEcFidONkgc6aZ8LoodmsqfvXs0frwYIx1344U4RURZKDjGHPZzjyi1Nq0LWCcjkpNdN4PSW0LfNGucZUsENIxtUQeL86_iTviLcuc5uas079Mx8nFz88HODYGppyfIhHU0FuPSEBROHHe4WrYdMMFbQ4MT6Q0hyjWkBrS4cICmGLRw"],"session_id":"pfbid02RTVv1VJxifdwi1PBXxDAhwbfmPmKXvtt458QY8vLP5ossRUj9bopBqz1YrAi4ge8l","actor_id":"'+ uid_page +'","client_mutation_id":"2"},"useDefaultActor":false,"scale":1}',
        'server_timestamps': 'true',
        'doc_id': '5703418209680126',
    }
    response = requests.post('https://www.facebook.com/api/graphql/', headers=headers_sent_, data=data_sent_).text
    print(f'[{dem}] -> {time} -> REACTION TO -> {uid_post} -> PRO5 -> {uid_page} -> {name} -> SUCCESS')
def huhu():
    hat_delay(delay_send_like)
threading.Thread(target=huhu).start()
for x in range(amount):
    camxuc_can_buff = camxuc_can_buff = random.choice(list_random_reaction)
    dem=dem+1
    threading.Thread(target=Sent_Reaction, args=(x, cookie, link_post, uid_post)).start()
    sleep(20)

input(f'Success {amount} Reaction - Enter Để Exit Tool')

