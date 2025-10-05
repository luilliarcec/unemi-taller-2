from create import create_contact
from search import search_contact

def menu():
    while True:
        print("\n📞 Contact Manager")
        print("1. Crear contacto")
        print("2. Buscar contacto")
        print("3. Salir")
        choice = input("Selecciona una opción: ")

        if choice == '1':
            name = input("Nombre: ")
            phone = input("Teléfono: ")
            if create_contact(name, phone):
                print("✅ Contacto creado.")
            else:
                print("❌ Número ya registrado.")
        elif choice == '2':
            query = input("Buscar por nombre o número: ")
            results = search_contact(query)
            if results:
                for c in results:
                    print(f"{c['Name']} - {c['Phone']}")
            else:
                print("🔍 No se encontraron coincidencias.")
        elif choice == '3':
            print("👋 Saliendo del gestor de contactos.")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == '__main__':
    menu()