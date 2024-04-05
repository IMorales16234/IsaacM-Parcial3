import requests

# Función para enviar la solicitud a la API y procesar la respuesta.
def get_character_info(character):
    # URL de la API.
    url = "https://dbd.tricky.lol/api/characterinfo"

    # Parámetros de la solicitud.
    params = {
        "character": character
    }

    # Realizar la solicitud GET a la API con los parámetros.
    response = requests.get(url, params=params)

    # Verificar si la solicitud fue exitosa (código de estado 200).
    if response.status_code == 200:
        # Obtener los datos en formato JSON.
        data = response.json()
        
        # Extraer los campos name, difficulty, gender, role, height, bio y story.
        name = data['name']
        diff = data['difficulty']
        role = data['role']
        gender = data['gender']
        height = data['height']
        bio = data['bio']
        story = data['story']
        
        # Imprimir los campos extraídos.
        print("Name:", name)
        print("Difficulty:", diff)
        print("Role:", role)
        print("Gender:", gender)
        print("Height:", height)
        print("Info:", bio)
        print("Story:", story)

    else:
        # Si la solicitud no fue exitosa, imprimir el mensaje de error.
        print("Error en la solicitud:", response.text)


# Titulo de la App. 
print("--------------------------------------------------------------------------------------------------------------------------")
print("| ####    ######    ##    ####       #####    ##  ##     ####       ##     ##  ##   ##      ####    ####   ##  ##  ###### |")
print("| ## ##   ##       ####   ## ##      ##  ##   ##  ##     ## ##     ####    ##  ##   ##       ##    ##  ##  ##  ##    ##   |")
print("| ##  ##  ##      ##  ##  ##  ##     ##  ##   ##  ##     ##  ##   ##  ##   ##  ##   ##       ##    ##      ##  ##    ##   |")
print("| ##  ##  ####    ######  ##  ##     #####     ####      ##  ##   ######    ####    ##       ##    ## ###  ######    ##   |")
print("| ##  ##  ##      ##  ##  ##  ##     ##  ##     ##       ##  ##   ##  ##     ##     ##       ##    ##  ##  ##  ##    ##   |")
print("| ## ##   ##      ##  ##  ## ##      ##  ##     ##       ## ##    ##  ##     ##     ##       ##    ##  ##  ##  ##    ##   |")
print("| ####    ######  ##  ##  ####       #####      ##       ####     ##  ##     ##     ######  ####    ####   ##  ##    ##   |")
print("--------------------------------------------------------------------------------------------------------------------------")

#Tabla de IDs de supervivientes y asesinos.
print(" ------------------------------------------------------------------------------------------------------------------------- ")
print("| IDs y Nombres de los personajes jugables en Dead By Daylight.                                                           |")
print(" ------------------------------------------------------------------------------------------------------------------------- ")
print(" _____________________________________      ______________________________________________________________________________ ")
print("| Supervivientes                      |    | Asesinos                                                                     |")
print("|-------------------------------------|    |------------------------------------------------------------------------------|")
print("| ID        | Nombre                  |    | ID         | Nombre                                                          |")
print("| ----------|-------------------------|    |------------|-----------------------------------------------------------------|")
print("| dwight    | Dwight Fairfield        |    | chuckles   | The Trapper (El Trampero) (Evan McMillan)                       |")
print("| ----------|-------------------------|    |------------|-----------------------------------------------------------------|")
print("| meg       | Meg Thomas              |    | bob        | The Wraith (El Espectro) (Philip Ojomo)                         |")
print("| ----------|-------------------------|    |------------|-----------------------------------------------------------------|")
print("| claudette | Caludette Morel         |    | hillbilly  | The Hillbilly (El Pueblrerino) (Max Thompson Jr.)               |")
print("|-----------|-------------------------|    |------------|-----------------------------------------------------------------|")
print("| jake      | Jake Park               |    | nurse      | The Nurse (La Enfermera) (Sally Smithson)                       |")
print("| ----------|-------------------------|    |------------|-----------------------------------------------------------------|")
print("| nea       | Nea Karlsson            |    | witch      | The Hag (La Bruja) (Lisa Sherwood)                              |")
print("| ----------|-------------------------|    |------------|-----------------------------------------------------------------|")
print("| laurie    | Laurie Strode           |    | shape      | The Shape (La Forma) (Michael Myers)                            |")
print("| ----------|-------------------------|    |------------|-----------------------------------------------------------------|")
print("| ace       | Ace Visconti            |    | killer07   | The Doctor (El Doctor) (Herman Carter)                          |")
print("| ----------|-------------------------|    |------------|-----------------------------------------------------------------|")
print("| bill      | William 'Bill' Overbeck |    | bear       | The Huntress (La Cazadora) (Anna)                               |")
print("| ----------|-------------------------|    |------------|-----------------------------------------------------------------|")
print("| feng      | Feng Ming               |    | cannibal   | The Cannibal (EL Caníbal) (Leatherface)                         |")
print("| ----------|-------------------------|    |------------|-----------------------------------------------------------------|")
print("| smoke     | David King              |    | nightmare  | The Nightmare (La Pesadilla) (Freddy Krueger)                   |")
print("| ----------|-------------------------|    |------------|-----------------------------------------------------------------|")
print("| kate      | Kate Denson             |    | pig        | The Pig (La Cerda) (Amanda Young)                               |")
print("| ----------|-------------------------|    |------------|-----------------------------------------------------------------|")
print("| quentin   | Quentin Smith           |    | clown      | The Clown (El Payaso) (Kenneth Chase)                           |")
print("| ----------|-------------------------|    |------------|-----------------------------------------------------------------|")
print("| eric      | Detective Tapp          |    | spirit     | The Spirit (La Espiritu) (Rin Yamaoka)                          |")
print("| ----------|-------------------------|    |------------|-----------------------------------------------------------------|")
print("| adam      | Adam Francis            |    | legion     | The Legion (La Legion) (Frank, Julie, Susie, Joey)              |")
print("| ----------|-------------------------|    |------------|-----------------------------------------------------------------|")
print("| jeff      | Jeff Johansen           |    | plague     | The Plague (La Plaga) (Adiris)                                  |")
print("| ----------|-------------------------|    |------------|-----------------------------------------------------------------|")
print("| jane      | Jane Romero             |    | ghostface  | The Ghostface (Danny Johnson?)                                  |")
print("| ----------|-------------------------|    |------------|-----------------------------------------------------------------|")
print("| ash       | Ashley J. Williams      |    | demogorgon | The Demogorgon (El Demogorgon) (???)                            |")
print("| ----------|-------------------------|    |------------|-----------------------------------------------------------------|")
print("| nacy      | Nancy Wheeler           |    | oni        | The Oni (El Oni) (Kazan Yamaoka)                                |")
print("| ----------|-------------------------|    |------------|-----------------------------------------------------------------|")
print("| steve     | Steve Harrington        |    | gunslinger | The Deathslinger (El Arponero de la Muerte) (Caleb Quinn)       |")
print("| ----------|-------------------------|    |------------|-----------------------------------------------------------------|")
print("| yui       | Yui Kimura              |    | k20        | The Executioner (Pyramid Head)                                  |")
print("| ----------|-------------------------|    |------------|-----------------------------------------------------------------|")
print("| zarina    | Zarina Kassir           |    | k21        | The Blight (El Deterioro) (Talbot Grimes)                       |")
print("| ----------|-------------------------|    |------------|-----------------------------------------------------------------|")
print("| s22       | Cheryl Manson           |    | k22        | The Twins (Los Gemelos) (Charlotte & Victor Deshayes)           |")
print("| ----------|-------------------------|    |------------|-----------------------------------------------------------------|")
print("| s23       | Felix Ritcher           |    | k23        | The Trickster (El Traicionero) (Ji-Woon Hak)                    |")
print("| ----------|-------------------------|    |------------|-----------------------------------------------------------------|")
print("| s24       | Éliode Rakoto           |    | k24        | The Nemesis (Némesis)                                           |")
print("| ----------|-------------------------|    |------------|-----------------------------------------------------------------|")
print("| s25       | Yun-Jin Lee             |    | k25        | The Cenobite (El Cenobita) (Pinhead)                            |")
print("| ----------|-------------------------|    |------------|-----------------------------------------------------------------|")
print("| s26       | Jill Valentine          |    | k26        | The Artist (La Artista) (Carmina Mora)                          |")
print("| ----------|-------------------------|    |------------|-----------------------------------------------------------------|")
print("| s27       | Leon S. Kennedy         |    | k27        | The Onryō (La Onryō) (Sadako Yamamura)                          |")
print("| ----------|-------------------------|    |------------|-----------------------------------------------------------------|")
print("| s28       | Mikaela Reid            |    | k28        | The Dredge (La Draga) (????)                                    |")
print("| ----------|-------------------------|    |------------|-----------------------------------------------------------------|")
print("| s29       | Jonah Vazquez           |    | k29        | The Mastermind (La Mente Maestra) (Alber Wesker)                |")
print("| ----------|-------------------------|    |------------|-----------------------------------------------------------------|")
print("| s30       | Yoichi Asakawa          |    | k30        | The Knight (El Caballero) (Tarhos Kovács)                       |")
print("| ----------|-------------------------|    |------------|-----------------------------------------------------------------|")
print("| s31       | Haddie Kaur             |    | k31        | The Skull Merchant (La Comerciante de Calaveras) (Adriana Imai) |")
print("| ----------|-------------------------|    |------------|-----------------------------------------------------------------|")
print("| s32       | Ada Wong                |    | k32        | The Singularity (La Singularidad) (HUX-A7-13)                   |")
print("| ----------|-------------------------|    |------------|-----------------------------------------------------------------|")
print("| s33       | Rebecca Chambers        |    | k33        | The Xenomorph (El Xenomorfo) (Alien)                            |")
print("| ----------|-------------------------|    |------------|-----------------------------------------------------------------|")
print("| s34       | Vitorio Toscano         |    | k34        | The Good Guy (El Chico bueno) (Charles Lee Ray)                 |")
print("| ----------|-------------------------|    |------------|-----------------------------------------------------------------|")
print("| s35       | Thalita Lyra            |    | k35        | The Unknown (Lo Desconocido) (????)                             |")
print("|-----------|-------------------------|    |____________|_________________________________________________________________|")
print("| s36       | Renato Lyra             |                                                                                    ")
print("|-----------|-------------------------|                                                                                    ")
print("| s38       | Nicolas Cage            |                                                                                    ")
print("|-----------|-------------------------|                                                                                    ")
print("| s39       | Ellen Ripley            |                                                                                    ")
print("|-----------|-------------------------|                                                                                    ")
print("| s40       | Alan Wake               |                                                                                    ")
print("|-----------|-------------------------|                                                                                    ")
print("| s41       | Sable Ward              |                                                                                    ")
print("|___________|_________________________|                                                                                    ")


# Mensaje de indicación para el usuario.
print("Por favor, introduzca el ID del personaje del que quiera conocer su información:")

# Leer la entrada del usuario.
character_name = input("ID: ")

# Llamar a la función para obtener información del personaje.
get_character_info(character_name)

# Bucle para solicitar al usuario que ingrese el ID del personaje hasta que se proporcione uno válido.
while True:
    # Leer la entrada del usuario.
    character_name = input("ID: ")
    
    # Llamar a la función para obtener información del personaje.
    get_character_info(character_name)
    
    # Preguntar al usuario si desea intentarlo nuevamente si hubo un error de solicitud o si quiere ingresar otro ID.
    retry = input("¿Desea intentarlo de nuevo? (s/n): ")
    if retry.lower() != 's':
        break  # Salir del bucle si el usuario no quiere intentarlo de nuevo.