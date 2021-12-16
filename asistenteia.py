import speech_recognition as sr

import webbrowser as wb

def asistente_personal():

    sr.Microphone(device_index = 0)

    reconocimiento = sr.Recognizer()

    reconocimiento.energy_threshold=1000
    reconocimiento.dynamic_energy_threshold = False

    with sr.Microphone() as source:

        print('Hola Byron, ¿Qué necesitas?:')
        #reconocimiento.adjust_for_ambient_noise(source)
        audio = reconocimiento.listen(source)
        try:
            texto = reconocimiento.recognize_google(audio, language='es-EC')#en-US
            print(f"Acabas de decir: {texto} ?")
            navegador = "https://www.google.com/search?q="
            busqueda  = navegador + texto
            wb.open(busqueda)
        except TimeoutException as msg:
            print(msg)
        except WaitTimeoutError:
            print("El tiempo de escuha se agotó, mientras se esperaba la frase. Adiós...")
            quit()
        except LookupError:
            print("Lo siento mucho, no se pudo procesar tu solicitud.")
        else:
            print("Los resultados deben aparecer en tu navegador web...")
            
asistente_personal()



