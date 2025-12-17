projects = {}
tasks = {}

def menu():
    print("\n=== MENU UTAMA ===")
    print("1. CRUD Proyek")
    print("2. CRUD Task")
    print("3. Sorting / Search")
    print("0. Keluar")

def crud_proyek():
    print("\n--- CRUD PROYEK ---")
    print("1. Tambah")
    print("2. Update")
    print("3. Hapus")
    choice = input("Pilih: ")

    if choice == "1":
        pid = input("ID Proyek: ")
        name = input("Nama Proyek: ")
        projects[pid] = name
        print("Proyek ditambahkan")

    elif choice == "2":
        pid = input("ID Proyek: ")
        if pid in projects:
            projects[pid] = input("Nama baru: ")
            print("Proyek diupdate")
        else:
            print("ID Proyek tidak ditemukan")

    elif choice == "3":
        pid = input("ID Proyek: ")
        if pid in projects:
            del projects[pid]
            print("Proyek dihapus")
        else:
            print("ID Proyek tidak ditemukan")

def crud_task():
    pid = input("Masukkan ID Proyek: ")
    if pid not in projects:
        print("ID Proyek tidak valid")
        return

    print("\n--- CRUD TASK ---")
    print("1. Tambah")
    print("2. Update")
    print("3. Hapus")
    choice = input("Pilih: ")

    tasks.setdefault(pid, [])

    if choice == "1":
        task = input("Nama Task: ")
        tasks[pid].append(task)
        print("Task ditambahkan")

    elif choice == "2":
        for i, t in enumerate(tasks[pid]):
            print(i, t)
        idx = int(input("Index task: "))
        tasks[pid][idx] = input("Nama baru: ")
        print("Task diupdate")

    elif choice == "3":
        for i, t in enumerate(tasks[pid]):
            print(i, t)
        idx = int(input("Index task: "))
        tasks[pid].pop(idx)
        print("Task dihapus")

def sorting_search():
    print("\n--- SORTING / SEARCH ---")
    print("1. Sorting Proyek")
    print("2. Cari Proyek")
    choice = input("Pilih: ")

    if choice == "1":
        for k in sorted(projects):
            print(k, projects[k])

    elif choice == "2":
        keyword = input("Cari nama proyek: ")
        for k, v in projects.items():
            if keyword.lower() in v.lower():
                print(k, v)

# MAIN LOOP
while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        crud_proyek()
    elif pilihan == "2":
        crud_task()
    elif pilihan == "3":
        sorting_search()
    elif pilihan == "0":
        print("Keluar...")
        break
    else:
        print("Menu tidak valid")