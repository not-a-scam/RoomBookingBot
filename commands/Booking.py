class Booking:
    def __init__(
            self = None, 
            name= None, 
            pax= None, 
            date= None, 
            time= None, 
            purpose= None,
            screen= None, 
            request= None):
        self.name = name
        self.pax = pax
        self.date = date
        self.time = time
        self.purpose = purpose
        self.screen = screen
        self.request = request
    
    def __str__(self):
        res = ""
        if self.name : res += ("Name: " + self.name + '\n')
        if self.pax : res += ("Number of people: " + self.pax + '\n')
        if self.date : res += ("Date: " + self.date + '\n')
        if self.time : res += ("Time: " + self.time + '\n')
        if self.purpose : res += ("Purpose: " + self.purpose + '\n')
        if self.screen : res += ("Need Screen: " + self.screen + '\n')
        if self.request : res += ("Requests: " + self.request + '\n')
        if res == "" : res = "Empty"
        return res