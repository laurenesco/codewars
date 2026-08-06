# https://www.codewars.com/kata/588a00ad70720f2cd9000005/train/python

from typing import Callable

class Router():
    def __init__(self):
        """
        Initialize Router object
        
        boundRoutes is a tuple-key dictionary storing route information
        """
        self.bound_routes = {}
    
    def bind(self, route: str, method: str, action: Callable) -> None:
        """
        Bind new routes (overwrites existing routes if duplicate provided)
        
        Params:
          - route:  The route, e.g., "\login"
          - method: HTTPS method, e.g., "GET", "POST"
          - action: lambda storing appropriate action on route access
        """
        self.bound_routes[(route, method)] = action
        
    def runRequest(self, route:str, method:str) -> str:
        """
        Runs a specified request, if it exists. Else return error
        """
        try:
            return self.bound_routes[(route, method)]()        
        except KeyError:
            return 'Error 404: Not Found'
        
