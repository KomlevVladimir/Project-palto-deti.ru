class Orders(object):
    def __init__(self, name="", lastname="", email="", phone="", adress="", city="", state="", postcode=""):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.adress = adress
        self.city = city
        self.state = state
        self.postcode = postcode
        
    @classmethod
    def random(cls):
        from random import randint
        return cls(name="name" + str(randint(0, 100000)),
                   lastname="lastname" + str(randint(0, 100000)),
                   email="user" + str(randint(0, 100000)) + "@test.com",
                   phone="1234567",
                   adress="street" + str(randint(0, 9999)),
                   city="Moscow",  state=str(randint(0, 9999)),
                   postcode=str(randint(0, 9))*3)