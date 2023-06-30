class GeneralInfoStyle():
    _Id = None
    _IdWorkcenter = None
    _StyleNumber = None
    _TypeStyle = None
    _LeadTime = None
    _Workflow = None
    _Comment = None

    def __init__(self, Id, IdWorkcenter, StyleNumber, TypeStyle, Leadtime, Workflow, Comment) -> None:
        self._Id = Id
        self._IdWorkcenter = IdWorkcenter
        self._StyleNumber = StyleNumber
        self._TypeStyle = TypeStyle
        self._LeadTime = Leadtime
        self._Workflow = Workflow
        self._Comment = Comment
        self.getData()
    
    def getData():
        pass