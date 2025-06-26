import codex
import main
from colorama import init, Fore
init(autoreset=True)
while True:
 x=input(Fore.GREEN  +">")
 if x=="help":
    print( Fore.GREEN  + "#" * 90)
    print(Fore.GREEN  +"the comend:")
    print(Fore.GREEN  +"file_eye:",Fore.GREEN  +"monitor file size")
    print(Fore.GREEN  +"B:",Fore.GREEN  +"watching the battery")
    print(Fore.GREEN  +"ip")
    print(Fore.GREEN  +"port")
    print(Fore.GREEN  +"core:",Fore.GREEN  +"the core cpue")
    print(Fore.GREEN  +"f_d:",Fore.GREEN  +"watching the aded and deleted")
    print(Fore.GREEN  +"remove")
    print(Fore.GREEN  +"net")
    print(Fore.GREEN  +"gui:",Fore.GREEN  +"woidos gui ")
    print(Fore.GREEN  +"xor")
    print(Fore.GREEN  +"disk:",Fore.GREEN  +"this comend is informetion is disk and momr rtorg")
    print(Fore.GREEN  +"remov-folder:",Fore.GREEN  +"this comend is remove folder")
    print(Fore.GREEN  +"ram:",Fore.GREEN  +"information ram")
    print(Fore.GREEN  +"C:",Fore.GREEN  +"information camer  is open or close")
    print(Fore.GREEN  +"make:",Fore.GREEN  +"make new file ")
    print(Fore.GREEN  +"s_d:",Fore.GREEN  +"this comend is shutdown pc ")
    print(Fore.GREEN  + "#" * 90)
 elif x=="file_eye":
     y=input(Fore.GREEN  +"enter file:")
     codex.main2(y)
 elif x=="B":
     codex.battery()
 elif x=="ip":
    codex.get_ip()
 elif x=="port":
    codex.get_port()
 elif x=="core":
    codex.core_cpu()
 elif x=="f_d":
    folder=input(Fore.GREEN  +"enter the folder:")
    codex.mainf(folder)
 elif x=="remove":
    filepathe=input(Fore.GREEN  +"enter the file dleta:")
    codex.delet_file(filepathe)
 elif x=="net":
    codex.network_scan()
 elif x=="gui":
    print(Fore.GREEN  +"the windos gui")
    main.gui()
 elif x=="xor":
    try:
     path_file=input(Fore.GREEN  +"enter the file crpto:")
     key=input(Fore.GREEN  +"enter the key:")
     codex.crpto(path_file,int(key))
    except:
      print(Fore.RED+"erore44")
 elif x=="disk":
   codex.disk()
 elif x=="remov-folder":
   c=input(Fore.GREEN  +"enter the path folder:")
   codex.folder_r(c)
 elif x=="ram":
    codex.momory()
 elif x=="C":
    codex.camera()
 elif x=="make":
    name1=input("enter the name file:")
    p=input("enter the content file:")
    codex.make(name1,p)
 elif x=="s_d":
    codex.s_d()
 else:
    print(Fore.RED +f"erore comend:{x}")