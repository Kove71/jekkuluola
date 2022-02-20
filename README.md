# Jekkuluola, Tsoha 2022

Sivu, jossa voi katsoa, kommentoida ja äänestää käyttäjien tekemiä vitsejä. [Alkuperäinen määrittely tästä näin](/maarittelydokumentti.md).

## Nykyinen toiminallisuus

- Käyttäjä voi rekisteröityä ja kirjautua
- Kirjautunut käyttäjä voi julkaista vitsin
- Etusivulla näkee kaikki vitsit aikajärjestyksessä
- Vitsit voi järjestää myös pisteiden mukaan
- Käyttäjien profiileja voi katsoa, joissa näkyy heidän julkaisemat vitsit ja saamansa pisteet
- Vitseihin voi kommentoida
- Vitsejä voi äänestää, ja niiden saamat pisteet näytetään yhteenvetona
- Käyttäjillä voi olla admin-oikeudet, ja voivat antaa ylläpito-oikeudet tai bännätä muita käyttäjiä
- Bännätty käyttäjä ei voi kirjautua

En saanut paljoa aikaan tällä viikolla muuton takia. Implementoin vertaisarvioinnin antamat vinkit ja lisäsin melkein kaiken perustoiminnalisuuden. Loppupalautusta vartaen aion korjata ulkoasun, parantaa turvallisuutta ja lisätä tägit ja yksinkertaisen etsimistoiminnallisuuden + viimeistellä admin-hommat. 

## Heroku

- https://jekkuluola.herokuapp.com/

### Testikäyttäjät
#### admin
isojehu
1234

#### bännit
hemuli
0000

Heroku ilmesesti toimii GMT-ajassa, eli kaikki julkasut yms. näkyy olevan 2 tuntia aikasemmin kuin mitä oikeasti on.
