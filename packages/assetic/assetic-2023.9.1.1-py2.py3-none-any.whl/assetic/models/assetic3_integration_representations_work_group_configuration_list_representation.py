from assetic.models.work_group_configuration_list_representation import WorkGroupConfigurationListRepresentation
import warnings
import six
class Assetic3IntegrationRepresentationsWorkGroupConfigurationListRepresentation(WorkGroupConfigurationListRepresentation):
	def __init__(self, **kwargs):
		warnings.warn('The "Assetic3IntegrationRepresentationsWorkGroupConfigurationListRepresentation" class is deprecated, use "WorkGroupConfigurationListRepresentation" instead',stacklevel=2)
		super(WorkGroupConfigurationListRepresentation, self).__init__()
		for attr, _ in six.iteritems(self.swagger_types):
			val = None
			if attr in kwargs:
				val = kwargs[attr]
			setattr(self, "_" + attr, val) 
