from django import forms

class buscar_skin(forms.Form):
    skin = forms.CharField(label="Arma", max_length=20)
    skin_pack = forms.CharField(label="skin pack", max_length=20)

    from django import forms

class BuscarSkin(forms.Form):  # minúscula, igual que tu vista
    arma = forms.CharField(label="Arma", max_length=100)
    skin_pack = forms.CharField(label="Skin Pack", max_length=100)
    fecha_creacion = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))

