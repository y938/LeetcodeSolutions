class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if coordinates[0] in ("a","c","e","g"):
            if int(coordinates[1]) % 2 ==0:
                return True
            else:
                return False
        elif coordinates[0] in ("b","d","f","h"):
            if int(coordinates[1]) % 2 ==0:
                return False
            else:
                return True