import os
import socket

SERVER_HOST = ""
SERVER_PORT = 8000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)

print("Servidor em execução...")
print("Escutando por conexões na porta %s" % SERVER_PORT)

while True:
    client_connection, client_address = server_socket.accept()
    request = client_connection.recv(1024).decode()
    print("\n***********\n\n[+] Cliente {} realizando requisições !!!".format(client_address))
    if request:
        headers = request.split("\n")
        solicitacao = str(headers[0]).split("/")[0]
        solicitacao = solicitacao.replace(" ","")
        print("\n[+] Requisição do tipo: " + solicitacao)
        filename = headers[0].split()[1]
        
        if solicitacao == "GET":
            if filename == "/":
                filename = "/index.html"
            try:
                fin = open("htdocs" + filename)
                content = fin.read()
                fin.close()
                response = "HTTP/1.1 200 OK\n\n" + content
                print("\n[+] 200 - Success - Arquivo retornado ao cliente!!!")
            except FileNotFoundError:
                fin_error = open("htdocs/404_error.html")
                content_error = fin_error.read()
                fin_error.close()
                response = "HTTP/1.1 404 NOT FOUND\n\n" + content_error
                print("\n[+] 404 - Error - O Arquivo não foi encontrado no Servidor!!!")
            client_connection.sendall(response.encode())
        
        elif solicitacao == "DELETE":
            if os.path.exists("receitas" + str(filename)):
                    fin = open("receitas" + str(filename))
                    fin.close()
                    os.remove("receitas" + str(filename))
                    response = "HTTP/1.1 200 OK\n\n<h1> 200 - Success - Arquivo Apagado!!!</h1>"
                    print("\n[+] 200 - Success - Arquivo Apagado!!!")
            else:
                fin_error = open("htdocs/404_error.html")
                content_error = fin_error.read()
                fin_error.close()
                response = "HTTP/1.1 404 NOT FOUND\n\n" + content_error
                print("\n[+] 404 - Error - O Arquivo não foi encontrado no Servidor!!! **")
            client_connection.sendall(response.encode())

        elif solicitacao == "PUT":
            if headers[1] == '':
                receita = str(headers[0]).split(":")[1].split("}")[0].replace('"','')
            else:
                receita = str(headers[-1:]).split(":")[1].split("}")[0].replace('"','')
            if (receita == ""):
                fin_error = open("htdocs/400_error.html")
                content_error = fin_error.read()
                fin_error.close()
                response = "HTTP/1.1 400 BAD REQUEST\n\n" + content_error
                print("\n[+] 400 - Error - Houve um erro na requisição!!!")
            else:
                if not os.path.exists("receitas" + str(filename)):
                        fin = open("receitas" + str(filename), "w")
                        fin.write(receita)
                        fin.close()
                        response = "HTTP/1.1 201 OK\n\n<h1> 201 - Success - Arquivo Criado!!! </h1>" 
                        print("\n[+] 201 - Success - Arquivo Criado!!!")
                else:
                    fin = open("receitas" + str(filename), "w")
                    fin.write(receita)
                    fin.close()
                    response = "HTTP/1.1 200 OK\n\n<h1> 200 - Success -  Arquivo Sobrescrito!!! </h1>"
                    print("\n[+] 200 - Success - Arquivo Sobrescrito!!!") 
            client_connection.sendall(response.encode())
        
        elif solicitacao == "POST":
            if headers[1] == '':
                receita = str(headers[0]).split(":")[1].split("}")[0].replace('"','')
            else:
                receita = str(headers[-1:]).split(":")[1].split("}")[0].replace('"','')
            if (receita == ""):
                fin_error = open("htdocs/400_error.html")
                content_error = fin_error.read()
                fin_error.close()
                response = "HTTP/1.1 400 BAD REQUEST\n\n" + content_error
                print("\n[+] 400 - Error - Houve um erro na requisição!!!")
            else:
                if not os.path.exists("receitas" + str(filename)):      
                        fin = open("receitas" + str(filename), "w")
                        fin.write(receita)
                        fin.close()
                        response = "HTTP/1.1 201 OK\n\n<h1> 201 - Success -  Arquivo Criado!!! </h1>"
                        print("\n[+] 201 - Success - Arquivo Criado!!!") 
                else:
                        fin = open("receitas" + str(filename), "a")
                        fin.write(receita)
                        fin.close() 
                        response = "HTTP/1.1 200 OK\n\n<h1> 200 - Success - Arquivo Alterado!!! </h1>" 
                        print("\n[+] 200 - Success - Arquivo Alterado!!!")
            client_connection.sendall(response.encode())
            
        else:
            fin_error = open("htdocs/501_error.html")
            content_error = fin_error.read()
            fin_error.close()
            response = "HTTP/1.1 501 NOT IMPLEMENTED\n\n" + content_error
            print("\n[+] 501 - Error - O Servidor não suporta a funcionalidade requisitada!!!")
            client_connection.sendall(response.encode())

        client_connection.close()
server_socket.close()
