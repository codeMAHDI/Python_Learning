# Bangla Language - Step 2 (Variables + Print)

memory = {}   # ekhane variables store hobe

while True:
    code = input("Bangla Code Likho: ")

    # exit system (optional)
    if code == "EXIT":
        break

    # =========================
    # 1. PRINT SYSTEM
    # =========================
    if code.startswith("DEKH VAI"):
        text = code.replace("DEKH VAI", "").strip()

        # variable check
        if text in memory:
            print(memory[text])
        else:
            print(text)

    # =========================
    # 2. VARIABLE SYSTEM
    # =========================
    elif code.startswith("NIRDHARON"):
        parts = code.replace("NIRDHARON", "").strip().split("=")

        var_name = parts[0].strip()
        value = parts[1].strip()

        memory[var_name] = value
        print(f"{var_name} saved!")

    else:
        print("Unknown command")
