url = input("URL: ").strip()
########## the programmer way of find and replace

username = url.replace("https://twitter.com/", "")
print(f"username: {username}")