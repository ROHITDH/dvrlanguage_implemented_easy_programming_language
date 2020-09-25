#0.infinate user input.1.add the shell

import dvr
import os

clear = lambda: os.system('cls' if os.name == 'nt' else 'cls')

while True:
    text = input('<dvr☺>  ')
    if text.strip() == "":continue
    if text== "cls" or text=="clr":
        clear()
    result,error = dvr.run('<stdin>',text)
    
    
    if error: 
        print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))
            
      
    

