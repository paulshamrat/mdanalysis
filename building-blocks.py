class NewAnalysis(AnalysisBase):
    def __init__(self, atomgroup, parameter, **kwargs):
        super(NewAnalysis, self).__init__(atomgroup.universe.trajectory,
                                          **kwargs)
        self._parameter = parameter
        self._ag = atomgroup

    def _prepare(self):
        # OPTIONAL
        # Called before iteration on the trajectory has begun.
        # Data structures can be set up at this time
        self.result = []

    def _single_frame(self):
        # REQUIRED
        # Called after the trajectory is moved onto each new frame.
        # store result of `some_function` for a single frame
        self.result.append(some_function(self._ag, self._parameter))

    def _conclude(self):
        # OPTIONAL
        # Called once iteration on the trajectory is finished.
        # Apply normalisation and averaging to results here.
        self.result = np.asarray(self.result) / np.sum(self.result)