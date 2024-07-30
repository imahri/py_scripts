
def cans(name):
    defcons = name + "::" + name + "()\n{\n\tstd::cout << \"Default "+ name +" constructor called\" <<std::endl;\n}\n"
    defdes = name + "::~" + name + "()\n{\n\tstd::cout << \""+ name +" Destructor called\" <<std::endl;\n}\n"
    defcopy = name + "::" + name + "(const "+ name +" &"+ name[0].lower() + name[-1].lower() + ")\n{\n\tstd::cout << \"" + name + " Copy constructor called\" <<std::endl;\n\t*this = " + name[0].lower() + name[-1].lower() + ";\n}\n"
    assop = name + " &"+ name +"::operator=(const " + name + " &" +  name[0].lower() + name[-1].lower() +")\n{\n\t(void)" + name[0].lower() + name[-1].lower() + ";\n"
    assop +=  "\tstd::cout << \""+ name +" Copy assignment operator called\" << std::endl;\n\t//[...]\n\treturn *this;\n}"
    canonical = defcons
    canonical += defdes
    canonical += defcopy
    canonical += assop
    return canonical