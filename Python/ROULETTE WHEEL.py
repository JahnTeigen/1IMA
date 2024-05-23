import tkinter as tk
import random
import time

class RouletteWheel:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()
        self.colors = ["red", "black", "green"]
        self.numbers = list(range(1, 37)) + ["00"]
        self.spin_length = tk.StringVar()
        self.spin_length.set("5")  # Default spin length

        self.spin_button = tk.Button(master, text="Spin", command=self.spin)
        self.spin_button.pack()

        self.spin_length_label = tk.Label(master, text="Spin Length (seconds):")
        self.spin_length_label.pack()

        self.spin_length_entry = tk.Entry(master, textvariable=self.spin_length)
        self.spin_length_entry.pack()

    def spin(self):
        spin_time = int(self.spin_length.get())
        spin_result = random.choice(self.numbers)
        self.animate_wheel(spin_time, spin_result)

    def animate_wheel(self, spin_time, spin_result):
        start_time = time.time()
        while time.time() - start_time < spin_time:
            self.canvas.delete("all")
            self.draw_wheel()
            self.draw_ball()
            self.master.update()
            time.sleep(0.01)

        self.canvas.delete("all")
        self.draw_wheel()
        self.draw_result(spin_result)

    def draw_wheel(self):
        self.canvas.create_oval(50, 50, 350, 350, outline="black", width=2)
        angle = 0
        for i in range(0, 37):
            arc_start = angle * 10
            arc_end = (angle + 1) * 10
            color = self.colors[i % 2]
            self.canvas.create_arc(50, 50, 350, 350, start=arc_start, extent=10, outline="black", fill=color)
            angle += 1

    def draw_ball(self):
        self.canvas.create_oval(195, 195, 205, 205, outline="black", fill="white")

    def draw_result(self, result):
        self.canvas.create_text(200, 200, text=str(result), font=("Helvetica", 20, "bold"))

def main():
    root = tk.Tk()
    root.title("American Roulette Wheel")
    roulette_wheel = RouletteWheel(root)
    root.mainloop()

if __name__ == "__main__":
    main()

