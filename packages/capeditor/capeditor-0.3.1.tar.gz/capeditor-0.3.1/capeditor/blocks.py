import json

import shapely
from django import forms
from django.contrib.gis.geos import GEOSGeometry
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _
from shapely import Point
from shapely.geometry import shape
from wagtail import blocks
from wagtail.blocks import FieldBlock, StructValue
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.models import Site
from wagtailiconchooser.blocks import IconChooserBlock

from .forms.fields import PolygonField, BoundaryPolygonField
from .forms.widgets import CircleWidget
from .utils import file_path_mime


class BoundaryFieldBlock(FieldBlock):
    def __init__(self, required=True, help_text=None, srid=4326, **kwargs):
        self.field_options = {
            "required": required,
            "help_text": help_text,
            "srid": srid
        }

        super().__init__(**kwargs)

    @cached_property
    def field(self):
        return BoundaryPolygonField(**self.field_options)

    def value_from_form(self, value):
        if isinstance(value, GEOSGeometry):
            value = value.json
        return value


class PolygonFieldBlock(FieldBlock):
    def __init__(self, required=True, help_text=None, srid=4326, **kwargs):
        self.field_options = {
            "required": required,
            "help_text": help_text,
            "srid": srid
        }

        super().__init__(**kwargs)

    @cached_property
    def field(self):
        return PolygonField(**self.field_options)

    def value_from_form(self, value):
        if isinstance(value, GEOSGeometry):
            value = value.json
        return value


class CircleFieldBlock(blocks.TextBlock):
    @cached_property
    def field(self):
        field_kwargs = {"widget": CircleWidget()}
        field_kwargs.update(self.field_options)
        return forms.CharField(**field_kwargs)


class AlertAddress(blocks.StructBlock):
    name = blocks.TextBlock(label=_("Name"), help_text=_("Name of the recipient"))
    address = blocks.TextBlock(label=_("Address"), help_text=_("Address Information of the recipient"))


class AlertReferenceStructValue(StructValue):
    @property
    def ref_alert_identifier(self):
        alert_page = self.get("ref_alert").specific

        if hasattr(alert_page, "cap_reference_id"):
            return alert_page.cap_reference_id

        return None


class AlertReference(blocks.StructBlock):
    class Meta:
        value_class = AlertReferenceStructValue

    ref_alert = blocks.PageChooserBlock(label=_("Reference Alert"),
                                        help_text=_("Earlier alert referenced by this alert"))


class AlertIncident(blocks.StructBlock):
    incident = blocks.TextBlock(label=_("Incident"), help_text=_("Referent incident to this alert message"))


class AlertInfoParameter(blocks.StructBlock):
    valueName = blocks.TextBlock(label=_("Name"))
    value = blocks.TextBlock(label=_("Value"))


class AlertResponseType(blocks.StructBlock):
    RESPONSE_TYPE_CHOICES = (
        ("Shelter", _("Shelter - Take shelter in place or per instruction")),
        ("Evacuate", _("Evacuate - Relocate as instructed in the instruction")),
        ("Prepare", _("Prepare - Relocate as instructed in the instruction")),
        ("Execute", _("Execute - Execute a pre-planned activity identified in instruction")),
        ("Avoid", _("Avoid - Avoid the subject event as per the instruction")),
        ("Monitor", _("Monitor - Attend to information sources as described in instruction")),
        ("Assess", _("Assess - Evaluate the information in this message - DONT USE FOR PUBLIC ALERTS")),
        ("AllClear", _("All Clear - The subject event no longer poses a threat or concern and any follow "
                       "on action is described in instruction")),
        ("None", _("No action recommended")),
    )

    response_type = blocks.ChoiceBlock(choices=RESPONSE_TYPE_CHOICES, label=_("Response type"),
                                       help_text=_("The code denoting the type of action recommended for the "
                                                   "target audience"))


class AlertAreaBoundaryStructValue(StructValue):
    @cached_property
    def area(self):
        polygon_geojson_str = self.get("boundary")
        polygon_geojson_dict = json.loads(polygon_geojson_str)

        polygon = shape(polygon_geojson_dict)
        coords = " ".join(["{},{}".format(x, y) for x, y in list(polygon.exterior.coords)])

        area_data = {
            "areaDesc": self.get("areaDesc"),
            "polygon": coords,
        }

        if self.get("altitude"):
            area_data.update({"altitude": self.get("altitude")})
            if self.get("ceiling"):
                area_data.update({"ceiling": self.get("ceiling")})

        return area_data

    @cached_property
    def geojson(self):
        polygon = self.get("boundary")
        return json.loads(polygon)
    
    # @cached_property
    # def aread_desc(self):
    #     area_desc = self.get("areaDesc")
    #     return json.loads(polygon)


class AlertAreaBoundaryBlock(blocks.StructBlock):
    class Meta:
        value_class = AlertAreaBoundaryStructValue

    ADMIN_LEVEL_CHOICES = (
        (1, "Level 1"),
        (2, "Level 2"),
        (3, "Level 3")
    )

    areaDesc = blocks.TextBlock(label=_("Affected areas / Regions"),
                                help_text=_("The text describing the affected area of the alert message"))
    admin_level = blocks.ChoiceBlock(choices=ADMIN_LEVEL_CHOICES, default=1, label=_("Administrative Level"))
    boundary = BoundaryFieldBlock(label=_("Boundary"),
                                  help_text=_("The paired values of points defining a polygon that delineates "
                                              "the affected area of the alert message"))

    altitude = blocks.CharBlock(max_length=100, required=False, label=_("Altitude"),
                                help_text=_("The specific or minimum altitude of the affected "
                                            "area of the alert message"))
    ceiling = blocks.CharBlock(max_length=100, required=False, label=_("Ceiling"),
                               help_text=_("The maximum altitude of the affected area of the alert message."
                                           "MUST NOT be used except in combination with the altitude element. "))


class AlertAreaPolygonStructValue(StructValue):
    @cached_property
    def area(self):
        polygon_geojson_str = self.get("polygon")
        polygon_geojson_dict = json.loads(polygon_geojson_str)

        polygon = shape(polygon_geojson_dict)
        coords = " ".join(["{},{}".format(x, y) for x, y in list(polygon.exterior.coords)])

        area_data = {
            "areaDesc": self.get("areaDesc"),
            "polygon": coords,
        }

        if self.get("altitude"):
            area_data.update({"altitude": self.get("altitude")})
            if self.get("ceiling"):
                area_data.update({"ceiling": self.get("ceiling")})

        return area_data

    @cached_property
    def geojson(self):
        polygon = self.get("polygon")
        return json.loads(polygon)


class AlertAreaPolygonBlock(blocks.StructBlock):
    class Meta:
        value_class = AlertAreaPolygonStructValue

    areaDesc = blocks.TextBlock(label=_("Affected areas / Regions"),
                                help_text=_("The text describing the affected area of the alert message"))
    polygon = PolygonFieldBlock(label=_("Polygon"),
                                help_text=_("The paired values of points defining a polygon that delineates "
                                            "the affected area of the alert message"))
    altitude = blocks.CharBlock(max_length=100, required=False, label=_("Altitude"),
                                help_text=_("The specific or minimum altitude of the affected "
                                            "area of the alert message"))
    ceiling = blocks.CharBlock(max_length=100, required=False, label=_("Ceiling"),
                               help_text=_("The maximum altitude of the affected area of the alert message."
                                           "MUST NOT be used except in combination with the altitude element. "))


class AlertAreaCircleStructValue(StructValue):
    @cached_property
    def area(self):
        area_data = {
            "areaDesc": self.get("areaDesc"),
            "circle": self.get("circle"),
        }

        if self.get("altitude"):
            area_data.update({"altitude": self.get("altitude")})
            if self.get("ceiling"):
                area_data.update({"ceiling": self.get("ceiling")})

        return area_data

    @cached_property
    def geojson(self):
        circle_str = self.get("circle")
        parts = circle_str.split()
        coords = parts[0].split(',')

        # Extract the longitude, latitude, and radius
        longitude, latitude, radius_km = float(coords[0]), float(coords[1]), float(parts[1])

        # Convert radius to degrees (approximation for small distances)
        radius_deg = radius_km / 111.12

        # Create a point for the center
        center_point = Point(longitude, latitude)

        circle = center_point.buffer(radius_deg)

        return shapely.geometry.mapping(circle)


class AlertAreaCircleBlock(blocks.StructBlock):
    class Meta:
        value_class = AlertAreaCircleStructValue

    areaDesc = blocks.TextBlock(label=_("Affected areas / Regions"),
                                help_text=_("The text describing the affected area of the alert message"))
    circle = CircleFieldBlock(label=_("Circle"), help_text=_("Drag the marker to change position"))

    altitude = blocks.CharBlock(max_length=100, required=False, label=_("Altitude"),
                                help_text=_("The specific or minimum altitude of the affected "
                                            "area of the alert message"))
    ceiling = blocks.CharBlock(max_length=100, required=False, label=_("Ceiling"),
                               help_text=_("The maximum altitude of the affected area of the alert message."
                                           "MUST NOT be used except in combination with the altitude element. "))


class AlertAreaGeocodeStructValue(StructValue):
    @cached_property
    def area(self):
        area_data = {
            "areaDesc": self.get("areaDesc"),
            "geocode": {"valueName": self.get("valueName"), "value": self.get("value")},
        }

        if self.get("altitude"):
            area_data.update({"altitude": self.get("altitude")})
            if self.get("ceiling"):
                area_data.update({"ceiling": self.get("ceiling")})

        return area_data

    @cached_property
    def geojson(self):
        return {}


class AlertAreaGeocodeBlock(blocks.StructBlock):
    class Meta:
        value_class = AlertAreaGeocodeStructValue

    areaDesc = blocks.TextBlock(label=_("Affected areas / Regions"),
                                help_text=_("The text describing the affected area of the alert message"))
    valueName = blocks.TextBlock(label="Name")
    value = blocks.TextBlock(label=_("Value"))

    altitude = blocks.CharBlock(max_length=100, required=False, label=_("Altitude"),
                                help_text=_("The specific or minimum altitude of the affected "
                                            "area of the alert message"))
    ceiling = blocks.CharBlock(max_length=100, required=False, label=_("Ceiling"),
                               help_text=_("The maximum altitude of the affected area of the alert message."
                                           "MUST NOT be used except in combination with the altitude element. "))


SENDER_NAME_HELP_TEXT = _("The human-readable name of the agency or authority issuing this alert.")
CONTACT_HELP_TEXT = _("The text describing the contact for follow-up and confirmation of the alert message")
EVENT_HELP_TEXT = _("The text denoting the type of the subject event of the alert message")
AUDIENCE_HELP_TEXT = _("The text describing the intended audience of the alert message")


class FileResourceStructValue(StructValue):
    @property
    def mime_type(self):
        doc = self.get('file')

        try:
            doc_file = doc.file.path
            mimetype = file_path_mime(doc_file)
            return mimetype
        except Exception:
            return None

    @property
    def uri(self):
        doc = self.get('file')
        return doc.url

    @property
    def resource(self):
        return {
            "type": "doc",
            "resourceDesc": self.get("resourceDesc"),
            "mimeType": self.mime_type,
            "uri": self.uri
        }


class ExternalResourceStructValue(StructValue):
    @property
    def resource(self):
        return {
            "type": "external",
            "resourceDesc": self.get("resourceDesc"),
            "mimeType": "text/uri-list",
            "uri": self.get('external_url')
        }


class FileResource(blocks.StructBlock):
    resourceDesc = blocks.TextBlock(label=_("Resource Description"),
                                    help_text=_("The text describing the type and content of the resource file"))
    file = DocumentChooserBlock()

    class Meta:
        value_class = FileResourceStructValue


class ExternalResource(blocks.StructBlock):
    resourceDesc = blocks.TextBlock(label=_("Resource Description"),
                                    help_text=_("The text describing the type and content of the resource file"))
    external_url = blocks.URLBlock(verbose_name=_("External Resource Link"),
                                   help_text=_("Link to external resource. "
                                               "This can be for example a link to related websites. "))

    class Meta:
        value_class = ExternalResourceStructValue


class AlertEventCode(blocks.StructBlock):
    valueName = blocks.TextBlock(label=_("Name"), help_text=_("Name for the event code"))
    value = blocks.TextBlock(label=_("Value"), help_text=_("Value of the event code"), )


class AlertInfoStructValue(StructValue):
    @cached_property
    def event_icon(self):
        from .models import CapSetting
        event = self.get("event")
        try:
            site = Site.objects.get(is_default_site=True)
            if site:
                cap_setting = CapSetting.for_site(site)

                if cap_setting.hazard_types:
                    for hazard in cap_setting.hazard_types:
                        event_name = hazard.value.get("hazard")
                        if event_name == event:
                            return hazard.value.get("icon")
        except Exception:
            pass

        return None

    @cached_property
    def resource(self):
        resource = self.get("resource")
        resources = []
        if resource:
            for res in resource:
                resources.append(res.value.resource)
            return resources
        return None

    @cached_property
    def area(self):
        area_blocks = self.get("area")
        areas = []

        if area_blocks:
            for area in area_blocks:
                areas.append(area.value.area)
            return areas

    @cached_property
    def geojson(self):
        area_blocks = self.get("area")
        
        features = []
        if area_blocks:
            for area in area_blocks:
                features.append(area.value.geojson)
            return features

    @cached_property
    def area_properties(self):
        severity_blocks = self.get("severity")
        certainty_blocks = self.get("certainty")
        urgency_blocks = self.get("urgency")
        event_blocks = self.get("event")

        return {
            'severity':severity_blocks,
            'certainty':certainty_blocks,
            'urgency':urgency_blocks,
            'event':event_blocks
        }

    @cached_property
    def features(self):
        area_blocks = self.get("area")
        
        features = []

        if area_blocks:
            for feature in area_blocks:
                if feature.value.geojson:
                    features.append({
                        "type": "Feature", 
                        "geometry": feature.value.geojson,
                        "properties":{
                            "areaDesc":feature.value.area.get('areaDesc'),
                                       **self.area_properties}
                    })
        return features


class AlertInfo(blocks.StructBlock):
    class Meta:
        value_class = AlertInfoStructValue

    LANGUAGE_CHOICES = (
        ('en', _("English")),
    )

    CATEGORY_CHOICES = (
        ('Geo', _("Geophysical")),
        ('Met', _("Meteorological")),
        ('Safety', _("General emergency and public safety")),
        ('Security', _("Law enforcement, military, homeland and local/private security")),
        ('Rescue', _("Rescue and recovery")),
        ('Fire', _("Fire suppression and rescue")),
        ('Health', _("Medical and public health")),
        ('Env', _("Pollution and other environmental")),
        ('Transport', _("Public and private transportation")),
        ('Infra', _("Utility, telecommunication, other non-transport infrastructure")),
        ('Cbrne', _("Chemical, Biological, Radiological, Nuclear or High-Yield Explosive threat or attack")),
        ('Other', _("Other events")),
    )

    URGENCY_CHOICES = (
        ('Immediate', _("Immediate - Responsive action SHOULD be taken immediately")),
        ('Expected', _("Expected - Responsive action SHOULD be taken soon (within next hour)")),
        ('Future', _("Future - Responsive action SHOULD be taken in the near future")),
        ('Past', _("Past - Responsive action is no longer required")),
        ('Unknown', _("Unknown - Urgency not known")),
    )

    SEVERITY_CHOICES = (
        ('Extreme', _("Extreme - Extraordinary threat to life or property")),
        ('Severe', _("Severe - Significant threat to life or property")),
        ('Moderate', _("Moderate - Possible threat to life or property")),
        ('Minor', _("Minor - Minimal to no known threat to life or property")),
        ('Unknown', _("Unknown - Severity unknown")),
    )

    CERTAINTY_CHOICES = (
        ('Observed', _("Observed - Determined to have occurred or to be ongoing")),
        ('Likely', _("Likely - Likely (percentage > ~50%)")),
        ('Possible', _("Possible - Possible but not likely (percentage <= ~50%)")),
        ('Unlikely', _("Unlikely - Not expected to occur (percentage ~ 0)")),
        ('Unknown', _("Unknown - Certainty unknown")),
    )
    event = blocks.CharBlock(max_length=255, label=_("Event"), help_text=EVENT_HELP_TEXT)

    category = blocks.ChoiceBlock(choices=CATEGORY_CHOICES, default="Met", label=_("Category"),
                                  help_text=_("The code denoting the category of the subject"
                                              " event of the alert message"))
    language = blocks.ChoiceBlock(choices=LANGUAGE_CHOICES, default="en", required=False, label=_("Language"),
                                  help_text=_("The code denoting the language of the alert message"), )
    
    urgency = blocks.ChoiceBlock(choices=URGENCY_CHOICES, label=_("Urgency"),
                                 help_text=_("The code denoting the urgency of the subject "
                                             "event of the alert message"))
    severity = blocks.ChoiceBlock(choices=SEVERITY_CHOICES, label=_("Severity"),
                                  help_text=_("The code denoting the severity of the subject "
                                              "event of the alert message"))
    certainty = blocks.ChoiceBlock(choices=CERTAINTY_CHOICES, label=_("Certainty"),
                                   help_text=_("The code denoting the certainty of the subject "
                                               "event of the alert message"))
    headline = blocks.CharBlock(max_length=160, required=False, label=_("Headline"),
                                help_text=_("The text headline of the alert message. "
                                            "Make it direct and actionable as possible while remaining short"))
    description = blocks.TextBlock(required=True, label=_("Description"),
                                   help_text=_(
                                       "The text describing the subject event of the alert message. "
                                       "An extended description of the hazard or event that occasioned this message"))
    instruction = blocks.TextBlock(required=False, label=_("Instruction"),
                                   help_text=_("The text describing the recommended action to be taken by "
                                               "recipients of the alert message"))
    effective = blocks.DateTimeBlock(required=False, label=_("Effective"),
                                     help_text=_("The effective time of the information of the alert message. "
                                                 "If not set, the sent date will be used"))
    onset = blocks.DateTimeBlock(required=False, label=_("Onset"),
                                 help_text=_("The expected time of the beginning of the subject event "
                                             "of the alert message"))
    expires = blocks.DateTimeBlock(required=True, label=_("Expires"),
                                   help_text=_("The expiry time of the information of the alert message. "
                                               "If not set, each recipient is free to set its own policy as to when the"
                                               " message is no longer in effect."))
    responseType = blocks.ListBlock(AlertResponseType(label="Response Type"), label=_("Response Types"), default=[])

    senderName = blocks.CharBlock(max_length=255, label=_("Sender name"), required=False,
                                  help_text=SENDER_NAME_HELP_TEXT)
    contact = blocks.CharBlock(max_length=255, required=False, label=_("Contact"), help_text=CONTACT_HELP_TEXT)
    audience = blocks.CharBlock(max_length=255, required=False, label=_("Audience"),
                                help_text=AUDIENCE_HELP_TEXT)
    area = blocks.StreamBlock([
        ("boundary_block", AlertAreaBoundaryBlock(label=_("Admin Boundary"))),
        ("polygon_block", AlertAreaPolygonBlock(label=_("Draw Polygon"))),
        ("circle_block", AlertAreaCircleBlock(label=_("Circle"))),
        ("geocode_block", AlertAreaGeocodeBlock(label=_("Geocode"))),
    ], label=_("Alert Area"), help_text=_("Admin Boundary, Polygon, Circle or Geocode"))

    resource = blocks.StreamBlock([
        ("file_resource", FileResource()),
        ("external_resource", ExternalResource()),
    ], required=False, label=_("Resources"), help_text=_("Additional file with supplemental information "
                                                         "related to this alert information"))

    parameter = blocks.ListBlock(AlertInfoParameter(label=_("Parameter")), label=_("Parameters"), default=[])
    eventCode = blocks.ListBlock(AlertEventCode(label=_("Event Code")), label=_("Event codes"), default=[])

    # NOTE: web attribute is obtained from the url of the page

    class Meta:
        value_class = AlertInfoStructValue
        label_format = "({language}) {event}"

class HazardTypeBlock(blocks.StructBlock):
    hazard = blocks.CharBlock(max_length=255, label=_("Hazard"), help_text="Name of Hazard")
    icon = IconChooserBlock(required=False)


class AudienceTypeBlock(blocks.StructBlock):
    audience = blocks.CharBlock(max_length=255, label=_("Audience"), help_text="Intended audience")


class ContactBlock(blocks.StructBlock):
    contact = blocks.CharBlock(max_length=255, label=_("Contact Detail"))
