HCLI Core |pyver|_ |build status|_ |pypi|_
==========================================

An HCLI Connector that can be used to expose a REST API with a built-in CLI, via hypertext
command line interface (HCLI) semantics.

----

HCLI Core implements an HCLI Connector, a type of Service Connector, as a WSGI application and provides a way
for developers to expose a service hosted CLI, as a REST API, via HCLI semantics. Such an API exposes a "built-in"
CLI that can be interacted with dynamically with any HCLI client. Up to date, in-band, man page style API/CLI
documentation is readily available for use to help understand how to interact with the API.

Most, if not all, programming languages have a way to issue shell commands. With the help
of a generic HCLI client, such as Huckle [1], APIs that make use of HCLI semantics are readily consumable
anywhere via the familiar command line (CLI) mode of operation, and this, without there being a need to write
a custom and dedicated CLI to interact with a specific HCLI API.

You can find out more about HCLI on hcli.io [2]

The HCLI Internet-Draft [3] is a work in progress by the author and 
the current implementation leverages hal+json alongside a static form of ALPS
(semantic profile) [4] to help enable widespread cross media-type support.

Help shape HCLI and it's ecosystem by raising issues on github!

[1] https://github.com/cometaj2/huckle

[2] http://hcli.io

[3] https://github.com/cometaj2/I-D/tree/master/hcli

[4] http://alps.io

Installation
------------

hcli_core requires a supported version of Python and pip.

You'll need an WSGI compliant application server to run hcli_core. For example, you can use Green Unicorn (https://gunicorn.org/), and an
HCLI client such as Huckle (https://github.com/cometaj2/huckle). The following runs the default *jsonf* HCLI bundled with HCLI Core.


.. code-block:: console

    pip install hcli_core
    pip install gunicorn
    pip install huckle
    gunicorn --workers=5 --threads=2 -b 127.0.0.1:8000 --chdir `hcli_core path` "hcli_core:connector()"

Usage
-----

Open a different shell window.

Setup the huckle env eval in your .bash_profile (or other bash configuration) to avoid having to execute eval everytime you want to invoke HCLIs by name (e.g. jsonf).

Note that no CLI is actually installed by Huckle. Huckle reads the HCLI semantics exposed by the API and ends up behaving *like* the CLI it targets.


.. code-block:: console

    huckle cli install http://127.0.0.1:8000
    eval $(huckle env)
    jsonf help

3rd Party HCLI Installation
---------------------------

If you want to load a sample HCLI other than the default sample application, you can try loading one of the other sample HCLIs
included with HCLI Core. For example, the *hg* HCLI (hypertext GPT-3.5-Turbo chatbot).

A folder path to any other 3rd party HCLI can be provided in the same way to the HCLI Connector, provided the 3rd party HCLI meets
CLI interface (cli.py) and HCLI template (template.json) requirements:

.. code-block:: console

    pip install hcli_core
    pip install gunicorn
    pip install huckle
    gunicorn --workers=5 --threads=2 --chdir `hcli_core path` "hcli_core:connector(\"`hcli_core sample hg`\")"

3rd Party HCLI Usage
--------------------

Open a different shell window.

Setup the huckle env eval in your .bash_profile (or other bash configuration) to avoid having to execute eval everytime you want to invoke HCLIs by name (e.g. hg).

.. code-block:: console
    
    huckle cli install http://127.0.0.1:8000
    eval $(huckle env)
    hg help

Versioning
----------
    
This project makes use of semantic versioning (http://semver.org) and may make use of the "devx",
"prealphax", "alphax" "betax", and "rcx" extensions where x is a number (e.g. 0.3.0-prealpha1)
on github. Only full major.minor.patch releases will be pushed to pip from now on.

Supports
--------

- HTTP/HTTPS.
- HCLI version 1.0 server semantics for hal+json
- Web Server Gateway Interface (WSGI) through PEP 3333 and Falcon.
- Bundled Sample HCLIs:
    - jsonf - a simple formatter for JSON.
    - hg    - an HCLI for interacting with GPT-3.5-Turbo via terminal input and output streams.
    - hfm   - a file upload and download manager that works with \*nix terminal shell input and output streams.
    - hptt  - a rudimentary HCLI Push To Talk (PTT) channel management service.
    - hub   - a rudimentary HCLI service discovery hub.
    - nw    - a flexible IP Address Management (IPAM) service.
    - hc    - a gcode streamer for GRBL compliant controller and a CNC interface (e.g. OpenBuilds BlackBox controller v1.1g and Interface CNC Touch).
- Support for use of any 3rd party HCLI code that meets CLI interface requirements and HCLI template requirements (i.e. see sample HCLIs).
- Support large input and output streams as application/octet-stream.

To Do
-----

- Automated tests for all bundled HCLI samples.
- A memory layer for the GPT-3.5-Turbo HCLI (hg).
    - Automatic context switching per NLP on received input stream.
    - Context blending to mary different contexts.
    - Automatic context compression to yield a more substantial memory footprint per context window.
- A shell mode for the GPT-3.5-Turbo HCLI (hg) to enable shell CLI execution per sought goal.
- Separate out HCLI applications from HCLI Core to help avoid application dependencies bleeding onto HCLI Core (e.g. OpenAI, GRBL, pyserial, etc.).
- Update GRBL controller HCLI (hc) to include support for additional commands and/or echo of hexadecimal values.
- Update hc to include job removal and insertion.
- Update hc to function in a multi-process environment (e.g. multiple workers in gunicorn).
- Implement GRBL emulation tests for hc.

Bugs
----

- No good handling of control over request and response in cli code which can lead to exceptions and empty response client side.
- The hfm sample HCLI fails disgracefully when copying a remote file name that doesn't exist (server error).

.. |build status| image:: https://circleci.com/gh/cometaj2/hcli_core.svg?style=shield
.. _build status: https://circleci.com/gh/cometaj2/huckle
.. |pypi| image:: https://badge.fury.io/py/hcli-core.svg
.. _pypi: https://badge.fury.io/py/hcli-core
.. |pyver| image:: https://img.shields.io/pypi/pyversions/hcli-core.svg
.. _pyver: https://pypi.python.org/pypi/hcli-core
