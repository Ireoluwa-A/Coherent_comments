import csv
import random
import subprocess
import xml.etree.ElementTree as ET
import re

# Define the input and output file paths
# input_file = 'RawText/Non-coherent.txt'
# output_file = 'comment_non_coherent.csv'
# coherent = 0
# sample_probability = 1


input_file = 'RawText/Coherent.txt'
output_file = 'comment_coherent.csv'
coherent = 1
approximate_sample_size = 5510
num_snippets = 640
sample_probability = num_snippets / approximate_sample_size

# Initialize variables to store file, comment, and code data
current_file = ""
current_comment = ""
current_code = ""
in_code_section = False

def calculate_cyclomatic_complexity(java_code):
    # Count the number of decision points in the code
    decision_points = count_decision_points(java_code)

    # McCabe Cyclomatic Complexity formula: E - N + 2P
    return decision_points + 1

def count_decision_points(java_code):
    # Regular expression to match decision point keywords
    pattern = re.compile(r'\b(if|else if|for|while|case)\b')
    matches = pattern.findall(java_code)

    return len(matches)

def count_lines_of_code(java_code):
    # Count the number of lines of code in the string
    lines = java_code.split('\n')
    # Exclude empty lines and lines containing only whitespace
    non_empty_lines = [line for line in lines if line.strip()]
    return len(non_empty_lines)

# Open the input and output files
with open(input_file, 'r', encoding='utf-8') as input_data, open(output_file, 'w', newline='') as output_data:
    # Create a CSV writer
    csv_writer = csv.writer(output_data)
    
    # Write header row to the CSV file
    csv_writer.writerow(['File', 'Comment', 'Code', 'Coherent', 
                         'Cyclomatic', 'LOC', 'Comment in Code'])
            
    # Read lines from the input file
    for line in input_data:
        if line.startswith("#File"):            
            current_file = line.split(":")[1].strip()
        elif line.startswith("#Comment"):
            current_comment = ""
            for line in input_data:
                if line.startswith("#Code"):
                    in_code_section = True
                    break
                else:
                    new_comment = line.replace('*', '').replace('/', '')
                    current_comment += new_comment.strip() + ' '

        elif in_code_section:
            if line.startswith("#"):
                in_code_section = False

                cyclomatic_complexity = calculate_cyclomatic_complexity(current_code)
                lines_of_code = count_lines_of_code(current_code)

                # Check if any part of the comment is in the code section
                comment_in_code = 1 if (any(comment_word in current_code for comment_word in current_comment.split())) else 0

                # Write file, comment, and code to the CSV file
                selector = random.random()
                if selector <= sample_probability:
                    csv_writer.writerow([current_file, current_comment.strip(), current_code.strip(), coherent, 
                                        cyclomatic_complexity, lines_of_code, comment_in_code])
                current_code = ""
            else:
                current_code += line

print(f"Data successfully written to {output_file}.")