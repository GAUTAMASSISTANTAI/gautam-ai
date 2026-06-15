from datetime import datetime

print("🤖 Gautam Assistant AI")
print("Type 'bye' to exit.\n")

name = input("What is your name: ")

print(f"🤖 Hello {name}!")

while True:

    user = input("You: ").lower()

    if user == "bye":
        print(f"AI: Bye {name}! 👋")
        break

    elif "hello" in user or "hi" in user:
        print(f"AI: Hello {name}! 😊")

    elif "how are you" in user:
        print(f"AI: I am fine, {name}! 😊")

    elif "kaise ho" in user:
        print(f"AI: Main theek hoon {name}. Tum kaise ho? 😊")

    elif "namaste" in user:
        print(f"AI: Namaste {name}! 🙏")

    elif "mera naam" in user:
        print(f"AI: Tumhara naam {name} hai. 😊")

    elif "name" in user:
        print("AI: Mera naam Gautam Assistant AI hai. 🤖")

    elif "math" in user:
        print("AI: Main maths me help kar sakta hoon. ➕")

    elif "science" in user:
        print("AI: Main science me help kar sakta hoon. 🔬")

    elif user == "time" or "what is the time" in user:
        now = datetime.now()
        print("AI:", now.strftime("%I:%M %p"))

    elif "date" in user:
        now = datetime.now()
        print("AI:", now.strftime("%d-%m-%Y"))

    elif "good morning" in user:
        print(f"AI: Good morning {name}! ☀️ Have a wonderful day.")

    elif "good afternoon" in user:
        print(f"AI: Good afternoon {name}! 😊")

    elif "good evening" in user:
        print(f"AI: Good evening {name}! 🌇")

    elif "good night" in user:
        print(f"AI: Good night {name}! 🌙 Sweet dreams.")

    elif "thank you" in user or "shukriya" in user:
        print(f"AI: You're welcome {name}! 😊")

    elif "who made you" in user:
        print("AI: Mujhe Gautam ne banaya hai. 😎")

    elif "joke" in user:
        print("AI: Teacher: Homework kahan hai? Student: Sir, network issue tha. 😂")

    elif "kya haal hai" in user:
        print(f"AI: Main bilkul theek hoon {name}. Aap kaise ho? 😊")

    elif "i love you" in user:
        print("AI: Thank you! ❤️ Main aapka AI assistant hoon. 😊")

    elif "who are you" in user:
        print("AI: Main Gautam Assistant AI hoon. 🤖")

    elif "bye bye" in user:
        print(f"AI: Bye bye {name}! 👋")
        break

    elif "motivate me" in user:
        print("AI: Kabhi haar mat mano. Chhote steps se bada result milta hai. 💪")

    elif "study tip" in user:
        print("AI: Roz 1-2 ghante dhyan se padhai karo. 📚")

    elif "tell a fact" in user:
        print("AI: Octopus ke 3 hearts hote hain. 🐙")

    elif "help" in user:
        print("AI: Main hello, time, date, maths aur simple baaton me help kar sakta hoon. 🤖")

    else:
        try:
            answer = eval(user)
            print("AI:", answer)

        except:
            print("AI: Mujhe abhi iska answer nahi pata.")