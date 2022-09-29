#!/usr/bin/env python3

# example python code using GMime via GObject Introspection

# Author: Daniel Kahn Gillmor <dkg@fifthhorseman.net>
# License: GPL-3+

import gi
gi.require_version('GMime', '3.0')
from gi.repository import GMime
GMime.init()

f = GMime.StreamFile.open('/usr/share/doc/gir1.2-gmime-3.0/examples/example.eml', 'r')
parser = GMime.Parser.new_with_stream(f)
msg = parser.construct_message()

print("Subject is:", msg.subject)
