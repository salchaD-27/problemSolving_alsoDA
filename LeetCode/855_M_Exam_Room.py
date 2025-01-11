import json

inputSeating = str(input())
trimmedSeating = inputSeating[1:-1]
seatingMov = [element.strip().strip('"') for element in trimmedSeating.split(",")]

inputSeatingNum = str(input())
trimmedSeatingNum = inputSeatingNum[1:-1]
seatingMovNum = [element.strip().strip('[]') for element in trimmedSeatingNum.split(",")]

class ExamRoom:    
    seatsOccupied = []
    seatsDiff = []
    seatsOrig = []

    def __init__(self, n, ExamRoomSize):
        self.finalSeating = ['null'] * n
        self.finalSeating[1] = 0
        self.seatsOccupied.append(0)
        self.seatsOccupied.sort()
        
        self.finalSeating[2] = ExamRoomSize - 1
        self.seatsOccupied.append(ExamRoomSize - 1)
        self.seatsOccupied.sort()
    
    def seatNumber(self):
        self.seatsOccupied.sort()
        self.seatsDiff.clear()
        self.seatsOrig.clear()
        for j in range(1, len(self.seatsOccupied)):
            i = j - 1
            self.seatsDiff.append((self.seatsOccupied[j] - self.seatsOccupied[i]) // 2)
            self.seatsOrig.append(self.seatsOccupied[i])
        
        minDiff = 0
        minOrig = 0
        for k in range(len(self.seatsDiff)):
            if self.seatsDiff[k] > minDiff:
                minDiff = self.seatsDiff[k]
                minOrig = self.seatsOrig[k]
        return minDiff + minOrig

    def seat(self, i):
        tempSeat = self.seatNumber()
        self.finalSeating[i] = tempSeat
        self.seatsOccupied.append(tempSeat)
        self.seatsOccupied.sort()

    def leave(self, i, p):
        self.finalSeating[i] = 'null'
        self.seatsOccupied.remove(p)

ExamRoomSize = int(seatingMovNum[0])
n = len(seatingMov)
obj = ExamRoom(n, ExamRoomSize)

for i in range(3, len(seatingMov)):
    if seatingMov[i] == 'seat':
        obj.seat(i)
    elif seatingMov[i] == 'leave':
        obj.leave(i, int(seatingMovNum[i]))

obj.finalSeating = [None if item == 'null' else item for item in obj.finalSeating]
finalSeatingJSON = json.dumps(obj.finalSeating)
print(finalSeatingJSON)