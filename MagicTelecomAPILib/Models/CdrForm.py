# -*- coding: utf-8 -*-

"""
   MagicTelecomAPILib.Models.CdrForm
 
   This file was automatically generated by APIMATIC v2.0 on 06/22/2016
"""
from MagicTelecomAPILib.APIHelper import APIHelper
from MagicTelecomAPILib.Models.Cdrs import Cdrs

class CdrForm(object):

    """Implementation of the 'Cdr Form' model.

    TODO: type model description here.

    Attributes:
        cdrs (Cdrs): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the CdrForm class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    cdrs -- Cdrs -- Sets the attribute cdrs
        
        """
        # Set all of the parameters to their default values
        self.cdrs = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "cdrs": "cdrs",
        }

        # Parse all of the Key-Value arguments
        if kwargs is not None:
            for key in kwargs:
                # Only add arguments that are actually part of this object
                if key in replace_names:
                    setattr(self, replace_names[key], kwargs[key])

            # Other objects also need to be initialised properly
            if "cdrs" in kwargs:
                self.cdrs = Cdrs(**kwargs["cdrs"])

    def resolve_names(self):
        """Creates a dictionary representation of this object.
        
        This method converts an object to a dictionary that represents the
        format that the model should be in when passed into an API Request.
        Because of this, the generated dictionary may have different
        property names to that of the model itself.
        
        Returns:
            dict: The dictionary representing the object.
        
        """
        # Create a mapping from Model property names to API property names
        replace_names = {
            "cdrs": "cdrs",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)