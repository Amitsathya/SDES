from django import forms
from django.core.validators import RegexValidator
from .models import Input

# class Integer1Field(forms.MultiValueField):

#     def __init__(self, *args, **kwargs):

#         fields = (
#             forms.IntegerField(validators=[
#                 RegexValidator(r'[1-9]+', 'Enter a valid first name(only numbers)')
#             ]), # test
#             forms.IntegerField(validators=[
#                 RegexValidator(r'[1-9]+', 'Enter a valid second name(only numbers)')
#             ]),  # none
#             forms.IntegerField(validators=[
#                 RegexValidator(r'[1-9]+', 'Enter a valid second name(only numbers)')
#             ]),
#             forms.IntegerField(validators=[
#                 RegexValidator(r'[1-9]+', 'Enter a valid second name(only numbers)')
#             ]),
#             forms.IntegerField(validators=[
#                 RegexValidator(r'[1-9]+', 'Enter a valid second name(only numbers)')
#             ]),
#             forms.IntegerField(validators=[
#                 RegexValidator(r'[1-9]+', 'Enter a valid second name(only numbers)')
#             ]),
#             forms.IntegerField(validators=[
#                 RegexValidator(r'[1-9]+', 'Enter a valid second name(only numbers)')
#             ])
#         )

#         super().__init__(fields, *args, **kwargs)

#     def compress(self, data_list):
#         # data_list = ['text','none']
#         return f'{data_list[0]} {data_list[1]} {data_list[2]} {data_list[3]} {data_list[4]} {data_list[5]} {data_list[6]}'
#         #'text none'


    
     

class InputForm(forms.ModelForm):
    K = forms.CharField(required=True, label=("Key"))
    PT = forms.CharField(required=True, label=("PlainText"))
    IP = forms.IntegerField(required=False, label=("IP"), widget=forms.TextInput(attrs={'placeholder': '2, 6, 3, 1, 4, 8, 5, 7'}))
    IPi = forms.IntegerField(required=False, label=("IPi"), widget=forms.TextInput(attrs={'placeholder': '4, 1, 3, 5, 7, 2, 8, 6'}))
    P10 = forms.IntegerField(required=False, label=("P10"), widget=forms.TextInput(attrs={'placeholder': '3, 5, 2, 7, 4, 10, 1, 9, 8, 6'}))
    P8 = forms.IntegerField(required=False, label=("P8"), widget=forms.TextInput(attrs={'placeholder': '6, 3, 7, 4, 8, 5, 10, 9'}))
    P4 = forms.IntegerField(required=False, label=("P4"), widget=forms.TextInput(attrs={'placeholder': '2, 4, 3, 1'}))
    E = forms.IntegerField(required=False, label=("E"), widget=forms.TextInput(attrs={'placeholder': '4, 1, 2, 3, 2, 3, 4, 1'}))
    S0 = forms.IntegerField(required=False, label=("S0"), widget=forms.TextInput(attrs={'placeholder': '[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]'}))
    S1 = forms.IntegerField(required=False, label=("S1"), widget=forms.TextInput(attrs={'placeholder': '[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]'}))
    O = forms.IntegerField(required=False)

    class Meta:
        model = Input
        # fields =('K','PT')
        fields = ('K','PT','IP','IPi','P10','P8','P4','E','S0','S1','O')

    

