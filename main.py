from jinja2 import Environment, FileSystemLoader, meta

env = Environment(loader=FileSystemLoader('.'))
filename =  'index.html'
# get undeclared variables
template_source = env.loader.get_source(env, filename)
parsed_content = env.parse(template_source)
vars = meta.find_undeclared_variables(parsed_content)
vars = dict.fromkeys(sorted(vars), None)
for var in vars:
    vars[var] = input(var+ ' :')
# render template
template = env.get_template(filename)
print(template.render(vars))
