import click
import os
from os.path import join

@click.command()
@click.option("--l", '--list', default=None, help="list all snippets argument should be 'all'")
@click.option("--a", '--add', default=None, help="specify name of snippet to be added")
@click.option("--f", '--file', default=None, help="file to be added as snippet")
@click.option("--c", '--create',default=None, help="create a new file pass snippet name using -s")
@click.option("--s",'--snippet', default=None, help="name of snippet")
@click.option("--d",'--delete', default=None, help="name of snippet file to be deleted (with extention)")
def cli(l,a,f,c,s,d):
    snippet_location = join(__file__.replace('sptm\\cli.py' , '') , 'snippets')
    if not os.path.exists(snippet_location):
        os.makedirs(snippet_location)
    if l:
        snippet_list = os.listdir(snippet_location)
        for snippet in snippet_list:
            click.echo(snippet)
        return
    if d:
        os.remove(join(snippet_location , d))
        return
    current_user_path = os.path.abspath('.')

    if c and s:
        if a or f:
            click.echo('cannot use both --a and --c at the same time')
            return
        fname , ext = os.path.splitext(c)
        if ext == '':
            c = c+'.txt'
            ext = '.txt'
        fname2 , ext2 = os.path.splitext(s)
        if ext2 == '':
            s = s+ext
        newfile = open(join(current_user_path , c) , 'w' )
        snippet = open(join(snippet_location , s ) , 'r')
        newfile.write(snippet.read())
        newfile.close()
        click.echo('file created succesfully')
        return
    if a and f:
        if '.' in a:
            newfile = open(join(snippet_location , a) , 'w')
            readfile = open(join(current_user_path , f) , 'r')
            newfile.write(readfile.read())
            newfile.close()
        else:
            readfile = open(join(current_user_path , f) , 'r')
            fname,ext = os.path.splitext(f)
            newfile = open(join(snippet_location , a+ext) , 'w')
            newfile.write(readfile.read())
            newfile.close()
        click.echo('snippet '+a+' added')
        return
    click.echo('some argument are missing retry')
