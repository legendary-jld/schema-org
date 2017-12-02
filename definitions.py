import datetime

class SchemaDefinition(object):
    def __init__(self, itemType=None, itemTypeUrl=None,
        canonicalAttributes=None, lastUpdated=None):
        self.itemType = itemType
        self.itemTypeUrl = itemTypeUrl
        self.canonicalAttributes = canonicalAttributes
        self.lastUpdated = lastUpdated

def Thing():
    return SchemaDefinition(
        itemType="Thing",
        itemTypeUrl="http://schema.org/Thing",
        canonicalAttributes=('additionalType', 'alternateName', 'description',
            'disambugatingDescription', 'identifier', 'image', 'mainEntityOfPage',
            'name', 'potentialAction', 'sameAs', 'subjectOf', 'url'),
        lastUpdated=datetime.date(2017, 12, 1)
        )

def Action():
    return SchemaDefinition(
        itemType="Action",
        itemTypeUrl="http://schema.org/Action",
        canonicalAttributes=('actionStatus', 'agent', 'endTime', 'error',
            'instrument', 'location', 'object', 'participant', 'result',
            'startTime', 'target'),
        lastUpdated=datetime.date(2017, 12, 1)
        )


def CreativeWork():
    return SchemaDefinition(
        itemType="CreativeWork",
        itemTypeUrl="http://schema.org/CreativeWork",
        canonicalAttributes=('about', 'accessMode', 'accessModeSufficient',
            'accessibilityAPI', 'accessibilityControl', 'accessibilityFeature',
            'accessibilityHazard', 'accessibilitySummary', 'accountablePerson',
            'aggregateRating', 'alternativeHeadline', 'associatedMedia',
            'audience', 'audio', 'author', 'award', 'character', 'citation',
            'comment', 'commentCount', 'contentLocation', 'contentRating',
            'contentReferenceTime', 'contributor', 'copyrightHolder',
            'copyrightYear', 'creator', 'dateCreated', 'dateModified',
            'datePublished', 'discussionUrl', 'editor', 'educationalAlignment',
            'educationalUse', 'encoding', 'exampleOfWork', 'expires',
            'fileFormat', 'funder', 'genre', 'hasPart', 'headline', 'inLanguage',
            'interactionStatistic', 'interactivityType', 'isAccessibleForFree',
            'isBasedOn', 'isFamilyFriendly', 'isPartOf', 'keywords',
            'learningResourceType', 'license', 'locationCreated', 'mainEntity',
            'material', 'mentions', 'offers', 'position', 'producer', 'provider',
            'publication', 'publisher', 'publisherImprint', 'publishingPrinciples',
            'recordedAt', 'releasedAt', 'review', 'schemaVersion',
            'sourceOrganization', 'spatialCoverage', 'sponsor', 'temporalCoverage',
            'text', 'thumbnailUrl', 'timeRequired', 'translationOfWork',
            'translator', 'typicalAgeRange', 'version', 'video', 'workExample',
            'workTranslation'),
        lastUpdated=datetime.date(2017, 12, 1)
        )


def Person():
    return SchemaDefinition(
        itemType="Person",
        itemTypeUrl="http://schema.org/Person",
        canonicalAttributes=('additionalName', 'address', 'affiliation',
            'alumniOf', 'award', 'birthDate', 'birthPlace', 'brand', 'children',
            'colleague', 'contactPoint', 'deathDate', 'duns', 'email',
            'familyName', 'faxNumber', 'follows', 'funder', 'gender', 'givenName',
            'globalLocation', 'hasOccupation', 'hasOfferCatalog', 'hasPOS',
            'height', 'homeLocation', 'honorificPrefix', 'honorificSuffix',
            'isicV4', 'jobTitle', 'knows', 'makesOffer', 'memberOf', 'naics',
            'nationality', 'netWorth', 'owns', 'parent', 'performerIn',
            'publishingPrinciples', 'relatedTo', 'seeks', 'sibling', 'sponsor',
            'spouse', 'taxID', 'telephone', 'vatID', 'weight', 'workLocation',
            'worksFor'),
        lastUpdated=datetime.date(2017, 12, 1)
        )

def Intangible():
    return SchemaDefinition(
        itemType="Intangible",
        itemTypeUrl="http://schema.org/Intangible",
        canonicalAttributes=(),
        lastUpdated=datetime.date(2017, 12, 1)
        )
