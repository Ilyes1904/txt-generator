def txtfile_generators () :
    """
    generator of text file
    """
    i=0
    n=0
    login = input("[Insert a text] ")
    #login is an exemple of what you can do with.
    passw = input("[Insert a text] ")
    #passw : password is an exemple of what you can do with.
    while i <= 20 : 
        n+=1
        f =  open (f"insert name here {n}.txt","w",encoding="utf-8")
        f.write(f'Login : {login}\nPassword : {passw} ')
        #passw : password and Login is an exemple of what you can do with.
        f.close()
        i+=1
        

txtfile_generators()

