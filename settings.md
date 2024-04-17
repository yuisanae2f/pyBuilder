# [settings.py](./settings.py)
> Manage the values when running [build.py](./build.py)  
> Do not change the keys(the strings which goes before columns).

# super_ignore_and_just_run_this
> When it is not "",
> this will be decided the entire command line.

# path
> Category for the paths.

## gcc
> Path of the GCC Compiler.

## build 
> Path to store the built executable file.

## sources
> Path where the source codes are located.

## obj
> Paths where the object files are located.
> Generated object files from sources will be located at the first path written at the first index.

## subproj
> Paths where the dependencies are located.  

# ext
> is the array of file extensions to be decided to be compiled.

# args
## pre
> just the string which comes after the [path of gcc](#gcc) before the [path of output](#build).  
> is set `-o` as default.