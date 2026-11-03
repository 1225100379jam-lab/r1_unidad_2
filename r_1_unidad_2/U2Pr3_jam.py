import requests


def menu():
  while True:
    print("\n================== MENÚ THESPORTSDB ==================")
    print("1. Consultar equipo")
    print("2. Consultar jugador")
    print("3. Consultar listado de todas las ligas")
    print("4. Consultar una liga en específico")
    print("5. Salir")
    print("=======================================================")

    opcion_input = input("Selecciona una opción (1-5): ").strip()

    if not opcion_input.isdigit():
      print("[Error] Ingresa un número válido de opción.")
      continue

    opcion = int(opcion_input)

    if opcion == 1:
      equipo = input("Ingresa el nombre del equipo (ej. Arsenal): ").strip()
      if not equipo:
        print("[Error] El nombre no puede estar vacío.")
        continue
      url = f"https://www.thesportsdb.com/api/v1/json/123/searchteams.php?t={equipo}"
      consultar_api(url, "equipo")

    elif opcion == 2:
      jugador = input("Ingresa el nombre del jugador (ej. Messi): ").strip()
      if not jugador:
        print("[Error] El nombre no puede estar vacío.")
        continue
      url = f"https://www.thesportsdb.com/api/v1/json/123/searchplayers.php?p={jugador}"
      consultar_api(url, "jugador")

    elif opcion == 3:
      url = "https://www.thesportsdb.com/api/v1/json/123/all_leagues.php"
      consultar_api(url, "ligas")

    elif opcion == 4:
      id_liga = input("Ingresa el ID de la liga (por defecto 4346): ").strip()
      if not id_liga.isdigit():
        print("[Error] El ID debe ser un valor numérico.")
        continue
      url = f"https://www.thesportsdb.com/api/v1/json/123/lookupleague.php?id={id_liga}"
      consultar_api(url, "liga_especifica")

    elif opcion == 5:
      print("¡Saliendo del programa. Hasta luego!")
      break
    else:
      print("[Error] Opción fuera de rango. Elige un número del 1 al 5.")


def consultar_api(url, tipo):
  try:
    response = requests.get(url)
    if response.status_code != 200:
      print(f"[Aviso] La API respondió con código de estado: {response.status_code}")
      return

    data = response.json()

    if tipo == "equipo":
      teams = data.get("teams")
      if teams:
        t = teams[0]
        print(f"\n--- INFORMACIÓN DEL EQUIPO ---")
        print(f"ID del equipo: {t.get('idTeam')}")
        print(f"Nombre del equipo: {t.get('strTeam')}")
        print(f"Descripción (ES): {t.get('strDescriptionES', 'No disponible')}")
        print(f"Página oficial: {t.get('strWebsite')}")
        print(f"Nombre del estadio: {t.get('strStadium')}")
      else:
        print("\n[Resultado] No se encontró información para ese equipo. Prueba con 'Arsenal'.")

    elif tipo == "jugador":
      players = data.get("player") or data.get("players")
      if players:
        p = players[0]
        print(f"\n--- INFORMACIÓN DEL JUGADOR ---")
        print(f"Nombre completo: {p.get('strPlayer')}")
        print(f"Nacionalidad: {p.get('strNationality')}")
        print(f"Equipo en el que juega: {p.get('strTeam')}")
        print(f"Lugar de nacimiento: {p.get('strBirthLocation')}")
        print(f"Facebook: {p.get('strFacebook')}")
        print(f"Altura: {p.get('strHeight')}")
        print(f"Peso: {p.get('strWeight')}")
      else:
        print("\n[Resultado] No se encontró información para ese jugador.")

    elif tipo == "ligas":
      leagues = data.get("leagues", [])
      print(f"\n--- LISTADO DE LIGAS (Total: {len(leagues)}) ---")
      for l in leagues[:15]:
        print(f"ID Liga: {l.get('idLeague')} | Nombre: {l.get('strLeague')}")

    elif tipo == "liga_especifica":
      leagues = data.get("leagues")
      if leagues:
        l = leagues[0]
        print(f"\n--- INFORMACIÓN DE LA LIGA ---")
        print(f"ID de la liga: {l.get('idLeague')}")
        print(f"Nombre de la liga: {l.get('strLeague')}")
        print(f"Deporte: {l.get('strSport')}")
      else:
        print("\n[Resultado] No se encontró una liga con ese ID.")

  except requests.exceptions.RequestException:
    print("[Error] Ocurrió un problema de conexión con la API.")


if __name__ == "__main__":
  menu()