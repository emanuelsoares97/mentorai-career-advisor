from flask import Blueprint, render_template, request, send_file
from app.services.sugestoes import sugerir_top2_carreiras
from app.services.vagas_api import buscar_vagas
from app.utils.historico import salvar_resultado
from fpdf import FPDF
import io

bp = Blueprint('frontend', __name__)

@bp.route('/')
def inicio():
    return render_template('inicio.html')

@bp.route('/quiz', methods=['POST'])
def quiz():
    nome = request.form.get('nome')
    return render_template('index.html', nome=nome)

@bp.route('/resultado', methods=['POST'])
def resultado():
    nome = request.form.get('nome')
    logica = request.form.get('logica') == 'sim'
    visual = request.form.get('visual') == 'sim'
    dados = request.form.get('dados') == 'sim'
    seguranca = request.form.get('seguranca') == 'sim'

    respostas = (logica, visual, dados, seguranca)
    (carreira1, explicacao1), (carreira2, explicacao2) = sugerir_top2_carreiras(respostas)

    vagas = buscar_vagas(carreira1)
    salvar_resultado(nome, respostas, carreira1, carreira2)

    return render_template('resultado.html', 
                           nome=nome,
                           carreira1=carreira1, explicacao1=explicacao1,
                           carreira2=carreira2, explicacao2=explicacao2,
                           respostas=respostas, vagas=vagas)

@bp.route('/gerar_pdf', methods=['POST'])
def gerar_pdf():
    nome = request.form.get('nome')
    carreira1 = request.form.get('carreira1')
    explicacao1 = request.form.get('explicacao1')
    carreira2 = request.form.get('carreira2')
    explicacao2 = request.form.get('explicacao2')

    titulos = request.form.getlist('vaga_titulo')
    empresas = request.form.getlist('vaga_empresa')
    links = request.form.getlist('vaga_link')

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Relatório de Perfil - MentorAI", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Olá {nome}, aqui está teu perfil MentorAI!", ln=True)
    pdf.ln(5)
    pdf.cell(200, 10, txt=f"Carreira Principal: {carreira1}", ln=True)
    pdf.multi_cell(0, 10, txt=explicacao1)
    pdf.ln(5)
    pdf.cell(200, 10, txt=f"Segunda Sugestão: {carreira2}", ln=True)
    pdf.multi_cell(0, 10, txt=explicacao2)

    if titulos:
        pdf.ln(10)
        pdf.cell(200, 10, txt="Vagas Relacionadas:", ln=True)
        for titulo, empresa, link in zip(titulos, empresas, links):
            pdf.set_font("Arial", style="B", size=11)
            pdf.cell(200, 10, txt=f"{titulo} ({empresa})", ln=True)
            pdf.set_font("Arial", size=10)
            pdf.multi_cell(0, 8, txt=f"{link}")
            pdf.ln(1)

    pdf_buffer = io.BytesIO()
    pdf_output = pdf.output(dest='S').encode('latin-1')
    pdf_buffer.write(pdf_output)
    pdf_buffer.seek(0)

    return send_file(pdf_buffer, as_attachment=True, download_name="mentorai_perfil.pdf", mimetype='application/pdf')