# LUCS-UVC (Version Checker)

## Übersicht

LUCS-UVC ist ein Python-Modul, das eine Klasse zur Versionsüberprüfung bereitstellt. Es ermöglicht die Überprüfung der aktuellen Version einer Anwendung gegen eine Version auf einem Versionsserver. Dies ist nützlich, um sicherzustellen, dass Ihre Anwendung stets auf dem neuesten Stand ist.

## Funktionen

Das Modul besteht aus folgenden Komponenten:
- **UVC Klasse**: Eine Dienstprogrammklasse zur Versionsüberprüfung.
  - **Methoden**:
    - `__init__`: Initialisiert das UVC-Objekt mit der URL des Versionsservers, dem Anwendungsnamen und der aktuellen Version.
    - `get_external_versions`: Ruft externe Versionen vom Versionsserver ab.
    - `check_version`: Vergleicht die aktuelle Version mit den externen Versionen und liefert Feedback zum Update-Status.

## Abhängigkeiten

- `urllib`: Für HTTP-Anfragen zum Abrufen von Versionsinformationen vom Server.
- `re`: Für reguläre Ausdrucksmuster zum Validieren von Versionsformaten.
- `logging`: Zum Protokollieren von Fehlern, die während der Versionsüberprüfung auftreten.

## Installation

Installieren Sie das Paket über `pip`:

```sh
pip install lucs-uvc