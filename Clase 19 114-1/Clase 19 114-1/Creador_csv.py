nombres_columnas = ["pregunta,""respuesta_1","respuesta_2","respuesta_2","respuesta_3","respuesta_4","respuesta_correcta"]
matriz = [
    # Pregunta 1
    ["¿En qué ciudad nació Lionel Messi?",
     {"respuesta_1": "Rosario", "respuesta_2": "Buenos Aires", "respuesta_3": "Córdoba", "respuesta_4": "Posadas", "respuesta_correcta": 1}],
    
    # Pregunta 2
    ["¿Cuál es la capital de Argentina?",
     {"respuesta_1": "Buenos Aires", "respuesta_2": "Córdoba", "respuesta_3": "Rosario", "respuesta_4": "Mendoza", "respuesta_correcta": 1}],
    
    # Pregunta 3
    ["¿En qué año ganó Argentina su primer mundial de fútbol?",
     {"respuesta_1": "1978", "respuesta_2": "1986", "respuesta_3": "2002", "respuesta_4": "1930", "respuesta_correcta": 1}],
    
    # Pregunta 4
    ["¿Quién es conocido como el 'Padre de la Patria' en Argentina?",
     {"respuesta_1": "Juan Manuel de Rosas", "respuesta_2": "José de San Martín", "respuesta_3": "Manuel Belgrano", "respuesta_4": "Bernardino Rivadavia", "respuesta_correcta": 2}],
    
    # Pregunta 5
    ["¿Cuál es el pico más alto de Argentina?",
     {"respuesta_1": "Cerro Aconcagua", "respuesta_2": "Cerro Tronador", "respuesta_3": "Cerro Fitz Roy", "respuesta_4": "Nevado Ojos del Salado", "respuesta_correcta": 1}],
    
    # Pregunta 6
    ["¿Qué río separa a Argentina de Uruguay?",
     {"respuesta_1": "Río Paraná", "respuesta_2": "Río Colorado", "respuesta_3": "Río de la Plata", "respuesta_4": "Río Uruguay", "respuesta_correcta": 3}],
    
    # Pregunta 7
    ["¿Quién compuso la canción 'Gracias a la Vida'?",
     {"respuesta_1": "Mercedes Sosa", "respuesta_2": "Charly García", "respuesta_3": "Violeta Parra", "respuesta_4": "Fito Páez", "respuesta_correcta": 3}],
    
    # Pregunta 8
    ["¿En qué año fue elegido presidente Néstor Kirchner?",
     {"respuesta_1": "2000", "respuesta_2": "2003", "respuesta_3": "2007", "respuesta_4": "1999", "respuesta_correcta": 2}],
    
    # Pregunta 9
    ["¿En qué provincia se encuentra la ciudad de Ushuaia?",
     {"respuesta_1": "Santa Cruz", "respuesta_2": "Chubut", "respuesta_3": "Tierra del Fuego", "respuesta_4": "Neuquén", "respuesta_correcta": 3}],
    
    # Pregunta 10
    ["¿Qué moneda se utiliza en Argentina?",
     {"respuesta_1": "Dólar", "respuesta_2": "Peso", "respuesta_3": "Real", "respuesta_4": "Euro", "respuesta_correcta": 2}],
    
    # Pregunta 11
    ["¿Qué famoso cantante argentino popularizó el tango?",
     {"respuesta_1": "Astor Piazzolla", "respuesta_2": "Carlos Gardel", "respuesta_3": "Sandro", "respuesta_4": "Luis Alberto Spinetta", "respuesta_correcta": 2}],
    
    # Pregunta 12
    ["¿Cuál es la danza tradicional de Argentina?",
     {"respuesta_1": "Salsa", "respuesta_2": "Cumbia", "respuesta_3": "Tango", "respuesta_4": "Cueca", "respuesta_correcta": 3}],
    
    # Pregunta 13
    ["¿Cuál es el nombre del famoso glaciar en la Patagonia?",
     {"respuesta_1": "Perito Moreno", "respuesta_2": "Martial", "respuesta_3": "Upsala", "respuesta_4": "Viedma", "respuesta_correcta": 1}],
    
    # Pregunta 14
    ["¿Quién es el autor de 'Martín Fierro'?",
     {"respuesta_1": "Jorge Luis Borges", "respuesta_2": "José Hernández", "respuesta_3": "Julio Cortázar", "respuesta_4": "Ricardo Güiraldes", "respuesta_correcta": 2}],
    
    # Pregunta 15
    ["¿Cuál es la montaña más alta de América del Sur?",
     {"respuesta_1": "Cerro Bonete", "respuesta_2": "Monte Pissis", "respuesta_3": "Aconcagua", "respuesta_4": "Nevado del Huila", "respuesta_correcta": 3}],
    
    # Pregunta 16
    ["¿Qué bebida es famosa en Argentina?",
     {"respuesta_1": "Tequila", "respuesta_2": "Mate", "respuesta_3": "Pisco", "respuesta_4": "Café", "respuesta_correcta": 2}],
    
    # Pregunta 17
    ["¿Cuál es el nombre del teatro más famoso de Buenos Aires?",
     {"respuesta_1": "Teatro Colón", "respuesta_2": "Teatro Gran Rex", "respuesta_3": "Teatro Nacional", "respuesta_4": "Luna Park", "respuesta_correcta": 1}],
    
    # Pregunta 18
    ["¿Cuál es la Avenida más ancha del mundo ubicada en Buenos Aires?",
     {"respuesta_1": "Avenida de Mayo", "respuesta_2": "Avenida Corrientes", "respuesta_3": "Avenida 9 de Julio", "respuesta_4": "Avenida Libertador", "respuesta_correcta": 3}],
    
    # Pregunta 19
    ["¿Qué prócer argentino creó la bandera?",
     {"respuesta_1": "Domingo Sarmiento", "respuesta_2": "José de San Martín", "respuesta_3": "Manuel Belgrano", "respuesta_4": "Juan Lavalle", "respuesta_correcta": 3}],
    
    # Pregunta 20
    ["¿Qué actriz argentina fue esposa de Juan Domingo Perón?",
     {"respuesta_1": "Tita Merello", "respuesta_2": "Eva Perón", "respuesta_3": "Libertad Lamarque", "respuesta_4": "China Zorrilla", "respuesta_correcta": 2}],
    
    # Pregunta 21
    ["¿En qué año fue la Guerra de las Malvinas?",
     {"respuesta_1": "1980", "respuesta_2": "1982", "respuesta_3": "1984", "respuesta_4": "1978", "respuesta_correcta": 2}],
    
    # Pregunta 22
    ["¿Cuál es el nombre del equipo de fútbol conocido como 'La Academia'?",
     {"respuesta_1": "Boca Juniors", "respuesta_2": "Racing Club", "respuesta_3": "River Plate", "respuesta_4": "San Lorenzo", "respuesta_correcta": 2}],
    
    # Pregunta 23
    ["¿En qué provincia se encuentra la ciudad de Mendoza?",
     {"respuesta_1": "Santa Fe", "respuesta_2": "San Juan", "respuesta_3": "Mendoza", "respuesta_4": "La Rioja", "respuesta_correcta": 3}],
    
    # Pregunta 24
    ["¿Cuál es el ave nacional de Argentina?",
     {"respuesta_1": "Cóndor", "respuesta_2": "Ñandú", "respuesta_3": "Hornero", "respuesta_4": "Tero", "respuesta_correcta": 3}],
    
    # Pregunta 25
    ["¿Qué escritora argentina ganó el Premio Cervantes en 2018?",
     {"respuesta_1": "Silvina Ocampo", "respuesta_2": "María Elena Walsh", "respuesta_3": "María Teresa Andruetto", "respuesta_4": "Ida Vitale", "respuesta_correcta": 3}],
    
    # Pregunta 26
    ["¿Cuál es el símbolo químico del oro?",
     {"respuesta_1": "Au", "respuesta_2": "Ag", "respuesta_3": "O", "respuesta_4": "Gd", "respuesta_correcta": 1}],
    
    # Pregunta 27
    ["¿Cuál es el océano que baña la costa este de Argentina?",
     {"respuesta_1": "Océano Atlántico", "respuesta_2": "Océano Pacífico", "respuesta_3": "Mar Caribe", "respuesta_4": "Mar Mediterráneo", "respuesta_correcta": 1}],
    
    # Pregunta 28
    ["¿Qué científico argentino ganó el Premio Nobel en 1947?",
     {"respuesta_1": "Luis Leloir", "respuesta_2": "César Milstein", "respuesta_3": "Bernardo Houssay", "respuesta_4": "René Favaloro", "respuesta_correcta": 3}],
    
    # Pregunta 29
    ["¿Cuál es la capital de la provincia de Córdoba?",
     {"respuesta_1": "Río Cuarto", "respuesta_2": "Córdoba", "respuesta_3": "Carlos Paz", "respuesta_4": "Villa María", "respuesta_correcta": 2}],
    
    # Pregunta 30
    ["¿Qué deporte practica la selección conocida como 'Los Pumas'?",
     {"respuesta_1": "Fútbol", "respuesta_2": "Hockey", "respuesta_3": "Rugby", "respuesta_4": "Básquet", "respuesta_correcta": 3}],
    
    # Pregunta 31
    ["¿Qué actriz protagonizó la película 'La historia oficial'?",
     {"respuesta_1": "Norma Aleandro", "respuesta_2": "Graciela Borges", "respuesta_3": "Soledad Silveyra", "respuesta_4": "Cecilia Roth", "respuesta_correcta": 1}],
    
    # Pregunta 32
    ["¿Qué provincia argentina es conocida por sus viñedos?",
     {"respuesta_1": "Salta", "respuesta_2": "Mendoza", "respuesta_3": "Jujuy", "respuesta_4": "La Pampa", "respuesta_correcta": 2}],
    
    # Pregunta 33
    ["¿Qué famoso escritor argentino escribió 'Fervor de Buenos Aires'?",
     {"respuesta_1": "Jorge Luis Borges", "respuesta_2": "Roberto Arlt", "respuesta_3": "Ernesto Sabato", "respuesta_4": "Manuel Puig", "respuesta_correcta": 1}],
    
    # Pregunta 34
    ["¿Cuál es el tren turístico que recorre la Patagonia?",
     {"respuesta_1": "Tren del Fin del Mundo", "respuesta_2": "Tren de las Sierras", "respuesta_3": "Tren Patagónico", "respuesta_4": "Tren de la Quebrada", "respuesta_correcta": 3}],
    
    # Pregunta 35
    ["¿Qué animal es símbolo de la fauna patagónica?",
     {"respuesta_1": "Yacaré", "respuesta_2": "Puma", "respuesta_3": "Guanaco", "respuesta_4": "Tucán", "respuesta_correcta": 3}],
    
    # Pregunta 36
    ["¿Qué ciudad argentina es famosa por su Fiesta Nacional de la Vendimia?",
     {"respuesta_1": "San Juan", "respuesta_2": "Mendoza", "respuesta_3": "Salta", "respuesta_4": "Tucumán", "respuesta_correcta": 2}],
    
    # Pregunta 37
    ["¿Qué importante científico desarrolló el bypass coronario?",
     {"respuesta_1": "Luis Leloir", "respuesta_2": "Bernardo Houssay", "respuesta_3": "César Milstein", "respuesta_4": "René Favaloro", "respuesta_correcta": 4}],
    
    # Pregunta 38
    ["¿Qué provincia limita con Bolivia y Paraguay?",
     {"respuesta_1": "Salta", "respuesta_2": "Jujuy", "respuesta_3": "Formosa", "respuesta_4": "Chaco", "respuesta_correcta": 3}],
    
    # Pregunta 39
    ["¿Qué jugador argentino ganó 7 Balones de Oro?",
     {"respuesta_1": "Diego Maradona", "respuesta_2": "Lionel Messi", "respuesta_3": "Alfredo Di Stéfano", "respuesta_4": "Mario Kempes", "respuesta_correcta": 2}],
    
    # Pregunta 40
    ["¿Qué ciudad fue sede de los Juegos Olímpicos de la Juventud 2018?",
     {"respuesta_1": "La Plata", "respuesta_2": "Rosario", "respuesta_3": "Buenos Aires", "respuesta_4": "Córdoba", "respuesta_correcta": 3}],
    
    # Pregunta 41
    ["¿Qué cadena montañosa recorre el oeste argentino?",
     {"respuesta_1": "Los Pirineos", "respuesta_2": "Los Alpes", "respuesta_3": "Los Andes", "respuesta_4": "La Sierra de Córdoba", "respuesta_correcta": 3}],
    
    # Pregunta 42
    ["¿Qué festividad se celebra el 25 de mayo en Argentina?",
     {"respuesta_1": "Día de la Independencia", "respuesta_2": "Día de la Revolución de Mayo", "respuesta_3": "Día de la Bandera", "respuesta_4": "Día del Trabajador", "respuesta_correcta": 2}],
    
    # Pregunta 43
    ["¿Qué actor protagonizó 'El secreto de sus ojos'?",
     {"respuesta_1": "Leonardo Sbaraglia", "respuesta_2": "Guillermo Francella", "respuesta_3": "Ricardo Darín", "respuesta_4": "Pablo Rago", "respuesta_correcta": 3}],
    
    # Pregunta 44
    ["¿Qué provincia es conocida por sus empanadas y la Casa Histórica?",
     {"respuesta_1": "Salta", "respuesta_2": "Catamarca", "respuesta_3": "Tucumán", "respuesta_4": "La Rioja", "respuesta_correcta": 3}],
    
    # Pregunta 45
    ["¿Cuál es la ciudad más poblada del país?",
     {"respuesta_1": "Rosario", "respuesta_2": "Buenos Aires", "respuesta_3": "Córdoba", "respuesta_4": "La Plata", "respuesta_correcta": 2}],
    
    # Pregunta 46
    ["¿Qué músico argentino compuso 'Canción Animal'?",
     {"respuesta_1": "Fito Páez", "respuesta_2": "Gustavo Cerati", "respuesta_3": "Charly García", "respuesta_4": "Luis Alberto Spinetta", "respuesta_correcta": 2}],
    
    # Pregunta 47
    ["¿En qué provincia se encuentran las Ruinas de Quilmes?",
     {"respuesta_1": "Tucumán", "respuesta_2": "Catamarca", "respuesta_3": "Salta", "respuesta_4": "Santiago del Estero", "respuesta_correcta": 1}],
    
    # Pregunta 48
    ["¿Qué periodista y conductor fue símbolo de la TV argentina y falleció en 2019?",
     {"respuesta_1": "Marcelo Tinelli", "respuesta_2": "Chiche Gelblung", "respuesta_3": "Juan Alberto Badía", "respuesta_4": "Marcelo Zlotogwiazda", "respuesta_correcta": 4}],
    
    # Pregunta 49
    ["¿Qué artista argentino pintó 'La canción del pueblo'",
     {"respuesta_1": "Antonio Berni", "respuesta_2": "Xul Solar", "respuesta_3": "Benito Quinquela Martín", "respuesta_4": "Eduardo Sívori", "respuesta_correcta": 1}],
    
    # Pregunta 50
    ["¿Qué nombre recibe la región noreste de Argentina?",
     {"respuesta_1": "NOA", "respuesta_2": "NEA", "respuesta_3": "Pampa Húmeda", "respuesta_4": "Patagonia", "respuesta_correcta": 2}]
]


with open("Preguntas.csv", "w",encoding="utf-8") as archivo:
    archivo.write(",".join(nombres_columnas) + "\n")

    for fila in matriz :
        linea = ""
        for i in range(len(fila)):
            linea += str(fila[i])
            if i < (len(fila) -1 ):
                linea += ","
        archivo.write(linea +"\n")

