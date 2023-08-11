import random as rnd

__all__ = ["ChessGame"]


class ChessGame:
    _QUEEN_COUNT: int = 8 
    _SIZE_BOARD: int = 8 
    _TRUE_COUNT_POS = range(1, 11)

    def __init__(self):
        self._true_positions = [] 

    def check_queen(self, positions: list[tuple]) -> bool:
        result = True

        if len(positions) != self._QUEEN_COUNT:
            result = False
        else:
            for i in range(self._QUEEN_COUNT - 1):
                if not result:
                    break
                row_1, col_1 = positions[i]
                for j in range(i + 1, self._QUEEN_COUNT):
                    row_2, col_2 = positions[j]
                    if row_1 == row_2 or col_1 == col_2 or abs(row_1 - row_2) == abs(col_1 - col_2):
                        result = False
                        break

        return result

    def gen_true_positions(self, count_pos: int) -> list:
        if count_pos not in self._TRUE_COUNT_POS:
            count_pos = min(self._TRUE_COUNT_POS)

        case_ok = 0
        while case_ok < count_pos:
            generated_position = self._gen_positions()
            if self.check_queen(generated_position):
                case_ok += 1
                self._true_positions.append(generated_position)

        return self._true_positions

    def _gen_positions(self) -> list[tuple[int, int]]:
        result = []
        for i in range(self._SIZE_BOARD):
            result.append((i, rnd.randint(0, self._SIZE_BOARD - 1)))
        return result
