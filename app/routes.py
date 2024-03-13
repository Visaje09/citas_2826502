from . import app, db
from .models import Medico , Paciente , Cita , Consultorio
from flask import render_template, request , flash , redirect



@app.route("/medicos")
def get_all_medicos():
    medicos = Medico.query.all()
    return render_template("medicos.html" , medicos=medicos)

@app.route("/pacientes")
def get_all_pacientes():
    pacientes = Paciente.query.all()
    return render_template("pacientes.html" , pacientes=pacientes)

@app.route("/citas")
def get_all_citas():
    citas = Cita.query.all()
    return render_template("citas.html" , citas=citas)

@app.route("/consultorios")
def get_all_consultorios():
    consultorios = Consultorio.query.all()
    return render_template("consultorios.html" , consultorios=consultorios)
#crear ruta de medicos por id(get)

@app.route("/medicos/<int:id>")
def get_medico_by_id(id):
    medico = Medico.query.get(id)
    return render_template("medico.html",
                           med = medico )


@app.route("/pacientes/<int:id>")
def get_paciente_by_id(id):
    #return "id del medico:" + str(id) 
    #traer el medico por id utilizando la entidad medico 
    paciente = Paciente.query.get(id)
    #y meterlo en una lista 
    return render_template("paciente.html",
                           pac = paciente )


@app.route("/medicos/create", methods = ["GET", "POST"])
def create_medico():
    if(request.method == "GET" ):
        especialidades = [
            "Cardiologia", "Pediatra", "Argerologia"
        ]
        return render_template("medico_form.html", especialidades = especialidades)
    
    elif(request.method == "POST"):
        new_medico = Medico(nombre = request.form["nombre"],
                     apellido = request.form["apellidos"],
                     tipo_identificacion = request.form["ti"],
                     numero_identificacion = request.form["ni"],
                     registro_medico = request.form["rm"],
                     especialidad = request.form["es"] 
                     )
        db.session.add(new_medico)
        db.session.commit()
        flash("Medico registrado correctamente")
        return redirect("/medicos")
    
    
@app.route("/pacientes/create", methods = ["GET", "POST"])
def create_paciente():
    if(request.method == "GET" ):
        sangre = [
            "A+", "O+", "B+", "AB+" , "A-" , "O-" , "AB-"
        ]
        return render_template("paciente_form.html", sangre = sangre)
    
    elif(request.method == "POST"):
        new_paciente = Paciente(nombre = request.form["pnombre"],
                     apellido = request.form["papellidos"],
                     tipo_identificacion = request.form["pti"],
                     altura = request.form["paltura"],
                     tipo_sangre = request.form["blood"], 
                     )
        db.session.add(new_paciente)
        db.session.commit()
        return "Paciente registrado"     
     
    
@app.route("/consulorios/create", methods = ["GET", "POST"])
def create_consultorio():
    if(request.method == "GET" ):
        return render_template("consultorios_form.html",)
    
    elif(request.method == "POST"):
        new_consultorio = Consultorio(nombre = request.form["pnombre"],
                     apellido = request.form["papellidos"],
                     )
        db.session.add(new_consultorio)
        db.session.commit()
        return "Consultorio registrado"

@app.route("/medicos/update/<int:id>", methods=["POST" , "GET"])
def update_medico(id):
    especialidades = [
        "Cardiologia", "Pediatra", "Argerologia"
        
    ]
    medico_update = Medico.query.get(id)
    if(request.method == "GET"):
        return render_template("medico_update.html",
                           medico_update = medico_update, 
                           especialidades = especialidades)
    elif(request.method == "POST"):
        medico_update.nombre = request.form["nombre"] 
        medico_update.apellido = request.form["apellidos"] 
        medico_update.tipo_identificacion = request.form["ti"] 
        medico_update.numero_identificacion = request.form["ni"]
        medico_update.registro_medico = request.form["rm"] 
        medico_update.especialidad = request.form["es"]
        db.session.commit()
        return redirect("/medicos")
    
    
    
@app.route("/medicos/delete/<int:id>")
def delete_medico(id):
    medico_delete = Medico.query.get(id)
    db.session.delete(medico_delete)
    db.session.commit()
    return redirect("/medicos")  
    

