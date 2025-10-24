class Palindrome:
    def __init__(self, phrase):
        self.phrase = phrase

    def is_palindrome(self) -> bool:
        #Logica de programacion para determinar si es palindromo o no 
        # Limpiar la frase: quitar espacios y pasar a minúsculas
        cleaned = ''.join(c.lower() for c in self.phrase if c.isalnum())
        # Verificar si es igual al reverso
        if cleaned == cleaned[::-1]:
            return True
        else:
            return False