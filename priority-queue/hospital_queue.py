import tkinter as tk
import heapq  # For PriorityQueue functionality


class Patient:
    """Represents a patient with name, age, and graphical representation."""
    def __init__(self, name, age, color, is_critical=False):
        self.name = name
        self.age = age
        self.color = color
        self.is_critical = is_critical

    def __lt__(self, other):
        """Comparison based on critical status and age (higher age gets priority)."""
        if self.is_critical != other.is_critical:
            return self.is_critical > other.is_critical  # Critical patients have higher priority
        return self.age < other.age  # Within the same critical status, higher age gets priority


class PriorityQueue:
    """A priority queue implementation using a heap."""
    def __init__(self, max_size=5):
        self.queue = []
        self.max_size = max_size

    def enqueue(self, patient):
        """Add a patient to the queue."""
        if len(self.queue) < self.max_size:
            heapq.heappush(self.queue, (-int(patient.is_critical), -patient.age, patient))
            return f"Patient {patient.name}, {patient.age} added to the queue."
        else:
            return "Queue is full!"

    def dequeue(self):
        """Remove and return the highest-priority patient."""
        if not self.is_empty():
            _, _, patient = heapq.heappop(self.queue)
            return patient
        return None

    def peek(self):
        """View the highest-priority patient without removing them."""
        if not self.is_empty():
            _, _, patient = self.queue[0]
            return patient
        return None

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Get the number of elements in the priority queue."""
        return len(self.queue)

    def clear(self):
        """Clear the entire queue."""
        self.queue = []

    def update_priority(self, name, new_priority, is_critical=False):
        """Update the priority of a specific patient by name and re-sort the queue."""
        try:
            for i, (_, _, patient) in enumerate(self.queue):
                if patient.name == name:
                    # Update priority and heapify
                    self.queue[i] = (-int(is_critical), -new_priority, patient)
                    patient.age = new_priority  # Update the patient's age to reflect the new priority
                    patient.is_critical = is_critical
                    heapq.heapify(self.queue)
                    return f"Updated priority for {patient.name} to {new_priority}, critical: {is_critical}."
            return f"Patient {name} not found in the queue."
        except Exception as e:
            return f"Error updating priority: {str(e)}"


class HospitalQueueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Priority Queue Hospital System")

        # Set canvas dimensions
        self.canvas_width = 800
        self.canvas_height = 400
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

        # Initialize priority queue
        self.priority_queue = PriorityQueue(max_size=5)
        self.queue_start_x = 200  # Start patients farther from the hospital on the right
        self.queue_start_y = 250
        self.head_radius = 20
        self.gap = 100

        # Patient colors
        self.colors = ["red", "blue", "green", "purple", "orange"]

        # Draw the hospital
        self.draw_hospital(50, 100, 150, 200)  # Move hospital to the left

        # Buttons for functionality
        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack()

        tk.Button(self.buttons_frame, text="Enqueue", command=self.add_patient_gui).grid(row=0, column=0)
        tk.Button(self.buttons_frame, text="Dequeue", command=self.serve_patient).grid(row=0, column=1)
        tk.Button(self.buttons_frame, text="Peek", command=self.peek_patient).grid(row=0, column=2)
        tk.Button(self.buttons_frame, text="Clear", command=self.clear_queue).grid(row=0, column=3)
        tk.Button(self.buttons_frame, text="Is Empty", command=self.check_empty).grid(row=1, column=0)
        tk.Button(self.buttons_frame, text="Size", command=self.get_size).grid(row=1, column=1)
        tk.Button(self.buttons_frame, text="Update Priority", command=self.update_priority_gui).grid(row=1, column=2)

        # Notification Label
        self.notification_label = tk.Label(root, text="", fg="black", font=("Arial", 10), bg="white")
        self.notification_label.pack(pady=10)

        # Input Frame for Adding Patients
        self.input_frame = tk.Frame(root)
        self.input_frame.pack(pady=10)

        tk.Label(self.input_frame, text="Name:").grid(row=0, column=0)
        self.name_entry = tk.Entry(self.input_frame)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.input_frame, text="Age:").grid(row=1, column=0)
        self.age_entry = tk.Entry(self.input_frame)
        self.age_entry.grid(row=1, column=1)

        tk.Label(self.input_frame, text="Color:").grid(row=2, column=0)
        self.color_entry = tk.Entry(self.input_frame)
        self.color_entry.grid(row=2, column=1)

        tk.Label(self.input_frame, text="Critical (yes/no):").grid(row=3, column=0)
        self.critical_entry = tk.Entry(self.input_frame)
        self.critical_entry.grid(row=3, column=1)

        tk.Label(self.input_frame, text="New Priority:").grid(row=4, column=0)
        self.priority_entry = tk.Entry(self.input_frame)
        self.priority_entry.grid(row=4, column=1)

        # Initial patients
        self.add_initial_patients()
        self.draw_queue()

    def show_notification(self, message):
        """Display a notification in the GUI."""
        self.notification_label.config(text=message)

    def draw_hospital(self, x, y, width, height):
        """Draw the hospital structure with enhancements."""
        self.canvas.create_rectangle(x, y, x + width, y + height, fill="lightgray", outline="black")
        cross_size = width * 0.5
        cross_x = x + (width - cross_size) / 2
        cross_y = y + 20
        self.canvas.create_rectangle(cross_x, cross_y, cross_x + cross_size * 0.3, cross_y + cross_size, fill="red", outline="red")
        self.canvas.create_rectangle(cross_x - cross_size * 0.2, cross_y + cross_size * 0.4, cross_x + cross_size * 0.5, cross_y + cross_size * 0.6, fill="red", outline="red")
        self.canvas.create_text(x + width / 2, y + height - 20, text="HOSPITAL", font=("Arial", 12, "bold"), fill="black")

    def draw_queue(self):
        """Draw the queue of patients on the canvas, ordered by priority (critical status and age descending)."""
        self.canvas.delete("patient")  # Clear existing patients

        # Sort the queue based on priority (critical status and age descending) for display purposes
        sorted_queue = sorted(self.priority_queue.queue, key=lambda x: (x[0], x[1]))  # Sort by critical first, then age

        for i, (_, _, patient) in enumerate(sorted_queue):
            x = self.queue_start_x + i * (self.head_radius * 2 + self.gap)
            y = self.queue_start_y
            self.draw_person(x, y, self.head_radius, patient.color, patient.name, patient.age)

    def draw_person(self, x, y, head_radius, head_color, name, age):
        """Draw a stick figure person with a name and age label."""
        try:
            self.canvas.create_oval(
                x - head_radius, y - head_radius, x + head_radius, y + head_radius,
                fill=head_color, outline="black", tags="patient"
            )
            body_length = 2 * head_radius
            self.canvas.create_line(x, y + head_radius, x, y + head_radius + body_length, fill="black", tags="patient")
            arm_length = head_radius * 1.5
            self.canvas.create_line(x - arm_length, y + head_radius + head_radius // 2, x + arm_length, y + head_radius + head_radius // 2, fill="black", tags="patient")
            leg_length = head_radius * 1.5
            self.canvas.create_line(x, y + head_radius + body_length, x - head_radius, y + head_radius + body_length + leg_length, fill="black", tags="patient")
            self.canvas.create_line(x, y + head_radius + body_length, x + head_radius, y + head_radius + body_length + leg_length, fill="black", tags="patient")
            self.canvas.create_text(x, y - head_radius - 10, text=f"{name}, {age}", font=("Arial", 8), tags="patient")
        except Exception as e:
            self.show_notification(f"Error drawing person: {str(e)}")

    def add_initial_patients(self):
        """Add initial patients to the priority queue."""
        try:
            initial_patients = [
                Patient("Alice", 65, "red", is_critical=False),
                Patient("Bob", 45, "blue", is_critical=False),
                Patient("Charlie", 75, "green", is_critical=True),
                Patient("Diana", 30, "purple", is_critical=False),
                Patient("Edward", 50, "orange", is_critical=True)
            ]
            for patient in initial_patients:
                self.priority_queue.enqueue(patient)
        except Exception as e:
            self.show_notification(f"Error adding initial patients: {str(e)}")

    def add_patient_gui(self):
        """Add a new patient to the priority queue from GUI input."""
        name = self.name_entry.get()
        age = self.age_entry.get()
        color = self.color_entry.get()
        critical = self.critical_entry.get().strip().lower()

        if not name or not age or not color or not critical:
            self.show_notification("Please fill in all fields!")
            return

        try:
            age = int(age)
            if age <= 0:
                raise ValueError("Age must be greater than zero!")

            is_critical = critical == "yes"

            new_patient = Patient(name, age, color, is_critical=is_critical)
            message = self.priority_queue.enqueue(new_patient)
            self.show_notification(message)
            self.draw_queue()
        except ValueError as e:
            self.show_notification(str(e))
        except Exception as e:
            self.show_notification(f"Error adding patient: {str(e)}")

    def update_priority_gui(self):
        """Update the priority of a specific patient from GUI input."""
        name = self.name_entry.get()
        new_priority = self.priority_entry.get()
        critical = self.critical_entry.get().strip().lower()

        if not name or not new_priority or not critical:
            self.show_notification("Please fill in the name, new priority, and critical status!")
            return

        try:
            new_priority = int(new_priority)
            is_critical = critical == "yes"
            message = self.priority_queue.update_priority(name, new_priority, is_critical=is_critical)
            self.show_notification(message)
            self.draw_queue()
        except ValueError:
            self.show_notification("New priority must be a number!")
        except Exception as e:
            self.show_notification(f"Error updating priority: {str(e)}")

    def serve_patient(self):
        """Serve the highest-priority patient."""
        try:
            if not self.priority_queue.is_empty():
                served = self.priority_queue.dequeue()
                self.show_notification(f"Serving: {served.name}, {served.age}, Critical: {served.is_critical}")
                self.draw_queue()
            else:
                self.show_notification("No patients in the queue!")
        except Exception as e:
            self.show_notification(f"Error serving patient: {str(e)}")

    def peek_patient(self):
        """View the highest-priority patient."""
        try:
            if not self.priority_queue.is_empty():
                patient = self.priority_queue.peek()
                self.show_notification(f"Next to serve: {patient.name}, {patient.age}, Critical: {patient.is_critical}")
            else:
                self.show_notification("No patients in the queue!")
        except Exception as e:
            self.show_notification(f"Error peeking patient: {str(e)}")

    def clear_queue(self):
        """Clear the entire queue."""
        try:
            self.priority_queue.clear()
            self.draw_queue()
            self.show_notification("Queue cleared.")
        except Exception as e:
            self.show_notification(f"Error clearing queue: {str(e)}")

    def check_empty(self):
        """Check if the queue is empty."""
        try:
            self.show_notification("Queue is empty!" if self.priority_queue.is_empty() else "Queue is not empty!")
        except Exception as e:
            self.show_notification(f"Error checking if queue is empty: {str(e)}")

    def get_size(self):
        """Get the size of the queue."""
        try:
            self.show_notification(f"Queue size: {self.priority_queue.size()}")
        except Exception as e:
            self.show_notification(f"Error getting queue size: {str(e)}")


# Create the tkinter window
root = tk.Tk()
app = HospitalQueueApp(root)
root.mainloop()
