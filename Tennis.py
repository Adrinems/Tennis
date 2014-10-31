class Tennis:
    p2 = 0
    p1 = 0
    ps1 = 0
    ps2 = 0

   

    def add_point(self, player):

        if player == 1:
            if Tennis.p1 == 0:
                Tennis.p1 += 15
            elif Tennis.p1 == 15:
                Tennis.p1 += 15
            elif Tennis.p1 == 30:
                Tennis.p1 += 10
            elif Tennis.p1 >= 40:
                Tennis.p1 += 1
        else:
            if Tennis.p2 == 0:
                Tennis.p2 += 15
            elif Tennis.p2 == 15:
                Tennis.p2 += 15
            elif Tennis.p2 == 30:
                Tennis.p2 += 10
            elif Tennis.p2 >= 40:
                Tennis.p2 += 1

    def show_score(self):
        print '{0} {1}'.format(Tennis.p1, Tennis.p2)
        if (Tennis.p1 == 40) and (Tennis.p1 == Tennis.p2):
            return "DEUCE"
        elif Tennis.p1 > 40 and Tennis.p1 > Tennis.p2 and ((Tennis.p1 - Tennis.p2) >= 2):
            Tennis.ps1 += 1
            Tennis.p1 = 0
            Tennis.p2 = 0
            return "GAME Player 1"
        elif Tennis.p2 > 40 and Tennis.p2 > Tennis.p1 and ((Tennis.p2 - Tennis.p1) >= 2):
            Tennis.ps2 += 1
            Tennis.p1 = 0
            Tennis.p2 = 0
            return "GAME Player 2"
        elif Tennis.p1 > 40 and Tennis.p2 >= 40 and Tennis.p1 > Tennis.p2:
            return "ADV {0}".format(Tennis.p2)
        elif Tennis.p2 > 40 and Tennis.p1 >= 40 and Tennis.p2 > Tennis.p1:
            return "{0} ADV".format(Tennis.p1)

        else:
            return '{0} {1}'.format(Tennis.p1, Tennis.p2)
