class ETF():
    def __init__(self, ZINSSATZ, TER, EINKOMMENSSTEUERSATZ, STEUERFREIBETRAG, RESTBETRAG, LAUFZEIT):
        '''initialisiere die Variablen und starte die Berechnung'''
        #feste Variablen
        self.zinssatz = ZINSSATZ / 100
        self.ter = TER / 100
        self.steuersatz = EINKOMMENSSTEUERSATZ / 100
        self.steuerfreibetrag = STEUERFREIBETRAG
        self.zielsumme = RESTBETRAG
        self.laufzeit = LAUFZEIT
        #Schätzungsvariablen
        self.schrittweite = 500
        self.rate = 0
        self.gesamteinzahlung = 0
        self.gesamtzins = 0
        self.guthaben = 0
        self.weiter_schätzen = True
        #starte die Schätzung
        self.schätze_etf_rate()

    def weiter(self):
        '''Muss weiter geschätzt werden, wenn ja, mit welcher Rate und Schrittweite?'''
        if(self.guthaben > self.zielsumme):
            if(self.schrittweite == 5):
                self.weiter_schätzen = False
            else:
                self.rate -= self.schrittweite
                self.schrittweite /= 10

    def schätze_etf_rate(self):
        '''Schätze die monatliche ETF-Einlage, Annäherung iterativ in kleiner werdenden Intervallen'''
        while (self.weiter_schätzen):
            self.rate += self.schrittweite
            #setze Berechnungsvariablen zurück
            self.guthaben = 0
            self.gesamteinzahlung = 0
            self.gesamtzins = 0
            for jahr in range(1, self.laufzeit + 1):
                jahres_rate = self.rate * 12
                aktueller_zins = (self.guthaben + jahres_rate / 2) * self.zinssatz

                einkommenssteuer = (aktueller_zins - self.steuerfreibetrag) * self.steuersatz
                einkommenssteuer = 0 if(einkommenssteuer < 0) else einkommenssteuer # verhindere negative Steuern

                aktueller_ter = (self.guthaben + jahres_rate + aktueller_zins) * self.ter
                self.gesamteinzahlung += jahres_rate
                self.gesamtzins += aktueller_zins - einkommenssteuer - aktueller_ter
                self.guthaben += jahres_rate + aktueller_zins - einkommenssteuer - aktueller_ter
            
            self.weiter()