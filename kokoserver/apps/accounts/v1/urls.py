"""
Generated by 'esmerald createapp' using Esmerald 2.4.0.
"""
from esmerald import Gateway, Include

from .views import get_all_users

route_patterns = [Gateway(handler=get_all_users)]