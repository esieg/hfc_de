To the English-speaking folks first of all an apology. Since I am only familiar with the German laws, regulations and financial language (and that probably only rudimentarily), the tool is also in German. 
If you like - and you are familiar with the German and your laws, regulations and financial language - feel free to adapt it for your country. Or contact me with the corresponding info.

By the way, it feels quite strange to work with German variables, functions and classes.

About the actual...

hfr_de == Hausfinanzierungs-Rechner für Deutschland

Ein einfacher Python-Rechner für eine Hausfinanzierung. Der Finanzierungsanteil kann zwischen einem klassischen Ratenkredit (Tilgung zwischen 0 .. 7 %) und thesaurisierenden EFT (zur Tilgung der Restschuld und einem angenommenen durchschnittlichen Zinssatz pro Jahr von 4 ... 7,9 ... 15 %) und einer Laufzeit von 5 .. 20 Jahren gewählt werden.

Zur Konfiguration passen Sie bitte die Werte in der cfg.py an. Die Ergebnisse werden nach dem Start mit "python hfc.py" direkt in die Konsole ausgegeben.

Die Gesetzgebung und Verordnungen basieren denen in Deutschland. Für andere Länder können daher Anpassungen notwendig sein.

Da die Entwicklung des ETFs ohnehin nicht wirklich abgeschätzt werden kann, wird ein Jahresmittelwert angenommen.

Nochmal hier der Hinweis: Auch der Indexbasierte ETF hat seine Schwankungen. Es gibt keinerlei Sicherheit das das errechnete Guthaben zu dem Zeitpunkt wo es benötigt wird, auch da sein wird. Auch lassen sich aus Daten in der Vergangenheit keine verlässlichen Progrnosen für die Zukunft erstellen.

Mindestens Python 3.8

Zu den Variablen:
KREDIT: Höhe des Kredites
KREDIT_LAUFZEIT: Laufzeit des Kredites (auch: Zinsbindung) in Jahren
KREDIT_ZINSSATZ: Zinssatz des Kredites, Angabe in Prozent.
KREDIT_TILGUNGSSATZ: Tilgungssatz des Kredites. Achtung, sollte der Tilgungssatz so hochgewählt werden das der Kredit während der Laufzeit komplett getilgt wird, ergibt dieser Rechner keinen Sinn und gibt für den Kredit einen negativen Wert aus. Angabe in Prozent.

ETF_ZINSSATZ: Der Zinssatz der für den ETF erwartet wird (Historisch gesehen bei etwa 7,9%). Angabe in Prozent.
ETF_TER: Der TER des ETFs. Angabe in Prozent.
ETF_STEUERSATZ: Der Steuersatz der Einkommenssteuer. In Deutschland typischerweise bei 25 %, Angabe in Prozent.
ETF_FREIBETRAG: Freibetrag der Einkommenssteuer. In Deutschland ab 2023 bei 1000 € pro Person. 

Angabe als Prozent bedeutet: Für 7,9% geb bitte 7.9 ein.