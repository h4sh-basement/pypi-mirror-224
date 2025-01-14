from django.db import models
from django.conf import settings

from rest import models as rm
from rest import helpers as rh
import re

UNDEFINED = "TYUIFGHJ"

"""
Rule defines a set of checks that will create an incident from an incoming event.

There is no subscriptions.  Group with kind incident are created as buckets.
When a rule is triggered it will create a new incident

the incident will be assigned to the rule.group
the incident priority will be assigned to the rule.priority

Events can be bundled into a single Incident by setting bundle=<minutes>.  
So if bundle is set to 60 then for 60 minutes after the first event all events will get 
added to to same incident.

"""


class Rule(models.Model, rm.RestModel):
    class RestMeta:
        SEARCH_FIELDS = ["name", "group__name"]
        CAN_DELETE = True
        # VIEW_PERMS = ["example_permission"]
        GRAPHS = {
            "default": {
                "graphs": {
                    "group": "basic",
                    "created_by": "basic"
                },
            },
            "basic": {
                "fields": [
                    "created",
                    "priority",
                    "name",
                    "category",
                    "priority",
                    "action",
                    "action_after",
                    "bundle",
                    "bundle_by"
                ]
            }
        }

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=200)
    # the group the rule gets assigned to when triggered
    group = models.ForeignKey("account.Group", on_delete=models.CASCADE, null=True, default=None)
    # category allows us to limit running rules to only those with a category
    # if category is null then this will run on all events?
    category = models.CharField(max_length=200, db_index=True)
    created_by = models.ForeignKey("account.Member", on_delete=models.CASCADE, null=True, default=None)
    # this specifies the order the rule runs in and will assign the priority to the created incident
    priority = models.IntegerField(default=10, db_index=True)  # 1-10, 1 being the highest
    # if multiple events fire the same rule it will just bundle them together
    # this is in minutes (default=0=OFF)
    bundle = models.IntegerField(default=0)  # 0=off
    bundle_by = models.IntegerField(default=3)  # 0=none, 1=hostname, 2=component, 3=component and hostname
    # an action to perform if this rule is hit, default is notify
    # examples (ignore, notify, task:app_name:fname:channel)
    action = models.CharField(max_length=200, default=None, null=True)
    action_after = models.IntegerField(default=0)  # how many incidents before firing action
    
    def run(self, event):
        for check in self.checks.all():
            if not check.run(event):
                return False
        return True


class RuleCheck(models.Model, rm.RestModel):
    class RestMeta:
        SEARCH_FIELDS = ["name"]
        CAN_DELETE = True
        # VIEW_PERMS = ["example_permission"]
        GRAPHS = {
            "default": {
                "graphs": {
                    "parent": "basic"
                },
            }
        }

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey(Rule, on_delete=models.CASCADE, related_name="checks")
    # the lower the number the sooner it runs
    name = models.CharField(max_length=200)
    # the order for which this check runs
    index = models.IntegerField(default=0)
    comparator = models.CharField(max_length=32, default="==")
    field_name = models.CharField(max_length=124, default=None, null=True)
    value = models.CharField(max_length=124, default="")
    value_type = models.IntegerField(default=0)  # 0=int 1=float 2=string
 
    def run(self, event):
        # TODO ians look into does this support pulling metadata.....
        field_value = event.getProperty(self.field_name, UNDEFINED)
        if field_value == UNDEFINED:
            return False
        comp_value = self.value
        try:
            if self.comparator != "contains":
                if self.value_type == 0:
                    comp_value = int(comp_value)
                    field_value = int(field_value)
                elif self.value_type == 1:
                    comp_value = float(comp_value)
                    field_value = float(field_value)
        except Exception:
            return False

        if self.comparator in ["eq", "=="]:
            return field_value == comp_value
        if self.comparator == ">":
            return field_value > comp_value
        if self.comparator == ">=":
            return field_value >= comp_value        
        if self.comparator == "<":
            return field_value < comp_value     
        if self.comparator == "<=":
            return field_value <= comp_value
        if self.comparator == "contains":
            field_value = str(field_value)
            comp_value = str(comp_value)
            return field_value.find(comp_value) != -1
        if self.comparator == "regex":
            return re.match(comp_value, field_value)
        return False    

