class House:
    elementary_school = "FV Elementary"
    middle_school = "FV Middle"
    high_school = "FV High"

    # TODO: create an initialization method, and three instance attributes:
    # attribute name "size" with int value 2000
    # attribute name "owner" from argument during class calling
    # attribute name "address" from argument during class calling

    def __init__ (self, owner, address):
        self.size = 2500
        self.owner = owner
        self.address = address
