import psutil
import platform
import colorama
from time import sleep
from datetime import datetime
import cpuinfo
colorama.init()

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

