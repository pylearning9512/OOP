'''
goal is to practice OOP using examples from the "avatar/the last air bender" universe.
first creating an avatar class, which we will use to make instances of each avatar that the user inputs into the terminal, then print it out along with their attributes

got inspired to try this from watching the online CS50P course from Harvard

'''

class avatar:
    def __init__ (self,name:str,nation:str,element:str):
        #error handling
        if not name:
            raise ValueError("please run program again and enter name")
        
        valid_nation= ["air","fire","water","earth"]    
        if not any(keyword in nation for keyword in valid_nation):
            raise ValueError("thats not a nation in the avatar world :/")
        

        #class atributes
        self.name= name
        self.nation= nation
        self.element= element
    

    def __str__(self):
        return f"{self.name} is the bridge between the spirit and physical worlds"


def main():
    avatar= get_avatar()
    print(f'{avatar.name} is the avatar from the {avatar.nation} nation, they were born with affinity to the element {avatar.element}')
    print(avatar)

def get_avatar():
    name= input("what is the name?: ")
    name= name.capitalize()

    nation= input("what is the nation they were born to?: ")
    nation= nation.casefold() #method casefold ignores capitalization

    element= input("what is the element they weild?: ")
    element= element.casefold()
    
    return avatar(name,nation,element)
    
            
main()

