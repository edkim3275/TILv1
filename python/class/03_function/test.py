class Person():

    def __init__(self, name):
        self.name = name
        print(f'응애 난 아기 {self.name}')

    def talk(self):
        print('응애응애')

    
    def __del__(self):
        print(f'저는 갑니다...{self.name}')

hong = Person('길동')
hong.talk()