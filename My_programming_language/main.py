code= input("Bangla Code Likho:")

if code.startswith("DEKH VAI"):
    text= code.replace("DEKH VAI","").strip()
    print(text)
else:
    print("Unknown command")
    
