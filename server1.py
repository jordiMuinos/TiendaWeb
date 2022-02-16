# serve.py
import hashlib
import json
from urllib import response
from flask import Flask, redirect, url_for, make_response
from flask import render_template
from flask import request,session,jsonify
import os
import pathlib

from jinja2 import Undefined

def eliminarProd(id):
    tienda={}
    with open("datos_tienda.json",'r') as file:
        tienda=json.load(file)
        file.close()
    productos=tienda["productos"];
    pEliminar=None;
    for item in productos:
        if (item["id"]==id):
            pEliminar=item;
            break;
    productos.remove(pEliminar);
    with open("datos_tienda.json",'w') as file:
        json.dump(tienda,file,indent=2);
        file.close();
    return productos;


def guardarProducto(nombreProducto,descripcion,filename,precio,cantidad):
    tienda={}
    with open("datos_tienda.json",'r') as file:
        tienda=json.load(file)
        file.close()
    
    if("contador" in tienda.keys()):
        tienda["contador"]+=1
    else:
        tienda["contador"]=0
    contador=tienda["contador"]

    tienda["productos"].append(
        {"nombre":nombreProducto,
        "descripcion":descripcion,
        "img":filename,
        "precio":precio,
        "cantidad":cantidad,
        "id":contador
        })
    
    with open("datos_tienda.json",'w') as file:
        json.dump(tienda,file,indent=2);
        file.close();
    return tienda["productos"];

def nombreUnico(fichero,directorio):
    dir=pathlib.Path(directorio)
    encontrado=False;
    for file in dir.iterdir():
        if(file.name==fichero):
            encontrado=True
            break
    if(not encontrado):
        return fichero
    contador=fichero.split(".")[0][len(fichero.split(".")[0])-1]
    cont=0
    if(contador.isnumeric()):
        cont=int(contador)+1
    fichero=fichero.split(".")[0]+str(cont)+"."+fichero.split(".")[1]
    return nombreUnico(fichero,directorio)

def validar(usuario,password):
    tienda={};
    with open("datos_tienda.json","r") as file:
        tienda=json.load(file)
        file.close();
    for user in tienda["usuarios"]:
        if usuario==user["nombre"] and hashlib.sha224(bytes(password,encoding="utf-8")).hexdigest()==user["password"]:
            return True
    return False


def comprobarUsuario(usuario):
    tienda={}
    with open("datos_tienda.json","r") as file:
        tienda=json.load(file)
        file.close();
    for user in tienda["usuarios"]:
        if usuario==user["nombre"]:
            return True
    return False

def registrarUsuario(usuario,password):
    tienda={}
    with open("datos_tienda.json","r") as file:
        tienda=json.load(file)
        file.close();

    tienda["usuarios"].append({"nombre":usuario,"password":hashlib.sha224(bytes(password,encoding="utf-8")).hexdigest()})
    
    with open("datos_tienda.json","w") as file:
        json.dump(tienda,file,indent=2);
        file.close();

def leerProductos():
    tienda={}
    with open("datos_tienda.json","w") as file:
        json.dump(tienda,file,indent=2);
        file.close();
    return tienda["productos"];

# creates a Flask application, named app
app = Flask(__name__,static_folder='templates/static')

# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():
    #message = "Hello, World"
    dato=[1,2,3,4,5]
    return render_template('index.html',message=dato)

@app.route('/producto')
def paginaProducto():
    #name = request.cookies.get("cooki")
    nombreUsuario=session.get("nombreUsuario");
    if(nombreUsuario==None):
        return redirect(url_for("login"));
    else:
        return render_template('index.html', usuario=nombreUsuario)

@app.route('/crearproducto',methods=['GET','POST'])
def crearProducto():
    if(request.method=='GET'):
        return render_template("formularioProductos.html")
    else:
        nombreProducto=request.form["producto"]
        descripcion=request.form["comentario"]
        f=request.files["imgProducto"]
        filename =f.filename;
        filename=nombreUnico(filename,"./templates/static/img")
        precio=request.form["precio"]
        cantidad=request.form["cantidad"]
        
        f.save(os.path.join('./templates/static/img',filename))
        productos=guardarProducto(nombreProducto,descripcion,filename,precio,cantidad)
        print(productos);
        return redirect(url_for("crearProducto"))

@app.route('/login',methods = ['POST','GET'])
def login():
    if(request.method=='GET'):
        return render_template('login.html')
    elif(request.method=='POST'):
        usuario=request.form["usuario"];
        password=request.form["password"];
        if validar(usuario,password):
   
            #resp = make_response(render_template('index.html'))
            resp=make_response(redirect(url_for('paginaProducto')))
            #resp.set_cookie('cooki',str(hash(usuario)))
            session["nombreUsuario"]=usuario;
            return resp
            #return redirect(url_for('paginaProducto'))
        else:
            #return render_template('index.html')
            msg="usuario o contraseña incorrecto"
            return render_template('login.html',mensage=msg)

@app.route('/procesarlogin',methods = ['POST]'])
def procesar():
    return "hola mundo"

@app.route('/registrar', methods = ['GET'])
def registrar():
    return render_template('registrar.html')

@app.route('/crearUsuario',methods = ['POST'])
def crearUsuario():
    usuario=request.form.get("usuario");
    password=request.form.get("password");
    if(comprobarUsuario(usuario)):
        msg="Usuario ya existe";
        return redirect(url_for("registrar",mensage=msg))
    else:

        registrarUsuario(usuario,password)
        return redirect(url_for("login",user=usuario))

@app.route('/getproducts', methods=['GET'])
def getProducts():
    productos=leerProductos()
    return jsonify(productos)


@app.route('/cerrarSesion')
def cerrarSesion():
    resp=make_response(redirect(url_for('login')))
    resp.delete_cookie('cooki')
    return resp

@app.route('/prueba')
def prueba():
    return "Hola Mundo"

@app.route('/eliminarproducto',methods=["GET","[POST]"])
def eliminarProducto():
    idproducto=int(request.args["id"])
    result=eliminarProd(idproducto)
    return jsonify(result);


# run the application
if __name__ == "__main__":
    app.secret_key = "generador de claves"
    app.run(host="localhost",port=8080,debug=True)


