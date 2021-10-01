class Mamalia:
    def intro (self):
        print("Terdapat beragam spesies mamalia yang hidup di Bumi")

    def herbifora(self):
        print("hampir semua spesies mamalia pemakan tumbuhan, namun ada beberapa spesies mamalia yang tidak memakan tumbuhan")

class Jerapah (Mamalia):
    def herbifora(self):
        print("Jelapah merupakan spesies mamalia pemakan tumbuhan (herbifora)")

class Harimau (Mamalia):
    def herbifora(self):
        print("Harimau merupakan spesies mamalia pemakan daging (karnifora) dan tidak memakan tumbuhan")

class Sapi (Mamalia):
    def herbiforaa(self):
        print("Sapi merupakan spesies mamalia pemakan tumbuhan (herbifora)")

obj_mamalia = Mamalia()
obj_jerapah =Jerapah()
obj_harimau = Harimau()
obj_sapi = Sapi()

obj_mamalia.intro()
obj_mamalia.herbifora()

print ("===========================")
obj_mamalia.intro()
obj_jerapah.herbifora()

print ("===========================")
obj_mamalia.intro()
obj_harimau.herbifora()

print ("===========================")
obj_mamalia.intro()
obj_sapi.herbifora()

