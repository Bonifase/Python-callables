class EverExpandingAwareness():
    def __init__(self, awareness, love, beauty, abundance, intelligence):
        self.awareness = awareness
        self.love = love
        self.beauty = beauty
        self.abundance = abundance
        self.intelligence = intelligence

    def choice(self):
        if not self.awareness:
            sadness = True
            print('I am don\t {} you'.format(self.love))
