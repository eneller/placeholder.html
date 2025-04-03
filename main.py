from jinja2 import Environment, FileSystemLoader, meta

env = Environment(loader=FileSystemLoader('.'))
template_source = env.loader.get_source(env, 'index.html')
parsed_content = env.parse(template_source)
vars = meta.find_undeclared_variables(parsed_content)
vars = dict.fromkeys(vars, None)
print(vars)