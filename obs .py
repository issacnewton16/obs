class employe:
    # initializing (constructor)
    def __init__(self):
     print ("employe created.")
 # deleting (destructor)
    def __del__(self):
     print("destructor called ,employe deleted.")  
obj = employe()
del obj