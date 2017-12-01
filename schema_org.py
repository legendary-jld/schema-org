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
        super().__init__()
        self.canonicalAttributes = ('actionStatus', 'agent', 'endTime', 'error',
            'instrument', 'location', 'object', 'participant', 'result',
            'startTime', 'target')
        self.itemType = "Action"
        self.definitionLastUpdated = datetime.date(2017, 12, 1)
        for attribute in self.canonicalAttributes:
            setattr(self, attribute, kwargs.get(attribute, None))


class Person(Thing):
    def __init__(self, **kwargs):
        super().__init__()
        print("__init__ Person")
        self.additionalName = kwargs.get('additionalName', default=None)
        self.address = kwargs.get('address', default=None)
        self.affiliation = kwargs.get('affiliation', default=None)
        self.alumniOf = kwargs.get('alumniOf', default=None)
        self.award = kwargs.get('award', default=None)
        self.birthDate = kwargs.get('birthDate', default=None)
        self.birthPlace = kwargs.get('birthPlace', default=None)
        self.brand = kwargs.get('brand', default=None)
        self.children = kwargs.get('children', default=None)
        self.colleague = kwargs.get('colleague', default=None)
        self.contactPoint = kwargs.get('contactPoint', default=None)
        self.deathDate = kwargs.get('deathDate', default=None)
        self.deathPlace = kwargs.get('deathPlace', default=None)
        self.duns = kwargs.get('duns', default=None)
        self.email = kwargs.get('email', default=None)
        self.familyName = kwargs.get('familyName', default=None)
        self.faxNumber = kwargs.get('faxNumber', default=None)
        self.follows = kwargs.get('follows', default=None)
        self.funder = kwargs.get('funder', default=None)
        self.gender = kwargs.get('gender', default=None)
        self.givenName = kwargs.get('givenName', default=None)
        self.globalLocation = kwargs.get('globalLocation', default=None)
        self.hasOccupation = kwargs.get('hasOccupation', default=None)
        self.hasOfferCatalog = kwargs.get('hasOfferCatalog', default=None)
        self.hasPOS = kwargs.get('hasPOS', default=None)
        self.height = kwargs.get('height', default=None)
        self.homeLocation = kwargs.get('homeLocation', default=None)
        self.honorificPrefix = kwargs.get('honorificPrefix', default=None)
        self.honorificSuffic = kwargs.get('honorificSuffic', default=None)
        self.isicV4 = kwargs.get('isicV4', default=None)
        self.jobTitle = kwargs.get('jobTitle', default=None)
        self.knows = kwargs.get('knows', default=None)
        self.makesOffer = kwargs.get('makesOffer', default=None)
        self.memberOf = kwargs.get('additionalName', default=None)
        self.naics = kwargs.get('additionalName', default=None)
        self.nationality = kwargs.get('additionalName', default=None)
        self.netWorth = kwargs.get('additionalName', default=None)
        self.owns = kwargs.get('additionalName', default=None)
        self.parent = kwargs.get('additionalName', default=None)
        self.performerIn = kwargs.get('additionalName', default=None)
        self.publishingPrinciples = kwargs.get('additionalName', default=None)
        self.relatedTo = kwargs.get('additionalName', default=None)
        self.seeks = kwargs.get('additionalName', default=None)
        self.sibling = kwargs.get('additionalName', default=None)
        self.sponsor = kwargs.get('additionalName', default=None)
        self.spouse = kwargs.get('additionalName', default=None)
        self.taxID = kwargs.get('additionalName', default=None)
        self.telephone = kwargs.get('additionalName', default=None)
        self.vatID = kwargs.get('additionalName', default=None)
        self.weight = kwargs.get('additionalName', default=None)
        self.workLocation = kwargs.get('additionalName', default=None)
        self.worksFor = kwargs.get('additionalName', default=None)
