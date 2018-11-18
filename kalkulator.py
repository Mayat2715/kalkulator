# boleh liat" asal jangan di recode
# untuk pembelajaran
import sys
def buka():
    print "\n"*100
    print '''
\033[1;32m
 _         _ _          _       _
| | ____ _| | | ___   _| | __ _| |_ ___  _ __
| |/ / _` | | |/ / | | | |/ _` | __/ _ \| '__|
\033[1;34m|   < (_| | |   <| |_| | | (_| | || (_) | |
|_|\_\__,_|_|_|\_\.__,_|_|\__,_|\__\___/|_|
\033[0;1m____________________________________
\033[0;1m[\033[1;36m#\033[0;1m]\033[1;33mpertambahan
itung tambah <nomor1> <nomor2>
contoh: itung tambah 6 4
\033[0;1m____________________________________
\033[0;1m[\033[1;36m#\033[0;1m]\033[1;33mpengurangan
itung kurang <nomor1> <nomor2>
contoh: itung kurang 6 4
\033[0;1m____________________________________
\033[0;1m[\033[1;36m#\033[0;1m]\033[1;33mperkalian
itung kali <nomor1> <nomor2>
contoh: itung kali 6 4
\033[0;1m____________________________________
\033[0;1m[\033[1;36m#\033[0;1m]\033[1;33mpembagian
itung bagi <nomor1> <nomor2>
contoh: itung bagi 6 4
\033[0;1m____________________________________
\033[0;1m[\033[1;36m#\033[0;1m]\033[1;33mperpangkatan
itung pangkat <pangkat> <nomor>
contoh: itung pangkat 2 5
        itung pangkat 3 5
\033[0;1m____________________________________'''

def tambah(a,b):
    c = a+b
    return c
def kurang(a,b):
    c = a-b
    return c
def kali(a,b):
    c = a*b
    return c
def bagi(a,b):
    c = a/b
    return c
def pangkat(a,b):
    c = a**b
    return c
def fuck():
    if z == "tambah":
        d = "+"
        print a,d,b,"=",tambah(a,b)
    elif z == "kurang":
        d = "-"
        print a,d,b,"=",kurang(a,b)
    elif z == "bagi":
        d = ":"
        print a,d,b,"=",bagi(a,b)
    elif z == "kali":
        d = "x"
        print a,d,b,"=",kali(a,b)
    elif z == "pangkat":
        d = "^"
        print "%d%s%d ="%(a,d,b),pangkat(a,b)
try:
    a = int(sys.argv[2])
    b = int(sys.argv[3])
    z = sys.argv[1]
    fuck()
except ValueError:
    a = float(sys.argv[2])
    b = float(sys.argv[3])
    z = sys.argv[1]
    fuck()
except IndexError:
    buka()
