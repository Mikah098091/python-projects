import customtkinter as ctk
import socket
from concurrent.futures import ThreadPoolExecutor
import threading

ctk.set_appearance_mode("blue")
ctk.set_default_color_theme("blue")
class PRTScannerGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("prtScanner")
        self.geometry("500x380")
        self.resizable(False, False)

        self.ip_entry = ctk.CTkEntry(self, placeholder_text="Target IP or Hostname")
        self.ip_entry.grid(row=0, column=0, columnspan=3, padx=10, pady=(10, 0), sticky="ew")

        self.start_port_entry = ctk.CTkEntry(self, placeholder_text="Start Port")
        self.start_port_entry.grid(row=1, column=0, padx=10, pady=10)

        self.max_threads_entry = ctk.CTkEntry(self, placeholder_text="Max Threads")
        self.max_threads_entry.grid(row=1, column=1, padx=10, pady=10)

        self.end_port_entry = ctk.CTkEntry(self, placeholder_text="End Port")
        self.end_port_entry.grid(row=1, column=2, padx=10, pady=10)


        self.result_box = ctk.CTkTextbox(self, height=180, width=460)
        self.result_box.grid(row=2, column=0, columnspan=3, padx=10, pady=10)


        self.scan_button = ctk.CTkButton(self, text="SCAN", command=self.start_scan_thread)
        self.scan_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        self.save_button = ctk.CTkButton(self, text="SAVE", command=self.save_results)
        self.save_button.grid(row=3, column=2, padx=10, pady=10, sticky="ew")

    def start_scan_thread(self):
        thread = threading.Thread(target=self.start_scan)
        thread.daemon = True
        thread.start()

    def start_scan(self):
        ip = self.ip_entry.get()
        try:
            start_port = int(self.start_port_entry.get())
            end_port = int(self.end_port_entry.get())
            max_threads = int(self.max_threads_entry.get())

            if start_port <= 0 or end_port > 65535 or end_port <= start_port:
                self.result_box.insert("end", "Invalid port range.\n")
                return
        except ValueError:
            self.result_box.insert("end", "Please enter valid numbers.\n")
            return

        self.result_box.insert("end", f"Scanning {ip} from port {start_port} to {end_port} with {max_threads} threads...\n")
        self.result_box.see("end")

        def scan_port(port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((ip, port))
                if result == 0:
                    msg = f"Port {port} is open\n"
                    self.result_box.insert("end", msg)
                    self.result_box.see("end")
                sock.close()
            except Exception:
                pass

        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            for port in range(start_port, end_port + 1):
                executor.submit(scan_port, port)

        self.result_box.insert("end", "Scan complete.\n")
        self.result_box.see("end")

    def save_results(self):
        with open("scan_results.txt", "w", encoding="utf-8") as f:
            f.write(self.result_box.get("1.0", "end"))
        self.result_box.insert("end", "Results saved to scan_results.txt\n")
        self.result_box.see("end")

if __name__ == "__main__":
    app = PRTScannerGUI()
    app.mainloop()

