public_toilet = "PB"

def home():
    private_toilet = "PT"
    print(private_toilet)
    public_toilet = "LBT"  #even if the global variable is changed, gives the updated result
    print(public_toilet)

home()

def stranger():
    print(public_toilet) #global can be accessed anywhere
 #   print(private_toilet) #local variable cant be accessed

stranger()


