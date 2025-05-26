from flask import Flask, render_template, send_file
import pdfkit

app = Flask(__name__)

@app.route('/')
def invitacion():
    return render_template('invitacion.html')

@app.route('/descargar_pdf')
def descargar_pdf():
    renderizado = render_template('invitacion.html')
    config = pdfkit.configuration(wkhtmltopdf=r'C:\Users\Angel Sanabria\Desktop\Proyectos\wkhtmltopdf\bin\wkhtmltopdf.exe')
    options = {
        'enable-local-file-access': None
    }
    pdfkit.from_string(renderizado, 'invitacion.pdf', configuration=config, options=options)
    return 'PDF generado'

if __name__ == '__main__':
    app.run(debug=True)
