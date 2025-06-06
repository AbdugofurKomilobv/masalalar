def ai_assistant_simple(user_input):
    user_input = user_input.lower()
    if "salom" in user_input:
        return "Salom! Qanday yordam beray?"
    elif "qalay" in user_input or "qalaysan" in user_input:
        return "Yaxshi, rahmat! Sizchi?"
    elif "kim senga yordam berdi" in user_input:
        return "Mega Tron ChatGPT yordam berdi!"
    else:
        return "Kechirasiz, men buni tushunmadim."

def main():
    print("Sun'iy ong yordamchi. 'chiqish' deb yozib, dasturdan chiqishingiz mumkin.")
    while True:
        user_input = input("Siz: ")
        if user_input.lower() == "chiqish":
            print("Xayr!")
            break
        answer = ai_assistant_simple(user_input)
        print(f"Yordamchi: {answer}")

if __name__ == "__main__":
    main()
