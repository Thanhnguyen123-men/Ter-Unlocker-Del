import ctypes
import customtkinter as ctk
from tkinter import filedialog, messagebox
import core_logic
import threading
import os
import sys

def resource_path(relative_path):
    """ Lấy đường dẫn tuyệt đối đến tài nguyên, hoạt động cả trên dev và sau khi build exe """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Fix icon Taskbar
try:
    myappid = 'ter.unlocker.del.v1'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except Exception:
    pass

class TerUnlockerDel(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Ter-Unlocker Del")
        self.geometry("600x550")
        self.current_target = ""
        
        try:
            self.iconbitmap(resource_path("icon_Ter_Del.ico"))
        except Exception:
            pass
        
        ctk.set_appearance_mode("dark")
        
        self.label = ctk.CTkLabel(self, text="TER-UNLOCKER DEL", font=("Arial", 24, "bold"))
        self.label.pack(pady=20)

        self.btn_file = ctk.CTkButton(self, text="Select File", command=lambda: self.pick(1))
        self.btn_file.pack(pady=5)

        self.btn_folder = ctk.CTkButton(self, text="Select Folder", command=lambda: self.pick(2))
        self.btn_folder.pack(pady=5)

        self.log_box = ctk.CTkTextbox(self, width=540, height=250, font=("Consolas", 12))
        self.log_box.pack(pady=10)

        self.btn_kill = ctk.CTkButton(self, text="Kill All Lockers", fg_color="#E67E22", command=self.start_kill_thread)
        self.btn_kill.pack(pady=5)

        self.btn_delete = ctk.CTkButton(self, text="Force Delete F/F", fg_color="#C0392B", command=self.delete_target)
        self.btn_delete.pack(pady=5)

    def log(self, msg):
        self.log_box.insert("end", f"{msg}\n")
        self.log_box.see("end")

    def pick(self, mode):
        def select_task():
            path = filedialog.askopenfilename() if mode == 1 else filedialog.askdirectory()
            if path:
                self.after(0, lambda: self.process_selected_path(path))
        threading.Thread(target=select_task, daemon=True).start()

    def process_selected_path(self, path):
        self.current_target = path
        self.log_box.delete("1.0", "end")
        self.log(f"[>] Target: {path}")
        threading.Thread(target=self.scan_thread, args=(path,), daemon=True).start()

    def scan_thread(self, path):
        found = core_logic.scan_locker(path)
        self.after(0, lambda: self.show_results(found))

    def show_results(self, found):
        if found:
            for p in found:
                self.log(f" [!] Locked by: {p['name']} (PID: {p['pid']})")
        else:
            self.log(" [+] File is free (No lockers found).")

    def start_kill_thread(self):
        if not self.current_target: return
        self.log("[*] Đang tiêu diệt các tiến trình khóa...")
        threading.Thread(target=self.kill_logic_thread, daemon=True).start()

    def kill_logic_thread(self):
        found = core_logic.scan_locker(self.current_target)
        for p in found:
            core_logic.kill_process(p['pid'])
        self.after(0, lambda: self.log("[-] Đã Kill xong."))
        self.scan_thread(self.current_target)

    def delete_target(self):
        if not self.current_target: return
        if messagebox.askyesno("Xác nhận", f"Xóa vĩnh viễn:\n{self.current_target}?"):
            success, msg = core_logic.force_delete(self.current_target)
            
            if msg == "TI_BLOCK":
                self.log("\n" + "!"*40)
                self.log("File / Folder này bị TrustedInstaller nắm giữ")
                self.log("hãy xem hướng dẫn cách xóa file / folder bị TI nắm giữ trên google")
                self.log("!"*40 + "\n")
                messagebox.showwarning("Bị chặn bởi TI", 
                    "File / Folder này bị TrustedInstaller nắm giữ\nhãy xem hướng dẫn cách xóa file / folder bị TI nắm giữ trên google")
            else:
                self.log(f"[*] {msg}")

if __name__ == "__main__":
    app = TerUnlockerDel()
    app.mainloop()