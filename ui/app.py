import customtkinter as ctk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.title("Privacy Sentinel")
app.geometry("900x600")

label = ctk.CTkLabel(app, text="Monitoring Dashboard", font=("Ariel", 30))
label.pack(pady=20)

app.mainloop()