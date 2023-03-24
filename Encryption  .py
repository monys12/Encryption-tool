import marshal
import pyfiglet
import os

#colors
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = '\033[39m'

try:
    import marshal
    import pyfiglet

except ImportError:
    os.system("pip install marshal")
    os.system("pip install pyfiglet")
    



print("""

\033[32m
                        ███╗   ███╗ █████╗ ██████╗ ███████╗    ██████╗ ██╗   ██╗    ███╗   ███╗ ██████╗ ███╗   ██╗
                        ████╗ ████║██╔══██╗██╔══██╗██╔════╝    ██╔══██╗╚██╗ ██╔╝    ████╗ ████║██╔═══██╗████╗  ██║
                        ██╔████╔██║███████║██║  ██║█████╗      ██████╔╝ ╚████╔╝     ██╔████╔██║██║   ██║██╔██╗ ██║
                        ██║╚██╔╝██║██╔══██║██║  ██║██╔══╝      ██╔══██╗  ╚██╔╝      ██║╚██╔╝██║██║   ██║██║╚██╗██║
                        ██║ ╚═╝ ██║██║  ██║██████╔╝███████╗    ██████╔╝   ██║       ██║ ╚═╝ ██║╚██████╔╝██║ ╚████║
                        ╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝    ╚═════╝    ╚═╝       ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                                          
                                                                                                        \033[39m 



                                                   \033[35m     ♥ v 2.01 ♥    \033[39m 

                                        
""")


print("\033[31mPut the python file in same directory and put the name of the file :\033[39m ")


filee = input("\033[33m[+] - Write The File Name Or Path : ")

open_file = open(filee, 'r').read()

compile_file = compile(open_file, '', 'exec')

encrypt_file = marshal.dumps(compile_file)

encrypt_code = open('New_'+str(filee), 'w')

encrypt_code.write('import marshal\nexec(marshal.loads('+repr(encrypt_file)+'))')

print("\033[32mThe File Has Been Successfully Encrypted! : "+str(filee))










    


