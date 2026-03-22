from colorama import init, Fore
init()
print(Fore.GREEN + "=== Анализатор ===" + Fore.RESET)

print("Анализатор текста")
name = input("Имя: ")
text = input("Текст: ")
print(f"Привет {name}! Слов: {len(text.split())}, букв: {len(text)}")

