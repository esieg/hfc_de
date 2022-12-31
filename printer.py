class Printer():
    def __init__(self, kredit, laufzeit, k_rate, e_rate, restkredit, guthaben):
        self.kredit = kredit
        self.laufzeit = laufzeit
        self.kreditrate = k_rate
        self.etf_rate = e_rate
        self.restkredit = restkredit
        self.guthaben = guthaben
        self.ausgabe()

    def ausgabe(self):
        '''gebe das Resultat aus'''
        print('RESULTAT:\n\n',
        F'für einen Kredit über {self.kredit} über {self.laufzeit} ergibt sich eine',
        f'monatliche Gesamtbelastung: {self.kreditrate + self.etf_rate:.2f}€.\n',
        f'Diese setzt sich zusammen aus Kredit und ETF: {self.kreditrate:.2f}€ + {self.etf_rate:.2f}€\n',
        f'Wobei ein Restkredit von {self.restkredit:.2f}€ einem Guthaben von {self.guthaben:.2f}€ gegenübersteht.\n',
        f'Das ergibt einen Überschuss von {self.guthaben - self.restkredit:.2f}€\n\n',
        f'IMMER daran denken, das ist nur eine Schätzung und ohne jegliche Garantie! Siehe dazu auch das Readme.md')