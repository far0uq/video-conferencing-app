from vidstream import *
import tkinter as tk
import socket
import threading

localIPAddress = socket.gethostbyname(socket.gethostname())
#publicIPAddress = requests.get('https://api.ipify.org')

server = StreamingServer(localIPAddress, 6000)
reciever = AudioReceiver(localIPAddress, 7000)

def StartListening():
    t1 = threading.Thread(target = server.start_server)
    t2 = threading.Thread(target = reciever.start_server)
    t1.start()
    t2.start()
    
def StartCameraStream():
    camera_client = CameraClient(textTargetIP.get(1.0,'end-1c'), 9999)
    print("Executed\n")
    t3 = threading.Thread(target = camera_client.start_stream)
    t3.start()
    
def StartScreenSharing():
    screen_sharing = ScreenShareClient(textTargetIP.get(1.0,'end-1c'), 9999)
    t4 = threading.Thread(target = screen_sharing.start_stream)
    t4.start()
    
def StartAudioStream():
    audio_sender = AudioSender(textTargetIP.get(1.0,'end-1c'), 8888)
    t5 = threading.Thread(target = audio_sender.start_stream)
    t5.start()
    

#GUI
window = tk.Tk()
window.title("Peeps Video Conferencing")
window.geometry('500x850')
window.configure(bg = "#E8C4C4")

labelTargetIP = tk.Label(window,text = 'Target IP:',font = ("JetbrainsMono",20))
labelTargetIP.pack()

textTargetIP = tk.Text(window, height = 1, width = 15, font = ("JetbrainsMono",20),padx = 10)
textTargetIP.pack()

btnListen = tk.Button(window,text = "Start Listening", command = StartListening,font = "JetbrainsMono" ,bg = "#CE7777", fg = "black", height = 2, width = 15,padx = 50, pady = 25)
btnListen.pack(anchor = tk.CENTER,expand = True, pady = 40)

btnCamera = tk.Button(window,text = "Start Streaming Camera", command = StartCameraStream, font = "JetbrainsMono" ,bg = "#CE7777", fg = "black", height = 2, width = 15,padx = 50, pady = 25)
btnCamera.pack(anchor = tk.CENTER,expand = True, pady = 40)

btnScreen = tk.Button(window,text = "Start Streaming Screen", command = StartScreenSharing, font = "JetbrainsMono" ,bg = "#CE7777", fg = "black", height = 2, width = 15,padx = 50, pady = 25)
btnScreen.pack(anchor = tk.CENTER,expand = True, pady = 40)

btnAudio = tk.Button(window,text = "Start Streaming Audio", command = StartAudioStream,font = "JetbrainsMono" ,bg = "#CE7777", fg = "black", height = 2, width = 15,padx = 50, pady = 25)
btnAudio.pack(anchor = tk.CENTER,expand = True, pady = 40)

window.mainloop() 