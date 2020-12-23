from typing import List, Any, Optional
import astroid
import astroid.mixins


def import_(mod_node, modname=None):
    # type: (astroid.mixins.ImportFromMixin, Optional[str]) -> astroid.Module
    return mod_node.do_import_module(modname)


def import_module(mod_node, modname):
    # type: (astroid.Import, str) -> astroid.Module
    return import_(mod_node, modname)


def import_from_module(mod_node, modname=None):
    # type: (astroid.ImportFrom, Optional[str]) -> astroid.Module
    return import_(mod_node, modname)


def names(mod_node):
    # type: (astroid.Module) -> List[str]
    return mod_node.wildcard_import_names()


def main():
    # type: () -> List[str]
    mod_node = astroid.extract_node("import mod")
    if isinstance(mod_node, astroid.Import):
        n = names(import_module(mod_node, 'mod'))
    elif isinstance(mod_node, astroid.ImportFrom):
        n = names(import_from_module(mod_node))
    print(n)
    return n


if __name__ == '__main__':
    main()
