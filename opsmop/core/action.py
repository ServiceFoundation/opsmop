# Copyright 2018 Michael DeHaan LLC, <michael@michaeldehaan.net>
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

class Action(object):

    # __slots__ = [ 'do' ]

    def __init__(self, do=None):
        """
        The Action is just a wrapper around a simple string action type.
        They are generated by plan() methods on a provider, and processed by the apply() methods, 
        where they are sent in as a list.  The should() method on a provider actually processes
        the entire list of actions, not just this one object.
        """
        self.do = do

    def should(self, match):
        return self.do == match

    def __str__(self):
        return str(self.do)

    def to_dict(self):
        return dict(cls=self.__class__.__name__, do=self.do)
