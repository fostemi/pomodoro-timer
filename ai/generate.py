"""
Script that will generate files in the src/ directory.
This will provied options to create files and run code in the 
src/ directory.
"""
import os

from openai import OpenAI

code_prompt = """
Write a simple python program that will create a timer application. \
Have the output be just the code. \
Exclude the python at the begginning of the code.
"""

temp_dir = "./tmp"

def generate_code():
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY")
    )
    print("Writing python...")
    completion = client.chat.completions.create(
        model="gpt-4o",
        store=True,
        messages=[
            {"role": "user", "content": code_prompt}
        ]
    )

    content = completion.choices[0].message.content

    # Write to file
    if (os.path.isdir(temp_dir) == False):
        os.mkdir(temp_dir)
    filepath = temp_dir + "/timer.py"

    with open(filepath, "w") as file:
        file.write(content)

    delete_line(filepath, 1)
    # delete_last_line(filepath)

    print("Content Written")
    print(content)


def delete_line(filepath, line_number):
    try:
        with open(filepath, "r") as file:
            lines = file.readlines()
            if 1 <= line_number <= len(lines):
                del lines[line_number-1]

                with open(filepath, "w") as file:
                    file.writelines(lines)
            else:
                print("Line out of range for deletion")
    except FileNotFoundError:
        print(f"Error: File {filepath} not found")
    except Exception as e:
        print(f"Error: {e}")

def delete_last_line(filepath):
    try:
        with open(filepath, "r") as file:
            lines = file.readlines()
            del lines[len(lines)-1]

            with open(filepath, "w") as file:
                file.writelines(lines)

    except FileNotFoundError:
        print(f"Error: File {filepath} not found")
    except Exception as e:
        print(f"Error: {e}")

generate_code()
