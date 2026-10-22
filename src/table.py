def create_cell(value):
    return f"<td>{value}</td>"

def create_row(values):
    out = "<tr>"

    for value in values:
        out += create_cell(value)
    out += "</tr>"

    return out

def create_table(values):
    out = '<table class="prevent-select">'

    for value in values:
        out += create_row(value)

    out += "</table>"

    return out