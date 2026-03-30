import customtkinter as ctk
import threading
from core.screen_monitor import monitor_screen
from core.device_monitor import monitor_devices
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

from core.event_bus import register_listener

app = ctk.CTk()

app.title("Privacy Sentinel")
app.geometry("900x600")

label = ctk.CTkLabel(app, text="Monitoring Dashboard", font=("Ariel", 30))
label.pack(pady=20)

textbox = ctk.CTkTextbox(app, width=800, height=400)
textbox.pack(pady=20)

textbox.insert("end", "System started...\n")

def update_ui(msg):
    textbox.insert("end", msg + "\n")
    textbox.see("end")

register_listener(update_ui)

threading.Thread(target=monitor_screen, daemon=True).start()
threading.Thread(target=monitor_devices, daemon=True).start()

app.mainloop()