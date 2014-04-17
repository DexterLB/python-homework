class nonogram(list):
    def transpose(self):
        return nonogram([list(column) for column in zip(*self)])

    def row_counts(self):
        row_groups = []
        for row in self:
            streak = 0
            groups = []
            for cell in row:
                if cell == 'X':
                    streak += 1
                else:
                    if streak:
                        groups.append(streak)
                    streak = 0
            if streak:
                groups.append(streak)
            row_groups.append(groups)
        return row_groups

    def keys(self):
        return {'rows': self.row_counts(),
                'columns': self.transpose().row_counts()}


def validate_nonogram(matrix, keys):
    return nonogram(matrix).keys() == keys
