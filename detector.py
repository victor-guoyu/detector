from thesaurus import Thesaurus
from ntuple import NtupleFactory

class Detector:
    def __init__(self, synonym_file, input_file_1, input_file_2, tuple_size):
        self.thesaurus = Thesaurus(synonym_file)
        self.input_file_1 = input_file_1
        self.input_file_2 = input_file_2
        self.tuple_size = tuple_size

    def calculate_percentage(self):
        ntuple_factory = NtupleFactory(thesaurus=self.thesaurus, size=self.tuple_size)
        file_1_ntuples = ntuple_factory.get_ntuple_list_from_file(self.input_file_1)
        file_2_ntuples = ntuple_factory.get_ntuple_list_from_file(self.input_file_2)

        match_count = 0
        for each_tuple_1 in file_1_ntuples:
            for each_tuple_2 in file_2_ntuples:
                if each_tuple_1 == each_tuple_2:
                    match_count += 1

        percentage = 0
        ntuple_1_size = len(file_1_ntuples)
        if ntuple_1_size != 0:
            percentage = (match_count / ntuple_1_size) * 100
            percentage = round(percentage, 2)

        return percentage


