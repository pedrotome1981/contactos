with open("contactos.csv", 'r') as contactos_file:
    contents = contactos_file.read().splitlines()

    for row in contents:
        row_data = row.split(",")
        print(f"O {row_data[0]} é natural {row_data[1]}, o seu contacto telefónico é o {row_data[2]} e o seu email é o {row_data[3]}")
    contactos_file.close()
