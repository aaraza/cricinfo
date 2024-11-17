from enum import Enum

class Team(Enum):
    """
    Statistics can be filtered by team. 
    
    For any method where this class is a parameter, it can be passed as :obj:`None`,
    bypassing team filtering.
    """
    England = '1'
    Australia = '2'
    SouthAfrica = '3'
    WestIndies = '4'
    NewZealand = '5'
    India = '6'
    Pakistan = '7'
    SriLanka = '8'
    Zimbawe = '9'