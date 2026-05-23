from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def usuarios(request):

    lista_usuarios = [
        {"nome": "Rubens", "matricula": "1464", "idade": 25},
        {"nome": "Erizebete", "matricula": "1357", "idade": 20},
        {"nome": "José da Silva Sauro", "matricula": "1235", "idade": 42},
        {"nome": "Sinvastantino ", "matricula": "2314", "idade": 57},
        {"nome": "Luigi", "matricula": "3197", "idade": 31}
   
    ]

    context = {
        "usuarios": lista_usuarios
    }

    return render(request, "usuarios.html", context)