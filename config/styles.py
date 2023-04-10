# Heading Font Sizes
h1 = 39
h2 = 31
h3 = 25
h4 = 20
h5 = 14
h6 = 13

# Fonts
heading_font = 'Arial'
normal_font = 'Century Gothic'


def style_configurations(self):
    self.style.configure("title_label.TLabel", font=(
        normal_font, h3), padding=10, foreground='black', justify="center")
    self.style.configure("form_label.TLabel",
                         foreground='black', font=(normal_font, h6, "bold"))
    self.style.configure("login_button.TButton", font=(
        normal_font, h6, "bold"), width=54, padding=10)
    self.style.configure("create_account_button.Outline.TButton", font=(
        normal_font, h6, "bold"), width=54, padding=10)
    self.style.configure("success.TButton", font=(
        normal_font, h6, "bold"), width=24, padding=10)
    self.style.configure("secondary.Outline.TButton", font=(
        normal_font, h6, "bold"), width=24, padding=10)
