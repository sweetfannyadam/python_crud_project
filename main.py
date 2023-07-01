import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import sqlite3

import _tkinter

# --------------------------------------------------SQLITE CONNECTION---------------------------------------------------
conn = sqlite3.connect("data_koperasi.db")
cursor = conn.cursor()

# ----------------------------------------------------MAIN WINDOW-------------------------------------------------------
main_window = tkinter.Tk()
main_window.title("Formulir Anggota Koperasi")
window_height = 750
window_width = 650

screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()

x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))

main_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

# -------------------------------------------------------FRAMES----------------------------------------------------------
frame1 = tkinter.Frame(main_window)
frame1.grid(column=0, row=0, pady=10)

frame2 = tkinter.Frame(main_window)
frame2.grid(column=0, row=1, pady=10)

frame3 = tkinter.Frame(main_window)
frame3.grid(column=0, row=2, pady=10)

data_input_frame = tkinter.LabelFrame(frame1)
data_input_frame.pack(side=LEFT, anchor=CENTER, padx=10)

button_frame = tkinter.LabelFrame(frame1)
button_frame.pack(side=RIGHT, anchor=CENTER, padx=10)

table_frame = tkinter.LabelFrame(frame3)
table_frame.pack(side="left", padx=10)

search_frame = tkinter.LabelFrame(frame2, text="Cari Berdasarkan")
search_frame.grid(padx=10)

# -------------------------------------------------------LABELS----------------------------------------------------------
no_anggota_label = tkinter.Label(data_input_frame, text=f"{'No. Anggota:':>14}")
no_anggota_label.grid(column=0, row=0, sticky="w", padx=10, pady=3)

nama_anggota_label = tkinter.Label(data_input_frame, text=f"{'Nama:':>19}")
nama_anggota_label.grid(column=0, row=1, sticky="w", padx=10, pady=3)

alamat_anggota_label = tkinter.Label(data_input_frame, text=f"{'Alamat:':>19}")
alamat_anggota_label.grid(column=0, row=2, sticky="w", padx=10, pady=3)

kota_anggota_label = tkinter.Label(data_input_frame, text=f"{'Kota:':>21}")
kota_anggota_label.place(height=400)
kota_anggota_label.grid(column=0, row=3, sticky="w", padx=10, pady=3)

notelp_anggota_label = tkinter.Label(data_input_frame, text=f"{'No. Telp:':>19}")
notelp_anggota_label.place(height=400)
notelp_anggota_label.grid(column=0, row=4, sticky="w", padx=10, pady=3)

pekerjaan_anggota_label = tkinter.Label(data_input_frame, text=f"{'Pekerjaan:':>18}")
pekerjaan_anggota_label.place(height=400)
pekerjaan_anggota_label.grid(column=0, row=5, sticky="w", padx=10, pady=3)

kode_anggota_label = tkinter.Label(search_frame, text="Kode Anggota :", anchor="e")
kode_anggota_label.grid(row=0, column=2, padx=3)

nama_anggota_label = tkinter.Label(search_frame, text="Nama Anggota :")
nama_anggota_label.grid(row=0, column=4, padx=3)
main_window.bind("<Return>", (lambda event: AppFunctions.search_command()))

# -------------------------------------------------ENTRY BOXES----------------------------------------------------------
no_anggota_entry = tkinter.Entry(data_input_frame, width=20)
no_anggota_entry.grid(column=1, row=0, sticky='w', padx=5)

nama_entry = tkinter.Entry(data_input_frame, width=35)
nama_entry.grid(column=1, row=1, sticky='w', padx=5)

alamat_entry = tkinter.Entry(data_input_frame, width=50)
alamat_entry.grid(column=1, row=2, sticky='ew', padx=5)

kota_entry = tkinter.Entry(data_input_frame, width=25)
kota_entry.grid(column=1, row=3, sticky='w', padx=5)

notelp_entry = tkinter.Entry(data_input_frame, width=25)
notelp_entry.grid(column=1, row=4, sticky='w', padx=5)

pekerjaan_entry = tkinter.Entry(data_input_frame, width=25)
pekerjaan_entry.grid(column=1, row=5, sticky='w', padx=5)

kode_anggota_entry = tkinter.Entry(search_frame)
kode_anggota_entry.grid(row=0, column=3, pady=10, padx=10)

pencarian_nama_entry = tkinter.Entry(search_frame)
pencarian_nama_entry.grid(row=0, column=10, padx=10)

# -----------------------------------------------TREEVIEW TABLE---------------------------------------------------------
tv_scrollbar = Scrollbar(table_frame, orient=VERTICAL)
tv_scrollbar.pack(side=RIGHT, fill=Y)

tv = ttk.Treeview(table_frame,
                  columns=["1", "2", "3", "4", "5", "6"],
                  show="headings",
                  yscrollcommand=tv_scrollbar.set,
                  selectmode="extended")

tv.pack(side=LEFT)
tv.heading("1", text="No. Anggota")
tv.heading("2", text="Nama")
tv.heading("3", text="Alamat")
tv.heading("4", text="Kota")
tv.heading("5", text="No. Telpon")
tv.heading("6", text="Pekerjaan")

tv.column(1, anchor="center", width=80, stretch=False)
tv.column(2, anchor="center", width=110)
tv.column(3, anchor="center", width=150)
tv.column(4, anchor="center", width=90)
tv.column(5, anchor="center", width=80)
tv.column(6, anchor="center", width=100)

tv.tag_configure('oddrow', background="white")
tv.tag_configure('evenrow', background="lightblue")

tv_scrollbar.configure(command=tv.yview)

# ------------------------------------------------ FUNCTIONALITY -------------------------------------------------------


def query_database():
    fetch_database_dict_query = '''SELECT No_Anggota, Nama, Alamat, Kota, No_Telp, Pekerjaan FROM Data_Koperasi'''
    cursor.execute(fetch_database_dict_query)
    fetched_data = cursor.fetchall()

    for record in fetched_data:
        tv.insert(parent='', index='end', text='', values=record)

    conn.commit()


class AppFunctions:
    @classmethod
    def fetch_input_data(cls):
        no_anggota = no_anggota_entry.get()
        nama = nama_entry.get()
        alamat = alamat_entry.get()
        kota = kota_entry.get()
        no_telp = notelp_entry.get()
        pekerjaan = pekerjaan_entry.get()
        input_data = (
            no_anggota,
            nama,
            alamat,
            kota,
            no_telp,
            pekerjaan
        )
        return input_data

    @classmethod
    def create_table(cls):
        create_table_query = '''CREATE TABLE IF NOT EXISTS Data_Koperasi(
            No INTEGER PRIMARY KEY AUTOINCREMENT,
            No_Anggota VARCHAR NOT NULL, 
            Nama TEXT NOT NULL, 
            Alamat TEXT NOT NULL, 
            Kota TEXT NOT NULL, 
            No_Telp VARCHAR NOT NULL,
            Pekerjaan TEXT);'''
        cursor.execute(create_table_query)
        conn.commit()

    @classmethod
    def insert_data(cls):
        insert_data_tuple = AppFunctions.fetch_input_data()
        insert_data_query = '''INSERT INTO Data_Koperasi (
                No_Anggota,
                Nama, 
                Alamat, 
                Kota,
                No_Telp, 
                Pekerjaan) VALUES (?, ?, ?, ?, ?, ?);'''

        if len(insert_data_tuple[0]) == 0:
            messagebox.showerror("Error", "Masukkan No. Anggota terlebih dahulu!")
            
        elif len(insert_data_tuple[1]) == 0:
            messagebox.showerror("Error", "Masukkan Nama terlebih dahulu!")
            
        elif len(insert_data_tuple[2]) == 0:
            messagebox.showerror("Error", "Masukkan Alamat terlebih dahulu!")
            
        elif len(insert_data_tuple[3]) == 0:
            messagebox.showerror("Error", "Masukkan Kota terlebih dahulu!")
            
        elif len(insert_data_tuple[4]) == 0:
            messagebox.showerror("Error", "Masukkan No. Telpon terlebih dahulu!")
            
        elif len(insert_data_tuple[5]) == 0:
            messagebox.showerror("Error", "Masukkan Pekerjaan terlebih dahulu!")

        elif type(int(insert_data_tuple[0])) != int or type(int(insert_data_tuple[4])) != int:
            messagebox.showerror("Error", "Pastikan data yang Anda masukkan telah sesuai format angka")

        elif type(insert_data_tuple[1]) != str or type(insert_data_tuple[2]) != str \
                or type(insert_data_tuple[3]) != str or type(insert_data_tuple[5]) != str:
            messagebox.showerror("Error", "Pastikan data yang Anda masukkan telah sesuai format alfabet")

        else:
            cursor.execute(insert_data_query, insert_data_tuple)
            conn.commit()
            
    @classmethod
    def delete_data(cls):
        selected = tv.focus()
        selected_items = tv.item(selected, "values")
        print(f"selected_items: {selected_items[0]}")
        conn.execute('''DELETE from Data_Koperasi WHERE No_Anggota = ?''',
                     (selected_items[0],))
        tv.delete(selected)

    @classmethod
    def delete_alldata(cls):
        cursor.execute('''DELETE FROM Data_Koperasi;''')
        conn.commit()
        cursor.execute('''VACUUM;''')
        conn.commit()

    @classmethod
    def update_popup(cls):
        selected = tv.focus()
        selected_items = tv.item(selected, "values")

        root = Toplevel(main_window)
        root.title("Ubah Data")
        root.attributes('-topmost', True)
        root.tk.eval(f'tk::PlaceWindow {root} center')

        frame = tkinter.LabelFrame(root)
        frame.pack(side=LEFT, anchor=CENTER, padx=10, pady=10)

        update_no_anggota_label = tkinter.Label(frame, text=f"{'No. Anggota:':>14}")
        update_no_anggota_label.grid(column=0, row=0, sticky="w", padx=10, pady=3)

        update_nama_anggota_label = tkinter.Label(frame, text=f"{'Nama:':>19}")
        update_nama_anggota_label.grid(column=0, row=1, sticky="w", padx=10, pady=3)

        update_alamat_anggota_label = tkinter.Label(frame, text=f"{'Alamat:':>19}")
        update_alamat_anggota_label.grid(column=0, row=2, sticky="w", padx=10, pady=3)

        update_kota_anggota_label = tkinter.Label(frame, text=f"{'Kota:':>21}")
        update_kota_anggota_label.grid(column=0, row=3, sticky="w", padx=10, pady=3)

        update_notelp_anggota_label = tkinter.Label(frame, text=f"{'No. Telp:':>19}")
        update_notelp_anggota_label.grid(column=0, row=4, sticky="w", padx=10, pady=3)

        update_pekerjaan_anggota_label = tkinter.Label(frame, text=f"{'Pekerjaan:':>18}")
        update_pekerjaan_anggota_label.grid(column=0, row=5, sticky="w", padx=10, pady=3)

        update_no_anggota_entry = tkinter.Entry(frame, width=20)
        update_no_anggota_entry.grid(column=1, row=0, sticky='w', padx=5)
        update_no_anggota_entry.insert(0, selected_items[0])

        update_nama_entry = tkinter.Entry(frame, width=35)
        update_nama_entry.grid(column=1, row=1, sticky='w', padx=5)
        update_nama_entry.insert(0, selected_items[1])

        update_alamat_entry = tkinter.Entry(frame, width=50)
        update_alamat_entry.grid(column=1, row=2, sticky='ew', padx=5)
        update_alamat_entry.insert(0, selected_items[2])

        update_kota_entry = tkinter.Entry(frame, width=25)
        update_kota_entry.grid(column=1, row=3, sticky='w', padx=5)
        update_kota_entry.insert(0, selected_items[3])

        update_notelp_entry = tkinter.Entry(frame, width=25)
        update_notelp_entry.grid(column=1, row=4, sticky='w', padx=5)
        update_notelp_entry.insert(0, selected_items[4])

        update_pekerjaan_entry = tkinter.Entry(frame, width=25)
        update_pekerjaan_entry.grid(column=1, row=5, sticky='w', padx=5)
        update_pekerjaan_entry.insert(0, selected_items[5])

        def update_data():
            update_no_anggota = update_no_anggota_entry.get()
            update_nama = update_nama_entry.get()
            update_alamat = update_alamat_entry.get()
            update_kota = update_kota_entry.get()
            update_notelp = update_notelp_entry.get()
            update_pekerjaan = update_pekerjaan_entry.get()

            update_data_tuple = (
                update_no_anggota,
                update_nama,
                update_alamat,
                update_kota,
                update_notelp,
                update_pekerjaan,
                selected_items[0]
            )

            update_data_query = '''UPDATE Data_Koperasi SET
                                No_Anggota = ?,
                                Nama = ?, 
                                Alamat = ?, 
                                Kota = ?,
                                No_Telp = ?, 
                                Pekerjaan = ? WHERE No_Anggota =?'''

            if len(update_data_tuple[0]) == 0:
                messagebox.showerror("Error", "Masukkan No. Anggota terlebih dahulu!")
            elif len(update_data_tuple[1]) == 0:
                messagebox.showerror("Error", "Masukkan Nama terlebih dahulu!")
            elif len(update_data_tuple[2]) == 0:
                messagebox.showerror("Error", "Masukkan Alamat terlebih dahulu!")
            elif len(update_data_tuple[3]) == 0:
                messagebox.showerror("Error", "Masukkan Kota terlebih dahulu!")
            elif len(update_data_tuple[4]) == 0:
                messagebox.showerror("Error", "Masukkan No. Telpon terlebih dahulu!")
            elif len(update_data_tuple[5]) == 0:
                messagebox.showerror("Error", "Masukkan Pekerjaan terlebih dahulu!")

            try:
                type(int(update_data_tuple[0])) != int or type(int(update_data_tuple[4])) != int
            except ValueError:
                messagebox.showerror("Error", "Pastikan data yang Anda masukkan telah sesuai format angka")

            try:
                type(update_data_tuple[1]) != str or type(update_data_tuple[2]) != str \
                    or type(update_data_tuple[3]) != str or type(update_data_tuple[5]) != str
            except ValueError:
                messagebox.showerror("Error", "Pastikan data yang Anda masukkan telah sesuai format alfabet")

            else:
                cursor.execute(update_data_query, update_data_tuple)
                conn.commit()
                root.destroy()
                try:
                    tv.item(selected, text="", values=update_data_tuple)
                except IndexError:
                    messagebox.showerror("Error", "Anda belum memasukkan data")
                print(f"update_data_tuple : {update_data_tuple}")

        update_button = Button(frame, command=update_data, text="Simpan")
        update_button.grid(row=6, padx=5, columnspan=2, pady=5)

    @classmethod
    def search_popup(cls):
        selected = tv.focus()
        selected_items = tv.item(selected, "values")

        root = Toplevel(main_window)
        root.title("Hasil Pencarian Data")
        root.attributes('-topmost', True)
        root.tk.eval(f'tk::PlaceWindow {root} center')

        frame = tkinter.LabelFrame(root)
        frame.pack(side=LEFT, anchor=CENTER, padx=10, pady=10)

        search_no_anggota_label = tkinter.Label(frame, text=f"{'No. Anggota:':>14}")
        search_no_anggota_label.grid(column=0, row=0, sticky="w", padx=10, pady=3)

        search_nama_anggota_label = tkinter.Label(frame, text=f"{'Nama:':>19}")
        search_nama_anggota_label.grid(column=0, row=1, sticky="w", padx=10, pady=3)

        search_alamat_anggota_label = tkinter.Label(frame, text=f"{'Alamat:':>19}")
        search_alamat_anggota_label.grid(column=0, row=2, sticky="w", padx=10, pady=3)

        search_kota_anggota_label = tkinter.Label(frame, text=f"{'Kota:':>21}")
        search_kota_anggota_label.grid(column=0, row=3, sticky="w", padx=10, pady=3)

        search_notelp_anggota_label = tkinter.Label(frame, text=f"{'No. Telp:':>19}")
        search_notelp_anggota_label.grid(column=0, row=4, sticky="w", padx=10, pady=3)

        search_pekerjaan_anggota_label = tkinter.Label(frame, text=f"{'Pekerjaan:':>18}")
        search_pekerjaan_anggota_label.grid(column=0, row=5, sticky="w", padx=10, pady=3)

        search_no_anggota_entry = tkinter.Entry(frame, width=20)
        search_no_anggota_entry.grid(column=1, row=0, sticky='w', padx=5)
        search_no_anggota_entry.insert(0, selected_items[0])

        search_nama_entry = tkinter.Entry(frame, width=35)
        search_nama_entry.grid(column=1, row=1, sticky='w', padx=5)
        search_nama_entry.insert(0, selected_items[1])

        search_alamat_entry = tkinter.Entry(frame, width=50)
        search_alamat_entry.grid(column=1, row=2, sticky='ew', padx=5)
        search_alamat_entry.insert(0, selected_items[2])

        search_kota_entry = tkinter.Entry(frame, width=25)
        search_kota_entry.grid(column=1, row=3, sticky='w', padx=5)
        search_kota_entry.insert(0, selected_items[3])

        search_notelp_entry = tkinter.Entry(frame, width=25)
        search_notelp_entry.grid(column=1, row=4, sticky='w', padx=5)
        search_notelp_entry.insert(0, selected_items[4])

        search_pekerjaan_entry = tkinter.Entry(frame, width=25)
        search_pekerjaan_entry.grid(column=1, row=5, sticky='w', padx=5)
        search_pekerjaan_entry.insert(0, selected_items[5])

    @classmethod
    def search_command(cls):
        search_no_anggota = kode_anggota_entry.get()
        search_nama = pencarian_nama_entry.get()
        if len(search_no_anggota) == 0 and len(search_nama) == 0:
            messagebox.showerror("Error", "Masukkan kode atau nama anggota")
        else:
            kode_anggota_entry.delete(0, END)
            pencarian_nama_entry.delete(0, END)
            messagebox.showinfo("Important", "Find out how to search on AppFunctions db hehehe")
        
    @classmethod
    def edit_command(cls):
        global selected_items
        try:
            selected = tv.focus()
            selected_items = tv.item(selected, "values")
            print(f"selected_items : {selected_items}")
        except _tkinter.TclError:
            messagebox.showerror("Error", "Pilih data yang ingin diubah")

        if len(selected_items) != 0:
            AppFunctions.update_popup()
        else:
            messagebox.showerror("Error", "Pilih data yang ingin diubah")

    @classmethod
    def delete_command(cls):
        selected = tv.focus()
        selected_items = tv.item(selected, "values")
        print(f"selected_items : {selected_items}")
        if len(selected_items) != 0:
            yesno = messagebox.askyesno(title="Konfirmasi", message="Apakah Anda yakin ingin menghapus data?")
            if yesno:
                AppFunctions.delete_data()
            else:
                pass
        else:
            messagebox.showerror("Error", "Pilih data yang ingin dihapus")

    @classmethod
    def simpan_command(cls):
        AppFunctions.create_table()
        AppFunctions.insert_data()
        AppFunctions.update_table()
        no_anggota_entry.delete(0, END)
        nama_entry.delete(0, END)
        alamat_entry.delete(0, END)
        kota_entry.delete(0, END)
        notelp_entry.delete(0, END)
        pekerjaan_entry.delete(0, END)

    @classmethod
    def reset_command(cls):
        AppFunctions.delete_alldata()
        for data in tv.get_children():
            tv.delete(data)

    @classmethod
    def fetch_database_dict(cls):
        fetch_database_dict_query = '''SELECT No,
                                    No_Anggota, 
                                    Nama, Alamat, 
                                    Kota, 
                                    No_Telp, 
                                    Pekerjaan 
                                    FROM Data_Koperasi'''

        cursor.execute(fetch_database_dict_query)
        fetched_data = cursor.fetchall()
        conn.commit()
        db_dict = {}
        for user_id in range(len(fetched_data)):
            db_dict.update({
                f"User_{user_id + 1}":
                    {
                        "No": fetched_data[user_id][0],
                        "No_Anggota": fetched_data[user_id][1],
                        "Nama": fetched_data[user_id][2],
                        "Alamat": fetched_data[user_id][3],
                        "Kota": fetched_data[user_id][4],
                        "No_Telp": fetched_data[user_id][5],
                        "Pekerjaan": fetched_data[user_id][6]
                    }
            })

        print(f"db_dict_all : {db_dict}")
        return db_dict

    @classmethod
    def fetch_database_list(cls):
        fetch_database_dict_query = '''SELECT No_Anggota, Nama, Alamat, Kota, No_Telp, Pekerjaan FROM Data_Koperasi'''
        cursor.execute(fetch_database_dict_query)
        fetched_data = cursor.fetchall()
        conn.commit()
        return fetched_data

    @classmethod
    def update_table(cls):
        try:
            fetched_data = AppFunctions.fetch_input_data()
            tv.insert("", index="end", values=fetched_data)
        except IndexError:
            messagebox.showerror("Error", "Anda belum memasukkan data")


# --------------------------------------------------BUTTON--------------------------------------------------------------


save_button = tkinter.Button(button_frame, text="Simpan", command=AppFunctions.simpan_command)
save_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

delete_button = tkinter.Button(button_frame, text=str("Delete"), command=AppFunctions.delete_command)
delete_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

edit_button = tkinter.Button(button_frame, text="Ubah", padx=5, pady=5, command=AppFunctions.edit_command)
edit_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

reset_button = tkinter.Button(button_frame, text="Reset", padx=5, pady=5, command=AppFunctions.reset_command)
reset_button.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

tv.bind("", )

query_database()
# try:
#     tabel = AppFunctions.fetch_database_list()
#     print(tabel)
#     for data in tabel:
#         tv.insert('', 'end', values=data)
# except AppFunctionsite3.OperationalError:
#     pass

main_window.mainloop()
