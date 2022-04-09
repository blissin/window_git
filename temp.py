class SoccerPlayer(object):
    def __init__(self, name, position, back_number):
        self.name=name
        self.position=position
        self.back_number=back_number
    
    def __str__(self):
        return "hello, my name is %s" %(self.name)
    
    def change_back_number(self,new_number) :
        print("선수의 등번호를 번경합니다 : from %d to %d" % (self.back_number, new_number))
        self.back_number=new_number
    pass
choi= SoccerPlayer("choi","mf",20)
print(choi)
choi.change_back_number(100)