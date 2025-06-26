import os
import time
import threading
from tkinter import messagebox , Tk
import socket
import  psutil
import keyboard
import subprocess
import platform
import requests
from colorama import init, Fore
import cv2
import fastapi
###########--operation function--########################################
################--log--################################################## 
def log(mass):
   print(Fore.GREEN  + mass)
   with open("main_data.txt","a",encoding='utf-8') as file_log:
      file_log.write(mass + '\n')
################--file--################################################## 
def file(folder):
    sleep=3
    v=os.listdir(folder)
    file_arry={}
    for f1 in v: 
        path=os.path.join(folder,f1)
        if os.path.isfile(path):
         size=os.path.getsize(path)
         file_arry[f1]=size 
    time.sleep(sleep) 
    for x in file_arry:
       path=os.path.join(folder,x)
       size_new=os.path.getsize(path)
       size_olde_kb=file_arry[x]/1024
       size_new_kb=size_new/1024 
       if file_arry[x] != size_new:
            log(f"🟥 the file has been modified [ {x} - new size: {size_new_kb:.2f} KB 📂 ]")
            gui_text_Boex(x)
       else:
          log(f"✅ the file is clear [ {x} - size: {size_olde_kb:.2f} KB 📂 ]")
################--filedel--################################################## 
def filedel(folder):
   sleep=3
   b1=set(os.listdir(folder))
   time.sleep(sleep)
   b2=set(os.listdir(folder))
   remove=b1-b2
   add=b2-b1
   if add:
      for f1 in add:
       log(Fore.RED+f"🟥 File added:{os.path.join(folder,f1)}")
       gui_text_Boex_add(f1)
       
   if  remove:
      for f2 in remove:
         log(Fore.RED+f"🟥 File remove:{os.path.join(folder,f2)}")
         gui_text_Boex_remove(f2)

   if not add and not  remove:
      log(f"✅ Folder is unchanged: {folder} ")    
   b1=b2
################--massg box--##################################################  
def gui_text_Boex(file):
   op=Tk()
   op.withdraw()
   messagebox.showinfo("File Modified", f"The file '{file}' has been modified!")
   op.destroy()
################--massg box--################################################## 
def gui_text_Boex_add(file):
   op=Tk()
   op.withdraw()
   messagebox.showinfo("haker",f"the file add {file}!")
   op.destroy()
################--massg box--################################################## 
def gui_text_Boex_remove(file):
   op=Tk()
   op.withdraw()
   messagebox.showinfo("haker",f"the file remove {file}!")
   op.destroy()
################--get_ip--##################################################  
def get_ip():
   h1=socket.gethostname()
   h2_ip=socket.gethostbyname(h1)
   if h2_ip:
      log(f"✅ the ip pc is:{h2_ip}")
   else:
      log(Fore.RED+"🟥 erore 44")
   return h2_ip
################--get_port--##################################################
def get_port():
   net=psutil.net_connections()
   open_port=set()
   for i in net:
      if i.status =='LISTEN':
         ipx = i.laddr.ip
         port = i.laddr.port
         name=i.pid
         app= psutil.Process(name).name()
         open_port.add(f"{ipx}:{app}:{port}")
   log(f"Number of open ports: {len(open_port)}") 
   log("Open ports:")
   log("ip:port")
   for addr in sorted(open_port):
      ip, prog, port = addr.rsplit(":", 2)  
      log(f"{ip:<15} -> {port:<5} ({prog})")
   return len(open_port), open_port
################--core cpu--##################################################  
def core_cpu():
   log("consume the core")
   core=psutil.cpu_count(logical=False)
   corex=psutil.cpu_count(logical=True)
   using=psutil.cpu_percent(interval=1,percpu=True)
   for i in using:
      log(f"✅  :  {i}%")
   log(f"mutch the core {corex}")
#############--delet_file---##########################################
def delet_file(pathx):
   os.remove(pathx)
###########--battery--######################################################
def battery():
    battery = psutil.sensors_battery()
    if battery is None:
        log("🔌 no buttry")
    else:
        percent = battery.percent
        plugged = battery.power_plugged
        status = "🔌 conect charg"if plugged else "🔋 in conect charg"
        log(f"🔋 namber of charg: {percent}% - {status}")
##############-- xor ---#############################################
def xor(input,key):
   return ''.join(chr(ord(char) ^ key) for char in input)
#############--crpto--###############################################
def crpto(path,key):
   fil=os.listdir(path)
   for x in fil:
      full= os.path.join(path, x) 
      log(x)
      if os.path.isfile(full)and not x.endswith(".py"):
       with open(full,"r") as f:
          read1=f.read()
          v=xor(read1,key)
       with open(f"{full}x","w", encoding="utf-8") as xorf:
            xorf.write(v)
       os.remove(full)
#############--disk--################################################
def disk():
   using=psutil.disk_partitions()
   log("🔍 Disk Information:")
   for x in using:
      try:
       usd = psutil.disk_usage(x.mountpoint)
       log(f"📁 Device: {x.device}")
       log(f"📂 Mount Point: {x.mountpoint}")
       log(f"📂 momrey usd {usd.used /(1024**3):2f}GB")
       log(f"📂 momory total {usd.total/(1024**3):2f}")
       log("-" * 30)
      except Exception as e:
            log(f"⚠️ Skipping {x.device} ({x.mountpoint}) - {e}")
#############--folderrmove--#########################################
def folder_r(path):
     fil=os.listdir(path)
     for x in fil:
      full= os.path.join(path, x) 
      log(x)
      if os.path.isfile(full):
       os.remove(full)
     os.rmdir(path)
#############--momory--###############################################
def momory():
   mem=psutil.virtual_memory()
   total=mem.total /(1024**3)
   free=mem.available /(1024**3)
   use=mem.used/(1024**3)
   parsnt=mem.percent
   log(f"==RAM information==")
   log(f"✅ total momory RAM {total:.2f}GB")
   log(f"✅ used momory RAM {use:.2f}GB")
   log(f"✅ free momory RAM {free:.2f}GB")
   log(f"✅ p.c. {parsnt}%")
#############--network_scan--#########################################
def network_scan():
   pass   
####################--cmera--###########################################
def camera():
   cap=cv2.VideoCapture(0)
   if cap is None or not cap.isOpened():
      log("🟥 the camer is open")
   else:
      log("✅ not used a camera")
##############--i--################################################
def i():
   cap=cv2.VideoCapture(0)
   while True:
      ret,free=cap.read()
      if not ret:
         break
      cv2.imshow('camera',free)
################--make--##############################################
def make(name,ma):
   with open(name,"w") as file:
      file.write(ma)
###############--s_d--####################################################
def s_d():
   os.system("shutdown /s /f /t 0")
##############---main function--########################################
def main1(folder):
   try:
    while (True):
      log("ctrl+c stpe this porgrem")
      log("###############################################")
      t1=threading.Thread(target=file, args=(folder,))
      t2=threading.Thread(target=filedel, args=(folder,))
      t1.start()
      t2.start()
      t1.join()
      t2.join()
   except KeyboardInterrupt:
      log("Program stopped by user with Ctrl+C")
def main2(folder):
    try:
     while (True):
      log("ctrl+c stpe this porgrem")
      log("###############################################")
      file(folder)
      filedel(folder)
    except KeyboardInterrupt:
        log("Program stopped by user with Ctrl+C")

def mainf(folder):
    try:
     while (True):
      log("ctrl+c stpe this porgrem")
      log("###############################################")
      filedel(folder)
    except KeyboardInterrupt:
        log("Program stopped by user with Ctrl+C")
