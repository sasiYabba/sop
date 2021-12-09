 
 ​#!/usr/bin/python2 
 ​# coding=utf-8 
 ​# Coded By Yayan XD 
 ​# My Facebook ( https://www.facebook.com/KM39453 ) 
  
 ​#      (C) Copyright 407 Authentic Exploit 
 ​#      Rebuild Copyright Can't make u real programmer:) 
 ​#      Coded By Yayan XD. 
  
 ​import​ ​os 
 ​try​: 
 ​    ​import​ ​requests 
 ​except​ ​ImportError​: 
 ​    ​print​ ​'​\n​ [×] Modul requests belum terinstall!...​\n​' 
 ​    ​os​.​system​(​'pip2 install requests'​) 
  
 ​try​: 
 ​    ​import​ ​concurrent​.​futures 
 ​except​ ​ImportError​: 
 ​    ​print​ ​'​\n​ [×] Modul Futures belum terinstall!...​\n​' 
 ​    ​os​.​system​(​'pip2 install futures'​) 
  
 ​try​: 
 ​    ​import​ ​bs4 
 ​except​ ​ImportError​: 
 ​    ​print​ ​'​\n​ [×] Modul Bs4 belum terinstall!...​\n​' 
 ​    ​os​.​system​(​'pip2 install bs4'​) 
  
 ​import​ ​requests​, ​os​, ​re​, ​bs4​, ​sys​, ​json​, ​time​, ​random​, ​datetime 
 ​from​ ​concurrent​.​futures​ ​import​ ​ThreadPoolExecutor​ ​as​ ​YayanGanteng 
 ​from​ ​datetime​ ​import​ ​datetime 
 ​from​ ​bs4​ ​import​ ​BeautifulSoup 
 ​ct​ ​=​ ​datetime​.​now​() 
 ​n​ ​=​ ​ct​.​month 
 ​bulan​ ​=​ [​'Januari'​, ​'Februari'​, ​'Maret'​, ​'April'​, ​'Mei'​, ​'Juni'​, ​'Juli'​, ​'Agustus'​, ​'September'​, ​'Oktober'​, ​'November'​, ​'Desember'​] 
 ​try​: 
 ​    ​if​ ​n​ ​<​ ​0​ ​or​ ​n​ ​>​ ​12​: 
 ​        ​exit​() 
 ​    ​nTemp​ ​=​ ​n​ ​-​ ​1 
 ​except​ ​ValueError​: 
 ​    ​exit​() 
  
 ​current​ ​=​ ​datetime​.​now​() 
 ​ta​ ​=​ ​current​.​year 
 ​bu​ ​=​ ​current​.​month 
 ​ha​ ​=​ ​current​.​day 
 ​op​ ​=​ ​bulan​[​nTemp​] 
 ​reload​(​sys​) 
 ​sys​.​setdefaultencoding​(​'utf-8'​) 
 ​### WARNA RANDOM ### 
 ​P​ ​=​ ​'​\x1b​[1;97m'​ ​# PUTIH 
 ​M​ ​=​ ​'​\x1b​[1;91m'​ ​# MERAH 
 ​H​ ​=​ ​'​\x1b​[1;92m'​ ​# HIJAU 
 ​K​ ​=​ ​'​\x1b​[1;93m'​ ​# KUNING 
 ​B​ ​=​ ​'​\x1b​[1;94m'​ ​# BIRU 
 ​U​ ​=​ ​'​\x1b​[1;95m'​ ​# UNGU 
 ​O​ ​=​ ​'​\x1b​[1;96m'​ ​# BIRU MUDA 
 ​N​ ​=​ ​'​\x1b​[0m'​    ​# WARNA MATI 
 ​my_color​ ​=​ [ 
 ​ ​P​, ​M​, ​H​, ​K​, ​B​, ​U​, ​O​, ​N​] 
 ​warna​ ​=​ ​random​.​choice​(​my_color​) 
 ​#  Moch Yayan Juan Alvredo XD.  # 
 ​#-------------------------------> 
 ​koh​ ​=​ ​'100005395413800' 
 ​xi_jimpinx​ ​=​ ​'1714000985456399' 
 ​ok​, ​cp​, ​id​, ​loop​ ​=​ [], [], [], ​0 
 ​hoetank​ ​=​ ​random​.​choice​([​'Yang posting orang nya ganteng:)'​, ​'Lo ngentod:v'​, ​'Never surrentod tekentod kentod:v'​]) 
 ​bulan_ttl​ ​=​ {​"01"​: ​"Januari"​, ​"02"​: ​"Februari"​, ​"03"​: ​"Maret"​, ​"04"​: ​"April"​, ​"05"​: ​"Mei"​, ​"06"​: ​"Juni"​, ​"07"​: ​"Juli"​, ​"08"​: ​"Agustus"​, ​"09"​: ​"September"​, ​"10"​: ​"Oktober"​, ​"11"​: ​"November"​, ​"12"​: ​"Desember"​} 
  
 ​# lempankkkkkkkk 
 ​def​ ​jalan​(​z​): 
 ​    ​for​ ​e​ ​in​ ​z​ ​+​ ​'​\n​'​: 
 ​        ​sys​.​stdout​.​write​(​e​) 
 ​        ​sys​.​stdout​.​flush​() 
 ​        ​time​.​sleep​(​0.03​) 
  
 ​def​ ​tod​(): 
 ​    ​titik​ ​=​ [​'​\x1b​[1;92m.   '​, ​'​\x1b​[1;93m..  '​, ​'​\x1b​[1;96m... '​,​'​\x1b​[1;92m.   '​, ​'​\x1b​[1;93m..  '​, ​'​\x1b​[1;96m... '​] 
 ​    ​for​ ​x​ ​in​ ​titik​: 
 ​        ​print​ ​'​\r​ %s[%s+%s] menghapus token %s'​%​(​N​,​M​,​N​,​x​), 
 ​        ​sys​.​stdout​.​flush​() 
 ​        ​time​.​sleep​(​1​) 
  
 ​# LO KONTOL 
 ​logo​ ​=​ ​''' ​\033​[0;96m __  __        __  ______  ____
 
░██████╗░█████╗░░██████╗██╗
██╔════╝██╔══██╗██╔════╝██║
╚█████╗░███████║╚█████╗░██║
░╚═══██╗██╔══██║░╚═══██╗██║
██████╔╝██║░░██║██████╔╝██║
╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝