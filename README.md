# Beschreibung-im-use-case-Templates
# Projekt: Use Case Beschreibung

## UC 1.01: Benutzeranmeldung

### Ziel
Der Use Case beschreibt den Vorgang, bei dem ein registrierter Benutzer sich im System anmeldet, um Zugriff auf geschützte Inhalte und Funktionen zu erhalten.

### Akteure
- **Primärer Akteur**: Registrierter Benutzer  
- **Sekundärer Akteur**: Authentifizierungs-Service

### Vorbedingungen
- Benutzer verfügt über gültige Login-Daten (Benutzername/E-Mail, Passwort).  
- Das System ist erreichbar (Server, Datenbank etc.).

### Ablauf (Hauptszenario)
1. Benutzer ruft die Login-Seite auf.  
2. Benutzer gibt Benutzernamen/E-Mail und Passwort ein.  
3. Benutzer klickt auf „Login“.  
4. System prüft die Anmeldedaten (Authentifizierung).  
5. Bei korrekten Daten wird der Benutzer auf sein Dashboard weitergeleitet.

### Nachbedingung
- **Erfolgreich**: Benutzer ist eingeloggt und sieht sein personalisiertes Dashboard.  
- **Fehlgeschlagen**: Benutzer bleibt auf der Login-Seite und erhält eine Fehlermeldung.

### Ausnahmen
1. **Falsche Zugangsdaten**: System zeigt Fehlermeldung „Benutzerdaten inkorrekt“.  
2. **Verbindungsfehler**: System meldet einen technischen Fehler. Benutzer versucht es erneut.



