# Desarrollar una clase RedSocial que permita crear perfiles de usuarios, agregar amigos, publicar mensajes y dar "me gusta" a las publicaciones.

class RedSocial:

    users = []
    cantUsers = 0

    def __init__(self, nombre, maxUsers):
        self.nombre = nombre
        self.maxUsers = maxUsers

    def addUser (self, usuario):
        self.users.append(usuario)

    def registrarse(self, user):
        if self.cantUsers < self.maxUsers:
            data = {

            }
            data['name'] = user.name
            data['age']= user.age
            data['ID'] = user.id

            self.addUser(data)

            data = {}

            self.plusUser()

        else:
            print(f'Se ha alcanzado el número máximo de usuarios. No podemos registrar a {user.name}')


    def plusUser(self):
        self.cantUsers += 1

    @property
    def showUsers(self):
        print(self.users)



class Usuario:
    last_id = 0
    connections = []
    connections_request = []
    def __init__(self, name, age):
      self.name = name
      self.age = age
      self.id = Usuario.generate_id()

    @classmethod
    def generate_id(self):
        self.last_id += 1
        return self.last_id

    def requestConnection(self, usuario):
        dic = {'nombre': self.name, 'id': self.id}
        if dic not in usuario.connections and dic not in usuario.connections_request:
            usuario.connections_request.append(dic)
        elif dic in usuario.connections:
            print(f'Ya estás entre los amigos de {usuario.name}')
        elif dic in usuario.connections_request:
            print(f'Ya has enviado una solicitud de amistad.')

    @property
    def showCReqs(self):
        if len(self.connections_request) > 0:
            for req in self.connections_request:
                print (f'{req["nombre"]} (ID: {req["id"]}) te ha enviado una solicitud de conección.')
        elif len(self.connections_request) < 1:
            print ('No tienes solicitudes de conección.')

    def accCReqs(self, nombre, id):
        conn = {'nombre': nombre, 'id': id}
        for i in range (len(self.connections_request)):
            if self.connections_request[i] == conn:
                self.connections.append(conn)
                del self.connections_request[i]

    @property
    def showConn(self):
        print('Amigos:')
        for conn in self.connections:
            print(f"     Nombre: {conn['nombre']} (ID: {conn['id']})")

facebook = RedSocial('Facebook', 10)
julian_martinez = Usuario('Julian Martinez', 24)
manuel_martinez = Usuario('Manucho Martinez', 20)
nicolas_martinez = Usuario('Nicolas Martinez', 17)
paula_acciarri = Usuario('Paula Acciarri', 25)
facebook.registrarse(julian_martinez)
facebook.registrarse(manuel_martinez)
facebook.registrarse(nicolas_martinez)
facebook.registrarse(manuel_martinez)
facebook.registrarse(paula_acciarri)

julian_martinez.requestConnection(nicolas_martinez)

nicolas_martinez.connections_request
nicolas_martinez.accCReqs('Julian Martinez', 1)
julian_martinez.requestConnection(nicolas_martinez)
julian_martinez.requestConnection(nicolas_martinez)
nicolas_martinez.showConn



