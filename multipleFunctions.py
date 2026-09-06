class SubfieldsInAI():
        def Subfields():
            print("Sub-fields in AI are:")
            list=['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
            for i in range(len(list)):
                print(list[i])
        
        def OddEven():
            num=int(input("Enter a number:"))
            if(num%2==0):
                print(num ,"is Even number")
            else:
                print(num ,"is ODD number")   
        
        def MarriageElegible():
            Gender=input("Enter your Gender:")
            Age=int(input("Enter your Age:"))
            Elg=""
            if(Gender=='Male' and Age>=21):
                print("Eligible")
                Elg="Eligible"
            elif(Gender=='Female' and Age>=18):
                print("Eligible")
                Elg="Eligible"
            else:    
                print("Not Eligible")
                Elg="Not Eligible"
            return Elg
        
        def percentage():
            marks = [98, 87, 95, 95, 93]
            total = 0
            
            for i in range(len(marks)):
                print("Subject", i, "=", marks[i])
                total += marks[i]
                
            print("Total =", total)
            percentage = total / len(marks)
            print("Percentage =", percentage, "%")        
         

        def triangle():
            Height=32
            Breadth=34
            print("Height:",Height)
            print("Breadth:",Breadth)
            print("Area formula: (Height*Breadth)/2")
            Area=(Height*Breadth)/2
            print("Area of Triangle:",Area)
            Height1=2
            Height2=4
            Breadth=4
            print("Height1:",Height1)
            print("Height2:",Height2)
            print("Breadth:",Breadth)
            print("Perimeter formula: Height1+Height2+Breadth")
            Perimeter=Height1+Height2+Breadth
            print("Perimeter of Triangle:",Perimeter)  