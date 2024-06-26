from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from .models import Paciente
from django.core.exceptions import ValidationError

@login_required(redirect_field_name='login')
def home(request):
    return render(request, 'home.html')

@login_required(redirect_field_name='login')
def minhas_medidas(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    return render(request, 'minhas-medidas.html', {'paciente': paciente})


@login_required(redirect_field_name='login')
@staff_member_required(login_url='/')
def cadastrar_paciente(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        nome_completo = request.POST.get('nome_completo')
        genero = request.POST.get('genero')
        data_nascimento = request.POST.get('data_nascimento')
        ocupacao = request.POST.get('ocupacao')
        cep = request.POST.get('cep')
        celular = request.POST.get('celular')
        print(username)
        try:
            novo_usuario = User.objects.create_user(username=username, email=email, password=senha)
            Paciente.objects.create(
                user=novo_usuario,
                nutricionista=request.user,
                nome_completo=nome_completo,
                genero=genero,
                data_nascimento=data_nascimento,
                ocupacao=ocupacao,
                cep=cep,
                celular=celular
            )
            return redirect('home')
        except ValidationError as e:
            print(f"Error: {e}")
            return render(request, 'novo-paciente.html', {'errors': e})

    return render(request, 'novo-paciente.html')

@login_required(redirect_field_name='login')
@staff_member_required(login_url='/')
def pacientes(request):
    nutricionista = request.user
    pacientes = Paciente.objects.filter(nutricionista=nutricionista)
    return render(request, 'pacientes.html', {'pacientes': pacientes})


@login_required(redirect_field_name='login')
@staff_member_required(login_url='/')
def editar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    if request.method == 'POST':
        
        #########   DADOS    #########
        nome_completo = request.POST.get('nome_completo')
        genero = request.POST.get('genero')
        data_nascimento = request.POST.get('data_nascimento')
        ocupacao = request.POST.get('ocupacao')
        cep = request.POST.get('cep')
        celular = request.POST.get('celular')
        
        #########   ANAMNESE    #########
        objetivo_consulta = request.POST.get('question-one')
        historico_alimentar = request.POST.get('question-two')
        alergias = request.POST.get('question-three')
        rotina_alimentacao = request.POST.get('question-four')
        rotina_atividade_fisica = request.POST.get('question-five')
        preferencias_restricoes = request.POST.get('question-six')
        
        #########   AVALIAÇÃO    #########
        peso = request.POST.get('weigth')
        altura = request.POST.get('heigth')
        dobraIliocristal = request.POST.get('dobraIliocristal')
        dobraSupraespinal = request.POST.get('dobraSupraespinal')
        dobraAbdominal = request.POST.get('dobraAbdominal')
        dobraAxilar = request.POST.get('dobraAxilar')
        dobraCoxa = request.POST.get('dobraCoxa')
        dobraPeitoral = request.POST.get('dobraPeitoral')
        dobraSubescapular = request.POST.get('dobraSubescapular')
        dobraSuprailíaca = request.POST.get('dobraSuprailíaca')
        dobraTricipital = request.POST.get('dobraTricipital')
        cintura = request.POST.get('waist')
        quadril = request.POST.get('hip')

        #########   EXAMES    #########
        colesHDL = request.POST.get('colesHDL')
        colesLDL = request.POST.get('colesLDL')
        colesTotal = request.POST.get('colesTotal')
        pressDiastolica = request.POST.get('pressDiastolica')
        pressSistolica = request.POST.get('pressSistolica')
        trig = request.POST.get('trig')
        
        #########   COMPOSIÇÃO    #########
        massa_gorda = request.POST.get('massa_gorda')
        massa_muscular = request.POST.get('massa_muscular')
        percFat = request.POST.get('percFat')
        percMuscle = request.POST.get('percMuscle')
        imc = request.POST.get('imc')
        

        #########   DADOS    #########
        paciente.nome_completo = nome_completo
        paciente.genero = genero
        paciente.data_nascimento = data_nascimento
        paciente.ocupacao = ocupacao
        paciente.cep = cep
        paciente.celular = celular
        
        #########   ANAMNESE    #########
        paciente.objetivo_consulta = objetivo_consulta
        paciente.historico_alimentar = historico_alimentar
        paciente.alergias = alergias
        paciente.rotina_de_alimentacao = rotina_alimentacao
        paciente.rotina_de_atividade_fisica = rotina_atividade_fisica
        paciente.preferencias_e_restricoes = preferencias_restricoes

        #########   AVALIAÇÃO    #########
        paciente.peso = peso.replace(',', '.') if peso else 0
        paciente.altura = altura.replace(',', '.') if altura else 0
        paciente.dobra_cutanea_iliocristal = dobraIliocristal.replace(',', '.') if dobraIliocristal else 0
        paciente.dobra_cutanea_supraespinhal = dobraSupraespinal.replace(',', '.') if dobraSupraespinal else 0
        paciente.dobra_cutanea_abdominal = dobraAbdominal.replace(',', '.') if dobraAbdominal else 0
        paciente.dobra_cutanea_axilar_media = dobraAxilar.replace(',', '.') if dobraAxilar else 0
        paciente.dobra_cutanea_coxa = dobraCoxa.replace(',', '.') if dobraCoxa else 0
        paciente.dobra_cutanea_peitoral = dobraPeitoral.replace(',', '.') if dobraPeitoral else 0
        paciente.dobra_cutanea_subescapular = dobraSubescapular.replace(',', '.') if dobraSubescapular else 0
        paciente.dobra_cutanea_suprailiaca = dobraSuprailíaca.replace(',', '.') if dobraSuprailíaca else 0
        paciente.dobra_cutanea_tricipital = dobraTricipital.replace(',', '.') if dobraTricipital else 0
        paciente.perimetro_cintura = cintura.replace(',', '.') if cintura else 0
        paciente.perimetro_quadril = quadril.replace(',', '.') if quadril else 0

        #########   EXAMES    #########
        paciente.colesterol_hdl = colesHDL.replace(',', '.') if colesHDL else 0
        paciente.colesterol_ldl = colesLDL.replace(',', '.') if colesLDL else 0
        paciente.colesterol_total = colesTotal.replace(',', '.') if colesTotal else 0
        paciente.pressao_arterial_diastolica = pressDiastolica.replace(',', '.') if pressDiastolica else 0
        paciente.pressao_arterial_sistolica = pressSistolica.replace(',', '.') if pressSistolica else 0
        paciente.triglicerideos = trig.replace(',', '.') if trig else 0

        #########   COMPOSIÇÃO    #########
        paciente.massa_gorda = massa_gorda
        paciente.massa_muscular = massa_muscular
        paciente.porcentagem_massa_gorda = percFat
        paciente.porcentagem_massa_muscular = percMuscle
        paciente.imc = imc
        
        
        paciente.save()

        return redirect('pacientes') 

    return render(request, 'editar-paciente.html', {'paciente': paciente})
