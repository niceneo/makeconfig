from jinja2 import Environment, FileSystemLoader
from yaml import load, FullLoader, YAMLError
import sys

def render_to_file(host,content):
    env = Environment(loader=FileSystemLoader('./'))
    tpl = env.get_template('template')
    out = tpl.render(host=host,data=content)
    with open(host + '.yml', 'w') as f:
        f.write(out)

if __name__ == "__main__":
    try:
        filename=sys.argv[1]
        try:
            with open(filename,'r') as f:
                filedata =  f.read()
                try:
                    content = load(filedata, Loader=FullLoader)
                    for host, boxs in content.items():
                        render_to_file(host=host,content=boxs)
                except YAMLError as e:
                    print ('load filedata Error: %s' % e)
        except IOError as e:
            print ('Open boxinfo.yml faild: %s' % e)
    except IndexError as e:
        print("Please Add Configuration: %s" % e)

