import argparse
from brute_ssh import brute_force_ssh
from brute_ftp import brute_force_ftp
from brute_http import brute_force_http
from crack_hashes import crack_hash

def main():
    parser = argparse.ArgumentParser(description="PassBreaker-Ethical - Password Testing Tool")
    parser.add_argument('--module', choices=['ssh', 'ftp', 'http', 'hash'], required=True)
    parser.add_argument('--target', help='Target IP/Host')
    parser.add_argument('--url', help='Target URL (for HTTP)')
    parser.add_argument('--username', help='Username to test')
    parser.add_argument('--wordlist', help='Path to wordlist')
    parser.add_argument('--hash', help='Hash to crack')
    parser.add_argument('--type', help='Hash type (md5, sha1, etc.)')
    args = parser.parse_args()

    if args.module == "ssh":
        brute_force_ssh(args.target, args.username, args.wordlist)
    elif args.module == "ftp":
        brute_force_ftp(args.target, args.username, args.wordlist)
    elif args.module == "http":
        brute_force_http(args.url, args.username, args.wordlist)
    elif args.module == "hash":
        crack_hash(args.hash, args.wordlist, args.type)

if __name__ == "__main__":
    main()