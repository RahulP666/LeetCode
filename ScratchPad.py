class A:
    def method1(self):
        return 0    
    
    def method2(self):
        print("Class A")
    
    
class B(A):
    def method1(self):
        return 0    
    
    def method2(self):
        print("Class B")


B().method2()
    

