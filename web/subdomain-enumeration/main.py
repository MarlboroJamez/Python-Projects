import requests

# the domain to scan for subdomains
domain = "google.com"

# Open/Read/Split all subdomains
file = open("list.txt")
content = file.read()
subdomains = content.splitlines()

# a list of discovered subdomains
discovered_subdomains = []
for subdomain in subdomains:
    # construct the url & checking weather live or not if theres an error, it is passed
    url = f"http://{subdomain}.{domain}"
    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print("[+] Discovered subdomain:", url)
        # append the discovered subdomain to our list
        discovered_subdomains.append(url)

        # save the discovered subdomains into a file
with open("discovered_subdomains.txt", "w") as f:
    for subdomain in discovered_subdomains:
        print(subdomain, file=f)