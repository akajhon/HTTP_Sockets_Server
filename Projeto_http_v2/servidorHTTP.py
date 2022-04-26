import os
import socket

SERVER_HOST = ""
SERVER_PORT = 5050

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((SERVER_HOST, SERVER_PORT))

server_socket.listen(1)

print("Servidor em execução...")
print("Escutando por conexões na porta %s" % SERVER_PORT)

while True:
    client_connection, client_address = server_socket.accept()

    request = client_connection.recv(1024).decode()
    if request:
        print(request)
        
        headers = request.split("\n")
        
        print("\n\n\n*****Segue aqui as headers: " + str(headers))

        print("\n\n\n*****Segue aqui as headers na posição zero: " +str(headers[0]))

        solicitacao = str(headers[0]).split("/")[0]
        solicitacao = solicitacao.replace(" ","")
        print("\n\n\n*****Segue aqui a solicitação do usuário: " + solicitacao)

        filename = headers[0].split()[1]


        print("\n\n*****Segue aqui o filename: " + str(filename))
        if solicitacao == "GET":
            if filename == "/":
                filename = "/index.html"

            try:
                fin = open("htdocs" + filename)
                content = fin.read()
                fin.close()
                response = "HTTP/1.1 200 OK\n\n" + content
            except FileNotFoundError:
                response = "HTTP/1.1 404 NOT FOUND\n\n<h1>ERROR 404!<br>File Not Found!</h1>"


            client_connection.sendall(response.encode())
        
        elif solicitacao == "DELETE":
            if os.path.exists("htdocs" + str(filename)):
                    print("******Este é o Filename: " + str(filename))
                    fin = open("htdocs" + str(filename))
                    fin.close()
                    os.remove("htdocs" + str(filename))

                    response = "HTTP/1.1 200 OK\n\n<h1>Arquivo Apagado!!!</h1>"

            else:
                response = "HTTP/1.1 404 NOT FOUND\n\n<h1>ERROR 404!<br>File Not Found!</h1>"

            client_connection.sendall(response.encode())

        elif solicitacao == "PUT":
            if not os.path.exists("htdocs" + str(filename)):
                    print("******Este é o Filename: " + str(filename))
                    fin = open("htdocs" + str(filename), "w")
                    fin.close()
                    response = "HTTP/1.1 200 OK\n\n<h1>Arquivo Criado!!!</h1>" 

                    
            else:
                print("entrei no else")
                response = "HTTP/1.1 404 NOT FOUND\n\n<h1>ERROR 204!<br>File Not Found!</h1>"

            client_connection.sendall(response.encode())
        
        elif solicitacao == "POST":
            if os.path.exists("htdocs" + str(filename)):
                    print("******Este é o Filename: " + str(filename))
                    fin = open("htdocs" + str(filename), "a")
                    fin.write("oi")
                    fin.close()
                    response = "HTTP/1.1 200 OK\n\n" 

            else:
                print("entrei no else")
                response = "HTTP/1.1 404 NOT FOUND\n\n<h1>ERROR 204!<br>File Not Found!</h1>"

            client_connection.sendall(response.encode())
            

        client_connection.close()

server_socket.close()
