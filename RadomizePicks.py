import random

def read_every_other_line_and_shuffle(input_filename, output_filename):
    # 1. Read all lines from the input file
    with open(input_filename, 'r') as f:
        all_lines = f.readlines()

    # 2. Separate the lines: every other line and the remaining lines
    other_lines = all_lines[::2]  # Lines at index 0, 2, 4, ...
    remaining_lines = all_lines[1::2] # Lines at index 1, 3, 5, ...

    # 3. Randomly shuffle the 'other_lines' list
    random.shuffle(other_lines)

    # 4. Reconstruct the content with shuffled lines in their original positions
    # Determine the number of lines to process
    total_lines = len(all_lines)
    reordered_lines = []
    other_idx = 0
    remaining_idx = 0

    for i in range(total_lines):
        if i % 2 == 0:
            # Place a shuffled 'other' line
            reordered_lines.append(other_lines[other_idx])
            other_idx += 1
        else:
            # Place a 'remaining' line
            reordered_lines.append(remaining_lines[remaining_idx])
            remaining_idx += 1

    # 5. Write the reordered content to an output file
    with open(output_filename, 'w') as f:
        f.writelines(reordered_lines)

# Example Usage:
input_file_name = 'output_data.txt'
output_file_name = 'dick.txt'
read_every_other_line_and_shuffle(input_file_name, output_file_name)
