from safedelete.managers import SafeDeleteManager, DELETED_INVISIBLE

class BasicManager(SafeDeleteManager):
  _safedelete_visibility = DELETED_INVISIBLE