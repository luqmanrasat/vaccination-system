class Vaccine:
    def __init__(self, vacCode, dosRequired, interval, ageMin, ageMax):
        self.vacCode = vacCode
        self.dosRequired = dosRequired
        self.interval = interval
        self.ageMin = ageMin
        self.ageMax = ageMax

    def isEligible(self, age):
        if self.ageMax == '-':
            if age >= self.ageMin:
                return True
        else:
            if age >= self.ageMin and age <= self.ageMax:
                return True
        return False
