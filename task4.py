# Задание 4
# Каждый год ваша компания предоставляет различным государственным организациям 
# финансовую отчетность. В зависимости от организации форматы отчетности разные. 
# Используя механизм декораторов, решите вопрос отчетности для организаций

def json_report(func):
    def wrapper(*args, **kwargs):
        report = func(*args, **kwargs)
        return f'{{"report": "{report}"}}'
    return wrapper

def xml_report(func):
    def wrapper(*args, **kwargs):
        report = func(*args, **kwargs)
        return f'<report>{report}</report>'
    return wrapper

def plain_text_report(func):
    def wrapper(*args, **kwargs):
        report = func(*args, **kwargs)
        return f'Report: {report}'
    return wrapper

def generate_report(data):
    return f'Data: {data}'

@json_report
def report_for_organization_a(data):
    return generate_report(data)

@xml_report
def report_for_organization_b(data):
    return generate_report(data)

@plain_text_report
def report_for_organization_c(data):
    return generate_report(data)

data = "data"

print(report_for_organization_a(data))
print(report_for_organization_b(data))
print(report_for_organization_c(data))