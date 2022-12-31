from konfig import *
from kredit import Kredit
from etf import ETF
from printer import Printer

if __name__ == '__main__':
    kredit = Kredit(KREDIT, KREDIT_LAUFZEIT, KREDIT_ZINSSATZ, KREDIT_TILGUNGSSATZ)
    etf = ETF(ETF_ZINSSATZ, ETF_TER, ETF_STEUERSATZ, ETF_FREIBETRAG, kredit.rest, KREDIT_LAUFZEIT)
    printer = Printer(KREDIT, KREDIT_LAUFZEIT, kredit.rate, etf.rate, kredit.rest, etf.guthaben)
