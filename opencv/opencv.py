from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin
import cv2
import face_recognition
import numpy as np

app = Flask(__name__)

@app.route('/asistencia_opencv', methods = ['POST'])
@cross_origin()
def asistencia_opencv():  #Funcion para obtener respuesta de la comparacion de rostros
    if request.method == 'POST':
        f = request.files['file']
        t = request.form['ubicacion']
        filename = f.filename
        f.save("C:/Users/pradi/Downloads/test/" + filename)   #Guarda la imagen a comparar con la otra imagen guardada.
        image = cv2.imread("C:/Users/pradi/Downloads/test/" + t) #Carga la imagen guardada del usuario.
        face_loc = face_recognition.face_locations(image)[0] #Encuentra ubicaciones que contengan rostros en la imagen
        hola = ""
        face_image_encodings = face_recognition.face_encodings(image, known_face_locations=[face_loc])[0] #Genera el vector de caracteristicas de la imagen guardada
        image2 = cv2.imread("C:/Users/pradi/Downloads/test/" + filename) #Carga la imagen a comparar para guardar la asistencia
        face_locations = face_recognition.face_locations(image2, model="mtcnn") #Detecta el rostro en la imagen a comparar
        #Compara el vector de caracteristicas del alumno con las ubicaciones encontradas en la imagen a comparar.
        if face_locations != []:
          for face_location in face_locations:
               face_frame_encodings = face_recognition.face_encodings(image2, known_face_locations=[face_location])[0]
               result = face_recognition.compare_faces([face_image_encodings], face_frame_encodings)
               hola=str(result[0])
    

        return hola #Devuelve la respuesta si existe coincidencia
    

#Funcion para subir la foto del usuario en el servidor.
@app.route('/upload_photo', methods = ['POST'])
@cross_origin()
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        t = request.form['dni']
        filename = f.filename
        test=filename.split(".")
        f.save("C:/Users/pradi/Downloads/test/" +t+"."+test[1]) 
        result=t+"."+test[1]
    return str(result)

if __name__ == '__main__':
    app.run(debug=True, port=5002)

