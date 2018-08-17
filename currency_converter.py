print("the currency formats are:\n[japanese yen], [hong kong dollar],")
print("[sri lankan rupees], [pakistani rupee]")
print("[pound], [canadian dollar], [euro]")
print("[us dollar], [singapur dollar], [bangalideshi taka]")
print("[chinese yuan], [indonesian rupia], [swiss france]")
print("[omami rail], [australian dollar], [new zealand dollar]")
print("[argentina peso], [egyptian pound]")
print("")
	           	
num1 = float(input(" how much money do you want to convert:"))
one = input("in which kind of format:")
print("")
onea = "us dollar"
two = "euro"
threea = "pound"
foura = "japanese yen"
fivea = "hong kong dollar"
sixa = "sri lankan rupees"
sevena = "pakistani rupee"
eighta = "canadian dollar"
ninea = "mexican peso"
tena = "88.93"
elevena = "south korian won"
twelvea = "singapore dollar"
therteena = "bangalideshi taka"
fourteena = "chinese yuan"
fifteena = "indonesian rupiah"
sixteena = "swiss france"
seventeena = "omami rial"
eighteena = "australian dollar"
ninteena = "new zealand dollar"
twentya = "argentina peso"
twentyonea = "egyptian pound"
xxx = "test"


def convert(num1):
    if one == onea:
        return 71.67*num1
    elif one == two:
        return 88.93*num1     
    elif one == threea:
        return 88*num1
    elif one == foura:
        return 0.63155*num1
    elif one == fivea:
        return 8.97*num1
    elif one == sixa:
        return 0.437*num1
    elif one == sevena:
        return 0.571*num1
    elif one == eighta:
        return 53.27*num1
    elif one == ninea:
        return 3.66*num1
    elif one == tena:
        return 88.93*num1
    elif one == elevena:
        return 0.061*num1
    elif one == twelvea:
        return 50.79*num1
    elif one == therteena:
        return 0.829*num1
    elif one == fourteena:
        return 10.11*num1
    elif one == fifteena:
        return 0.00479*num1
    elif one == sixteena:
        return 70.46*num1
    elif one == seventeena:
        return 182*num1
    elif one == eighteena:
        return 51*num1
    elif one == ninteena:
        return 47*num1
    elif one == twentya:
        return 2.34*num1
    elif one == twentyonea:
        return 3.909*num1                                       
                
    elif one == xxx:
        return 1*num1                             
    else:
        print("please check it again\nfor your help all the formats are given above.")

print(convert(num1))
                    