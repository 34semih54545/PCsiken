Bu toolu çalıştırmak için pythın,git ve coloramanın yüklü olması gerekir.

cmd,powershell vb. termianllerde kurmak için de kurmak için:
```
curl -o python-installer.exe https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe
python-installer.exe /quiet InstallAllUsers=1 PrependPath=1
curl -o git-installer.exe https://github.com/git-for-windows/git/releases/download/v2.41.0.windows.1/Git-2.41.0-64-bit.exe
git-installer.exe /quiet InstallAllUsers=1 PrependPath=1
pip install colorama
git clone https://www.https://github.com/34semih54545/PCsiken
cd PCsiken
python PCsiken.py
```
termux vb. terminallerde kurmak için:
```
pkg update
pkg install python
pkg install git
pip install colorama
git clone https://github.com/34semih54545/PCsiken
cd PCsiken
python PCsiken.py
```

Dilerseniz komutları tek tek satır olarka yapıştırabilirsiniz. Dilerseniz ise hepsini tek parça oalrak yapıştıabilrisiniz terminale.
Eğer colorama,Python ve git zaten yüklüyse bütün terminallerde sadece şu kodu girerek çalıştırabilirsiniz:
```
git clone https://github.com/34semih54545/PCsiken
cd PCsiken
python PCsiken.py
```
