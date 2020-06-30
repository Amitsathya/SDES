from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.views.generic import TemplateView

from .forms import InputForm
from .models import Input

class InputView(TemplateView):
    template_name = 'form.html'

    def get(self, request):
        form = InputForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = InputForm(request.POST)
        if form.is_valid(): 
                    
            key = form.cleaned_data['K']
            pt = form.cleaned_data['PT']
            p10=form.cleaned_data['P10']
            p8=form.cleaned_data['P8']
            pt4=form.cleaned_data['P4']
            ip=form.cleaned_data['IP']
            ipi=form.cleaned_data['IPi']
            e=form.cleaned_data['E']
            s0=form.cleaned_data['S0']
            s1=form.cleaned_data['S1']
            key = str(key)
            cipher = str(pt)
            
            if p10 != None:
                p10=str(p10)
                l=[]
                for d in p10:
                    l.append(int(d))
                o=l.index(0)
                l[o-1]=10
                l.remove(0)
                P10=tuple(l)
            else:
                P10 = (3, 5, 2, 7, 4, 10, 1, 9, 8, 6)

            if p8 != None:
                p8=str(p8)
                l=[]
                for d in p8:
                    l.append(int(d))
                o=l.index(0)
                l[o-1]=10
                l.remove(0)
                P8=tuple(l)
            else:
                P8 = (6, 3, 7, 4, 8, 5, 10, 9)

            if pt4 != None:
                pt4=str(pt4)
                l=[]
                for d in pt4:
                    l.append(int(d))
                P4=tuple(l)
            else:
                P4 = (2, 4, 3, 1)

            if ip != None:
                ip=str(ip)
                l=[]
                for d in ip:
                    l.append(int(d))
                IP=tuple(l)
            else:
                IP = (2, 6, 3, 1, 4, 8, 5, 7)
            
            if ipi != None:
                ipi=str(ipi)
                l=[]
                for d in ipi:
                    l.append(int(d))
                IPi=tuple(l)
            else:
                IPi = (4, 1, 3, 5, 7, 2, 8, 6)

            if e != None:
                e=str(e)
                l=[]
                for d in e:
                    l.append(int(d))
                E=tuple(l)
            else:
                E = (4, 1, 2, 3, 2, 3, 4, 1)

            if s0 != None:
                s0=str(s0)
                l,s=[],[]
                for d in s0:
                    l.append(int(d))
                for i in range(0,4):
                    x=[]
                    for j in range(0,4):
                        x.append(l.pop(0))
                    s.append(x)
                S0=s[:]
            else:
                S0 = [
                    [1, 0, 3, 2],
                    [3, 2, 1, 0],
                    [0, 2, 1, 3],
                    [3, 1, 3, 2]
                ]

            if s1 != None:
                s1=str(s1)
                l,s=[],[]
                for d in s1:
                    l.append(int(d))
                for i in range(0,4):
                    x=[]
                    for j in range(0,4):
                        x.append(l.pop(0))
                    s.append(x)
                S1=s[:]
            else:
                S1 = [
                    [0, 1, 2, 3],
                    [2, 0, 1, 3],
                    [3, 0, 1, 0],
                    [2, 1, 0, 3]
                ]

            def permutation(perm, key):
                permutated_key = ""
                for i in perm:
                    permutated_key += key[i-1]

                return permutated_key

            def p4(perm, key): #P4(P4,1110)
                permutated_key = ""
                for i in perm:
                    permutated_key += key[i-1]

                return permutated_key

            def generate_first_key(left_key, right_key):
                left_key_rot = left_key[1:] + left_key[:1]
                right_key_rot = right_key[1:] + right_key[:1]
                key_rot = left_key_rot + right_key_rot
                return permutation(P8, key_rot)

            def generate_second_key(left_key, right_key):
                left_key_rot = left_key[3:] + left_key[:3]
                right_key_rot = right_key[3:] + right_key[:3]
                key_rot = left_key_rot + right_key_rot
                return permutation(P8, key_rot)

            def F(right, subkey):
                expanded_cipher = permutation(E, right)
                xor_cipher = bin( int(expanded_cipher, 2) ^ int(subkey, 2) )[2:].zfill(8)
                left_xor_cipher = xor_cipher[:4]
                right_xor_cipher = xor_cipher[4:]
                left_sbox_cipher = Sbox(left_xor_cipher, S0)
                right_sbox_cipher = Sbox(right_xor_cipher, S1)
                if (len(left_sbox_cipher) == 1) | (len(right_sbox_cipher) == 1) :
                    left_sbox_cipher = left_sbox_cipher.zfill(2)
                    right_sbox_cipher = right_sbox_cipher.zfill(2)
                return p4(P4, left_sbox_cipher + right_sbox_cipher)

            def Sbox(input, sbox):
                row = int(input[0] + input[3], 2)
                column = int(input[1] + input[2], 2)
                return bin(sbox[row][column])[2:]

            def f(first_half, second_half, key):
                left = int(first_half, 2) ^ int(F(second_half, key), 2)
                # print ("Fk: " + bin(left)[2:].zfill(4) + second_half)
                return bin(left)[2:].zfill(4), second_half

            p10key = permutation(P10, key)
            x = int(len(p10key)/2)
            left = p10key[:x]
            right = p10key[x:]
            if 'encode' in request.POST:
                first_key = generate_first_key(left, right)
                second_key = generate_second_key(left, right)
            else :
                second_key = generate_first_key(left, right)
                first_key = generate_second_key(left, right)

            # print ("[*] First key: " + first_key)
            # print ("[*] Second key: " + second_key)

            permutated_cipher = permutation(IP, cipher)
            # print ("IP: " + permutated_cipher)
            first_half_cipher = permutated_cipher[:int(len(permutated_cipher)/2)]
            second_half_cipher = permutated_cipher[int(len(permutated_cipher)/2):]

            left, right = f(first_half_cipher, second_half_cipher, first_key)
            # print ("SW: " + right +" "+ left+ " second key: "+second_key)
            left, right = f(right, left, second_key) # switch left and right!

            # print ("IP^-1: " + permutation(IPi, left + right))
            Input.objects.all().delete()
            form.save()
            t = Input.objects.get(K=key)
            t.O =permutation(IPi, left + right)
            t.save()
            

            posts = Input.objects.all()
            form = InputForm()
            return render(request, self.template_name, {'posts': posts,'form': form})

        else:
            form=1 #Unbound Form
            
    
        return render(request, 'form.html', {'form': form})
