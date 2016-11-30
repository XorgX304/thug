#!/usr/bin/env python
#
# HTMLClassifier.py
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA  02111-1307  USA

import logging
from .BaseClassifier import BaseClassifier

log = logging.getLogger("Thug")

class HTMLClassifier(BaseClassifier):
    default_rule_file = "rules/htmlclassifier.yar"
    classifier        = "HTML Classifier"

    def __init__(self):
        BaseClassifier.__init__(self)

    def classify(self, url, html):
        for match in self.rules.match(data = html):
            if (url, match) in self.matches:
                continue

            self.matches.append((url, match))

            rule = match.rule
            tags = ",".join([" ".join(t.split('_')) for t in match.tags])
            log.ThugLogging.log_classifier("html", url, rule, tags)
