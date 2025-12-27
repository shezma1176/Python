class CSStudent:

    # Class Variable
    stream = 'cse'

    # The init method or constructor
    def __init__(self, Roll):
        # Instance Variable
        self.roll= Roll

    def setAddress(self, address):
        self.address = address
    
    # Retrieves Instance variable
    def getAddress(self):
        return self.address
    
# Driver Code
add = CSStudent(101)
add.setAddress("Narsingdi, Bangladesh")
print(add.getAddress())