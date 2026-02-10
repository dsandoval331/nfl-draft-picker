import tkinter as tk

def sort_list_gui():
    """Retrieves input, sorts it numerically, and displays the result."""
    try:
        # Get the input string from the entry widget
        input_str = entry_input.get()
        # Convert string of numbers (comma-separated) to a list of integers
        # Split by comma, strip spaces, convert each to int
        num_list = [int(x.strip()) for x in input_str.split(',') if x.strip()]
        
        # Sort the list in place (ascending by default)
        num_list.sort()
        
        # Update the output label with the sorted list
        # Join numbers back into a string for display
        output_var.set(f"Sorted List: {', '.join(map(str, num_list))}")
    except ValueError:
        output_var.set("Error: Please enter a comma-separated list of numbers.")

# --- GUI Setup ---
root = tk.Tk()
root.title("List Sorter")
root.geometry("400x200")

# Input Frame
frame_input = tk.Frame(root, padx=10, pady=10)
frame_input.pack(pady=10)

label_input = tk.Label(frame_input, text="Enter numbers (comma-separated):")
label_input.pack(side=tk.LEFT)

entry_input = tk.Entry(frame_input, width=30)
entry_input.pack(side=tk.LEFT, padx=5)

# Sort Button
button_sort = tk.Button(root, text="Sort List", command=sort_list_gui)
button_sort.pack(pady=10)

# Output Label
output_var = tk.StringVar()
label_output = tk.Label(root, textvariable=output_var, wraplength=380, fg="blue")
label_output.pack(pady=10)

# Start the GUI event loop
root.mainloop()
