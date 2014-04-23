
class Integer(object):

    def __init__(self,number,Negative):

        self.Int = number

        if(Negative):
            self.Int = -number
        
    def display(self):
        
        print self.Int
        
    
class NegInt(Integer):

    def __init__(self, number):

        super(NegInt, self).__init__(number, True)

    def display(self):
        print "Negative is: "
        Integer.display(self)
        
        
if __name__=="__main__":
    
    
    
    My_test = Integer(raw_input("Print a negative number :(: "))
    
    
    My_2test = NegInt(raw_input("Print your favorite positive number :): "), False)
    
    List = [My_test, My_2test]
    
    for i in List:
        i.display()


    def operation(A,S,K ):

        if (K=="add"):
            return A.Int+S.Int

        if (K=="subtract"):
            return A.Int-S.Int

        if (K=="divide"):
            return A.Int/S.Int

        if (K=="multiply"):
            return A.Int*S.Int

    
    print Integer.operation(My_test, My_2test, raw_input("Please insert operation: "))