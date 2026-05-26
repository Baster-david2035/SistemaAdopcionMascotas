class Usuario:
    def __init__(self, id_usuario, nome, email, senha):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email
        self.senha = senha

    def __str__(self):
        return f"Usuario(id_usuario={self.id_usuario}, nome='{self.nome}', email='{self.email}')"