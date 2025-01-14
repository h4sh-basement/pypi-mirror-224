from tqdm.auto import tqdm
from joblib import Parallel


class ParallelTqdm(Parallel):
    def __init__(self,
                 use_tqdm=True,
                 total=None,
                 desc='',
                 colour='blue',
                 *args, **kwargs):
        self._use_tqdm = use_tqdm
        self._total = total
        self._desc = desc
        self._colour = colour
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        with tqdm(disable=not self._use_tqdm,
                  total=self._total,
                  desc=self._desc,
                  colour=self._colour) as self._pbar:
            return Parallel.__call__(self, *args, **kwargs)

    def print_progress(self):
        if self._total is None:
            self._pbar.total = self.n_dispatched_tasks
        self._pbar.n = self.n_completed_tasks
        self._pbar.refresh()
