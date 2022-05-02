class configure_widgets():

    def configure_cpu_bar(self):
        r = self.cpu.cpu_percent()
        for i in range(self.cpu.cpu_count_logical):
            self.list_label[i].configure(text = f'core {i + 1} usage: {r[i]}%')
            self.list_pbar[i].configure(value = r[i])

        r2 = self.cpu.ram_usage()
        self.ram_lab.configure(text = f'RAM usage: {r2[2]}%, used {round(r2[3]/1048576)} MB,\
            \n available: {round(r2[1]/1048576)} MB')
        self.ram_bar.configure(value = r2[2])


        self.wheel = self.after(850, self.configure_cpu_bar)

    def configure_win(self):
        if self.wm_overrideredirect():
            self.overrideredirect(False)
        else:
            self.overrideredirect(True)
        self.update()

    def configure_minimal_win(self):
        self.bar_one.configure(value = self.cpu.cpu_one())
        self.ram_bar.configure(value = self.cpu.ram_usage()[2])
        self.wheel = self.after(850, self.configure_minimal_win)

    def clear_win(self):
        for i in self.winfo_children():
            i.destroy()