import tkinter as tk
from tkinter import ttk, messagebox
import random


class StackFullError(Exception):
    """Custom exception for when stack is full."""
    pass


class StackEmptyError(Exception):
    """Custom exception for when stack is empty."""
    pass


class CandyStack:
    def __init__(self, max_size=5):
        self._stack = []
        self._max_size = max_size
        self._candy_types = [
            {"name": "Cherry Burst", "color": "#FF3031"},
            {"name": "Lemon Zest", "color": "#FFD700"},
            {"name": "Mint Glacier", "color": "#50C878"},
            {"name": "Dark Chocolate", "color": "#8B4513"},
            {"name": "Blueberry Dream", "color": "#4169E1"}
        ]

    def push(self, element=None):
        if self.is_full():
            raise StackFullError("Stack is full!")
        if element is None:
            element = random.choice(self._candy_types)
        self._stack.append(element)
        return element

    def pop(self):
        if self.is_empty():
            raise StackEmptyError("Stack is empty!")
        return self._stack.pop()

    def peek(self):
        if self.is_empty():
            raise StackEmptyError("Stack is empty!")
        return self._stack[-1]

    def is_full(self):
        return len(self._stack) >= self._max_size

    def is_empty(self):
        return len(self._stack) == 0

    def size(self):
        return len(self._stack)


class CandyStackDispenser:
    def __init__(self, root):
        self.root = root
        self.root.title("Candy Stack Dispenser")
        self.root.geometry("600x500")
        self.root.configure(bg='#F0F0F0')

        self.myStack = CandyStack(5)
        self.frame = ttk.Frame(root, padding=10)
        self.frame.grid(sticky=(tk.W, tk.E, tk.N, tk.S))

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.canvas = tk.Canvas(
            self.frame, background="floral white", width=400, height=300,
            highlightthickness=1, relief=tk.RAISED
        )
        self.canvas.grid(column=0, row=0, columnspan=10, rowspan=10, padx=10, pady=10)

        self.pad = 3
        self.hWidth = 140
        self.candyHeight = 20
        self.x0 = 120 + self.pad
        self.x1 = self.x0 - self.pad + self.hWidth - self.pad
        self.y0 = 10 + self.pad
        self.step = 25
        self.springTags = []
        self.candyTags = []

        self.draw_dispenser_outline()
        self.refreshSpring()
        self.create_buttons()

    def draw_dispenser_outline(self):
        self.canvas.create_line(120, 10, 120, 260, width=2)
        self.canvas.create_line(120, 260, 120 + self.hWidth, 260, width=2)
        self.canvas.create_line(120 + self.hWidth, 260, 120 + self.hWidth, 10, width=2)

    def refreshSpring(self):
        for tag in self.springTags:
            self.canvas.delete(tag)
        self.springTags.clear()

        left = 120 + self.pad
        right = 120 - self.pad + self.hWidth
        bottom = 260 - self.pad
        y_init = bottom
        squeeze = 40 - (self.myStack.size() * 4.2)

        self.springTags.append(self.canvas.create_line(self.x0, y_init, self.x1, y_init))
        for x in range(6):
            if x % 2 == 0:
                self.springTags.append(self.canvas.create_line(left, y_init, right, (y_init - squeeze)))
            else:
                self.springTags.append(self.canvas.create_line(left, (y_init - squeeze), right, y_init))
            y_init = y_init - squeeze
        self.springTags.append(self.canvas.create_line(left, y_init, right, y_init))

    def redraw_stack(self):
        """Redraws the stack on the canvas based on the backend stack."""
        for rect, text in self.candyTags:
            self.canvas.delete(rect)
            self.canvas.delete(text)
        self.candyTags.clear()

        for index, candy in enumerate(reversed(self.myStack._stack)):
            y_offset = self.y0 + (self.step * index)
            rect = self.canvas.create_rectangle(
                self.x0, y_offset, self.x1, y_offset + self.candyHeight,
                fill=candy['color']
            )
            text = self.canvas.create_text(
                (self.x0 + self.x1) / 2,
                y_offset + self.candyHeight / 2,
                text=candy['name'], fill='white',
                font=('Arial', 8, 'bold')
            )
            self.candyTags.append((rect, text))

    def _push(self):
        try:
            candy = self.myStack.push()
            self.redraw_stack()  # Redraw the stack to ensure synchronization
            self.refreshSpring()  # Update the spring
        except StackFullError:
            messagebox.showerror(title='Error', message="Stack is full! You cannot push any more candies.")
        except Exception as e:
            messagebox.showerror(title='Error', message=str(e))

    def _pop(self):
        try:
            # Remove the topmost candy from the backend stack
            popped_candy = self.myStack.pop()

            # Redraw the stack to ensure synchronization with the backend
            self.redraw_stack()

            # Update the spring
            self.refreshSpring()

            # Inform the user
            messagebox.showinfo(title='Candy Popped', message=f"Popped {popped_candy['name']} candy!")
        except StackEmptyError:
            messagebox.showerror(title='Error', message="Stack is empty! You cannot pop any more candies.")
        except Exception as e:
            messagebox.showerror(title='Error', message=str(e))

    def _peek(self):
        try:
            top_candy = self.myStack.peek()
            messagebox.showinfo(
                title='Peek', message=f"Top candy is {top_candy['name']} with {top_candy['color']} color"
            )
        except StackEmptyError:
            messagebox.showerror(title='Error', message="Stack is empty! There is no candy to peek at.")
        except Exception as e:
            messagebox.showerror(title='Error', message=str(e))

    def _size(self):
        try:
            size = self.myStack.size()
            messagebox.showinfo(title='Stack Size', message=f"Current stack size: {size}")
        except Exception as e:
            messagebox.showerror(title='Error', message=str(e))

    def _is_empty(self):
        try:
            is_empty = self.myStack.is_empty()
            messagebox.showinfo(
                title='Stack Status', 
                message="Stack is empty!" if is_empty else "Stack is not empty."
            )
        except Exception as e:
            messagebox.showerror(title='Error', message=str(e))

    def create_buttons(self):
        buttons_frame = ttk.Frame(self.frame)
        buttons_frame.grid(column=12, row=0, rowspan=4, padx=10)

        ttk.Label(
            buttons_frame, text="Candy Stack Dispenser", font=('Arial', 12, 'bold')
        ).grid(column=0, row=0, pady=10)

        button_configs = [
            ("Push Random Candy", self._push),
            ("Pop Candy", self._pop),
            ("Peek Candy", self._peek),
            ("Get Size", self._size),
            ("Is Empty", self._is_empty)
        ]

        for i, (text, command) in enumerate(button_configs, 1):
            ttk.Button(buttons_frame, text=text, width=20, command=command).grid(column=0, row=i, pady=5)


def main():
    root = tk.Tk()
    app = CandyStackDispenser(root)
    root.mainloop()


if __name__ == "__main__":
    main()
