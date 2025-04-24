import hashlib

def crack_hash(hash_to_crack, wordlist, hash_type="md5"):
    print(f"[HASH] Type: {hash_type}")
    for word in open(wordlist):
        word = word.strip()
        hash_func = getattr(hashlib, hash_type)
        if hash_func(word.encode()).hexdigest() == hash_to_crack:
            print(f"[+] Match: {word}")
            return word
    print("[-] No match found.")