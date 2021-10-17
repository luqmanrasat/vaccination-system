class VaccinationRecord:
    def __init__(self, patientId, dose1, dose2='-'):
        self.patientId = patientId
        self.dose1 = dose1
        self.dose2 = dose2