import sys
import time
from colorama import init, Fore, Style

def animate_text(target_text: str, delay: float = 0.01):
    init()  # Inicializa colorama para Windows/Linux/macOS
    current_text = ""
    print('\x1b[?25l', end='', flush=True)  # Ocultar cursor

    try:
        while current_text != target_text:
            for char in map(chr, range(32, 127)):
                print(
                    '\r' + 
                    Fore.GREEN + current_text + 
                    Fore.LIGHTBLACK_EX + char + 
                    Style.RESET_ALL, 
                    end='', flush=True
                )
                time.sleep(delay)

                if char == target_text[len(current_text)]:
                    current_text += char
                    break
    finally:
        print('\n' + '\x1b[?25h' + Style.RESET_ALL)  # Mostrar cursor al final

def main():
    if len(sys.argv) < 2:
        print("USO: python3 animation-text.py Tu Texto Aquí")
        sys.exit(1)

    user_text = ' '.join(sys.argv[1:])
    animate_text(user_text)

if __name__ == "__main__":
    main()
