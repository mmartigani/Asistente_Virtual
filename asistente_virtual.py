from http.client import MOVED_PERMANENTLY
import pyttsx3
import speech_recognition as sr
import pywhatkit
from tomlkit import date
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

#escuchar nuestro microfono y devolver
#el audio como texto

def transformar_audio_en_texto():
    
    #almacenar el recognizer en una var 
    r=sr.Recognizer()
    #configurar el microfono
    with sr.Microphone() as origen:
        #tiempo de espera
        r.pause_threshold=0.8
        #informar que comenzo la grabacion 
        print('ya puedes hablar')
        #guardar lo que escuche en un audio 
        audio=r.listen(origen)
        try:
            #buscar en google
            pedido=r.recognize_google(audio, language="es-ar")
            #prueba de que puedo ingresar 
            print("Dijiste: " + pedido)
            
            #devolcer el pedido
            return pedido
        #en caso de que no lo pueda hacer 
        except sr.UnknownValueError:
               
               #prueba de que no comprendio el audio
               print("ups , no entendio")
               #devolver error 
               return "sigo esperando"
        except sr.RequestError:
                #prueba de que no comprendio el audio
               print("ups , no hay servicio")
               #devolver error 
               return "sigo esperando"
        #error inesperado
        except:
            #prueba de que no comprendio el audio
               print("ups , algo salio mal")
               #devolver error 
               return "sigo esperando"
           
           
#transformar_audio_en_texto()

#funcion para que el asistente pueda ser escuchado 

def hablar(mensaje):
    
    #encender el motor pyttsx3
    engine=pyttsx3.init()
    engine.setProperty('voice',id1)
    #pronunciar el mensaje
    engine.say(mensaje)
    engine.runAndWait()
    


#para visualizar mis opciones 
#de idiomas en mi pc
#engine=pyttsx3.init()
#for voz in engine.getProperty('voices'):
    #print(voz)

id1="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0"


#hablar("hola deby. buenos dias. que deseas desayunar")

#pedir dia de la semana 
def pedir_dia():
    dia=datetime.date.today()
    #print(dia)
    
    dia_semana=dia.weekday()
    #print(dia_semana)
    
    calendario={0:'lunes',
                1:'martes',
                2:'miercoles',
                3:'jueves',
                4:'viernes',
                5:'sabado',
                6:'domingo'}
    hablar(f'Hoy es {calendario[dia_semana]}')

pedir_dia()

#informar la hora
def pedir_hora():
    hora=datetime.datetime.now()
    hora=f'en este momneto son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    hablar(hora)
    
pedir_hora()

#saludo inicial 
def saludo_inicial():
    hora=datetime.datetime.now()
    if hora.hour <6 or hora.hour >20:
        momento="buenas noches"
    elif 6 <=  hora.hour  <13:
        momento="buen dia"
    else:
        momento='buenas tardes'
    
    hablar(f'{momento}, Soy Deby , tu asistente personal. Por favor, dime en que puedo ayudarte ')

#saludo_inicial()

#funcion central del asistente 

def pedir():
    
    saludo_inicial()
    comenzar=True
    while comenzar:
        pedido=transformar_audio_en_texto().lower()
        if 'abrir youtube' in pedido:
            hablar('Estoy abriendo YouTube')
            webbrowser.open('https://youtube.com')
            continue
        elif 'abrir google'in pedido:
            hablar('Estoy en eso')
            webbrowser.open('https://www.google.com')
            continue
        elif 'que dia es hoy'in pedido:
            pedir_dia()
            continue
        elif 'que hora es' in pedido:
            pedir_hora()
            continue
        elif 'buscar en wikipedia' in pedido:
            hablar('buscando en wikipedia')
            pedido=pedido.replace('wikipedia', '')
            wikipedia.set_lang('es')
            resultado=wikipedia.summary(pedido, sentences=1)
            hablar('wikipedia dice lo siguiente')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('ahora estoy en eso')
            pedido=pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('esto es lo que encontre')
        elif 'reproducir' in pedido:
            hablar('ya comienzo a reproducirlo')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
     
        elif 'gracias' in pedido:
            hablar('hasta pronto')
            break
            
pedir()
