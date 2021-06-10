from PyQt5 import QtWidgets,QtCore,QtGui,QtMultimedia
import getpass
import sys
import os
 
class Music(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.pause = True
        self.prox =-1

        self.abrir = ([],'')
        
        self.svg_stop = '<?xml version="1.0" ?><svg id="blue_copy" style="enable-background:new 0 0 100 100;" version="1.1" viewBox="0 0 100 100" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><g id="Layer_7_copy"><path d="M39.806,72.858h-8.915c-2.176,0-3.94-1.764-3.94-3.94V31.119c0-2.176,1.764-3.94,3.94-3.94h8.915   c2.176,0,3.94,1.764,3.94,3.94v37.799C43.746,71.094,41.982,72.858,39.806,72.858z"/><path d="M68.109,72.821h-8.915c-2.176,0-3.94-1.764-3.94-3.94V31.082c0-2.176,1.764-3.94,3.94-3.94h8.915   c2.176,0,3.94,1.764,3.94,3.94v37.799C72.049,71.057,70.285,72.821,68.109,72.821z"/><path d="M40.489,27.248c0.769,0.719,1.257,1.735,1.257,2.871v37.799c0,2.176-1.764,3.94-3.94,3.94h-8.915   c-0.234,0-0.46-0.03-0.683-0.069c0.704,0.658,1.643,1.069,2.683,1.069h8.915c2.176,0,3.94-1.764,3.94-3.94V31.119   C43.746,29.177,42.338,27.573,40.489,27.248z"/><path d="M68.792,27.211c0.769,0.719,1.257,1.735,1.257,2.871v37.799c0,2.176-1.764,3.94-3.94,3.94h-8.915   c-0.234,0-0.46-0.03-0.683-0.069c0.704,0.658,1.643,1.069,2.683,1.069h8.915c2.176,0,3.94-1.764,3.94-3.94V31.082   C72.049,29.14,70.641,27.535,68.792,27.211z"/><path d="M39.806,72.858h-8.915c-2.176,0-3.94-1.764-3.94-3.94V31.119   c0-2.176,1.764-3.94,3.94-3.94h8.915c2.176,0,3.94,1.764,3.94,3.94v37.799C43.746,71.094,41.982,72.858,39.806,72.858z" style="fill:none;stroke:#000000;stroke-miterlimit:10;"/><path d="M68.109,72.821h-8.915c-2.176,0-3.94-1.764-3.94-3.94V31.082   c0-2.176,1.764-3.94,3.94-3.94h8.915c2.176,0,3.94,1.764,3.94,3.94v37.799C72.049,71.057,70.285,72.821,68.109,72.821z" style="fill:none;stroke:#000000;stroke-miterlimit:10;"/></g></svg>'
        self.svg_pass = '<?xml version="1.0" ?><svg id="blue_copy" style="enable-background:new 0 0 100 100;" version="1.1" viewBox="0 0 100 100" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><g id="Layer_8_copy_4_1_"><path d="M41.762,27.26v8.294c0,0.571,0.305,1.1,0.8,1.385l20.212,11.669c1.066,0.616,1.066,2.155,0,2.771L42.562,63.048   c-0.495,0.286-0.8,0.814-0.8,1.385v8.294c0,1.231,1.333,2.001,2.399,1.385l39.375-22.733c1.066-0.616,1.066-2.155,0-2.771   L44.161,25.875C43.095,25.259,41.762,26.029,41.762,27.26z"/><path d="M83.537,48.608L44.161,25.875c-0.193-0.112-0.395-0.164-0.597-0.19l37.972,21.923c1.066,0.616,1.066,2.155,0,2.771   L42.161,73.112c-0.1,0.058-0.205,0.092-0.308,0.126c0.308,0.914,1.401,1.398,2.308,0.874l39.375-22.733   C84.603,50.763,84.603,49.224,83.537,48.608z"/><path d="M41.762,27.26v8.294c0,0.571,0.305,1.1,0.8,1.385l20.212,11.669   c1.066,0.616,1.066,2.155,0,2.771L42.562,63.048c-0.495,0.286-0.8,0.814-0.8,1.385v8.294c0,1.231,1.333,2.001,2.399,1.385   l39.375-22.733c1.066-0.616,1.066-2.155,0-2.771L44.161,25.875C43.095,25.259,41.762,26.029,41.762,27.26z" style="fill:none;stroke:#000000;stroke-miterlimit:10;"/><path d="M14.664,27.273v8.294c0,0.571,0.305,1.1,0.8,1.385l20.212,11.669c1.066,0.616,1.066,2.155,0,2.771L15.464,63.061   c-0.495,0.286-0.8,0.814-0.8,1.385v8.294c0,1.231,1.333,2.001,2.399,1.385l39.375-22.733c1.066-0.616,1.066-2.155,0-2.771   L17.063,25.888C15.997,25.272,14.664,26.042,14.664,27.273z"/><path d="M56.438,48.621L17.063,25.888c-0.193-0.112-0.395-0.164-0.597-0.19l37.972,21.923c1.066,0.616,1.066,2.155,0,2.771   L15.063,73.125c-0.1,0.058-0.205,0.092-0.308,0.126c0.308,0.914,1.401,1.398,2.308,0.874l39.375-22.733   C57.505,50.776,57.505,49.237,56.438,48.621z"/><path d="M14.664,27.273v8.294c0,0.571,0.305,1.1,0.8,1.385l20.212,11.669   c1.066,0.616,1.066,2.155,0,2.771L15.464,63.061c-0.495,0.286-0.8,0.814-0.8,1.385v8.294c0,1.231,1.333,2.001,2.399,1.385   l39.375-22.733c1.066-0.616,1.066-2.155,0-2.771L17.063,25.888C15.997,25.272,14.664,26.042,14.664,27.273z" style="fill:none;stroke:#000000;stroke-miterlimit:10;"/></g></svg>'
        self.svg_play = """<?xml version="1.0" encoding="iso-8859-1"?><svg version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="512px" height="512px" viewBox="0 0 512 512" style="enable-background:new 0 0 512 512;" xml:space="preserve"><g><path d="M256,0C114.609,0,0,114.609,0,256c0,141.391,114.609,256,256,256c141.391,0,256-114.609,256-256 C512,114.609,397.391,0,256,0z M256,472c-119.297,0-216-96.703-216-216S136.703,40,256,40s216,96.703,216,216S375.297,472,256,472z"/><path d="M353.661,237.879l-154.174-89.594c-16.844-9.969-32.987-1.938-32.987,17.844v179.766c0,19.75,16.143,27.797,32.987,17.812 l152.956-89.578C369.348,264.16,370.552,247.848,353.661,237.879z"/></g></svg>"""
        self.svg_list = '<?xml version="1.0" ?><svg viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><defs><style>.cls-1{fill:none;}</style></defs><title/><g data-name="Layer 2" id="Layer_2"><path d="M28,9H11a1,1,0,0,1,0-2H28a1,1,0,0,1,0,2Z"/><path d="M7,9H4A1,1,0,0,1,4,7H7A1,1,0,0,1,7,9Z"/><path d="M21,17H4a1,1,0,0,1,0-2H21a1,1,0,0,1,0,2Z"/><path d="M11,25H4a1,1,0,0,1,0-2h7a1,1,0,0,1,0,2Z"/><path d="M9,11a3,3,0,1,1,3-3A3,3,0,0,1,9,11ZM9,7a1,1,0,1,0,1,1A1,1,0,0,0,9,7Z"/><path d="M23,19a3,3,0,1,1,3-3A3,3,0,0,1,23,19Zm0-4a1,1,0,1,0,1,1A1,1,0,0,0,23,15Z"/><path d="M13,27a3,3,0,1,1,3-3A3,3,0,0,1,13,27Zm0-4a1,1,0,1,0,1,1A1,1,0,0,0,13,23Z"/><path d="M28,17H25a1,1,0,0,1,0-2h3a1,1,0,0,1,0,2Z"/><path d="M28,25H15a1,1,0,0,1,0-2H28a1,1,0,0,1,0,2Z"/></g><g id="frame"><rect class="cls-1" height="32" width="32"/></g></svg>'

        self.Frame()
        self.Buttons()
        
        self.Show()
 
 
    def Frame(self):
        self.frame = QtWidgets.QFrame(self)
 
        self.frame.setStyleSheet('QFrame{background-color:#333333;border-radius:10px;}')
 
        self.frame.resize(350,450)
 
    def Buttons(self):

        center_window = int(self.frame.size().width()/2)
        height_window = int(self.frame.size().height())
 
        self.btn_close = QtWidgets.QToolButton(self.frame)
        self.btn_play = QtWidgets.QToolButton(self.frame)
        self.btn_pass = QtWidgets.QToolButton(self.frame)
        self.btn_back = QtWidgets.QToolButton(self.frame)
        self.btn_list = QtWidgets.QToolButton(self.frame)

        if os.path.isfile('chaves.gif'):
            self.label_gif = QtWidgets.QLabel(self.frame)
            self.movie = QtGui.QMovie('chaves.gif')
            self.label_gif.setMovie(self.movie)
            self.label_gif.resize(200,200)
            self.label_gif.move(int(center_window-self.label_gif.size().width()/2),90)
        else:
            self.movie = False

            
        self.btn_close.resize(12,12)

        self.btn_list.setToolTip('Selecionar Musicas')
 
        self.btn_close.setStyleSheet('QToolButton{background-color:red;border:1px solid rgba(255,255,255,0);border-radius:6px;}')
 
        self.setStyleSheet('QToolButton{background-color:rgba(255,255,255,0);}')
 
        self.btn_play.setIcon(self.RenderSvg(self.svg_play))
        self.btn_pass.setIcon(self.RenderSvg(self.svg_pass))
        self.btn_list.setIcon(self.RenderSvg(self.svg_list))
        self.btn_back.setIcon(self.RenderSvg(self.svg_pass,True))
        
        self.btn_play.setIconSize(QtCore.QSize(40, 40))
        self.btn_pass.setIconSize(QtCore.QSize(40, 40))
        self.btn_back.setIconSize(QtCore.QSize(40, 40))
        self.btn_list.setIconSize(QtCore.QSize(40, 40))
 

        self.btn_play.move(int(center_window-self.btn_play.size().width()/2)+12,int(height_window-self.btn_play.size().height())-40)
        self.btn_pass.move(220,int(height_window-self.btn_play.size().height())-40)
        self.btn_back.move(60,int(height_window-self.btn_play.size().height())-40)
 
        self.btn_list.pressed.connect(self.PlayList)
        self.btn_play.pressed.connect(lambda:self.PlayMusic(self.pause))
        self.btn_pass.pressed.connect(lambda:self.PlayMusic(True,True))
        self.btn_back.pressed.connect(lambda:self.PlayMusic(True,True,True))
 
        self.btn_close.move(int(self.frame.size().width()-self.btn_close.size().width())-3,5)
 
        self.btn_close.pressed.connect(self.close)

    def PlayList(self):
        user = getpass.getuser()
        direct = r"C:\Users\{}\Music".format(user)
        self.abrir = QtWidgets.QFileDialog.getOpenFileNames(self,'Selecione Suas Musicas',direct,filter='*.wav')  
        
 
    def RenderSvg(self,svg,rotate=False):
        svg_bytes = bytearray(svg,encoding='utf-8')
        icon = QtGui.QIcon(QtGui.QPixmap.fromImage(QtGui.QImage.fromData(svg_bytes) \
                                                   if rotate == False else QtGui.QImage.fromData(svg_bytes).transformed(QtGui.QTransform().rotate(180))))
        return icon
        
    def PlayMusic(self,pause=None,prox=False,negative=False):

        if not prox or self.pause == True:
            self.pause = (False if self.pause else True)
            self.btn_play.setIcon(self.RenderSvg(self.svg_stop) if pause else self.RenderSvg(self.svg_play))
        else:
            if negative:
                self.prox -=1
            else:
                self.prox +=1

        if self.prox !=0 and self.movie:
            self.movie.start()

        
        if self.abrir[0] != []:

            if abs(self.prox) < len(self.abrir[0]):
                self.p_Sound = QtMultimedia.QSound(self.abrir[0][self.prox])
                self.p_Sound.play() if pause else self.p_Sound.stop()
            else:
                self.prox = 0
 
    def Show(self):
        self.setGeometry(0,0,350,450)
 
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.move(center - self.rect().center())
        self.show()
 
 
if __name__ == '__main__':
   
    app = QtWidgets.QApplication(sys.argv)
    center = app.desktop().screen().rect().center()
 
    window = Music()
    sys.exit(app.exec_())
