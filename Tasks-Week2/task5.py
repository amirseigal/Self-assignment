def events_on(events, target_date):
    return [name for name, date in events.items() if date == target_date]


if __name__ == '__main__':
    dortmund_events = {
        "Dortmunder U": "2026-09-19",
        "Museum fuer Kunst und Kulturgeschichte (MKK)": "2026-09-19",
        "Naturmuseum Dortmund": "2026-09-19",
        "DASA Arbeitswelt Ausstellung": "2026-09-19",
        "Brauerei-Museum": "2026-09-19",
        "BORUSSEUM": "2026-09-19",
        "LWL-Museum Zeche Zollern": "2026-09-19",
        "Kindermuseum Adlerturm": "2026-09-19",
        "Konzerthaus Dortmund": "2026-09-19",
        "Kuenstlerinnenhaus Dortmund": "2026-09-19",
        "Ausstellung rund um den Hauptbahnhof": "2026-09-18",
        "Museums-Sonntag Fuehrungen": "2026-09-20",
        "Demokratietag Scharnhorst": "2026-09-25",
    }

    museumsnacht_date = "2026-09-19"
    running = events_on(dortmund_events, museumsnacht_date)

    print(f"Events during the Night of Museums on {museumsnacht_date}:")
    for event in running:
        print("-", event)
