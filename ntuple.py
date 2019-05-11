class Ntuple:
    def __init__(self, size):
        self.size = size
        self._tuple = []

    @property
    def value(self):
        return self._tuple.copy()

    def add(self, value):
        if len(self._tuple) == self.size:
            raise ValueError(f'Max Ntuple size: {self.size} reached')
        self._tuple.append(value)

    def add_all(self, all_value):
        if len(self._tuple) + len(all_value) > self.size:
            raise ValueError(f'Max Ntuple size: {self.size} reached')
        self._tuple += all_value

    def __eq__(self, ntuple):
        return set(self._tuple) == set(ntuple.value)

    def __str__(self):
        return str(self._tuple)

    def __repr__(self):
        return self.__str__()


class NtupleFactory:
    def __init__(self, thesaurus, size: int):
        self.size = size
        self.thesaurus = thesaurus

    def get_ntuple_from_line(self, line: str):
        ntuple_list = []
        line = line.lower()
        words = [self.thesaurus.get_synonym(each_word) for each_word in line.split()]
        word_len = len(words)

        if word_len < self.size:
            ntuple = Ntuple(self.size)
            ntuple.add_all(words)
            return [ntuple]

        index = 0
        while index < word_len:
            ntuple = Ntuple(self.size)
            end_index = index + self.size
            if end_index > word_len:
                break

            for pos in range(index, end_index):
                ntuple.add(words[pos])

            ntuple_list.append(ntuple)

            index += 1

        return ntuple_list

    def get_ntuple_list_from_file(self, file):
        ntuple_list = []
        with file as f:
            for each_line in f:
                ntuple_list += self.get_ntuple_from_line(each_line)
        return ntuple_list
