import requests

# the domain to scan for subdomains
domains = 'google.com'

# Open/Read/Split all subdomains
file = open("list.txt")
content = file.read()
subdomains = content.splitlines()

print("""\


 __       __                      __  __                                         _____                                             
/  \     /  |                    /  |/  |                                       /     |                                            
$$  \   /$$ |  ______    ______  $$ |$$ |____    ______    ______    ______     $$$$$ |  ______   _____  ____    ______   ________ 
$$$  \ /$$$ | /      \  /      \ $$ |$$      \  /      \  /      \  /      \       $$ | /      \ /     \/    \  /      \ /        |
$$$$  /$$$$ | $$$$$$  |/$$$$$$  |$$ |$$$$$$$  |/$$$$$$  |/$$$$$$  |/$$$$$$  | __   $$ | $$$$$$  |$$$$$$ $$$$  |/$$$$$$  |$$$$$$$$/ 
$$ $$ $$/$$ | /    $$ |$$ |  $$/ $$ |$$ |  $$ |$$ |  $$ |$$ |  $$/ $$ |  $$ |/  |  $$ | /    $$ |$$ | $$ | $$ |$$    $$ |  /  $$/  
$$ |$$$/ $$ |/$$$$$$$ |$$ |      $$ |$$ |__$$ |$$ \__$$ |$$ |      $$ \__$$ |$$ \__$$ |/$$$$$$$ |$$ | $$ | $$ |$$$$$$$$/  /$$$$/__ 
$$ | $/  $$ |$$    $$ |$$ |      $$ |$$    $$/ $$    $$/ $$ |      $$    $$/ $$    $$/ $$    $$ |$$ | $$ | $$ |$$       |/$$      |
$$/      $$/  $$$$$$$/ $$/       $$/ $$$$$$$/   $$$$$$/  $$/        $$$$$$/   $$$$$$/   $$$$$$$/ $$/  $$/  $$/  $$$$$$$/ $$$$$$$$/ 
                                                                                                                                   
                                                                                                                                   
                                                                                                                                   
""")

print("""\





 __                            __                              
(_    |_  _| _ __  _  o __    |_ __    __  _  __ _ _|_ o  _ __ 
__)|_||_)(_|(_)|||(_| | | |   |__| ||_||||(/_ | (_| |_ | (_)| |


Let's start....
""")

# a list of discovered subdomains
discovered_subdomains = []
for subdomain in subdomains:
    # construct the url & checking weather live or not if theres an error, it is passed
    url = f"http://{subdomain}.{domains}"
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