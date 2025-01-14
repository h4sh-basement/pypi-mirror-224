import tkinter
import tkhtmlview
import re
import PIL
import math
from io import BytesIO as btio
"""
Warning: To acheive the things that I did in this module I had to use both eval and exec.
Notes:
- Canvas is not supported yet even though there is an option for it 
- Scrollbars in the htmlscrolledtext widget don't change size but that is a small price to pay for this working
- Commands must be set manually <windowobject>.<childName>["command"] = <command>
- When grouping windows together, the object that should be used is <windowobject>.root
Todo:
- Optimize refresh for HTMLScrolledText
- Replace the eval and exec statements with dictionaries where possible
- Properly support canvas mode
"""
#Adobe flash minimum size is 262x0

def help():
   print("If you are confused about how to use this module, please run this module by itself and look at the test code at the bottom.")

class window:
   def __init__(self, width, height, title="Python",_type="canvas", color="#FFFFFF",mainwindow=True):
      self.oldmult = 100
      self.aboutwindowtext = "placeholdertext"
      self.oimagedict = {}
      self.rimagedict = {}
      self.oimgsize = {}
      self.hstfg = {}
      self.hstbg = {}
      self.otext = {}
      self.ftext = {}
      self.childlist = {}
      self.stfontbold = False
      if width < 262:
         width = 262
      self.startwidth = width
      self.startheight = height
      self.color = color
      self.mw = mainwindow
      if mainwindow == True:
         self.root = tkinter.Tk()
         self.root.minsize(262,int((262*self.startheight)/self.startwidth) + 28)
         self.menubar = tkinter.Menu(self.root, bd=1)
         self.filemenu = tkinter.Menu(self.menubar, tearoff=0)
         self.filemenu.add_command(label="Quit", font=("Terminal",8), command=self.endProcess)
         self.menubar.add_cascade(label="File", font=("Terminal",8), menu=self.filemenu)
         self.viewmenu = tkinter.Menu(self.menubar, tearoff=0)
         self.viewmenu.add_command(label="Full Screen", font=("Terminal",8), command=self.gofullscreen)
         self.viewmenu.add_command(label="Reset Size", font=("Terminal",8), command=self.resetSize)
         self.menubar.add_cascade(label="View", font=("Terminal",8), menu=self.viewmenu)
         self.controlmenu = tkinter.Menu(self.menubar, tearoff=0)
         self.controlmenu.add_command(label="Controls", font=("Terminal",8))
         self.menubar.add_cascade(label="Control", font=("Terminal",8), menu=self.controlmenu)
         self.helpmenu = tkinter.Menu(self.menubar, tearoff=0)
         self.helpmenu.add_command(label="About", font=("Terminal",8), command=self.aboutwin)
         self.menubar.add_cascade(label="Help", font=("Terminal",8), menu=self.helpmenu)
         self.root.config(menu=self.menubar)
      else:
         self.root = tkinter.Toplevel()
         self.root.minsize(262,int((262*self.startheight)/self.startwidth))
      self.root.title(title)
      self.root.geometry(f"{self.startwidth}x{self.startheight}")
      if _type == "canvas":
         self.display = tkinter.Canvas(self.root, background=self.color, confine=True)
         self.display.place(anchor="center", width=width, height=height, x=self.startwidth/2, y=self.startheight/2)
      elif _type == "frame":
         self.display = tkinter.Frame(self.root, background=self.color)
         self.display.place(anchor="center", width=width, height=height, x=self.startwidth/2, y=self.startheight/2)
      else:
         raise Exception("_type must be either frame or canvas.")
      self.root.bind("<Configure>",self.doResize)
      self.root.bind("<Escape>",self.outfullscreen)
   def resetSize(self):
      self.root.geometry(f"{self.startwidth}x{self.startheight}")
   def group(self, objectName:object):
      self.root.group(objectName)
   def toTop(self):
      self.root.lift()
   def round(self, num):
      tempList = str(num).split(".")
      tempList[1] = f".{tempList[1]}"
      if float(tempList[1]) >= 0.5: #0.85? 0.5? 1?
         return math.ceil(num)
      else:
         return math.floor(num)
   def tupletolist(self, tup):
      templist = []
      for i in tup:
         templist.append(i)
      return templist
   def listtotuple(self, li):
      return tuple(li)
   def minimumSize(self,_type:str="b",**kwargs):
      """
      _type must be either 'w','h',or 'b' (meaning width, height, or both). if nothing is passed, assumed to be 'b' (both)
      kwargs must include width, height, or both depending on what you chose for _type
      if 'w' or 'height' is chosen, the other will be assumed based on the ration of the original size
      """
      if _type == "w":
         if self.mw == True:
            self.root.minsize(kwargs["width"],int((kwargs["width"]*self.startheight)/self.startwidth) + 28)
         else:
            self.root.minsize(kwargs["width"],int((kwargs["width"]*self.startheight)/self.startwidth))
      elif _type == "h":
         if self.mw == True:
            self.root.minsize(int((self.startwidth*kwargs["height"])/self.startheight) - 52,kwargs["height"])
         else:
            self.root.minsize(int((self.startwidth*kwargs["height"])/self.startheight),kwargs["height"])
      elif _type == "b":
         self.root.minsize(kwargs["width"],kwargs["height"])
      else:
         print("Invalid type")
   def minimumSizeReset(self):
      if self.mw == True:
         self.root.minsize(262,int((262*self.startheight)/self.startwidth) + 28)
      else:
         self.root.minsize(262,int((262*self.startheight)/self.startwidth))
   def resizefont(self, font:tuple, mult):
      tempfont = self.tupletolist(font)
      tempfont[1] = self.round(font[1]*mult/100)
      tempfont = self.listtotuple(tempfont)
      return tempfont
   def _checkName(self, name:str):
      blacklist = ["(",")","{","}","[","]","!","@","#","$","%","^","&","*",",",".","<",">","/","\\","|","'","\"",":",";","-","+","=","~","`"]
      if name[0].isalpha():
         array = [i in name for i in blacklist]
         try:
            i = array.index(True)
         except:
            i = -1
         if i == -1:
            return True
         else:
            return False
      else:
         return False
   def mainloop(self):
      self.resizeChildren(100)
      self.root.mainloop()
   def enableResizing(self):
      self.root.resizable(True,True)
   def disableResizing(self):
      self.root.resizable(False,False)
   def endProcess(self):
      self.root.destroy()
   def gofullscreen(self):
      self.root.attributes("-fullscreen", True)
   def outfullscreen(self, useless):
      self.root.attributes("-fullscreen", False)
   def setAboutWindowText(self, text):
      self.aboutwindowtext = text
   def aboutwin(self):
      self.aboutwindow = tkinter.Toplevel(borderwidth=1)
      self.aboutwindow.geometry("350x155")
      self.aboutwindow.resizable(False,False)
      self.aboutwindow.group(self.root)
      self.aboutwindow.configure(background=self.color)
      self.aboutlabel1 = tkinter.Label(self.aboutwindow, font=("TkTextFont",9), justify="left", text=self.aboutwindowtext, background=self.color)
      self.aboutlabel1.place(anchor="nw", x=7, y=9)
      self.aboutokbutton = tkinter.Button(self.aboutwindow, text="OK", command=self.closeabout, background=self.color)
      self.aboutokbutton.place(anchor="nw", width=29, height=29, x=299, y=115)
   def closeabout(self):
      self.aboutwindow.destroy()
   def addButton(self, master:str, name:str, x, y, width, height, font, anchor:str="nw"):
      if master == "root":
         master = "display"
      if self._checkName(master) == False:
         print("Invalid Master")
         pass
      elif self._checkName(name) == False:
         print("Invalid Name")
         pass
      else:
         exec(f"self.{name} = tkinter.Button(self.{master})")
         eval(f"self.{name}").place(x=x,y=y,width=width,height=height,anchor=anchor)
         self.childlist[name] = [None,"Button",x,y,width,height,font,anchor]
         self.resizeChild(name, self.oldmult)
   def addLabel(self, master:str, name:str, x, y, width, height, font, anchor:str="nw"):
      if master == "root":
         master = "display"
      if self._checkName(master) == False:
         print("Invalid Master")
         pass
      elif self._checkName(name) == False:
         print("Invalid Name")
         pass
      else:
         exec(f"self.{name} = tkinter.Label(self.{master})")
         eval(f"self.{name}").place(x=x,y=y,width=width,height=height,anchor=anchor)
         self.childlist[name] = [None,"Label",x,y,width,height,font,anchor]
         self.resizeChild(name, self.oldmult)
   def addnwhLabel(self, master:str, name:str, x, y, font, anchor:str="nw"):
      if master == "root":
         master = "display"
      if self._checkName(master) == False:
         print("Invalid Master")
         pass
      elif self._checkName(name) == False:
         print("Invalid Name")
         pass
      else:
         exec(f"self.{name} = tkinter.Label(self.{master})")
         eval(f"self.{name}").place(x=x,y=y,anchor=anchor)
         self.childlist[name] = [None,"nwhLabel",x,y,None,None,font,anchor]
         self.resizeChild(name, self.oldmult)
   def addFrame(self, master:str, name:str, x, y, width, height, anchor:str="nw"):
      if master == "root":
         master = "display"
      if self._checkName(master) == False:
         print("Invalid Master")
         pass
      elif self._checkName(name) == False:
         print("Invalid Name")
         pass
      else:
         exec(f"self.{name} = tkinter.Frame(self.{master})")
         eval(f"self.{name}").place(x=x,y=y,width=width,height=height,anchor=anchor)
         self.childlist[name] = [None,"Frame",x,y,width,height,None,anchor]
         self.resizeChild(name, self.oldmult)
   def addHTMLScrolledText(self, master:str, name:str, x, y, width, height, font, anchor:str="nw"):
      if master == "root":
         master = "display"
      if self._checkName(master) == False:
         print("Invalid Master")
         pass
      elif self._checkName(name) == False:
         print("Invalid Name")
         pass
      else:
         exec(f"self.{name} = tkhtmlview.HTMLScrolledText(self.{master})")
         eval(f"self.{name}").place(x=x,y=y,width=width,height=height,anchor=anchor)
         self.hstfg[f"{name}"] = '#000000'
         self.hstbg[f"{name}"] = '#FFFFFF'
         self.otext[f"{name}"] = ""
         self.ftext[f"{name}"] = ""
         self.childlist[name] = [None,"HTMLScrolledText",x,y,width,height,font,anchor]
         self.resizeChild(name, self.oldmult)
   def prepareHTMLST(self, child:str, text:str):
      if self.otext[f"{child}"] == text:
         self.HTMLSTUpdateText(child, True)
      else:
         self.otext[f"{child}"] = text
         self.HTMLSTUpdateText(child)
   def HTMLSTUpdateText(self, child:str, rt=False):
      temp = eval(f"self.{child}")
      temp["state"] = "normal"
      font = self.childlist[child][6]
      fontsize = font[1]
      if rt == False:
         self.ftext[f"{child}"] = re.sub("(\t)", "    ", self.otext[f"{child}"])
      text = self.ftext[f"{child}"]
      if self.stfontbold == True:
         text = "<b>" + text + "</b>"
      text = f"<pre style=\"color: " + self.hstfg[f"{child}"] + "; background-color: " + self.hstbg[f"{child}"] + f"; font-size: {int(fontsize*self.oldmult/100)}px; font-family: {font[0]}\">{text}</pre>"
      temp.set_html(text)
      temp["state"] = "disabled"
   def addImage(self, image_name:str, image_data, size:tuple=""):
      """
      size the target (display) size of the image before resizing
      if size is not defined it is assumed to be the actual image size
      """
      self.oimagedict[f"{image_name}"] = image_data
      if size != "":
         self.oimgsize[image_name] = [size[0],size[1]]
      else:
         ims = PIL.Image.open(btio(image_data)).size
         self.oimgsize[image_name] = [ims[0],ims[1]]
   def addImageLabel(self, master:str, name:str, x, y, width, height, anchor:str="nw", image_name:str=""):
      if master == "root":
         master = "display"
      if self._checkName(master) == False:
         print("Invalid Master")
         pass
      elif self._checkName(name) == False:
         print("Invalid Name")
         pass
      else:
         self.resizeImage((width,height), image_name)
         exec(f"self.{name} = tkinter.Label(self.{master})")
         temp = eval(f"self.{name}")
         temp.place(x=x,y=y,width=width,height=height,anchor=anchor)
         temp["image"] = self.rimagedict[f'{image_name}']
         self.childlist[name] = [None,"ImageLabel",x,y,width,height,None,anchor,image_name]
         self.resizeChild(name, self.oldmult)
   def resizeImage(self, size:tuple, image_name):
      img = PIL.Image.open(btio(self.oimagedict[f"{image_name}"]))
      img.thumbnail(size)
      self.rimagedict[f"{image_name}"] = PIL.ImageTk.PhotoImage(img)
   def resizeChildren(self, mult):
      for i in self.oimagedict.keys():
         self.resizeImage((int(self.oimgsize[i][0]*mult/100),int(self.oimgsize[i][1]*mult/100)),i)
      for i in self.childlist.keys():
         temp = eval(f"self.{i}")
         cl = self.childlist[i]
         if cl[1] == "nwhLabel":
            temp.place(x=cl[2]*mult/100,y=cl[3]*mult/100,anchor=cl[7])
         else:
            temp.place(x=cl[2]*mult/100,y=cl[3]*mult/100,width=cl[4]*mult/100,height=cl[5]*mult/100,anchor=cl[7])
         if cl[1] == "HTMLScrolledText":
            self.HTMLSTUpdateText(i)
         elif cl[1] == "ImageLabel":
            temp["image"] = self.rimagedict[f"{cl[8]}"]
         elif cl[1] != "Frame":
            f = cl[6]
            temp["font"] = self.resizefont(f,mult)
   def resizeChild(self, child:str, mult):
      temp = eval(f"self.{child}")
      cl = self.childlist[child]
      if cl[1] == "nwhLabel":
         temp.place(x=cl[2]*mult/100,y=cl[3]*mult/100,anchor=cl[7])
      else:
         temp.place(x=cl[2]*mult/100,y=cl[3]*mult/100,width=cl[4]*mult/100,height=cl[5]*mult/100,anchor=cl[7])
      if cl[1] == "HTMLScrolledText":
         self.HTMLSTUpdateText(child)
      elif cl[1] == "ImageLabel":
         self.resizeImage((int(cl[4]*mult/100),int(cl[5]*mult/100)),cl[8])
         temp["image"] = self.rimagedict[f"{cl[8]}"]
      elif cl[1] != "Frame":
         f = cl[6]
         temp["font"] = self.resizefont(f,mult)
   def bindChild(self, child:str, tkevent, function):
      eval(f"self.{child}").bind(tkevent, function)
   def configureChild(self, child:str, **args):
      k = []
      v = []
      for i in args.keys():
         k.append(i)
      for i in args.values():
         v.append(i)
      i = 0
      while i < len(k):
         if k[i] == "x" or k[i] == "y" or k[i] == "width" or k[i] == "height" or k[i] == "font" or k[i] == "anchor":
            newlist = self.childlist[child]
            if k[i] == "x":
               newlist[2] = v[i]
            elif k[i] == "y":
               newlist[3] = v[i]
            elif k[i] == "width":
               newlist[4] = v[i]
            elif k[i] == "height":
               newlist[5] = v[i]
            elif k[i] == "font":
               newlist[6] = v[i]
            elif k[i] == "anchor":
               newlist[7] = v[i]
            self.childlist[j] = newlist
            self.resizeChild(child)
         elif k[i] == "text" or k[i] == "textadd":
            if self.childlist[child][1] == "HTMLScrolledText":
               if k[i] == "text":
                  text = v[i]
               else:
                  text = self.otext[f"{child}"] + v[i]
               self.prepareHTMLST(child, text)
            else:
               eval(f"self.{child}")[k[i]] = v[i]
         elif k[i] == "background" or k[i] == "foreground":
            if self.childlist[child][1] == "HTMLScrolledText":
               eval(f"self.{child}")[k[i]] = v[i]
               if k[i] == "background":
                  self.hstbg[f"{child}"] = v[i]
               else:
                  self.hstfg[f"{child}"] = v[i]
               self.prepareHTMLST(child, self.otext[f"{child}"])
            else:
               eval(f"self.{child}")[k[i]] = v[i]
         elif k[i] == "image":
            self.childlist[child][8] = v[i]
            self.resizeChild(child, self.oldmult)
         else:
            eval(f"self.{child}")[k[i]] = v[i]
         i += 1
   def destroyChild(self, child:str):
      htmlst = False
      if self.childlist[child][1] == "HTMLScrolledText":
         htmlst = True
      self.childlist.pop(i)
      if htmlst == True:
         self.otext.pop(f"{child}")
         self.ftext.pop(f"{child}")
      eval(f"self.{child}").destroy()
   def doResize(self, event):
      if event.widget == self.root:
         mult = self.calculate()
         self.set_size(mult)
         if mult != self.oldmult:
            self.oldmult = mult
            self.resizeChildren(mult)
   def calculate(self):
      newwidth = self.root.winfo_width()
      newheight = self.root.winfo_height()
      xmult = (100*newwidth)/self.startwidth
      ymult = (100*newheight)/self.startheight
      if xmult > ymult:
         mult = ymult
      elif xmult < ymult:
         mult = xmult
      elif xmult == ymult:
         mult = xmult
      if self.oldmult == mult:
         return self.oldmult
      else:
         return mult
   def set_size(self, mult):
      newwidth = self.root.winfo_width()
      newheight = self.root.winfo_height()
      self.display.place(anchor="center", width=self.startwidth*mult/100, height=self.startheight*mult/100, x=newwidth/2, y=newheight/2)

if __name__ == "__main__":
   #Test
   from platform import python_version
   testcolor = 0
   def test_cyclecolor():
      global testcolor
      testcolorlist = ["#FFFFFF","#8F2F9F","#AAAAAA"]
      testcolor += 1
      if testcolor >= 3:
         testcolor = 0
      return testcolorlist[testcolor]
   root = window(1176,662,title="Adobe Flash Projector-like Window Test",_type="frame")
   root.setAboutWindowText(f"Adobe Flash Projector-like window demo.\n\nPython {python_version()}")
   root.addButton("root","testbutton1",0,0,130,30,("Times New Roman",12))
   root.testbutton1["command"] = lambda: root.configureChild("testtext", background=test_cyclecolor())
   root.addLabel("root","testlabel1",0,30,100,20,("Times New Roman",12))
   root.addHTMLScrolledText("root","testtext",0,50,600,400,("Times New Roman",12),anchor="nw")
   root.configureChild("testtext", text="TestText", cursor="arrow", wrap="word")
   root.configureChild("testbutton1", text="TestButton")
   root.configureChild("testlabel1", text="TestLabel")
   secondwindow = window(400,400,title="Second Window",_type="frame",mainwindow=False)
   secondwindow.group(root.root)
   root.addButton("root","testbutton2",130,0,130,30,("Times New Roman",12))
   root.testbutton2["command"] = lambda: secondwindow.toTop()
   root.configureChild("testbutton2", text="TestButton2")
   root.mainloop()