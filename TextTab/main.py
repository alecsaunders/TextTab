from . import Note

class TextTabController():
    def __init__(self):
        self.tab = None

    def format_tab_to_text(self, tab):
        self.tab = tab
        measures = self.tab.split('&')

        all_notes = []

        for m_num, m in enumerate(measures, 1):
            m = m.strip()
            new_lines = []
            measure_notes = []
            for line_num, line in enumerate(m.splitlines(), 1):
                line = line.replace('| ', '').replace(' |', '')
                line = line.strip()
                line_notes = line.split(':')
                if line_notes:
                    for note in line_notes:
                        note = note.strip()
                        if note != '-':
                            position, duration = note.split('-')
                            new_note = Note.Note(m_num, line_num, position, duration)
                            measure_notes.append(new_note)
                        elif note == '-':
                            new_note = Note.Note(m_num, line_num, None, None)
                            measure_notes.append(new_note)
                else:
                    print('no notes')

            all_notes.append(measure_notes)

        divs = self.generate_divs(all_notes)
        return divs


    def generate_divs(self, all_notes):
        divs_list = []
        for m in all_notes:
            measure_lines_list = []
            string1 = "|"
            string2 = "|"
            string3 = "|"
            string4 = "|"
            string5 = "|"
            string6 = "|"

            max_den = int(max(n.denominator for n in m))
            max_char_len = int(max(n.char_len for n in m))

            for n in m:
                note_string = self.add_extra_hyphens(n, max_den, max_char_len)

                if n.string == 1:
                    if n.position:
                        string1 = string1 + note_string
                if n.string == 2:
                    if n.position:
                        string2 = string2 + note_string
                if n.string == 3:
                    if n.position:
                        string3 = string3 + note_string
                if n.string == 4:
                    if n.position:
                        string4 = string4 + note_string
                if n.string == 5:
                    if n.position:
                        string5 = string5 + note_string
                if n.string == 6:
                    if n.position:
                        string6 = string6 + note_string

            measure_lines_list.append(string1)
            measure_lines_list.append(string2)
            measure_lines_list.append(string3)
            measure_lines_list.append(string4)
            measure_lines_list.append(string5)
            measure_lines_list.append(string6)
            divs_list.append(measure_lines_list)


        return divs_list

    def add_extra_hyphens(self, n, max_den, max_char_len):
        note_char = '-' if n.position == 'n' else n.position
        if max_char_len >= 2:
            note_len = n.duration_frac * max_den * 4
        else:
            note_len = n.duration_frac * max_den * 2

        if max_den == 1:
            note_len = 4
        note_string = note_char


        while len(note_string) < note_len:
            note_string = note_string + '-'

        return note_string

    def validate_tab(self):
        if not self.tab:
            return False
        try:
            meta, tabs_raw = self.tab.split(':===:')
            meta_val = self.validate_tab_meta(meta)
            tabs_raw_val = self.validate_tab_tabs_raw(tabs_raw)
            return meta_val and tabs_raw_val
        except:
            return False
        return False

    def validate_tab_meta(self, meta):
        if not meta:
            return False
        meta_lines = meta.splitlines()
        for m in meta_lines:
            if m:
                if ":" not in m:
                    return False
        return True

    def validate_tab_tabs_raw(self, tabs_raw):
        if tabs_raw:
            return True
        return False



if __name__ == '__main__':
    ttc = TextTabController()
    txtab = open('assets/tab_format.txt', 'r').read()
    ttc.tab = txtab
    print(ttc.validate_tab())
