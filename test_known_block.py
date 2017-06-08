import lxml.html as lh
import urllib2
import re
from datetime import datetime, date, time
import time
import hashlib, struct, binascii,string,locale,os,math
import calendar
import subprocess
import numpy
import win32api,win32process,win32con
from termcolor import colored

def text_tail(node):
    yield node.text
    yield node.tail






blurb=''
block=468650
money10=[0]*1024
money9=[0]*512
money8=[0]*216

pred_int_7=0
dot_int_7=0
dot4_int_7=0
dot5_int_7=0


pred_int_9=0
dot_int_9=0
dot4_int_9=0
dot5_int_9=0


pred_int_7dnf=0
dot_int_7dnf=0
dot4_int_7dnf=0



pid = win32api.GetCurrentProcessId()
handle = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, True, pid)
win32process.SetPriorityClass(handle, win32process.HIGH_PRIORITY_CLASS)




sha256_=numpy.zeros((1024,513,290), int)
6
while block<468659:
 K=0
 url='http://blockchain.info/block-height/'+str(block)
 doc=lh.parse(urllib2.urlopen(url))
 for elt in doc.iter('td'):
    text=elt.text_content()
    if text.startswith('Nonce'):
        blurb=[text for node in elt.itersiblings('td')
               for subnode in node.iter()
               for text in text_tail(subnode) if text and text!=u'\xa0']
        break
 #print(re.sub(r'\s', '', '\n'.join(blurb)) )

 nonce=int(math.sqrt(math.sqrt(int(re.sub(r'\s', '', '\n'.join(blurb))))))
 print "____________"+str(nonce)+"////////////"
 for elt in doc.iter('td'):
    text=elt.text_content()
    if text.startswith('Merkle Root'):
        blurb=[text for node in elt.itersiblings('td')
               for subnode in node.iter()
               for text in text_tail(subnode) if text and text!=u'\xa0']
        break
 #print(re.sub(r'\s', '', '\n'.join(blurb)) )
 mrkl_root=re.sub(r'\s', '', '\n'.join(blurb))


 for elt in doc.iter('td'):
    text=elt.text_content()
    if text.startswith('Version'):
        blurb=[text for node in elt.itersiblings('td')
               for subnode in node.iter()
               for text in text_tail(subnode) if text and text!=u'\xa0']
        break
 #print(re.sub(r'\s', '', '\n'.join(blurb)) )
 ver=int(re.sub(r'\s', '', '\n'.join(blurb)),16)




 for elt in doc.iter('td'):
    text=elt.text_content()
    if text.startswith('Previous Block'):
        blurb=[text for node in elt.itersiblings('td')
               for subnode in node.iter()
               for text in text_tail(subnode) if text and text!=u'\xa0']
        break
 #print(re.sub(r'\s', '', '\n'.join(blurb)) )
 prev_block=re.sub(r'\s', '', '\n'.join(blurb)) 


 for elt in doc.iter('td'):
    text=elt.text_content()
    if text.startswith('Bits'):
        blurb=[text for node in elt.itersiblings('td')
               for subnode in node.iter()
               for text in text_tail(subnode) if text and text!=u'\xa0']
        break
 #print(hex(int(re.sub(r'\s', '', '\n'.join(blurb)))) )
 bits=int(hex(int(re.sub(r'\s', '', '\n'.join(blurb)))),16)


 for elt in doc.iter('td'):
    text=elt.text_content()
    if text.startswith('Time'):
        blurb=[text for node in elt.itersiblings('td')
               for subnode in node.iter()
               for text in text_tail(subnode) if text and text!=u'\xa0']
        break

 dt = datetime.strptime(re.sub(r'\s+', '', '\n'.join(blurb)), "%Y-%m-%d%H:%M:%S")



 mystr=""
 mystr+=hex(dt.year)
 mystr+=hex(dt.month)
 mystr+=hex(dt.day)
 mystr+=hex(dt.hour)
 mystr+=hex(dt.minute)
 mystr+=hex(dt.second)
 #print(dt.year)
 #print(dt.month)
 #print(dt.day)
 #print(dt.hour)
 #print(dt.minute)
 #print(dt.second)

 #print (int(calendar.timegm( dt.timetuple() ))  )
 time_=int(hex(int(calendar.timegm( dt.timetuple() )) ),16)





 pred="100000000000000002335a000000000000000000000000000000000000000000"
 
 #ver = 0x20000000
 #prev_block = "0000000000000000008f54187a143257be7a6fd31ba0ef1d60e07f11cd7d3b4e"
 #mrkl_root = "8f86ede7afc61a2e6d17cf9733e01467f743a51def8b949963a1fc247d11ca0f"
 #time_ = 0x5903C5B8 # 2014-02-20 04:57:25
 #bits = 0x18021B3E  
 bin_nonce=0
 # https://en.bitcoin.it/wiki/Difficulty
 exp = bits >> 24
 mant = bits & 0xffffff
 target_hexstr = '%064x' % (mant * (1<<(8*(exp - 3))))
 target_str = target_hexstr.decode('hex')

 nonce_1=0
 find=0
 while nonce_1<255:
 
  strb= struct.pack("<L", ver).encode('hex')+prev_block+mrkl_root+struct.pack("<LLL", time_, bits, nonce_1*nonce_1*nonce_1*nonce_1).encode('hex')

  header = ( struct.pack("<L", ver) + prev_block.decode('hex')[::-1] +
          mrkl_root.decode('hex')[::-1] + struct.pack("<LLL", time_, bits, nonce_1*nonce_1*nonce_1*nonce_1))





  strb= struct.pack("<L", ver).encode('hex')+prev_block+struct.pack("<LLL", time_, bits, nonce_1*nonce_1*nonce_1*nonce_1).encode('hex')

  header = ( struct.pack("<L", ver) + prev_block.decode('hex')[::-1] + struct.pack("<LLL", time_, bits, nonce_1*nonce_1*nonce_1*nonce_1))
                  
  #  bin_nonce=header.decode('hex');
          
  #  print bin(str(prev_block)+str(mrkl_root));
          
  hash = hashlib.sha256(hashlib.sha256(header).digest()).digest()
  strhash=hash[::-1].encode('hex')

  
 
# os.nice(20)
 #str= struct.pack("<LLL", time_, bits, 0).encode('hex')+mrkl_root+prev_block+ struct.pack("<L", ver).encode('hex')
 
 
 
  bin = ['0000','0001','0010','0011',
         '0100','0101','0110','0111',
         '1000','1001','1010','1011',
         '1100','1101','1110','1111']
  aa = ''
  bb = ''
  for i in range(len(strhash)):
   aa += bin[string.atoi(strhash[i],base=16)]

  for i in range(len(strb)):
   bb += bin[string.atoi(strb[i],base=16)] 



 
 #print aa 

 # print "------------------------------------" yes
 # print "nonce: "+str(nonce) yes


  strnonce=str(nonce)


  int_aa=int(math.sqrt(math.sqrt(math.sqrt(math.sqrt( int(aa,2) )))))
#  print int_aa yes

  aa10="10 "+aa+"\n"
  aa9="9 "+aa+"\n"
  aa8="7 "+aa+"\n"

  bb10="10 "+bb+"\n"
  bb9="9 "+bb+"\n"
  bb8="7 "+bb+"\n"
  


 
  int_9=0
  int_dnf9=0
  int_9b=0
  int_dnf9b=0


#--------------9-----------------------------------------------
#  text_file = open("C:\\bitcoin\\46planes_v9.txt", "w")

#  text_file.write(aa9)
# block=block+1
#  print block yes

 # text_file.close()



 # process = subprocess.Popen(['DNF.exe', ''], stdout=subprocess.PIPE)
 # out, err = process.communicate()

 # dnf=re.sub(r'\s', '', '\n'.join(out))
 #print(dnf)
 #print(dnf[1:10])
 # int_dnf9=int(dnf[1:10],2)

 # int_9=int(dnf[10:13])
  #if (int_dnf8==int_8):
  # print("plane9=" +str(int_9))  
   #print("dnf9="+str(int_dnf9)) 
 #if (int_dnf9>=256):
 # money9[int_9]=nonce
 # print "nonce_1::::"+str(nonce_1) 
#------------------9---------------------------





  #--------------9bb-----------------------------------------------
 # text_file = open("C:\\bitcoin\\46planes_v9.txt", "w")

#  text_file.write(bb9)
# block=block+1
 # print block yes

  #text_file.close()



 # process = subprocess.Popen(['DNF.exe', ''], stdout=subprocess.PIPE)
 # out, err = process.communicate()

 # dnf=re.sub(r'\s', '', '\n'.join(out))
 #print(dnf)
 #print(dnf[1:10])
 # int_dnf9b=int(dnf[1:10],2)

 # int_9b=int(dnf[10:13])
  #if (int_dnf8==int_8):
  # print("plane9_bb=" +str(int_9b)) 
  # print("dnf9_bb="+str(int_dnf9b)) 
 #if (int_dnf9>=256):
 # money9[int_9]=nonce
 # print "nonce_1::::"+str(nonce_1)
#------------------9bb---------------------------




#--------------8bb-----------------------------------------------
  text_file = open("C:\\bitcoin\\46planes_v9.txt", "w")

  text_file.write(bb8)
# block=block+1
 # print block yes

  text_file.close()



  process = subprocess.Popen(['DNF.exe', ''], stdout=subprocess.PIPE)
  out, err = process.communicate()

  dnf=re.sub(r'\s', '', '\n'.join(out))
 #print(dnf)
 #print(dnf[1:10])
  int_dnf8b=int(dnf[1:8],2)

  int_8b=int(dnf[8:11])
  #if (int_dnf8==int_8):
   #print("plane7_bb=" +str(int_8b)) 
   #print("dnf7_bb="+str(int_dnf8b)) 
 #if (int_dnf9>=256):
#------------------8bb---------------------------









  



 #if sha256_[int_dnf10-1][int_dnf9-1][int_9-1]>0:
 # if sha256_[int_dnf10-1][int_dnf9-1][int_9-1]<>nonce:
 #   wrong=1   
 #   print("!!!!!!!!!! wrong value: "+str(nonce)+" nessesary: "+str(sha256_[int_dnf10-1][int_dnf9-1][int_9-1])+"maybe use"+str(int_10))
 # else:
 #   print("ok!!!!!!!!"+str(nonce)+"---"+str(sha256_[int_dnf10-1][int_dnf9-1][int_9-1]))
        
 #sha256_[int_dnf10-1][int_dnf9-1][int_9-1]=nonce








#--------------7-----------------------------------------------


 #if ((int_dnf9<=int_9) & (int_dnf10<=int_10)):  
  text_file = open("C:\\bitcoin\\46planes_v9.txt", "w")

  text_file.write(aa8)
 #
 # print block yes

  text_file.close()



  process = subprocess.Popen(['DNF.exe', ''], stdout=subprocess.PIPE)
  out, err = process.communicate()

  dnf=re.sub(r'\s', '', '\n'.join(out))
 # print(dnf) yes
 # print(dnf[1:8]) yes
  int_dnf8=int(dnf[1:8],2)

  int_8=int(dnf[8:11])
  #if (int_dnf8==int_8):
  # print("DNF7="+ str(int_dnf8)) 
  # print("plane7="+str(int_8)) 


#  if ((int_dnf8>int_8) & (int_dnf9<=int_9) & (int_dnf10<=int_10)):
#    money8[int_dnf8]=nonce
#------------------7---------------------------



#-------------10----------------------------------------

  int_dnf10=0
  int_10=0
#  if ( abs(int_8*2-int_9)<4 ) or (abs(int_dnf8*4-int_dnf9)<10):
 # if( abs(int_9-int_9b)<34 ):
 # if (1==1):
  if (abs(int_dnf8-int_8)<2):
 # if ( (int_8==dot_int_7) or (abs(int_8-dot4_int_7)<5) or (abs(int_8-pred_int_7)<4) or (abs(int_8-dot5_int_7)<4) ) and ((abs(int_9-dot5_int_9)<4) or (abs(int_9-pred_int_9)<2) or ((abs(int_9-dot_int_9)<2)) or (abs(int_9-dot4_int_9)<4) ):
   text_file = open("C:\\bitcoin\\46planes_v9.txt", "w")

   text_file.write(aa10)
## block=block+1
  # print block yes

   text_file.close()



   process = subprocess.Popen(['DNF.exe', ''], stdout=subprocess.PIPE)
   out, err = process.communicate()

   dnf=re.sub(r'\s', '', '\n'.join(out))
 ##print(dnf)
 ##print(dnf[2:12])
   int_dnf10=int(dnf[2:12],2)

   int_10=int(dnf[12:15])

   wrong=0
 ##if int_dnf10>=int_10:
   if (abs(int_dnf8-int_8)<2):
    print("dnf10=" +str(int_dnf10)) 
    print("plane10="+str(int_10))
    print("plane9_bb=" +str(int_9b)) 
    print("dnf9_bb="+str(int_dnf9b))
    print("plane7_bb=" +str(int_8b)) 
    print("dnf7_bb="+str(int_dnf8b))
    print("plane7=" +str(int_8)) 
    print("dnf7="+str(int_dnf8))
 ##if money10[int_dnf10]>0:
 # #if money10[int_dnf10]<>nonce:
  ##  wrong=1   
   ## print("!!!!!!!!!! wrong value: "+str(nonce)+" nessesary: "+str(money10[int_dnf10])+"maybe use"+str(int_10))
 ## else:
  ##  print("ok!!!!!!!!"+str(nonce)+"---"+str(money10[int_dnf10]))
        
 ##money10[int_dnf10]=nonce

#-------------10---------------------------------------------




 #-------------10bb----------------------------------------

#  if ( abs(int_8*2-int_9)<4 ) or (abs(int_dnf8*4-int_dnf9)<10):
   text_file = open("C:\\bitcoin\\46planes_v9.txt", "w")

   text_file.write(bb10)
## block=block+1
 #  print block yes

   text_file.close()



   process = subprocess.Popen(['DNF.exe', ''], stdout=subprocess.PIPE)
   out, err = process.communicate()

   dnf=re.sub(r'\s', '', '\n'.join(out))
 ##print(dnf)
 ##print(dnf[2:12])
   int_dnf10b=int(dnf[2:12],2)

   int_10b=int(dnf[12:15])

   wrong=0
 ##if int_dnf10>=int_10:
   if abs(int_dnf8-int_8)<2:
    print("DNFbb10=" +str(int_dnf10b)) 
    print("Planebb10="+str(int_10b))
    print("NONCE"+str(nonce_1))
 ##if money10[int_dnf10]>0:
 # #if money10[int_dnf10]<>nonce:
  ##  wrong=1   
   ## print("!!!!!!!!!! wrong value: "+str(nonce)+" nessesary: "+str(money10[int_dnf10])+"maybe use"+str(int_10))
 ## else:
  ##  print("ok!!!!!!!!"+str(nonce)+"---"+str(money10[int_dnf10]))
        
 ##money10[int_dnf10]=nonce

#-------------10bb---------------------------------------------




  if (abs(int_dnf8-int_8)<2):
      if (((int_10b+nonce_1)/2)-6<=nonce<=((int_10b+nonce_1)/2)+6):
        K=K+1
      if (int_9b-6<=nonce<=int_9b+6):
        K=K+1
      if (int_dnf10b-6<=nonce<=int_dnf10b+6):
        K=K+1
      if (int_dnf10+int_9b-6<=nonce<=int_dnf10+int_9b+6):
        K=K+1
      if (int_10b+int_9b-6<=nonce<=int_10b+int_9b+6):
        K=K+1

      if (int_10-6<=nonce<=int_10+6):
        K=K+1
        

        
      print "THIS IS MAYBE EXIT"

  #print "------------------------------------" 
  
 # if ( abs(int_9-int_9b)<34 ) and ( abs(int_9-int_10)<2 ):
  if ( (int_8==dot_int_7) or (abs(int_8-dot4_int_7)<5) or (abs(int_8-pred_int_7)<4) or (abs(int_8-dot5_int_7)<4) ) and ((abs(int_9-dot5_int_9)<4) or (abs(int_9-pred_int_9)<2) or ((abs(int_9-dot_int_9)<2)) or (abs(int_9-dot4_int_9)<4) ):
      if (abs(int_9-int_10)<2):
       #  K=K+1
         print nonce_1
         if (nonce_1-4<=nonce<=nonce_1+4):
          find=1   
          print colored('BLOCK', 'red')


  if (nonce_1-4>0):
    dot5_int_7=dot4_int_7
    dot5_int_9=dot4_int_9
          
  if (nonce_1-3>0):
    dot4_int_7=dot_int_7
    dot4_int_9=dot_int_9 
  if (nonce_1-2>0):
    dot_int_7=pred_int_7
    dot_int_9=pred_int_9
  if (nonce-1>0):  
    pred_int_7=int_8
    pred_int_9=int_9

#   print dot4_int_7
#  print dot_int_7
#  print pred_int_7
    
  nonce_1=nonce_1+1 

 block=block+1
 print K
 if K==0:
     print "BAD!!!!!!!!!!!!"




 

 

     
 












