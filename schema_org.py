import datetime

# Local Libraries
import definitions


class Thing(object):
    def __init__(self, **kwargs):
        self.itemStructure = None
        self.parentStructure = None
        self.schema = definitions.Thing()
        self.setAttributes()

    def setAttributes(self, parent=None, **kwargs):
        if parent:
            self.itemStructure = "{0} > {1}".format(parent.schema.itemType, self.schema.itemType)
            self.parentStructure = parent.schema.itemType
        else:
            self.itemStructure = self.schema.itemType

        for attribute in self.schema.canonicalAttributes:
            setattr(self, attribute, kwargs.get(attribute, None))

    def validate(self):
        pass

    def toJSON(self):
        if self.validate(): # Must validate first
            pass

    def toHTML(self):
        if self.validate(): # Must validate first
            pass

    def __repr__(self):
        return "<SCHEMA:{0} - ID: {1} | Name: {2}>".format(
            self.itemStructure, self.identifier, self.name
            )


class Action(Thing):
    def __init__(self, **kwargs):
        Thing.__init__(self, **kwargs)
        self.schema = definitions.Action()
        self.setAttributes(parent=Thing(), **kwargs) # Would prefer not to create a Thing Instance just to get the itemType


class CreativeWork(Thing):
    def __init__(self, **kwargs):
        Thing.__init__(self, **kwargs)
        self.schema = definitions.CreativeWork()
        self.setAttributes(parent=Thing, **kwargs)


class Person(Thing):
    def __init__(self, **kwargs):
        Thing.__init__(self, **kwargs)
        self.schema = definitions.Person()
        self.setAttributes(parent=Thing, **kwargs)


class Intangible(Thing):
    def __init__(self, **kwargs):
        Thing.__init__(self, **kwargs)
        self.schema = definitions.Intangible()
        self.setAttributes(parent=Thing, **kwargs)
