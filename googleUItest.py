#THIS CODE IS THE CODE WE USED WITHOUT THE API KEY



from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import re
from tkinter import *
import datetime



api_key = "4EMxdJ0dSESRqyujjhoi1Kx9gBEOj1Dx"
model = "mistral-small-2402"


def ai(prompt):

    client = MistralClient(api_key=api_key)

    messages = [
        ChatMessage(role="user", content=prompt)
    ]

    chat_response = client.chat(
        model=model,
        messages=messages,
    )

    response = chat_response.choices[0].message.content

    return response



def query(question):
    text = "donne moi 15 noms droles/ridicules de site webs (avec leurs descriptions) qui repondent a la question: " + question 

    response = ai(text)

    sites = re.findall(r'\d+\.\s+(.*?)\s*(?=\d+\.|\Z)', response)

    descriptions = []
    websites = []

    for item in sites:
        item = item.split(" ")
        item[0] = item[0].replace('"', '')
        websites.append(item[0])
    
        descriptions.append(" ".join(item[1:]))
    

    
    

    print("\n \n")
    for i in range (len(websites)):
        websites[i] = websites[i].replace("*", "")
        descriptions[i] = descriptions[i].replace("(", "")
        descriptions[i] = descriptions[i].replace(")", "")


    return websites, descriptions, question





def on_recherche_click(event): #Fonction  supprimer "Rechercher avec Gogole"
    recherche.delete(0, "end")

def fonction_miracle(event): #Fonction tout supprimer
    websites, desc, question = query(recherche.get())
    for widget in fenetre.winfo_children():
      widget.destroy()
    googleRecherche(websites, desc, question)




fenetre = Tk() #Affichage de la fenêtre
fenetre['bg']="#fafcf9"
fenetre.geometry("1100x600")
fenetre.title('Gogole')
fenetre.resizable(height=False,width=False)

image =PhotoImage(file="/Users/alex/Desktop/Programs/Python/Picsart_24-03-05_18-22-35-231_2.gif") #Affichage de l'image
Canevas = Canvas(fenetre, width=480, height=174, borderwidth=0, highlightthickness=0)
item= Canevas.create_image(0,0, anchor=NW, image=image)
Canevas.place(relx=0.5, rely=0.30, anchor=CENTER)

recherche = Entry(fenetre, width=70, font="Roboto") #Entrée de texte
recherche.insert(0, 'Rechercher avec Gogole')
recherche.bind('<FocusIn>', on_recherche_click)
recherche.place(relx=0.5, rely=0.5, anchor=CENTER)

date_complète = (datetime.datetime.now()) #Affichage de la date
liste_date = [date_complète.strftime("%A"), " ", date_complète.strftime("%d"), " ", date_complète.strftime("%B")," ", date_complète.strftime("%Y")]
chaine_date = ''.join(liste_date)
date = Label(fenetre, bg ="#fafcf9", text=chaine_date, font=("Roboto", 14))
date.place(relx=0.05, rely=0.05, anchor=NW)

recherche.bind("<Return>", fonction_miracle) #Appel de la fonction pour supprimer quand on clique sur return



def on_enter(event): #Fonction de soulignage du lien
    event.widget.config(font=("Arial", 16, "underline"))

def on_leave(event): #Fonction de désoulignage
    event.widget.config(font=("Arial", 16))

image2 = PhotoImage(file="/Users/alex/Desktop/Programs/Python/petitgogole.gif") #Affichage de l'image en petit en haut à gauche

def googleRecherche(websites, desc, question):
    Canevas2 =Canvas(fenetre, width=96, height=35, borderwidth=0, highlightthickness=0)
    item2= Canevas2.create_image(0, 0, anchor=NW, image=image2)
    Canevas2.place(relx=0.1, rely=0.05, anchor=CENTER)

    recherche2 = Entry(fenetre, width=70, font="Roboto") #Entrée de texte en haut
    recherche2.insert(0, question)
    fenetre.bind('<FocusIn>', on_recherche_click)
    recherche2.place(relx=0.5, rely=0.05, anchor=CENTER)

    separation = Label(fenetre,width=1100,height=1,bg="blue", text = "About 15 results (3452 years)", fg = "white") #Label bande bleue en haut
    separation.place(relx=0.5, rely=0.1, anchor=CENTER)

    # Cadre pour contenir les widgets de texte
    frame = Frame(fenetre, bg="#fafcf9")
    frame.place(relx=0.1, rely=0.12, anchor=NW, relwidth=0.9, relheight=0.88)
    
    scrollbar =Scrollbar(frame, orient="vertical")
    scrollbar.pack(side=RIGHT, fill=Y)
    
    canvas =Canvas(frame, bg="#fafcf9", bd=0, highlightthickness=0, yscrollcommand=scrollbar.set)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    
    scrollbar.config(command=canvas.yview)
    
    inner_frame = Frame(canvas, bg="#fafcf9")
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    for k in range (len(websites)): #Création de tous les labels
        espace = Label(inner_frame, text="", bg="#fafcf9", pady=0)
        espace.pack()

        
        label_titre = Label(inner_frame, text=websites[k], font=("Arial", 16), fg="blue", bg="#fafcf9") #Création de label titre
        label_titre.pack(anchor="w")

        label_titre.bind("<Enter>", on_enter) #Appelle les fonctions pour souligner ou pas
        label_titre.bind("<Leave>", on_leave)

        label_description = Label(inner_frame, text=desc[k], font=("Arial", 16), fg="#5b6571", bg="#fafcf9", wraplength=850, justify='left') #Création de label description
        label_description.pack(anchor="w")


        inner_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    
    def fonction_miracle2(event): #Fonction tout supprimer
        websites, desc, question = query(recherche2.get())
        for widget in fenetre.winfo_children():
            widget.destroy()
        googleRecherche(websites, desc, question)

    recherche2.bind("<Return>", fonction_miracle2)


fenetre.mainloop()
