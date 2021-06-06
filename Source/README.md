**graverobber.py**: This file is the payload itself, responsible for identifying the files to infect, sending the originals to the central server, encoding the originals and showing the interface requiring a password.

**trail-blazer.py**: This is the front file, optional utility. It infects a machine from the inside out, identifying the operating system and downloading its payload. In future updates, it will be responsible for mapping (and spreading across) the network, checking external devices. Anyway, it will be the infection module.

**locksmith.py**: This is a simple helper utility to derive keys from node identifiers and signatures (node_id, node_sig). Usage:

```python locksmith.py [node_id] [node_sig]```
