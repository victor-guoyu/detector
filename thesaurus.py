class Thesaurus:
    def __init__(self, synonym_file):
        self.lookup_dict = self._init_lookup_dict(synonym_file)

    def get_synonym(self, word:str) -> str:
        """
        return the synonym of a given word
        if nothing is found, return the word itself
        """
        word = word.lower()
        return self.lookup_dict.get(word, word)

    @staticmethod
    def _init_lookup_dict(synonym_file):
        """
        Build a lookup table for all the synonym
            key - being the synonym
            value - first value from the synonym list
        """
        lookup_dict = {}
        with synonym_file as file:
            for each_line in file:
                synonyms = each_line.split()
                first_value = synonyms[0].lower()
                for each_synonym in synonyms:
                    each_synonym = each_synonym.lower()
                    lookup_dict[each_synonym] = first_value

        return lookup_dict
