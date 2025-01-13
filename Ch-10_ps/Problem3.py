class demo:
    a = 4

object = demo()
print(object.a)
#yahan instance attribute tha heen nahi isliye class attribute print hua.
 
object.a = 0
print(object.a)
# yahan instance attribute aa gya isliya instance attribute print hua. class attribute change nahi hua kyuki ham yahan ham class attribute print kra heen nahi rahe the

print(demo.a)
# yahan hamne class attribute print kraya hai aur ham dekhte hain ki wo change nahi hua hai