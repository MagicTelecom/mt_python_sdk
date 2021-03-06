"""
    MagicTelecomAPILib

    This file was automatically generated by APIMATIC BETA v2.0 on 06/22/2016
"""
from MagicTelecomAPILib.Models import *
from MagicTelecomAPILib.Controllers import *
from MagicTelecomAPILib.Decorators import *
from MagicTelecomAPILib.APIException import *

class MagicTelecomAPIClient(object):

    @LazyProperty
    def users_controller(self):
        return UsersController()

    @LazyProperty
    def accounts_controller(self):
        return AccountsController()

    @LazyProperty
    def dids_controller(self):
        return DidsController()

    @LazyProperty
    def dids_products_controller(self):
        return DidsProductsController()


    def __init__(self, 
                 x_auth_token = "123abcqwerty"):

        Configuration.x_auth_token = x_auth_token


