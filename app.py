from flask import Flask, render_template, request, send_file
from sugestoes import sugerir_top2_carreiras
from vagas_api import buscar_vagas
from fpdf import FPDF
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    logica = request.form.get('logica') == 'sim'
    visual = request.form.get('visual') == 'sim'
    dados = request.form.get('dados') == 'sim'
    seguranca = request.form.get('seguranca') == 'sim'

    respostas = (logica, visual, dados, seguranca)
    (carreira1, explicacao1), (carreira2, explicacao2) = sugerir_top2_carreiras(respostas)

    # Busca vagas da carreira principal
    vagas = buscar_vagas(carreira1)

    return render_template('resultado.html', 
                           carreira1=carreira1, explicacao1=explicacao1,
                           carreira2=carreira2, explicacao2=explicacao2,
                           respostas=respostas, vagas=vagas)


@app.route('/gerar_pdf', methods=['POST'])
def gerar_pdf():
    carreira1 = request.form.get('carreira1')
    explicacao1 = request.form.get('explicacao1')
    carreira2 = request.form.get('carreira2')
    explicacao2 = request.form.get('explicacao2')

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Relatório de Perfil - MentorAI", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Carreira Principal: {carreira1}", ln=True)
    pdf.multi_cell(0, 10, txt=f"{explicacao1}")
    pdf.ln(5)
    pdf.cell(200, 10, txt=f"Segunda Sugestão: {carreira2}", ln=True)
    pdf.multi_cell(0, 10, txt=f"{explicacao2}")

    pdf_buffer = io.BytesIO()
    pdf_output = pdf.output(dest='S').encode('latin-1')  # <- retorna string, precisa encoding
    pdf_buffer.write(pdf_output)
    pdf_buffer.seek(0)


    return send_file(pdf_buffer, as_attachment=True, download_name="mentorai_perfil.pdf", mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True)
