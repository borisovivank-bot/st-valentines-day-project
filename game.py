import tkinter as tk
from tkinter import messagebox
import random

class ValentineGame:
    def __init__(self, root):
        self.root = root
        self.root.title("St. Valentine's Day Matching Game 💘")
        self.root.geometry("800x600")
        self.root.configure(bg="#ffebee")  # Light pink background

        # Core game data - Riddles and Emojis
        self.matches_data = {
            "Бьётся в груди,\nлюбви вечный знак": "❤️",
            "С крыльями мальчик,\nстрелок он лихой": "👼",
            "Пахнет чудесно,\nно с острой шипой": "🌹",
            "В почту летит,\nсекреты хранит": "💌",
            "Круг золотой\nна пальце блестит": "💍",
            "Сладкая плитка,\nна лицах улыбка": "🍫"
        }

        self.show_menu()

    def show_menu(self):
        # Clear current window
        for widget in self.root.winfo_children():
            widget.destroy()

        menu_frame = tk.Frame(self.root, bg="#ffebee")
        menu_frame.pack(expand=True, fill="both")

        # Splash Screen Title
        title = tk.Label(
            menu_frame, 
            text="С Днем\nСвятого Валентина! 💖", 
            font=("Helvetica", 28, "bold"), 
            bg="#ffebee", 
            fg="#d81b60",
            pady=20
        )
        title.pack()

        # Try to load and display the image
        try:
            self.photo = tk.PhotoImage(file="image-for-st-valentines.png")
            # Calculate factor to maintain aspect ratio
            width_factor = self.photo.width() // 300
            height_factor = self.photo.height() // 300
            factor = max(width_factor, height_factor)
            
            if factor > 1:
                self.photo = self.photo.subsample(factor, factor)
            
            img_label = tk.Label(menu_frame, image=self.photo, bg="#ffebee")
            img_label.image = self.photo # Keep reference
            img_label.pack(pady=10)
        except Exception:
            # If image fails to load, just show the subtitle
            subtitle = tk.Label(
                menu_frame,
                text="Найди все пары и получи признание! 💘",
                font=("Helvetica", 14, "italic"),
                bg="#ffebee",
                fg="#ad1457"
            )
            subtitle.pack(pady=10)

        # Start Button
        start_btn = tk.Button(
            menu_frame,
            text="START GAME",
            font=("Helvetica", 18, "bold"),
            bg="#d81b60",
            fg="white",
            activebackground="#f06292",
            activeforeground="white",
            padx=40,
            pady=15,
            bd=0,
            cursor="heart",
            command=self.start_game
        )
        start_btn.pack(pady=30)

        # Decoration Label
        tk.Label(
            menu_frame,
            text="❤️ 🌹 🎁 💌 🧸",
            font=("Helvetica", 24),
            bg="#ffebee"
        ).pack(side="bottom", pady=20)

    def start_game(self):
        # Reset current window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Initialize game state
        self.matches = self.matches_data.copy()
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
                font=("Helvetica", 11),
                width=22,
                height=3,
                bg="#fce4ec",
                activebackground="#f8bbd0",
                justify="center",
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
                font=("Helvetica", 24),
                width=4,
                height=1,
                bg="#fce4ec",
                activebackground="#f8bbd0",
                command=lambda e=emoji: self.on_emoji_click(e)
            )
            btn.pack(pady=10)
            self.emoji_buttons[emoji] = btn

        # Back to menu button
        back_btn = tk.Button(
            self.root,
            text="← В меню",
            font=("Helvetica", 10),
            bg="#ffebee",
            fg="#d81b60",
            bd=0,
            cursor="hand2",
            command=self.show_menu
        )
        back_btn.pack(side="bottom", pady=10)

    def on_name_click(self, name):
        # Reset previous selection colors
        if self.selected_name:
            if self.selected_name in self.name_buttons:
                self.name_buttons[self.selected_name].configure(bg="#fce4ec")
        
        self.selected_name = name
        if name in self.name_buttons:
            self.name_buttons[name].configure(bg="#f06292")
        self.check_match()

    def on_emoji_click(self, emoji):
        # Reset previous selection colors
        if self.selected_emoji:
            if self.selected_emoji in self.emoji_buttons:
                self.emoji_buttons[self.selected_emoji].configure(bg="#fce4ec")

        self.selected_emoji = emoji
        if emoji in self.emoji_buttons:
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
                    self.show_menu() # Back to menu after win
            else:
                # No match - we wait for the next click or just reset after a delay (optional)
                # For now, let's keep it simple as before.
                pass

if __name__ == "__main__":
    root = tk.Tk()
    game = ValentineGame(root)
    root.mainloop()
