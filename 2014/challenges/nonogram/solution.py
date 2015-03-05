<<<<<<< HEAD
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
=======
EMPTY = ' '


def transpose(matrix):
    return [list(column) for column in zip(*matrix)]


def validate_row(row, row_keys):
    return all(len(filled_group) == key
               for filled_group, key in
               zip(filter(lambda x: x != '', ''.join(row).split(EMPTY)),
                   row_keys))


def validate_nonogram(nonogram, keys):
    lines_for_validation = zip(nonogram + transpose(nonogram),
                               keys['rows'] + keys['columns'])

    return all(validate_row(*line) for line in lines_for_validation)
>>>>>>> 27b8bc94a0affac85b2780f057b389ff39faf9ac
