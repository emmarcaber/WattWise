# Window after Succesful Login

from datetime import datetime
from random import choices
import ttkbootstrap as ttk
from ttkbootstrap.style import Bootstyle
from tkinter.filedialog import askdirectory
from ttkbootstrap.dialogs import Messagebox
from ttkbootstrap.constants import *
from tkinter.scrolledtext import ScrolledText
from pathlib import Path
import sys


PATH = Path(__file__).resolve().parent.parent / 'assets'


class boying(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack(fill=BOTH, expand=YES)

        image_files = {
            'properties-dark': 'icons8_settings_24px.png',
            'properties-light': 'icons8_settings_24px_2.png',
            'add-to-backup-dark': 'icons8_add_folder_24px.png',
            'add-to-backup-light': 'icons8_add_book_24px.png',
            'stop-backup-dark': 'icons8_cancel_24px.png',
            'stop-backup-light': 'icons8_cancel_24px_1.png',
            'play': 'icons8_play_24px_1.png',
            'refresh': 'icons8_refresh_24px_1.png',
            'stop-dark': 'icons8_stop_24px.png',
            'stop-light': 'icons8_stop_24px_1.png',
            'opened-folder': 'icons8_opened_folder_24px.png',
            'logo': 'gg.png'
        }

        self.photoimages = []
        imgpath = PATH
        for key, val in image_files.items():
            _path = imgpath / val
            self.photoimages.append(ttk.PhotoImage(name=key, file=_path))

        # head_bar
        head_bar = ttk.Frame(self, style='primary.TFrame')
        head_bar.pack(fill=X, pady=1, side=TOP)

        # new backup
        def _func(): return Messagebox.ok(message='Adding new backup')
        btn = ttk.Button(
            master=head_bar, text='GENERATE',
            image='add-to-backup-light',
            compound=LEFT,
            command=_func
        )
        btn.pack(side=LEFT, ipadx=5, ipady=5, padx=(1, 0), pady=1)

        # backup
        def _func(): return Messagebox.ok(message='Backing up...')
        btn = ttk.Button(
            master=head_bar,
            text='CHECK',
            image='play',
            compound=LEFT,
            command=_func
        )
        btn.pack(side=LEFT, ipadx=5, ipady=5, padx=0, pady=1)

        # refresh
        def _func(): return Messagebox.ok(message='Refreshing...')
        btn = ttk.Button(
            master=head_bar,
            text='ANALYSIS',
            image='refresh',
            compound=LEFT,
            command=_func
        )
        btn.pack(side=LEFT, ipadx=5, ipady=5, padx=0, pady=1)

        # stop
        def _func(): return Messagebox.ok(message='Stopping backup.')
        btn = ttk.Button(
            master=head_bar,
            text='LOG OUT',
            image='stop-light',
            compound=RIGHT,
            command=_func
        )
        btn.pack(side=RIGHT, ipadx=5, ipady=5, padx=0, pady=1)

        # settings
        def _func(): return Messagebox.ok(message='Changing settings')
        btn = ttk.Button(
            master=head_bar,
            text='Settings',
            image='properties-light',
            compound=LEFT,
            command=_func
        )
        btn.pack(side=LEFT, ipadx=5, ipady=5, padx=0, pady=1)

        # right panel
        r_panel = ttk.Frame(self, style='bg.TFrame')
        r_panel.pack(side=RIGHT, fill=Y, ipadx=10)

        # MENU (collapsible)
        status_cf = CollapsingFrame(r_panel)
        status_cf.pack(fill=BOTH, pady=1)

        # container
        status_frm = ttk.Frame(status_cf, padding=20)
        status_frm.columnconfigure(1, weight=1, minsize=260)
        status_cf.add(
            child=status_frm,
            title='MENU',
            bootstyle=SECONDARY
        )
        # subjects
        lbl = ttk.Label(status_frm, text='Subject:')
        lbl.grid(row=0, column=0, sticky=W, pady=6)
        sub = ttk.Combobox(status_frm, value=[
                           'ESAS', 'ENGINEERING', 'MATHEMATICS'])
        sub.current(0)
        sub.grid(row=0, column=1, sticky=EW, padx=5, pady=6)

        # category
        lbl = ttk.Label(status_frm, text='Set:')
        lbl.grid(row=1, column=0, sticky=W, pady=6)
        sub = ttk.Combobox(status_frm, value=[
                           'Category 1', 'Category 2', 'Category 3'])
        sub.current(0)
        sub.grid(row=1, column=1, sticky=EW, padx=5, pady=6)

        # number of questions
        lbl = ttk.Label(status_frm, text='No. of Questions:')
        lbl.grid(row=2, column=0, sticky=W, pady=6)
        sub = ttk.Combobox(status_frm, value=[
                           'Category 1', 'Category 2', 'Category 3'])
        sub.current(0)
        sub.grid(row=2, column=1, sticky=EW, padx=5, pady=6)

        cb = ttk.Checkbutton(
            master=status_frm,
            text="GENERATE QUESTIONS",
            bootstyle=(SUCCESS, OUTLINE, TOOLBUTTON)
        )
        cb.grid(row=3, column=1, sticky=EW, padx=5, pady=6)

        cb = ttk.Checkbutton(
            master=status_frm,
            text="PRINT",
            bootstyle=(PRIMARY, OUTLINE, TOOLBUTTON)
        )
        cb.grid(row=4, column=1, sticky=EW, padx=5, pady=6)

        # STATUS (collapsible)
        bus_cf = CollapsingFrame(r_panel)
        bus_cf.pack(fill=X, pady=1)

        # container
        bus_frm = ttk.Frame(bus_cf, padding=10)
        bus_frm.columnconfigure(1, weight=1, minsize=300)
        bus_cf.add(
            child=bus_frm,
            title='STATUS',
            bootstyle=SECONDARY)

        # Number of students
        lbl = ttk.Label(bus_frm, text='Students (SET A):')
        lbl.grid(row=0, column=0, sticky=W, pady=2)
        lbl = ttk.Label(bus_frm, textvariable='num_students1')
        lbl.grid(row=0, column=1, sticky=EW, padx=5, pady=2)
        # Di ko na alam kung paano i-count yung number of students hehehehe
        self.setvar('num_students1', '#')

        lbl = ttk.Label(bus_frm, text='Students (SET B):')
        lbl.grid(row=1, column=0, sticky=W, pady=2)
        lbl = ttk.Label(bus_frm, textvariable='num_students2')
        lbl.grid(row=1, column=1, sticky=EW, padx=5, pady=2)
        # Di ko na alam kung paano i-count yung number of students hehehehe
        self.setvar('num_students2', '#')

        lbl = ttk.Label(bus_frm, text='Students (SET C):')
        lbl.grid(row=2, column=0, sticky=W, pady=2)
        lbl = ttk.Label(bus_frm, textvariable='num_students3')
        lbl.grid(row=2, column=1, sticky=EW, padx=5, pady=2)
        # Di ko na alam kung paano i-count yung number of students hehehehe
        self.setvar('num_students3', '#')

        lbl = ttk.Label(bus_frm, text='Students (SET D):')
        lbl.grid(row=3, column=0, sticky=W, pady=2)
        lbl = ttk.Label(bus_frm, textvariable='num_students4')
        lbl.grid(row=3, column=1, sticky=EW, padx=5, pady=2)
        # Di ko na alam kung paano i-count yung number of students hehehehe
        self.setvar('num_students4', '#')

        lbl = ttk.Label(bus_frm, text='Students (SET E):')
        lbl.grid(row=4, column=0, sticky=W, pady=2)
        lbl = ttk.Label(bus_frm, textvariable='num_students5')
        lbl.grid(row=4, column=1, sticky=EW, padx=5, pady=2)
        # Di ko na alam kung paano i-count yung number of students hehehehe
        self.setvar('num_students5', '#')

        lbl = ttk.Label(bus_frm, text='Students (TOTAL):')
        lbl.grid(row=5, column=0, sticky=W, pady=2)
        lbl = ttk.Label(bus_frm, textvariable='num_students')
        lbl.grid(row=5, column=1, sticky=EW, padx=5, pady=2)
        # Di ko na alam kung paano i-count yung number of students hehehehe
        self.setvar('num_students', '#')

        # section separator
        sep = ttk.Separator(bus_frm, bootstyle=SECONDARY)
        sep.grid(row=6, column=0, columnspan=2, pady=10, sticky=EW)

        # properties button
        def _func(): return Messagebox.ok(message='Changing properties')
        bus_prop_btn = ttk.Button(
            master=bus_frm,
            text='Properties',
            image='properties-dark',
            compound=LEFT,
            command=_func,
            bootstyle=LINK
        )
        bus_prop_btn.grid(row=7, column=0, columnspan=2, sticky=W)

        # add to backup button
        def _func(): return Messagebox.ok(message='Adding to backup')
        add_btn = ttk.Button(
            master=bus_frm,
            text='Add to backup',
            image='add-to-backup-dark',
            compound=LEFT,
            command=_func,
            bootstyle=LINK
        )
        add_btn.grid(row=8, column=0, columnspan=2, sticky=W)

        # logo
        lbl = ttk.Label(r_panel, image='logo', style='bg.TLabel')
        lbl.pack(side='bottom', padx=125)

        # left panel
        l_panel = ttk.Frame(self, padding=(2, 1))
        l_panel.pack(side=LEFT, fill=BOTH, expand=YES)

        # file input
        browse_frm = ttk.Frame(l_panel)
        browse_frm.pack(side=TOP, fill=X, padx=2, pady=1)

        file_entry = ttk.Entry(browse_frm, textvariable='folder-path')
        file_entry.pack(side=LEFT, fill=X, expand=YES)

        btn = ttk.Button(
            master=browse_frm,
            image='opened-folder',
            bootstyle=(LINK, SECONDARY),
            command=self.get_directory
        )
        btn.pack(side=RIGHT)

        # Treeview
        tv = ttk.Treeview(l_panel, show='headings', height=10)
        tv.configure(columns=('Name', 'ID Number',
                     'Date of Examination', 'Set'))
        tv.column('Name', width=150, stretch=True)

        for col in ['Date of Examination', 'Set']:
            tv.column(col, stretch=False)

        for col in tv['columns']:
            tv.heading(col, text=col.title(), anchor=W)

        tv.pack(fill=X, pady=1)

        # scrolling text output
        scroll_cf = CollapsingFrame(l_panel)
        scroll_cf.pack(fill=BOTH, expand=YES)

        output_container = ttk.Frame(scroll_cf, padding=1)
        _value = 'Test Question'
        self.setvar('scroll-message', _value)

        scroll_cf.add(output_container, textvariable='scroll-message')

        # # notebook with table and text tabs
        my_notebook = ttk.Notebook(output_container, bootstyle="primary")
        my_notebook.pack(side=LEFT, padx=(1, 1), expand=YES, fill=BOTH)

        tab1 = ttk.Frame(my_notebook)
        tab2 = ttk.Frame(my_notebook)
        tab3 = ttk.Frame(my_notebook)
        tab4 = ttk.Frame(my_notebook)
        tab5 = ttk.Frame(my_notebook)

        my_label = ttk.Label(tab1, text="This is SET A",
                             font=("Helvetica", 18))
        my_label.pack(pady=20)

        my_label2 = ttk.Label(tab2, text="This is SET B",
                              font=("Helvetica", 18))
        my_label2.pack(pady=20)

        my_label3 = ttk.Label(tab3, text="This is SET C",
                              font=("Helvetica", 18))
        my_label3.pack(pady=20)

        my_label4 = ttk.Label(tab4, text="This is SET D",
                              font=("Helvetica", 18))
        my_label4.pack(pady=20)

        my_label5 = ttk.Label(tab5, text="This is SET E",
                              font=("Helvetica", 18))
        my_label5.pack(pady=20)

        # Add our frames to the notebook
        my_notebook.add(tab1, text="SET A")
        my_notebook.add(tab2, text="SET B")
        my_notebook.add(tab3, text="SET C")
        my_notebook.add(tab4, text="SET D")
        my_notebook.add(tab5, text="SET E")

        # starting sample directory
        file_entry.insert(END, 'D:/text/myfiles/top-secret/samples/')

        # treeview and backup logs
        # Testing ko lang ito
        for x in range(1, 35):
            result = choices(['Backup Up', 'Missed in Destination'])[0]
            set1 = choices(['SET A', 'SET B', 'SET C', 'SET D', 'SET E'])[0]
            timestamp = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
            tv.insert('', END, x, values=(
                f'Student {x}', f'C2010063{x}', timestamp, set1))
        tv.selection_set(1)

    def get_directory(self):
        # Open dialogue to get directory and update variable
        self.update_idletasks()
        d = askdirectory()
        if d:
            self.setvar('folder-path', d)


class CollapsingFrame(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.columnconfigure(0, weight=1)
        self.cumulative_rows = 0

        # widget images
        self.images = [
            ttk.PhotoImage(file=PATH/'icons8_double_up_24px.png'),
            ttk.PhotoImage(file=PATH/'icons8_double_right_24px.png')
        ]

    def add(self, child, title="", bootstyle=PRIMARY, **kwargs):
        if child.winfo_class() != 'TFrame':
            return

        style_color = Bootstyle.ttkstyle_widget_color(bootstyle)
        frm = ttk.Frame(self, bootstyle=style_color)
        frm.grid(row=self.cumulative_rows, column=0, sticky=EW)

        # header title
        header = ttk.Label(
            master=frm,
            text=title,
            bootstyle=(style_color, INVERSE)
        )
        if kwargs.get('textvariable'):
            header.configure(textvariable=kwargs.get('textvariable'))
        header.pack(side=LEFT, fill=BOTH, padx=10)

        # header toggle button
        def _func(c=child): return self._toggle_open_close(c)
        btn = ttk.Button(
            master=frm,
            image=self.images[0],
            bootstyle=style_color,
            command=_func
        )
        btn.pack(side=RIGHT)

        # assign toggle button to child so that it can be toggled
        child.btn = btn
        child.grid(row=self.cumulative_rows + 1, column=0, sticky=NSEW)

        # increment the row assignment
        self.cumulative_rows += 2

    def _toggle_open_close(self, child):
        if child.winfo_viewable():
            child.grid_remove()
            child.btn.configure(image=self.images[1])
        else:
            child.grid()
            child.btn.configure(image=self.images[0])


if __name__ == '__main__':
    print(PATH)
    root = ttk.Window("WattWise")
    root.state("zoomed")
    boying(root)
    root.mainloop()
