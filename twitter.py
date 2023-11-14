import re

# url = input("URL: ").strip()
########## the programmer way of find and replace

# username = url.replace("https://twitter.com/", "")
# print(f"username: {username}")


########## remove prefix ########
# url = input("URL: ").strip()
# username = url.removeprefix("https://twitter.com/", "")
# print(f"username: {username}")


########## use re.sub

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):

    print(f"Username:", matches.group(1))