# import pyshorteners
#
# link=input("Enter the URL you want to shoten :")
# shortener=pyshorteners.Shortener()
#
# x=shortener.tinyurl.short(link)
#
# print(x)

import pyshorteners


def small():
    print("........Welcome To URL Shortner Software.......")
    link=input ("Enter the URL you want to shrink it to smaller one : ")
    shortener= pyshorteners.Shortener()
    print(shortener.tinyurl.short(link))

    choice=input("Do you want to continue again press y and for exit press n :")
    if(choice=="y"):
        {
            small()
        }
    elif(choice=="Y"):
        {
            small()
        }
    else:
        {
            print("----------------------Thanking you-----------------------------")
        }





small()
