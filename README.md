# Snippet-manager

a snippet manager cli to manage your code snippets and use it whenever and wherever you need.

## Installation

clone/download github repository
```cmd
git clone https://github.com/ssrajputtheboss/SnippetManager---CLI.git
```
move to sptm directory and execute the command(don't do it on virtual environment otherwise it will not install the package globally):-

```cmd
pip install .
```

# Commands

### List snippets

to list snippets use this command-
```cmd
sptm --l all or
sptm --list all
```
by default there is only one snippet empty.txt .


### Add a new snippet

To add a new snippet you must have a file containing content for new snippet. Let you are creating a snippet for c++ programs and want to name it as 'default.cpp' . The content of 'default.cpp' could be :-

```c++
#include<bits/stdc++.h>
using namespace std;

int main(){

    return 0;
}
```

to add this file as snippet , in cmd/terminal move to the location where file exists and execute the command-

```cmd
sptm --add default.cpp --file default.cpp 
or in short:
sptm --a default.cpp --f default.cpp 
```

### creating a file using snippet
Now you can create any file with above code snippet simply by using command below .First you need to move to the location where you want to create file and execute below command - 

```cmd
sptm --create new.cpp --snippet default.cpp 
or in short:
sptm --c new.cpp --s default.cpp
```

this will create a file new.cpp with content of default.cpp.

### delete a snippet

use this command to delete the snippet (give file name with extension).

```cmd
sptm --d empty.txt
```
