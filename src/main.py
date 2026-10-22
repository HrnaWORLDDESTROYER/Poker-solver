import flask
import table
app = flask.Flask(__name__)

def create_dummy_data() -> list[list[float]]:
    return [[float(i+j) for i in range(13)] for j in range(13)]

def inject_file_data_at_marker(buffer, filepath, marker):
    with open(filepath, "r") as f:
        file_data = f.read()
    return inject_string_at_marker(buffer, file_data, marker)

def inject_string_at_marker(buffer, string, marker):
    return buffer.replace(marker, string)


@app.route('/')
def hello_world():

    data = create_dummy_data()
    table_html =  table.create_table(data)

    with open("../html/document_template.html", "r") as f:
        template_html = f.read()

    template_html = inject_file_data_at_marker(template_html, "../styles/table.css", "#insert_style#")
    template_html = inject_string_at_marker(template_html, table_html, "#insert_body#")

    return template_html




app.run(host='127.0.0.1', port=5000)