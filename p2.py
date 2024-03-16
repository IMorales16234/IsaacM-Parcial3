import pywhatkit

try:
    #pywhatkit.sendwhatmsg("+524448567429", "ola h ase desde python", 18,26)
    pywhatkit.sendwhatmsg_to_group_instantly("HMSd7sLfFPy4ivP0YtAqvE", "wut?" , 19,10)
    print("Mensaje enviado")
except:
    print("Error")