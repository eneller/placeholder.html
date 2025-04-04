from jinja2 import Environment, FileSystemLoader, meta
import click

@click.command()
@click.option('--output', '-o', default='output.html', help='Name of Output File')
def main(output):
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
    with open(output,'w') as out:
        out.write(template.render(vars))

if __name__ == '__main__':
    main()