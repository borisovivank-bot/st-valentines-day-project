import tkinter as tk
from tkinter import messagebox
import random

class ValentineGame:
    def __init__(self, root):
        self.root = root
        self.root.title("St. Valentine's Day Matching Game 💘")
        self.root.geometry("600x500")
        self.root.configure(bg="#ffebee")  # Light pink background

        self.matches = {
            "Сердце": "❤️",
            "Купидон": "👼",
            "Роза": "🌹",
            "Письмо": "💌",
            "Кольцо": "💍",
            "Шоколад": "🍫"
        }

        self.names = list(self.matches.keys())
        self.emojis = list(self.matches.values())
        
        random.shuffle(self.names)
        random.shuffle(self.emojis)

        self.selected_name = None
        self.selected_emoji = None
        self.name_buttons = {}
        self.emoji_buttons = {}

        self.create_widgets()

    def create_widgets(self):
        # Header
        header = tk.Label(
            self.root, 
            text="Найди пару! 💖", 
            font=("Helvetica", 24, "bold"), 
            bg="#ffebee", 
            fg="#d81b60",
            pady=20
        )
        header.pack()

        # Game Frame
        game_frame = tk.Frame(self.root, bg="#ffebee")
        game_frame.pack(expand=True, fill="both", padx=50)

        # Names Column
        names_frame = tk.Frame(game_frame, bg="#ffebee")
        names_frame.pack(side="left", expand=True)

        for name in self.names:
            btn = tk.Button(
                names_frame, 
                text=name, 
                font=("Helvetica", 12),
                width=15,
                bg="#fce4ec",
                activebackground="#f8bbd0",
                command=lambda n=name: self.on_name_click(n)
            )
            btn.pack(pady=10)
            self.name_buttons[name] = btn

        # Emojis Column
        emojis_frame = tk.Frame(game_frame, bg="#ffebee")
        emojis_frame.pack(side="right", expand=True)

        for emoji in self.emojis:
            btn = tk.Button(
                emojis_frame, 
                text=emoji, 
                font=("Helvetica", 20),
                width=5,
                bg="#fce4ec",
                activebackground="#f8bbd0",
                command=lambda e=emoji: self.on_emoji_click(e)
            )
            btn.pack(pady=5)
            self.emoji_buttons[emoji] = btn

    def on_name_click(self, name):
        # Reset previous selection colors
        if self.selected_name:
            self.name_buttons[self.selected_name].configure(bg="#fce4ec")
        
        self.selected_name = name
        self.name_buttons[name].configure(bg="#f06292")
        self.check_match()

    def on_emoji_click(self, emoji):
        # Reset previous selection colors
        if self.selected_emoji:
            self.emoji_buttons[self.selected_emoji].configure(bg="#fce4ec")

        self.selected_emoji = emoji
        self.emoji_buttons[emoji].configure(bg="#f06292")
        self.check_match()

    def check_match(self):
        if self.selected_name and self.selected_emoji:
            if self.matches[self.selected_name] == self.selected_emoji:
                # Success!
                self.name_buttons[self.selected_name].pack_forget()
                self.emoji_buttons[self.selected_emoji].pack_forget()
                
                del self.name_buttons[self.selected_name]
                del self.emoji_buttons[self.selected_emoji]
                
                self.selected_name = None
                self.selected_emoji = None

                if not self.name_buttons:
                    messagebox.showinfo("Победа!", "Все пары найдены! С Днем Святого Валентина! 💝")
                    self.root.destroy()
            else:
                # No match - we wait for the next click to reset or highlight error
                # For simplicity, just let them keep trying.
                pass

if __name__ == "__main__":
    root = tk.Tk()
    game = ValentineGame(root)
    root.mainloop()
