import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk
import sqlite3
import hashlib

# Database initialization
conn = sqlite3.connect('user_database.db') # Connection to database
cursor = conn.cursor() # Cursor allows us to execute commands to the database
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT,
        is_admin INTEGER
    )
''')
conn.commit() # Commits the command

# Function to hash the input using sha-256
def hash_input(input):
    return hashlib.sha256(input.encode()).hexdigest()

# Login function
def login():
    login_window = tk.Toplevel(root)
    login_window.geometry("200x200+620+300")
    login_window.title("Logg Inn")

    def check_login():
        entered_username = username_entry.get()
        hashed_entered_username =hash_input(entered_username)
        entered_password = hash_input(password_entry.get())

        cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (hashed_entered_username, entered_password))
        user = cursor.fetchone()

        if user:
            messagebox.showinfo("Innlogging Vellykket", "Velkommen, {}!".format(entered_username))
            login_window.destroy()
        else:
            messagebox.showerror("Innlogging Ikke Vellykket", "Ugyldig brukernavn eller passord")

    # Login window
    tk.Label(login_window, text="Brukernavn:").pack(pady=5)
    username_entry = tk.Entry(login_window)
    username_entry.pack()

    tk.Label(login_window, text="Passord:").pack(pady=5)
    password_entry = tk.Entry(login_window, show='*')
    password_entry.pack()

    login_button = tk.Button(login_window, text="Logg inn", command=check_login)
    login_button.pack(pady=10)
    go_back_button = tk.Button(login_window, text="Gå tilbake", command= lambda: go_back(login_window)).pack(pady=10)

# Function to add a user
def add_user():
    admin_password = simpledialog.askstring("Admin Passord", "Skriv Inn Admin Passord:", show='*')
    if admin_password != "admin":
        messagebox.showerror("Ugyldig Admin Passord", "Tilgang Nektet!")
        return

    add_user_window = tk.Toplevel(root)
    add_user_window.geometry("320x340+620+300")
    add_user_window.title("Legg Til Bruker")

    def add_to_database():
        if (var1.get() == 1) and (var2.get() == 1):
            new_username = new_username_entry.get()
            new_password = new_password_entry.get()
            reentered_password = new_password_reentry.get()
            hashed_new_username = hash_input(new_username)

            if new_username == False or new_password == False or reentered_password == False:
                messagebox.showerror("Input Error", "Alle felt må være fylt ut.")
                return

            # Check if username exists
            cursor.execute('SELECT * FROM users WHERE username=?', (hashed_new_username,))
            user = cursor.fetchone()

            if user:
                messagebox.showerror("User exists", "Username already exists in database.")
                return

            # Check if the password length is at least 8 characters
            elif len(new_password) < 8:
                messagebox.showerror("Password Length Error", "Passordet må ha minst 8 tegn.")
                return
            
            # Check if passwords are the same
            elif (new_password != reentered_password):
                messagebox.showerror("Password Check Error", "Passordene som du skrev inn er ikke like.")
                return

            hashed_new_password = hash_input(new_password_entry.get())

            # Inserts data and gives completion message
            cursor.execute('INSERT INTO users VALUES (?, ?, ?)', (hashed_new_username, hashed_new_password, 0))  # 0 for regular user
            conn.commit()

            messagebox.showinfo("Bruker Lagt Til", "Bruker {} har blitt lagt til!".format(new_username))
            add_user_window.destroy()
        
        else:
            messagebox.showerror("Input Error", "Begge boksen må være sjekket for å lage bruker.")

    # Add user window
    tk.Label(add_user_window, text="Brukernavn:").pack()
    new_username_entry = tk.Entry(add_user_window)
    new_username_entry.pack(pady=10)

    tk.Label(add_user_window, text="Passord:").pack()
    new_password_entry = tk.Entry(add_user_window)
    new_password_entry.pack(pady=10)

    tk.Label(add_user_window, text="Gjenta Passord:").pack()
    new_password_reentry = tk.Entry(add_user_window)
    new_password_reentry.pack(pady=10)

    var1 = tk.IntVar()
    tk.Checkbutton(add_user_window, text="Jeg er over alderen 13 år", variable=var1, onvalue=1, offvalue=0).pack(pady=5)

    var2 = tk.IntVar()
    tk.Checkbutton(add_user_window, text="Jeg tillater at personopplysningene mine blir lagret", variable=var2, onvalue=1, offvalue=0).pack(pady=5)

    add_button = tk.Button(add_user_window, text="Legg til Bruker", command=add_to_database)
    add_button.pack(pady=10)
    go_back_button = tk.Button(add_user_window, text="Gå tilbake", command= lambda: go_back(add_user_window)).pack(pady=10)

# Function to delete a user
def delete_user():
    admin_password = simpledialog.askstring("Admin Passord", "Skriv inn Admin Passord:", show='*')
    if admin_password != "admin_password":
        messagebox.showerror("Ugyldig Admin Passord", "Tilgang Nektet!")
        return

    delete_user_window = tk.Toplevel(root)
    delete_user_window.geometry("300x200+620+300")
    delete_user_window.title("Slett Bruker")

    def delete_from_database():
        delete_username = delete_username_entry.get()
        hashed_delete_username = hash_input(delete_username)

        # Checks if the user that is being deleted is in database
        cursor.execute("SELECT * FROM users WHERE username=?", (hashed_delete_username,))
        user = cursor.fetchone()

        if user and var1.get() == 1:
            cursor.execute('DELETE FROM users WHERE username=?', (hashed_delete_username,))
            conn.commit()

            messagebox.showinfo("Bruker Slettet", "Bruker {} har blitt slettet!".format(delete_username))
            delete_user_window.destroy()

        elif user and var1.get() == 0:
            messagebox.showerror("Sjekk av boksen", "Boksen må være sjekket av før du kan slette brukeren.")
        else:
            messagebox.showerror("Bruker ikke funnet", "Bruker {} finnes ikke i databasen.".format(delete_username))


    # Delete user window components
    tk.Label(delete_user_window, text="Brukernavn Som Skal Slettes:").pack()
    delete_username_entry = tk.Entry(delete_user_window)
    delete_username_entry.pack(pady=10)

    var1 = tk.IntVar()
    tk.Checkbutton(delete_user_window, text="Jeg vil slette den brukeren", variable=var1, onvalue=1, offvalue=0).pack(pady=10)

    delete_button = tk.Button(delete_user_window, text="Slett Bruker", command=delete_from_database)
    delete_button.pack(pady=10)
    go_back_button = tk.Button(delete_user_window, text="Gå tilbake", command= lambda: go_back(delete_user_window)).pack(pady=10)

# Function to read privacy policy
def privacy_policy():
    privacy_policy_window = tk.Toplevel(root)
    privacy_policy_window.geometry("800x400+380+200")
    privacy_policy_window.title("Les Mer om Personvern")

    # Text that is used in the window
    formatted_text="""
            § 5.Barns samtykke i forbindelse med informasjonssamfunnstjenester
            Aldersgrensen er 13 år for samtykke etter personvernforordningen 
             artikkel 6 nr. 1 bokstav a i forbindelse med formål som nevnt i 
             personvernforordningen artikkel 8 nr. 1.

            § 6.Behandling av særlige kategorier av personopplysninger i arbeidsforhold
            Personopplysninger​1 som nevnt i personvernforordningen artikkel 9 nr. 1 kan 
            behandles når det er nødvendig for å gjennomføre arbeidsrettslige plikter 
            eller rettigheter.

            1	Se personvernforordningen art. 4 nr. 1.
            § 7.Behandling av særlige kategorier av personopplysninger etter tillatelse 
            eller forskrift
            Datatilsynet kan i særlige tilfeller gi tillatelse til å behandle 
            personopplysninger​ som nevnt i personvernforordningen artikkel 9 nr. 1 dersom 
            behandling er nødvendig av hensyn til viktige allmenne interesser. 
            Datatilsynet skal fastsette vilkår for å verne den registrertes grunnleggende
            rettigheter og interesser.

            Kongen kan i forskrift åpne for behandling av personopplysninger som nevnt i
            personvernforordningen artikkel 9 nr. 1 når det er nødvendig av hensyn til 
            viktige allmenne interesser. I en slik forskrift skal det fastsettes egnede og 
            særlige tiltak for å verne den registrertes grunnleggende rettigheter og interesser.

            1	Se personvernforordningen art. 4 nr. 1.
            § 8.Behandling av personopplysninger for arkivformål i allmennhetens interesse,
            formål knyttet til vitenskapelig eller historisk forskning eller statistiske formål
            Personopplysninger​1 kan behandles på grunnlag av personvernforordningen artikkel 6 
            nr. 1 bokstav e dersom det er nødvendig for arkivformål i allmennhetens interesse, 
            formål knyttet til vitenskapelig eller historisk forskning eller statistiske formål.
            ​3 Behandlingen skal være omfattet av nødvendige garantier i samsvar med 
            personvernforordningen artikkel 89 nr. 1.

            1	Se personvernforordningen art. 4 nr. 1.
            3	Se personvernforordningen art. 5 nr. 1 bokstav b og art. 89 nr. 1.
            § 9.Behandling av særlige kategorier av personopplysninger uten samtykke for arkivformål 
            i allmennhetens interesse, formål knyttet til vitenskapelig eller historisk forskning 
            eller statistiske formål
            Personopplysninger​1 som nevnt i personvernforordningen artikkel 9 nr. 1 kan behandles 
            uten samtykke fra den registrerte​1 dersom behandlingen​2 er nødvendig for arkivformål i 
            allmennhetens interesse, formål knyttet til vitenskapelig eller historisk forskning eller 
            statistiske formål og samfunnets interesse i at behandlingen finner sted, klart overstiger 
            ulempene for den enkelte. Behandlingen skal være omfattet av nødvendige garantier i samsvar 
            med personvernforordningen artikkel 89 nr. 1.

            Før det foretas behandling på grunnlag av første ledd, skal den behandlingsansvarlige​3 
            rådføre seg med personvernombudet etter personvernforordningen artikkel 37 eller 
            en annen som oppfyller vilkårene i personvernforordningen artikkel 37 nr. 5 og 6 og 
            artikkel 38 nr. 3 første og annet punktum. Ved rådføringen skal det vurderes om behandlingen 
            vil oppfylle kravene i personvernforordningen og øvrige bestemmelser fastsatt i eller med 
            hjemmel i loven her. Rådføringsplikten gjelder likevel ikke dersom det er utført en vurdering 
            av personvernkonsekvenser etter personvernforordningen artikkel 35.

            Kongen kan gi forskrift om behandling av særlige kategorier av personopplysninger for 
            arkivformål i allmennhetens interesse, formål knyttet til vitenskapelig eller historisk 
            forskning eller statistiske formål.

            1	Se personvernforordningen art. 4 nr. 1.
            2	Se personvernforordningen art. 4 nr. 2.
            3	Se personvernforordningen art. 4 nr. 7.
            § 10.Rådføringsplikt før behandling av særlige kategorier av personopplysninger
            for forskningsformål på grunnlag av samtykke
            Rådføringsplikten etter § 9 annet ledd gjelder tilsvarende når personopplysninger
            ​1 som nevnt i personvernforordningen artikkel 9 nr. 1 skal behandles​1 for vitenskapelige
            eller historiske forskningsformål på grunnlag av den registrertes samtykke.​2

            1	Se personvernforordningen art. 4 nr. 1.
            2	Se personvernforordningen art. 4 nr. 11.
            § 11.Behandling av personopplysninger om straffedommer og lovovertredelser mv.
            Personvernforordningen artikkel 9 nr. 2 bokstav a og c til f samt §§ 6, 7 og 9 i loven her 
            gjelder tilsvarende for behandling​1 av personopplysninger​2 som nevnt i personvernforordningen 
            artikkel 10 som ikke utføres under en offentlig myndighets kontroll. Omfattende registre 
            over straffedommer kan bare føres under en offentlig myndighets kontroll.

            Rådføringsplikten etter § 9 annet ledd gjelder tilsvarende også når personopplysninger som 
            nevnt i personvernforordningen artikkel 10 skal behandles for vitenskapelige eller historiske 
            forskningsformål på grunnlag av

            a.	den registrertes samtykke,​3 uten hensyn til om behandlingen utføres under en offentlig 
            myndighets kontroll eller ikke
            b.	§ 8 i loven her, dersom behandlingen utføres under en offentlig myndighets kontroll.
            1	Se personvernforordningen art. 4 nr. 2
            2	Se personvernforordningen art. 4 nr. 1.
            3	Se personvernforordningen art. 4 nr. 11.
            § 12.Bruk av fødselsnummer og andre entydige identifikasjonsmidler
            Fødselsnummer og andre entydige identifikasjonsmidler kan bare behandles​1 når det er saklig 
            behov for sikker identifisering og metoden er nødvendig for å oppnå slik identifisering.​2

            Kongen kan gi forskrift om bruk av fødselsnummer og andre entydige identifikasjonsmidler.

            1	Se personvernforordningen art. 4 nr. 2.
            2	Se personvernforordningen art. 87 og art. 9 nr. 4.
            § 12 a.Adgang for offentlige myndigheter til å utlevere personopplysninger i arbeidet mot 
            arbeidslivskriminalitet
            Offentlige myndigheter kan utlevere personopplysninger til hverandre når det er nødvendig 
            for å forebygge, avdekke, forhindre eller sanksjonere arbeidslivskriminalitet. Første punktum 
            gjelder ikke personopplysninger som nevnt i personvernforordningen artikkel 9. Departementet 
            kan i forskrift gi nærmere regler om hvilke offentlige myndigheter som kan utveksle personopplysninger
            etter bestemmelsen her.

            Første ledd gjelder ikke der noe annet er bestemt i eller i medhold av lov og gir ikke adgang 
            til utlevering av opplysninger som er omfattet av lovbestemt taushetsplikt.

            0	Tilføyd ved lov 20 des 2018 nr. 116 (ikr. 20 des 2018 iflg. res. 20 des 2018 nr. 2093).
            § 13.Forskrifter om overføring av personopplysninger til tredjestater eller internasjonale organisasjoner
            Kongen kan gi forskrift om overføring av personopplysninger​1 til tredjestater eller internasjonale organisasjoner.

            1	Se personvernforordningen art. 4 nr. 1.
            § 14.Forskrifter om forhåndsdrøfting og forhåndsgodkjenning
            Kongen kan gi forskrift om forhåndsdrøfting med Datatilsynet og om forhåndsgodkjenning​1 fra Datatilsynet.

            1	Se personvernforordningen art. 36 nr. 5.
            § 15.Forskrifter om gjennomføring av delegerte rettsakter og gjennomføringsrettsakter
            Kongen kan gi forskrift om gjennomføring av delegerte rettsakter og gjennomføringsrettsakter.​1

            1	Se personvernforordningen art. 28 nr. 7, art. 40 nr. 9, art. 43 nr. 9 og art. 47 nr. 3.
            """
    
    # Canvas to make the page scrollable
    canvas = tk.Canvas(privacy_policy_window, scrollregion=(0,0,2000,1950))
    canvas.create_text(400,20, font="18", justify="center", text="Les Mer om Personvern og Lovene Vi Forholder Oss Til")
    canvas.create_text(400,930, justify="center", text=formatted_text)

    canvas.pack(expand=True, fill="both")

    # Scrollbar initilization
    scrollbar = ttk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

def go_back(window):
    window.destroy()

# Main GUI
root = tk.Tk()
root.title("Bruker Styringssystem")

root.geometry("320x260+620+300")

login_button = tk.Button(root, text="Logg Inn",  command=login).pack(pady=10)

add_user_button = tk.Button(root, text="Legg Til Bruker", command=add_user).pack(pady=10)

delete_user_button = tk.Button(root, text="Slett Bruker", command=delete_user).pack(pady=10)

privacy_policy_button = tk.Button(root, text="Personvern", command=privacy_policy).pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.destroy).pack(pady=10)

root.mainloop()

# Close the database connection
conn.close()