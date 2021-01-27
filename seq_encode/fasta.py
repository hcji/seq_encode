class Fasta:
    def read_fasta_file_as_list_of_pairs(self, file_name):
        fasta_file = open(file_name, 'r')
        main_list_sequences = []
        pairs = []
        line = fasta_file.readline()
        while line:
            if line[0] == '>':
                # Create new list pair with this line as id
                main_list_sequences.append(pairs)
                pairs = [line[1:], ""]
            else:
                # Concatenate the line to the last value of the last list
                pairs[1] = pairs[1] + line.replace('\n', '')
            line = fasta_file.readline()
        main_list_sequences.append(pairs)
        main_list_sequences.pop(0)
        fasta_file.close()
        return main_list_sequences

    def read_fasta_file_as_dictionary(self, file_name):
        fasta_file = open(file_name, 'r')
        main_dictionary_of_sequences = {}
        last_id = ""
        for line in fasta_file:
            if line[0] == '>':
                blank_string = ""
                main_dictionary_of_sequences.update({line[1:]: blank_string})
                last_id = line[1:]
            else:
                last_line = main_dictionary_of_sequences[last_id]
                updated_line = last_line + line.replace('\n', '')
                main_dictionary_of_sequences.update({last_id: updated_line})
        fasta_file.close()
        return main_dictionary_of_sequences