import copy

from templer.core.base import BaseTemplate
from templer.core.vars import EASY
from templer.core.vars import EXPERT
from templer.core.vars import StringVar, BooleanVar, IntVar, OnOffVar, BoundedIntVar

VAR_ZOPE_USER = StringVar(
    'zope_user',
    title='Initial Zope Username',
    description='Username for Zope root admin user',
    modes=(EASY, EXPERT),
    page='Main',
    default='admin',
    help="""
Your buildout will have a single user, with manager privileges, defined
at the root. This option lets you select the name for this user.
"""
    )

VAR_ZOPE_PASSWD = StringVar(
    'zope_password',
    title='Initial User Password',
    description='Password for Zope root admin user',
    modes=(EASY, EXPERT),
    page='Main',
    default='',
    help="""
Your buildout will have a single user, "%(zope_user)s", with manager 
privileges, defined at the root. This option lets you select the initial
password for this user. If left blank, the password will be randomly
generated.
"""
    )

VAR_HTTP = BoundedIntVar(
    'http_port',
    title='HTTP Port',
    description='Port that Zope will use for serving HTTP',
    default='8080',
    modes=(EXPERT,EASY),
    page='Main',
    help="""
This options lets you select the port # that Zope will use for serving
HTTP.
""",
    min=1024,
    max=65535,
    )

VAR_DEBUG_MODE = OnOffVar(
    'debug_mode',
    title='Debug Mode',
    description='Should debug mode be "on" or "off"?',
    default='off',
    modes=(EXPERT,EASY),
    page='Main',
    help="""
Debug mode (sometimes called "Debug/Development Mode") is the correct
setting for running a site under development--it ensures that on-disk
changes to templates and skin scripts are immediately visible, and
allows use of certain add-on debugging/profiling products. Running your
Zope in the foreground (with "bin/plonectl fg" or similar commands)
always puts you in debug mode; this setting controls whether you are
in debug mode even when running in the background.

You should set this to "on" during development; once you are ready to
deploy your site, you change this to "off" in your buildout.cfg.
"""
    )

VAR_VERBOSE_SEC = OnOffVar(
        'verbose_security',
        title='Verbose Security?',
        description='Should verbose security be "on" or "off"?',
        default='off',
        modes=(EASY, EXPERT),
        page='Main',
        help="""
Security error messages (such as "Unauthorized" errors) in Silva are
intentionally vague--the system doesn't want to reveal too much about
the security configuration in error messages, given that those error
messages may be inappropriately printed out/shared/email and intercepted
by others.

"Verbose security" is a buildout setting that enables significantly more
helpful, detailed unauthorized error messages.

There may be a small security risk in leaving this enabled on a site in
deployment; if you turn it on, you should consider turning it off.
"""
        )

class AbstractBuildout(BaseTemplate):
    """Abstract class for all templates that produce buildouts."""

    category = "Buildout"

    vars = copy.deepcopy(BaseTemplate.vars)

