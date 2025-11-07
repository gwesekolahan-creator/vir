import requests,json,os,sys,random,datetime,time,re,subprocess,shutil
kasihku = sys.prefix
aku_versi = f'{sys.version_info.major}.{sys.version_info.minor}'
out_path = f'{kasihku}/lib/python{aku_versi}/pwku.so'
src_path = 'firzah/pwku.cpp'
def compile_pwku():
    import subprocess, sysconfig
    if not os.path.exists(src_path):
        sys.exit('[!] pwku.cpp tidak ditemukan')
    compiler = shutil.which('g++') or shutil.which('clang++')
    if compiler is None:
        sys.exit('[!] g++/clang++ tidak ditemukan')
    inc = os.path.join(kasihku, 'include', f'python{aku_versi}')
    if not os.path.isdir(inc):
        inc = sysconfig.get_path('include')
    cmd = [
        compiler,
        '-x', 'c++',
        '-shared', '-fPIC',
        f'-I{inc}',
        src_path,
        f'-L{kasihku}/lib',
        f'-lpython{aku_versi}',
        '-o', out_path
    ]

    print('[*] Meng-compile pwku.cpp ...')
    if subprocess.call(cmd) != 0:
        sys.exit('[!] Gagal compile pwku.cpp')

    print('[✓] Compile berhasil!')

if os.path.exists(out_path):
    os.system('python rumah.py')
else:
    compile_pwku()
    os.system('python rumah.py')