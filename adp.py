class Mobile:
    def __init__(self,M):
        self.model = M

    def show_model(self):
        d = {
            'Model': self.model
        }
        return d

redme = Mobile('Redme')

a=redme.show_model()
print(id(a))