import os

def get_desktop_path():
    # Get the current username
    username = os.getlogin()
    # Construct the path to the desktop directory
    desktop_path = os.path.join("C:\\Users", username, "OneDrive - Viken fylkeskommune", "Desktop")
    return desktop_path

def create_and_write_text_file(text):
    desktop_path = get_desktop_path()
    file_path = os.path.join(desktop_path, 'example.txt')

    # Create a new text file and write the text into it
    with open(file_path, 'w') as file:
        file.write(text)

    return file_path

# Example text to write into the file
text_to_write = "Hello, this is some text that I'm writing into the file."

# Create the text file
created_file_path = create_and_write_text_file(text_to_write)

print("Text file created at:", created_file_path)