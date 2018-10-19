#!/usr/bin/env python3
import tkinter.ttk,socket#Bibliotecas
from tkinter import Button,Entry,Spinbox,WORD,W,E,Label,Tk,END,messagebox,Text#Bibliotecas
import portas

'''
Algoritmo para verificação de portas abertas no sistema
Trabalho de Sistemas Distribuídos, Professor Mestre Diógenes Antonio Marques José
Turma 2018/2 UNEMAT Barra do Bugres - MT

PortScanner By: Karan Luciano e Douglas Teles
'''
class PortScanner:#Classe o qual tudo sera definido
	def __init__(self):#Funcao init que cria a interface utilizando o TKinter
		
		interface = Tk() #Cria o objeto de referência TK
		
		self.srvr = Entry(interface,textvariable="server")#Recebe um Valor 
		self.srvr.setvar(name="server",value='127.0.0.1')#Fornecer um método bash de configuração de vars de ambiente
		self.srvr.grid(row=0,column=1,sticky=W)#Define as caracteristicas do Entry
		
		lbl = Label(interface,text="Host:")#Cria o Label do Host
		lbl.grid(row=0,column=0,sticky=W)#Define as caracteristicas do Label 
		
		self.spnr = Spinbox(interface,from_=1,to=65535,value=1)#Spinbox eh como o Entry, quando o usuário tiver apenas um número limitado de valores ordenados para escolher
		self.spnr.grid(row=1,column=1,sticky=W)#Define as caracteristicas
		
		lbl2 = Label(interface,text="Porta Inicial:")#Cria o Label da porta inicial
		lbl2.grid(row=1,column=0,sticky=W)#Define as caracteristicas do Label 
		
		self.spnr.grid(row=1,column=1,sticky=W)#Recebe a porta inicial
		self.spnr2 = Spinbox(interface,from_=1,to=65535,value=65535)#Define que vai de 1 a 65535
		self.spnr2.grid(row=2,column=1,sticky=W)#Define as caracteristicas
		
		lbl3 = Label(interface,text="Porta Final",)#Cria o Label da porta final
		lbl3.grid(row=2,column=0,sticky=W)#Define as caracteristicas do Label 
		
		interface.resizable(width=False,height=False,)#Tornar o tamanho da janela estático (não redimensionável)
		
		btn = Button(interface,text="Começar o Port Scan!",command=self.scan,  fg="red")#Botao de Start do programa
		btn.grid(row=3,column=1,sticky=W)#Define as caracteristicas do Botao 
		
		self.txt = Text(interface,width=50,height=20,wrap=WORD, bg="black", fg="green")#Texto de saida do resultado do scan
		self.txt.grid(row=4,column=0,columnspan=2,sticky=W)#Define as caracteristicas
		
		interface.title('Super_Mega_Scan_Port!') #Título da janela
		
		self.txt.insert(0.0,'Trabalho de Sistemas Distribuídos 2018/2\n\nProf. Me Diógenes Antonio Marques José\n\nBy: Karan Luciano e Douglas Teles\n')
		
		interface.mainloop() #Mostrar janela da GUI

	def pscan(self,port):#Funcao pega os valores
		try:
			target = self.srvr.get()#Recebe o ip digitado
			s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#AF_INET pega o ipv4 e SOCK_STREAM pega a porta
			s.connect((target,port))#Conecta ao ip e porta 
			return True
		except:
			return False
	
	def scan(self):
		self.txt.delete(0.0,END)
		print('Scanning',self.srvr.get())
		for x in range(int(self.spnr.get()),int(self.spnr2.get())+1):
			if self.pscan(x):
				
				if (x == 22):
					msg = "SSH! (TCP/UDP)\n"
					self.txt.insert(0.0,msg)
				if (x == 135):
					msg = "EPMAP! (TCP/UDP)\n"
					self.txt.insert(0.0,msg)	
				if (x == 139):
					msg = "NetBios! (TCP/UDP)\n"
					self.txt.insert(0.0,msg)
				if (x == 445):
					msg = "Microsoft-DS! (TCP)\n"
					self.txt.insert(0.0,msg)
				if (x == 554):
					msg = "RTSP! (TCP)\n"
					self.txt.insert(0.0,msg)	
				if (x == 631):
					msg = "IPP! (TCP/UDP)\n"
					self.txt.insert(0.0,msg)
				if (x >= 1024 and x< 49151):
					msg = "Porta registada\n"
					self.txt.insert(0.0,msg)
				if (x >=49152 and x< 65535):
					msg = "Porta dinâmica e/ou privada\n"
					self.txt.insert(0.0,msg)
				print('Porta: ',x,' Aberta!')
				msg = "\nPorta "+str(x)+" Aberta! "
				self.txt.insert(0.0,msg)	
			else:
				print('Porta: ',x,'Fechada!')
		messagebox.showinfo(title="PyPortScanner!",message="Scan Completo!")
ps = PortScanner()       
#shot()
