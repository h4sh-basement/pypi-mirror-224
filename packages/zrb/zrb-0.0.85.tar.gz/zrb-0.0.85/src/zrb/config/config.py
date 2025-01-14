from ..helper.string.conversion import to_boolean, to_logging_level
import os
import pkg_resources


def get_version():
    try:
        dist = pkg_resources.get_distribution("zrb")
        return dist.version
    except pkg_resources.DistributionNotFound:
        import flit
        meta = flit.read_module_metadata("zrb")
        return meta["module"]["version"]


def get_current_shell() -> str:
    current_shell = os.getenv('SHELL', '')
    if current_shell.endswith('zsh'):
        return 'zsh'
    return 'bash'


default_shell = os.getenv('ZRB_SHELL', get_current_shell())
init_script_str = os.getenv('ZRB_INIT_SCRIPTS', '')
init_scripts = init_script_str.split(':') if init_script_str != '' else []
logging_level = to_logging_level(os.getenv('ZRB_LOGGING_LEVEL', 'WARNING'))
should_load_builtin = to_boolean(os.getenv('ZRB_SHOULD_LOAD_BUILTIN', '1'))
env_prefix = os.getenv('ZRB_ENV', '')
show_advertisement = to_boolean(os.getenv('ZRB_SHOW_ADVERTISEMENT', '1'))
show_prompt = to_boolean(os.getenv('ZRB_SHOW_PROMPT', '1'))
version = get_version()
