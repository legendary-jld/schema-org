import datetime

class Thing(object):
    def __init__(self, **kwargs):
        self.canonicalAttributes = ('additionalType', 'alternateName', 'description',
            'disambugatingDescription', 'identifier', 'image', 'mainEntityOfPage',
            'name', 'potentialAction', 'sameAs', 'subjectOf', 'url')
        self.itemType = "Thing"
        self.definitionLastUpdated = datetime.date(2017, 12, 1)
        for attribute in self.canonicalAttributes:
            setattr(self, attribute, kwargs.get(attribute, None))

    def validate(self):
        pass

    def toJSON(self):
        if self.validate(): # Must validate first
            pass

    def toHTML(self):
        if self.validate(): # Must validate first
            pass


class Action(Thing):
    def __init__(self, **kwargs):
        Thing.__init__(self, **kwargs)
        self.canonicalAttributes = ('actionStatus', 'agent', 'endTime', 'error',
            'instrument', 'location', 'object', 'participant', 'result',
            'startTime', 'target')
        self.itemType = "Action"
        self.definitionLastUpdated = datetime.date(2017, 12, 1)
        for attribute in self.canonicalAttributes:
            setattr(self, attribute, kwargs.get(attribute, None))


class Person(Thing):
    def __init__(self, **kwargs):
        Thing.__init__(self, **kwargs)
        self.canonicalAttributes = ('additionalName', 'address', 'affiliation',
            'alumniOf', 'award', 'birthDate', 'birthPlace', 'brand', 'children',
            'colleague', 'contactPoint', 'deathDate', 'duns', 'email',
            'familyName', 'faxNumber', 'follows', 'funder', 'gender', 'givenName',
            'globalLocation', 'hasOccupation', 'hasOfferCatalog', 'hasPOS',
            'height', 'homeLocation', 'honorificPrefix', 'honorificSuffix',
            'isicV4', 'jobTitle', 'knows', 'makesOffer', 'memberOf', 'naics',
            'nationality', 'netWorth', 'owns', 'parent', 'performerIn',
            'publishingPrinciples', 'relatedTo', 'seeks', 'sibling', 'sponsor',
            'spouse', 'taxID', 'telephone', 'vatID', 'weight', 'workLocation',
            'worksFor')
        self.itemType = "Person"
        self.definitionLastUpdated = datetime.date(2017, 12, 1)
        for attribute in self.canonicalAttributes:
            setattr(self, attribute, kwargs.get(attribute, None))


class Intangible(Thing):
    def __init__(self, **kwargs):
        Thing.__init__(self, **kwargs)
        self.canonicalAttributes = ()
        self.itemType = "Intangible"
        self.definitionLastUpdated = datetime.date(2017, 12, 1)
        for attribute in self.canonicalAttributes:
            setattr(self, attribute, kwargs.get(attribute, None))
