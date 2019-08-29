
class CipherOrDecipher(object):
    #Propiedade para definir el diccionario de nuestro cifrado
    ABC = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    # Propiedad que guardará el mensaje del usuario
    message = None
    # Propiedad que guardará la opción que ha elegido el usuario (Cifrar o Descifrar)
    action = None

    # Constructor por defecto
    def __init__(self, message, action):
        self.message = message
        self.action = action
    # Método que iniciará el algoritmo para cifrar o descifrar
    def start_algorithm(self):
        new_message = ""
        
        for letter in self.message:
            if letter in self.ABC:
                new_letter = (
                        self.ABC[(self.ABC.find(letter) + 11) % 27],
                        self.ABC[(self.ABC.find(letter) - 11) % 27]
                    )[self.action=="decipher"]

                new_message = new_message + new_letter
            elif letter in self.ABC.lower():
                new_letter = (
                    self.ABC[(self.ABC.lower().find(letter) + 11) % 27],
                    self.ABC[(self.ABC.lower().find(letter) - 11) % 27]
                )[self.action=="decipher"]

                new_message = new_message + new_letter.lower()
            elif letter == ' ':
                new_message = new_message + ' '

        return new_message
