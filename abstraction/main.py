from vehicle import Bike,Car,Scooty

def main():
    Xpulse=Bike("Black",2,5)
    xuv700=Car("Dark blue",4,6)
    Activa=Scooty("White",2,0)

    Xpulse.display_details()
    print("\n")
    xuv700.display_details()
    print("\n")
    Activa.display_details()
    print("\n")

if __name__=="__main__":
    main()