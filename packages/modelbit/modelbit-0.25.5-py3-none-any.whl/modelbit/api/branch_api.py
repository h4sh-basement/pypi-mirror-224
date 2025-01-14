import logging

from modelbit.helpers import getCurrentBranch
from .api import MbApi

logger = logging.getLogger(__name__)

class BranchApi:
  api: MbApi

  def __init__(self, api: MbApi):
    self.api = api
  
  def raiseIfProtected(self):
    self.api.getJsonOrThrow("api/cli/v1/branch_check", { "branch": getCurrentBranch() })
