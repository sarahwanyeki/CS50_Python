greetings = input("Insert greeting: ").strip().lower()
# greet = greetings.strip().lower()
if "hello" in greetings:
    print("$0")
elif "h" == greetings[0]:
    print("$20")
else:
    print("$100")