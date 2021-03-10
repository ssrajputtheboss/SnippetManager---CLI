import click
import os
from os.path import join

@click.command()
@click.option("--l", '--list', default=None, help="list all snippets argument should be 'all'")
@click.option("--add", '-a', default=None, help="specify name of snippet to be added")
@click.option("--f", '--file', default=None, help="file to be added as snippet")
@click.option("--c", '--create',default=None, help="create a new file pass snippet name using -s")
@click.option("--s",'--snippet', default=None, help="name of snippet")
def cli(l,add,f,c,s):
    snippet_location = join(__file__.replace('sptm\\cli.py' , '') , 'snippets')
    if l:
        snippet_list = os.listdir(snippet_location)
        for snippet in snippet_list:
            click.echo(snippet)
        return
    current_user_path = os.path.abspath('.')
    if c and s:
        if add or f:
            click.echo('cannot use both --add and --c at the same time')
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
    if add and f:
        if '.' in add:
            newfile = open(join(snippet_location , add) , 'w')
            readfile = open(join(current_user_path , f) , 'r')
            newfile.write(readfile.read())
            newfile.close()
        else:
            readfile = open(join(current_user_path , f) , 'r')
            fname,ext = os.path.splitext(f)
            newfile = open(join(snippet_location , add+ext) , 'w')
            newfile.write(readfile.read())
            newfile.close()
        click.echo('snippet '+add+' added')
        return
    #newfile = open(snippet_location + add , 'w')
    #newfile.write(f)
    #newfile.close()
    click.echo('some argument might be missing retry')