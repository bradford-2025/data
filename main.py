from pathlib import Path
from mkdocs_macros import fix_url 


def define_env(env):
    """
    This is the hook for defining variables, macros and filters

    See [The Mkdocs-Marcos plugin documentation](https://mkdocs-macros-plugin.readthedocs.io/en/latest/macros/) for details.
    """

    ROOT = Path(env.conf['docs_dir'])

    @env.macro
    def dataset_link(x):
        target = f'datasets/{x}'
        if not (ROOT / target).exists():
            return 'NOT YET PUBLISHED'
        href = fix_url(target)
        return f'<a href="{fix_url(target)}" download="bradford-2025/{target}">CSV</a>'

