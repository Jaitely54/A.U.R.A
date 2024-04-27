import os
import webbrowser
import time

def open_websites(urls):
    """Opens multiple websites in the default web browser."""
    for url in urls:
        print(f"Opening {url}")
        webbrowser.open(url)
        time.sleep(2)  # Delay to prevent opening too quickly

def run_commands(commands):
    """Runs a list of specified commands in the system's command line interface."""
    for command in commands:
        print(f"Running command: {command}")
        os.system(command)

def create_directory(directory_path):
    """Creates a new directory."""
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Directory created at {directory_path}")
    else:
        print(f"Directory already exists at {directory_path}")

def write_to_file(file_path, text):
    """Writes text to a file."""
    with open(file_path, 'w') as file:
        file.write(text)
    print(f"Text written to {file_path}")

if __name__ == "__main__":
    print("System Automation Script")
    print("1. Open Multiple Websites")
    print("2. Run Multiple Commands")
    print("3. Create a Directory")
    print("4. Write to a File")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        urls = input("Enter URLs separated by commas: ").split(',')
        open_websites(urls)
    elif choice == '2':
        commands = input("Enter commands separated by commas: ").split(',')
        run_commands(commands)
    elif choice == '3':
        directory_path = input("Enter the directory path to create: ")
        create_directory(directory_path)
    elif choice == '4':
        file_path = input("Enter the file path: ")
        text = input("Enter text to write in the file: ")
        write_to_file(file_path, text)
    else:
        print("Invalid choice!")
