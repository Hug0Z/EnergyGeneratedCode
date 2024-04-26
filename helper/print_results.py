import json
import os

# Define the folder path
folder_path = "/home/hugo/runs/second"  # Change this to the path of your folder

# Initialize a list to store the generated texts
generated_texts = []

# # Iterate over all files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith(".txt") and "experiment_1" in file_name:
        file_path = os.path.join(folder_path, file_name)

        with open(file_path, "r") as file:
            # Read the first line and strip leading/trailing whitespaces
            generated_text = file.readline().strip()
            # Append the generated text to the list
            generated_texts.append(generated_text)

for index, text_data in enumerate(generated_texts, start=1):
    print(f"Generated text {index}:")
    # Split the text into code and solution parts based on the delimiter
    solution = text_data  # .split("It should =>", 1)
    # Strip leading/trailing whitespaces from code and solution
    code = ""  # code.strip()
    solution = solution.strip()
    # Replace "\n" characters with actual newlines in the solution code
    solution = solution.replace("\\n", "\n")
    # Print the formatted output
    print(f"Code:\n{code}\n")
    print("### Solution\n")
    print(f"```python\n{solution}\n```")
    print("\n" + "=" * 50 + "\n")  # Add a separator between generated texts
