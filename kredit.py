'''Modul zur Berechnung des Kredites'''
class Kredit():
    def __init__(self, KREDIT, LAUFZEIT, ZINSSATZ, TILGUNGSSATZ):
        '''initialisiere die Variablen und starte die Berechnung'''
        self.rest = KREDIT
        self.laufzeit = LAUFZEIT
        self.zinssatz = ZINSSATZ / 100
        self.tilgungssatz = TILGUNGSSATZ / 100
        # wird später berechnet
        self.rate = 0
        self.gesamt_tilgung = 0
        self.gesamt_zins = 0
        #starte die Berechnung
        self.rechne()

    def rechne(self):
        '''führe die Berechnungen aus'''
        self.berechne_rate()
        self.berechne_kredit()

    def berechne_rate(self):
        '''Berechne die Rate (gleichbleibend, wird durch die Variablen im ersten Monat definiert'''
        zinsen = self.rest * self.zinssatz / 12
        tilgung = self.rest * self.tilgungssatz / 12
        self.rate = zinsen + tilgung

    def berechne_kredit(self):
        '''Berechne den Kredit bis zum Ende der Laufzeit durch'''
        for monat in range(1, (self.laufzeit * 12) +1):
            aktuelle_zinsen = self.rest * self.zinssatz / 12
            aktuelle_rückzahlung = self.rate - aktuelle_zinsen
            self.gesamt_tilgung += aktuelle_rückzahlung
            self.gesamt_zins += aktuelle_zinsen
            self.rest -= aktuelle_rückzahlung