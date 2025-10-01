# Importem la classe 'date' de la llibreria 'datetime' per a treballar amb dates.
from datetime import date

print("--- CALCULADORA DE MAJORIA D'EDAT ---")

try:
    # Demanem la data de naixement a l'usuari per separat (dia, mes, any).
    dia_naixement = int(input("Introdueix el teu DIA de naixement (ex: 5): "))
    mes_naixement = int(input("Introdueix el teu MES de naixement (ex: 11): "))
    any_naixement = int(input("Introdueix el teu ANY de naixement (ex: 1998): "))

    # Obtenim la data actual del sistema.
    data_actual = date.today()

    # Intentem crear un objecte de data amb les dades introduïdes.
    # Si la data és impossible (ex: 30 de febrer), això donarà un error.
    data_naixement = date(any_naixement, mes_naixement, dia_naixement)

    # Comprovem que la data de naixement no sigui futura.
    if data_naixement > data_actual:
        print("\n❌ ERROR: La data de naixement no pot ser en el futur.")

    else:
        # Calculem l'edat.
        # Restem els anys i després ajustem si encara no ha fet els anys enguany.
        edat = data_actual.year - data_naixement.year - ((data_actual.month, data_actual.day) < (data_naixement.month, data_naixement.day))

        # Comprovem si és major d'edat.
        if edat >= 18:
            print(f"\n✅ Tens {edat} anys. Ets major d'edat.")
        else:
            print(f"\nℹ️ Tens {edat} anys. No ets major d'edat.")

# Si ocorreix un error en crear la data (ex: dia o mes no vàlids), s'executa aquest bloc.
except ValueError:
    print("\n❌ ERROR: La data introduïda és impossible o no és correcta. Revisa que la data sigui correcta.")

# Si l'usuari introdueix alguna cosa que no és un número (ex: text).
except TypeError:
    print("\n❌ ERROR: Si us plau, introdueix només números per a la data.")


print("\n--- Programa Finalitzat ---")