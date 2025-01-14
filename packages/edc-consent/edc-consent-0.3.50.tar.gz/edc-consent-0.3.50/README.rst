|pypi| |actions| |codecov| |downloads|

edc-consent
-----------

Add classes for the Informed Consent form and process.

Installation
============

Register your consent model, its version and period of validity, with ``site_consents``. ``site_consents`` will ``autodiscover`` ``consents.py`` in any app listed in ``INSTALLED_APPS``. For now we just create a version 1 consent. In ``consents.py`` add something like this:


.. code-block:: python

    from datetime import datetime
    from zoneifo import ZoneInfo

    from edc_consent.consent import Consent
    from edc_consent.site_consents import site_consents
    from edc_constants.constants import MALE, FEMALE

    subjectconsent_v1 = Consent(
        'edc_example.subjectconsent',
        version='1',
        start=datetime(2013, 10, 15, tzinfo=ZoneInfo("UTC")),
        end=datetime(2016, 10, 15, tzinfo=ZoneInfo("UTC")),
        age_min=16,
        age_is_adult=18,
        age_max=64,
        gender=[MALE, FEMALE])

    site_consents.register(subjectconsent_v1)

add to settings:

.. code-block:: bash

    INSTALLED_APPS = [
        ...
        'edc_consent.apps.AppConfig',
        ...
    ]


 Below needs to be updated

Features
========

* base class for an informed consent document
* data for models that require consent cannot be add until the consent is added
* consents have a version number and validity period
* maximum number of consented subjects can be controlled.
* data collection is only allowed within the validity period of the consent per consented participant
* data for models that require consent are tagged with the consent version

TODO
====

- link subject type to the consent model. e.g. maternal, infant, adult, etc.
- version at model field level (e.g. a new consent period adds additional questions to a form)
- allow a different subject's consent to cover for another, for example mother and infant.

Usage
=====

First, it's a good idea to limit the number of consents created to match your enrollment targets. Do this by creating a mixin for the consent model class:

.. code-block:: python

    from edc_quota.client.models import QuotaMixin, QuotaManager

    class ConsentQuotaMixin(QuotaMixin):

        QUOTA_REACHED_MESSAGE = 'Maximum number of subjects has been reached or exceeded for {}. Got {} >= {}.'

        class Meta:
                abstract = True

Then declare the consent model:

.. code-block:: python

        class MyConsent(ConsentQuotaMixin, BaseConsent):

            quota = QuotaManager()

        class Meta:
            app_label = 'my_app'

Declare the ModelForm:

.. code-block:: python

    class MyConsentForm(BaseConsentForm):

        class Meta:
            model = MyConsent


Now that you have a consent model class, identify and declare the models that will require this consent:

.. code-block:: python

    class Questionnaire(RequiresConsentMixin, models.Model):

        consent_model = MyConsent  # or tuple (app_label, model_name)

        report_datetime = models.DateTimeField(default=timezone.now)

        question1 = models.CharField(max_length=10)

        question2 = models.CharField(max_length=10)

        question3 = models.CharField(max_length=10)

    @property
    def subject_identifier(self):
        """Returns the subject identifier from ..."""
        return subject_identifier

    class Meta:
        app_label = 'my_app'
        verbose_name = 'My Questionnaire'

Notice above the first two class attributes, namely:

* consent_model: this is the consent model class that was declared above;
* report_datetime: a required field used to lookup the correct consent version from ConsentType and to find, together with ``subject_identifier``,  a valid instance of ``MyConsent``;

Also note the property ``subject_identifier``.

* subject_identifier: a required property that knows how to find the ``subject_identifier`` for the instance of ``Questionnaire``.

Once all is declared you need to:

* define the consent version and validity period for the consent version in ``ConsentType``;
* add a Quota for the consent model.

As subjects are identified:

* add a consent
* add the models (e.g. ``Questionnaire``)

If a consent version cannot be found given the consent model class and report_datetime a ``ConsentTypeError`` is raised.

If a consent for this subject_identifier cannot be found that matches the ``ConsentType`` a ``NotConsentedError`` is raised.

Specimen Consent
================

A participant may consent to the study but not agree to have specimens stored long term. A specimen consent is administered separately to clarify the participant\'s intention.

The specimen consent is declared using the base class ``BaseSpecimenConsent``. This is an abridged version of ``BaseConsent``. The specimen consent also uses the ``RequiresConsentMixin`` as it cannot stand alone as an ICF. The ``RequiresConsentMixin`` ensures the specimen consent is administered after the main study ICF, in this case ``MyStudyConsent``.

A specimen consent is declared in your app like this:

.. code-block:: python

        class SpecimenConsent(
            BaseSpecimenConsent, SampleCollectionFieldsMixin, RequiresConsentMixin,
            VulnerabilityFieldsMixin, AppointmentMixin, BaseUuidModel
        ):

            consent_model = MyStudyConsent

            registered_subject = models.OneToOneField(RegisteredSubject, null=True)

            objects = models.Manager()

            history = AuditTrail()

        class Meta:
            app_label = 'my_app'
            verbose_name = 'Specimen Consent'


Validators
==========

The ``ConsentAgeValidator`` validates the date of birth to within a given age range, for example:

.. code-block:: python

    from edc_consent.validtors import ConsentAgeValidator

    class MyConsent(ConsentQuotaMixin, BaseConsent):

        dob = models.DateField(
            validators=[ConsentAgeValidator(16, 64)])

        quota = QuotaManager()

        class Meta:
            app_label = 'my_app'

The ``PersonalFieldsMixin`` includes a date of birth field and you can set the age bounds like this:

.. code-block:: python

    from edc_consent.validtors import ConsentAgeValidator
    from edc_consent.models.fields import PersonalFieldsMixin

    class MyConsent(ConsentQuotaMixin, PersonalFieldsMixin, BaseConsent):

        quota = QuotaManager()

        MIN_AGE_OF_CONSENT = 18
        MAX_AGE_OF_CONSENT = 64

        class Meta:
            app_label = 'my_app'


Common senarios
===============

Tracking the consent version with collected data
++++++++++++++++++++++++++++++++++++++++++++++++

All model data is tagged with the consent version identified in ``ConsentType`` for the consent model class and report_datetime.

Reconsenting consented subjects when the consent changes
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The consent model is unique on subject_identifier, identity and version. If a new consent version is added to ``ConsentType``, a new consent will be required for each subject as data is reported within the validity period of the new consent.

Some care must be taken to ensure that the consent model is queried with an understanding of the unique constraint.


Linking the consent version to added or removed model fields on models that require consent
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

TODO

Infants use mother's consent
++++++++++++++++++++++++++++

TODO

By adding the property ``consenting_subject_identifier`` to the consent


Patient names
=============
If patient names need to be removed from the data collection, there are a few helper
attributes and methods to consider.

``settings.EDC_CONSENT_REMOVE_PATIENT_NAMES_FROM_COUNTRIES: list[str]``

If given a list of country names, name fields will be removed from any admin.fieldset.

See also edc_sites.all_sites

``ConsentModelAdminMixin.get_fieldsets``

.. code-block:: python

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        for country in get_remove_patient_names_from_countries():
            site = getattr(request, "site", None)
            if site and site.id in [s.site_id for s in self.all_sites.get(country)]:
                return self.fieldsets_without_names(fieldsets)
        return fieldsets

This method could be added to any ModeLadmin with names.



using


Other TODO
==========

* ``Timepoint`` model update in ``save`` method of models requiring consent
* handle added or removed model fields (questions) because of consent version change
* review verification actions
* management command to update version on models that require consent (if edc_consent added after instances were created)
* handle re-consenting issues, for example, if original consent was restricted by age (16-64) but the re-consent is not. May need to open upper bound.



.. |pypi| image:: https://img.shields.io/pypi/v/edc-consent.svg
    :target: https://pypi.python.org/pypi/edc-consent

.. |actions| image:: https://github.com/clinicedc/edc-consent/workflows/build/badge.svg?branch=develop
  :target: https://github.com/clinicedc/edc-consent/actions?query=workflow:build

.. |codecov| image:: https://codecov.io/gh/clinicedc/edc-consent/branch/develop/graph/badge.svg
  :target: https://codecov.io/gh/clinicedc/edc-consent

.. |downloads| image:: https://pepy.tech/badge/edc-consent
   :target: https://pepy.tech/project/edc-consent
