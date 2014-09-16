import pyVmomi
pyVmomi.sms = pyVmomi.VmomiSupport.LazyModule('sms')
if hasattr(pyVmomi.VmomiSupport, "_urnMap"):
    pyVmomi.VmomiSupport._urnMap["sms"] = "urn:sms"

# The following definitions were taken from the VMware package
# DO NOT EDIT

from pyVmomi.VmomiSupport import CreateDataType,  CreateManagedType,  CreateEnumType,  AddVersion,  AddVersionParent,  F_LINK,  F_LINKABLE,  F_OPTIONAL

AddVersion('sms.version.version1', 'sms', '1.0', 0, 'sms')
AddVersion('sms.version.version2', 'sms', '2.0', 0, 'sms')
AddVersion('sms.version.version3', 'sms', '3.0', 0, 'sms')
AddVersion('sms.version.version4', 'sms', '4.0', 0, 'sms')
AddVersion('vim.version.version1', 'vim2', '2.0', 1, 'vim25')
AddVersion('vim.version.version2', 'vim25', '2.5', 0, 'vim25')
AddVersion('vim.version.version3', 'vim25', '2.5u2', 1, 'vim25')
AddVersion('vim.version.version4', 'vim25', '2.5u2server', 0, 'vim25')
AddVersion('vim.version.version5', 'vim25', '4.0', 0, 'vim25')
AddVersion('vim.version.version6', 'vim25', '4.1', 0, 'vim25')
AddVersion('vmodl.query.version.version1', '', '', 0, 'vim25')
AddVersion('vmodl.query.version.version2', '', '', 0, 'vim25')
AddVersion('vmodl.query.version.version3', '', '', 0, 'vim25')
AddVersion('vmodl.version.version0', '', '', 0, 'vim25')
AddVersion('vmodl.version.version1', '', '', 0, 'vim25')
AddVersionParent('sms.version.version1', 'sms.version.version1')
AddVersionParent('sms.version.version1', 'vmodl.version.version0')
AddVersionParent('sms.version.version1', 'vmodl.version.version1')
AddVersionParent('sms.version.version2', 'sms.version.version1')
AddVersionParent('sms.version.version2', 'sms.version.version2')
AddVersionParent('sms.version.version2', 'vim.version.version1')
AddVersionParent('sms.version.version2', 'vim.version.version2')
AddVersionParent('sms.version.version2', 'vim.version.version3')
AddVersionParent('sms.version.version2', 'vim.version.version4')
AddVersionParent('sms.version.version2', 'vim.version.version5')
AddVersionParent('sms.version.version2', 'vim.version.version6')
AddVersionParent('sms.version.version2', 'vmodl.query.version.version1')
AddVersionParent('sms.version.version2', 'vmodl.query.version.version2')
AddVersionParent('sms.version.version2', 'vmodl.query.version.version3')
AddVersionParent('sms.version.version2', 'vmodl.version.version0')
AddVersionParent('sms.version.version2', 'vmodl.version.version1')
AddVersionParent('sms.version.version3', 'sms.version.version1')
AddVersionParent('sms.version.version3', 'sms.version.version2')
AddVersionParent('sms.version.version3', 'sms.version.version3')
AddVersionParent('sms.version.version3', 'vim.version.version1')
AddVersionParent('sms.version.version3', 'vim.version.version2')
AddVersionParent('sms.version.version3', 'vim.version.version3')
AddVersionParent('sms.version.version3', 'vim.version.version4')
AddVersionParent('sms.version.version3', 'vim.version.version5')
AddVersionParent('sms.version.version3', 'vim.version.version6')
AddVersionParent('sms.version.version3', 'vmodl.query.version.version1')
AddVersionParent('sms.version.version3', 'vmodl.query.version.version2')
AddVersionParent('sms.version.version3', 'vmodl.query.version.version3')
AddVersionParent('sms.version.version3', 'vmodl.version.version0')
AddVersionParent('sms.version.version3', 'vmodl.version.version1')
AddVersionParent('sms.version.version4', 'sms.version.version1')
AddVersionParent('sms.version.version4', 'sms.version.version2')
AddVersionParent('sms.version.version4', 'sms.version.version3')
AddVersionParent('sms.version.version4', 'sms.version.version4')
AddVersionParent('sms.version.version4', 'vim.version.version1')
AddVersionParent('sms.version.version4', 'vim.version.version2')
AddVersionParent('sms.version.version4', 'vim.version.version3')
AddVersionParent('sms.version.version4', 'vim.version.version4')
AddVersionParent('sms.version.version4', 'vim.version.version5')
AddVersionParent('sms.version.version4', 'vim.version.version6')
AddVersionParent('sms.version.version4', 'vmodl.query.version.version1')
AddVersionParent('sms.version.version4', 'vmodl.query.version.version2')
AddVersionParent('sms.version.version4', 'vmodl.query.version.version3')
AddVersionParent('sms.version.version4', 'vmodl.version.version0')
AddVersionParent('sms.version.version4', 'vmodl.version.version1')
AddVersionParent('vim.version.version1', 'vim.version.version1')
AddVersionParent('vim.version.version1', 'vmodl.query.version.version1')
AddVersionParent('vim.version.version1', 'vmodl.version.version0')
AddVersionParent('vim.version.version2', 'vim.version.version1')
AddVersionParent('vim.version.version2', 'vim.version.version2')
AddVersionParent('vim.version.version2', 'vmodl.query.version.version1')
AddVersionParent('vim.version.version2', 'vmodl.version.version0')
AddVersionParent('vim.version.version3', 'vim.version.version1')
AddVersionParent('vim.version.version3', 'vim.version.version2')
AddVersionParent('vim.version.version3', 'vim.version.version3')
AddVersionParent('vim.version.version3', 'vmodl.query.version.version1')
AddVersionParent('vim.version.version3', 'vmodl.version.version0')
AddVersionParent('vim.version.version4', 'vim.version.version1')
AddVersionParent('vim.version.version4', 'vim.version.version2')
AddVersionParent('vim.version.version4', 'vim.version.version3')
AddVersionParent('vim.version.version4', 'vim.version.version4')
AddVersionParent('vim.version.version4', 'vmodl.query.version.version1')
AddVersionParent('vim.version.version4', 'vmodl.version.version0')
AddVersionParent('vim.version.version5', 'vim.version.version1')
AddVersionParent('vim.version.version5', 'vim.version.version2')
AddVersionParent('vim.version.version5', 'vim.version.version3')
AddVersionParent('vim.version.version5', 'vim.version.version4')
AddVersionParent('vim.version.version5', 'vim.version.version5')
AddVersionParent('vim.version.version5', 'vmodl.query.version.version1')
AddVersionParent('vim.version.version5', 'vmodl.query.version.version2')
AddVersionParent('vim.version.version5', 'vmodl.version.version0')
AddVersionParent('vim.version.version5', 'vmodl.version.version1')
AddVersionParent('vim.version.version6', 'vim.version.version1')
AddVersionParent('vim.version.version6', 'vim.version.version2')
AddVersionParent('vim.version.version6', 'vim.version.version3')
AddVersionParent('vim.version.version6', 'vim.version.version4')
AddVersionParent('vim.version.version6', 'vim.version.version5')
AddVersionParent('vim.version.version6', 'vim.version.version6')
AddVersionParent('vim.version.version6', 'vmodl.query.version.version1')
AddVersionParent('vim.version.version6', 'vmodl.query.version.version2')
AddVersionParent('vim.version.version6', 'vmodl.query.version.version3')
AddVersionParent('vim.version.version6', 'vmodl.version.version0')
AddVersionParent('vim.version.version6', 'vmodl.version.version1')
AddVersionParent('vmodl.query.version.version1', 'vmodl.query.version.version1')
AddVersionParent('vmodl.query.version.version1', 'vmodl.version.version0')
AddVersionParent('vmodl.query.version.version2', 'vmodl.query.version.version1')
AddVersionParent('vmodl.query.version.version2', 'vmodl.query.version.version2')
AddVersionParent('vmodl.query.version.version2', 'vmodl.version.version0')
AddVersionParent('vmodl.query.version.version2', 'vmodl.version.version1')
AddVersionParent('vmodl.query.version.version3', 'vmodl.query.version.version1')
AddVersionParent('vmodl.query.version.version3', 'vmodl.query.version.version2')
AddVersionParent('vmodl.query.version.version3', 'vmodl.query.version.version3')
AddVersionParent('vmodl.query.version.version3', 'vmodl.version.version0')
AddVersionParent('vmodl.query.version.version3', 'vmodl.version.version1')
AddVersionParent('vmodl.version.version0', 'vmodl.version.version0')
AddVersionParent('vmodl.version.version1', 'vmodl.version.version0')
AddVersionParent('vmodl.version.version1', 'vmodl.version.version1')
CreateDataType('sms.AboutInfo', 'SmsAboutInfo', 'vmodl.DynamicData', 'sms.version.version2', [('name', 'string', 'sms.version.version2', 0), ('fullName', 'string', 'sms.version.version2', 0), ('vendor', 'string', 'sms.version.version2', 0), ('apiVersion', 'string', 'sms.version.version2', 0), ('instanceUuid', 'string', 'sms.version.version2', 0), ('vasaApiVersion', 'string', 'sms.version.version4', F_OPTIONAL)])
CreateDataType('sms.DbConnectionSpec', 'DbConnectionSpec', 'vmodl.DynamicData', 'sms.version.version1', [('url', 'string', 'sms.version.version1', 0), ('username', 'string', 'sms.version.version1', 0), ('password', 'string', 'sms.version.version1', 0)])
CreateDataType('sms.EntityReference', 'EntityReference', 'vmodl.DynamicData', 'sms.version.version1', [('id', 'string', 'sms.version.version1', 0), ('type', 'sms.EntityReference.EntityType', 'sms.version.version1', F_OPTIONAL)])
CreateEnumType('sms.EntityReference.EntityType', 'EntityReferenceEntityType', 'sms.version.version1', ['datacenter', 'resourcePool', 'storagePod', 'cluster', 'vm', 'datastore', 'host', 'vmFile', 'scsiPath', 'scsiTarget', 'scsiVolume', 'scsiAdapter', 'nasMount'])
CreateDataType('sms.ResyncSpec', 'ResyncSpec', 'vmodl.DynamicData', 'sms.version.version4', None)
CreateManagedType('sms.ServiceInstance', 'SmsServiceInstance', 'vmodl.ManagedObject', 'sms.version.version1', None, [('queryList', 'QueryList', 'sms.version.version1', (('contextEntity',   'sms.EntityReference',   'sms.version.version1',   F_OPTIONAL,   None), ('queryEntityType',   'sms.EntityReference.EntityType',   'sms.version.version1',   0,   None), ('querySpec',   'sms.list.QuerySpec',   'sms.version.version1',   F_OPTIONAL,   None)), (0, 'sms.list.QueryResult', 'sms.list.QueryResult'), 'StorageViews.View', ['sms.fault.QueryExecutionFault', 'sms.fault.EntityNotFound']), ('queryTopology', 'QueryTopology', 'sms.version.version1', (('entity',   'sms.EntityReference',   'sms.version.version1',   0,   None),), (0, 'sms.topology.Map', 'sms.topology.Map'), 'StorageViews.View', ['sms.fault.QueryExecutionFault', 'sms.fault.EntityNotFound']), ('sync', 'Sync', 'sms.version.version1', (), (0, 'void', 'void'), 'StorageViews.View', ['sms.fault.ProviderSyncFailed', 'sms.fault.DbConfigFailed']), ('configureSyncInterval', 'ConfigureSyncInterval', 'sms.version.version1', (('interval',   'int',   'sms.version.version1',   0,   None),), (0, 'void', 'void'), 'StorageViews.ConfigureService', None), ('updateVcDbConnectionInfo', 'UpdateVcDbConnectionInfo', 'sms.version.version1', (('dbConnectionSpec',   'sms.DbConnectionSpec',   'sms.version.version1',   F_OPTIONAL,   None),), (0, 'void', 'void'), 'StorageViews.ConfigureService', None), ('queryStorageManager', 'QueryStorageManager', 'sms.version.version2', (), (0, 'sms.StorageManager', 'sms.StorageManager'), 'StorageViews.View', None), ('queryAboutInfo', 'QueryAboutInfo', 'sms.version.version2', (), (0, 'sms.AboutInfo', 'sms.AboutInfo'), 'StorageViews.View', None)])
CreateManagedType('sms.StorageManager', 'SmsStorageManager', 'vmodl.ManagedObject', 'sms.version.version2', None, [('registerProvider', 'RegisterProvider_Task', 'sms.version.version2', (('providerSpec',   'sms.provider.ProviderSpec',   'sms.version.version2',   0,   None),), (0, 'sms.Task', 'sms.provider.Provider'), 'StorageViews.ConfigureService', ['vim.fault.AlreadyExists', 'sms.fault.ProviderRegistrationFault']), ('unregisterProvider', 'UnregisterProvider_Task', 'sms.version.version2', (('providerId',   'string',   'sms.version.version2',   0,   None),), (0, 'sms.Task', 'void'), 'StorageViews.ConfigureService', ['vim.fault.NotFound', 'sms.fault.ProviderUnregistrationFault']), ('queryProvider', 'QueryProvider', 'sms.version.version2', (), (F_OPTIONAL, 'sms.provider.Provider[]', 'sms.provider.Provider[]'), 'StorageViews.View', ['sms.fault.QueryExecutionFault']), ('queryArray', 'QueryArray', 'sms.version.version2', (('providerId',   'string[]',   'sms.version.version2',   F_OPTIONAL,   None),), (F_OPTIONAL, 'sms.storage.StorageArray[]', 'sms.storage.StorageArray[]'), 'StorageViews.View', ['vim.fault.NotFound', 'sms.fault.QueryExecutionFault']), ('queryProcessorAssociatedWithArray', 'QueryProcessorAssociatedWithArray', 'sms.version.version2', (('arrayId',   'string',   'sms.version.version2',   0,   None),), (F_OPTIONAL, 'sms.storage.StorageProcessor[]', 'sms.storage.StorageProcessor[]'), 'StorageViews.View', ['vim.fault.NotFound', 'sms.fault.QueryExecutionFault']), ('queryPortAssociatedWithArray', 'QueryPortAssociatedWithArray', 'sms.version.version2', (('arrayId',   'string',   'sms.version.version2',   0,   None),), (F_OPTIONAL, 'sms.storage.StoragePort[]', 'sms.storage.StoragePort[]'), 'StorageViews.View', ['vim.fault.NotFound', 'sms.fault.QueryExecutionFault']), ('queryPortAssociatedWithLun', 'QueryPortAssociatedWithLun', 'sms.version.version2', (('scsi3Id',   'string',   'sms.version.version2',   0,   None), ('arrayId',   'string',   'sms.version.version2',   0,   None)), (F_OPTIONAL, 'sms.storage.StoragePort', 'sms.storage.StoragePort'), 'StorageViews.View', ['vim.fault.NotFound', 'sms.fault.QueryExecutionFault']), ('queryLunAssociatedWithPort', 'QueryLunAssociatedWithPort', 'sms.version.version2', (('portId',   'string',   'sms.version.version2',   0,   None), ('arrayId',   'string',   'sms.version.version2',   0,   None)), (F_OPTIONAL, 'sms.storage.StorageLun[]', 'sms.storage.StorageLun[]'), 'StorageViews.View', ['vim.fault.NotFound', 'sms.fault.QueryExecutionFault']), ('queryArrayAssociatedWithLun', 'QueryArrayAssociatedWithLun', 'sms.version.version2', (('canonicalName',   'string',   'sms.version.version2',   0,   None),), (F_OPTIONAL, 'sms.storage.StorageArray', 'sms.storage.StorageArray'), 'StorageViews.View', ['vim.fault.NotFound', 'sms.fault.QueryExecutionFault']), ('queryPortAssociatedWithProcessor', 'QueryPortAssociatedWithProcessor', 'sms.version.version2', (('processorId',   'string',   'sms.version.version2',   0,   None), ('arrayId',   'string',   'sms.version.version2',   0,   None)), (F_OPTIONAL, 'sms.storage.StoragePort[]', 'sms.storage.StoragePort[]'), 'StorageViews.View', ['vim.fault.NotFound', 'sms.fault.QueryExecutionFault']), ('queryLunAssociatedWithArray', 'QueryLunAssociatedWithArray', 'sms.version.version2', (('arrayId',   'string',   'sms.version.version2',   0,   None),), (F_OPTIONAL, 'sms.storage.StorageLun[]', 'sms.storage.StorageLun[]'), 'StorageViews.View', ['vim.fault.NotFound', 'sms.fault.QueryExecutionFault']), ('queryFileSystemAssociatedWithArray', 'QueryFileSystemAssociatedWithArray', 'sms.version.version2', (('arrayId',   'string',   'sms.version.version2',   0,   None),), (F_OPTIONAL, 'sms.storage.StorageFileSystem[]', 'sms.storage.StorageFileSystem[]'), 'StorageViews.View', ['vim.fault.NotFound', 'sms.fault.QueryExecutionFault']), ('queryDatastoreCapability', 'QueryDatastoreCapability', 'sms.version.version2', (('datastore',   'vim.Datastore',   'sms.version.version2',   0,   None),), (F_OPTIONAL, 'sms.storage.StorageCapability', 'sms.storage.StorageCapability'), 'StorageViews.View', ['vim.fault.NotFound', 'sms.fault.QueryExecutionFault']), ('queryHostAssociatedWithLun', 'QueryHostAssociatedWithLun', 'sms.version.version2', (('scsi3Id',   'string',   'sms.version.version2',   0,   None), ('arrayId',   'string',   'sms.version.version2',   0,   None)), (F_OPTIONAL, 'vim.HostSystem[]', 'vim.HostSystem[]'), 'StorageViews.View', ['vim.fault.NotFound', 'sms.fault.QueryExecutionFault']), ('queryVmfsDatastoreAssociatedWithLun', 'QueryVmfsDatastoreAssociatedWithLun', 'sms.version.version2', (('scsi3Id',   'string',   'sms.version.version2',   0,   None), ('arrayId',   'string',   'sms.version.version2',   0,   None)), (F_OPTIONAL, 'vim.Datastore', 'vim.Datastore'), 'StorageViews.View', ['vim.fault.NotFound', 'sms.fault.QueryExecutionFault']), ('queryNfsDatastoreAssociatedWithFileSystem', 'QueryNfsDatastoreAssociatedWithFileSystem', 'sms.version.version2', (('fileSystemId',   'string',   'sms.version.version2',   0,   None), ('arrayId',   'string',   'sms.version.version2',   0,   None)), (F_OPTIONAL, 'vim.Datastore', 'vim.Datastore'), 'StorageViews.View', ['vim.fault.NotFound', 'sms.fault.QueryExecutionFault']), ('queryDrsMigrationCapabilityForPerformance', 'QueryDrsMigrationCapabilityForPerformance', 'sms.version.version2', (('srcDatastore',   'vim.Datastore',   'sms.version.version2',   0,   None), ('dstDatastore',   'vim.Datastore',   'sms.version.version2',   0,   None)), (0, 'boolean', 'boolean'), 'StorageViews.View', ['vim.fault.NotFound', 'sms.fault.QueryExecutionFault']), ('queryDrsMigrationCapabilityForPerformanceEx', 'QueryDrsMigrationCapabilityForPerformanceEx', 'sms.version.version3', (('datastore',   'vim.Datastore[]',   'sms.version.version3',   0,   None),), (0, 'sms.storage.DrsMigrationCapabilityResult', 'sms.storage.DrsMigrationCapabilityResult'), 'StorageViews.View', ['vim.fault.NotFound', 'sms.fault.QueryExecutionFault']), ('queryProviderUuid', 'GetVasaProviderUuid', 'sms.version.version4', (('providerId',   'string',   'sms.version.version4',   0,   None),), (0, 'string', 'string'), 'StorageViews.View', ['vim.fault.NotFound', 'sms.fault.QueryExecutionFault']), ('resyncVsanProviders', 'ResyncVsanProviders_Task', 'sms.version.version4', (('resyncSpec',   'sms.ResyncSpec',   'sms.version.version4',   F_OPTIONAL,   None),), (0, 'sms.Task', 'void'), 'StorageViews.ConfigureService', ['sms.fault.VsanProvidersResyncFailed'])])
CreateManagedType('sms.Task', 'SmsTask', 'vmodl.ManagedObject', 'sms.version.version2', None, [('queryResult', 'QuerySmsTaskResult', 'sms.version.version2', (), (F_OPTIONAL, 'anyType', 'anyType'), 'StorageViews.View', None), ('queryInfo', 'QuerySmsTaskInfo', 'sms.version.version2', (), (0, 'sms.TaskInfo', 'sms.TaskInfo'), 'StorageViews.View', None)])
CreateDataType('sms.TaskInfo', 'SmsTaskInfo', 'vmodl.DynamicData', 'sms.version.version2', [('key', 'string', 'sms.version.version2', 0), ('task', 'sms.Task', 'sms.version.version2', 0), ('object', 'vmodl.ManagedObject', 'sms.version.version2', F_OPTIONAL), ('error', 'vmodl.MethodFault', 'sms.version.version2', F_OPTIONAL), ('result', 'anyType', 'sms.version.version2', F_OPTIONAL), ('startTime', 'vmodl.DateTime', 'sms.version.version2', F_OPTIONAL), ('completionTime', 'vmodl.DateTime', 'sms.version.version2', F_OPTIONAL), ('state', 'string', 'sms.version.version2', 0), ('progress', 'int', 'sms.version.version2', F_OPTIONAL)])
CreateEnumType('sms.TaskInfo.State', 'SmsTaskState', 'sms.version.version1', ['running', 'success', 'error'])
CreateDataType('sms.fault.AuthConnectionFailed', 'AuthConnectionFailed', 'vim.fault.NoPermission', 'sms.version.version2', None)
CreateDataType('sms.fault.DbConfigFailed', 'DbConfigFailed', 'vmodl.MethodFault', 'sms.version.version1', None)
CreateDataType('sms.fault.EntityNotFound', 'EntityNotFound', 'vmodl.MethodFault', 'sms.version.version1', [('entity', 'sms.EntityReference', 'sms.version.version1', 0)])
CreateDataType('sms.fault.InvalidSession', 'InvalidSession', 'vim.fault.NoPermission', 'sms.version.version2', [('sessionCookie', 'string', 'sms.version.version2', 0)])
CreateDataType('sms.fault.MultipleSortSpecsNotSupported', 'MultipleSortSpecsNotSupported', 'vmodl.fault.InvalidArgument', 'sms.version.version1', None)
CreateDataType('sms.fault.ProviderConnectionFailed', 'ProviderConnectionFailed', 'vmodl.RuntimeFault', 'sms.version.version2', None)
CreateDataType('sms.fault.ProviderRegistrationFault', 'ProviderRegistrationFault', 'vmodl.MethodFault', 'sms.version.version2', None)
CreateDataType('sms.fault.ProviderSyncFailed', 'ProviderSyncFailed', 'vmodl.MethodFault', 'sms.version.version1', None)
CreateDataType('sms.fault.ProviderUnregistrationFault', 'ProviderUnregistrationFault', 'vmodl.MethodFault', 'sms.version.version2', None)
CreateDataType('sms.fault.ProxyRegistrationFailed', 'ProxyRegistrationFailed', 'vmodl.RuntimeFault', 'sms.version.version1', None)
CreateDataType('sms.fault.QueryExecutionFault', 'QueryExecutionFault', 'vmodl.MethodFault', 'sms.version.version1', None)
CreateDataType('sms.fault.QueryNotSupported', 'QueryNotSupported', 'vmodl.fault.InvalidArgument', 'sms.version.version1', [('entityType', 'sms.EntityReference.EntityType', 'sms.version.version1', F_OPTIONAL), ('relatedEntityType', 'sms.EntityReference.EntityType', 'sms.version.version1', 0)])
CreateDataType('sms.fault.ServiceNotInitialized', 'ServiceNotInitialized', 'vmodl.RuntimeFault', 'sms.version.version1', None)
CreateDataType('sms.fault.SyncInProgress', 'SyncInProgress', 'sms.fault.ProviderSyncFailed', 'sms.version.version1', None)
CreateDataType('sms.fault.VsanProvidersResyncFailed', 'VsanProvidersResyncFailed', 'vmodl.MethodFault', 'sms.version.version4', [('providerUrl', 'string[]', 'sms.version.version4', 0)])
CreateDataType('sms.list.FilterSpec', 'FilterSpec', 'vmodl.DynamicData', 'sms.version.version1', [('constraint', 'sms.list.FilterSpec.Constraint', 'sms.version.version1', 0)])
CreateEnumType('sms.list.FilterSpec.ComparisonOperator', 'FilterSpecComparisonOperator', 'sms.version.version1', ['equal', 'notEqual', 'greaterThanOrEqual', 'lessThanOrEqual', 'contains', 'notContains', 'beginsWith', 'endsWith'])
CreateEnumType('sms.list.FilterSpec.LogicalOperator', 'FilterSpecLogicalOperator', 'sms.version.version1', ['logicalOr', 'logicalAnd'])
CreateDataType('sms.list.FilterSpec.Constraint', 'FilterSpecConstraint', 'vmodl.DynamicData', 'sms.version.version1', [('propertyName', 'string', 'sms.version.version1', F_OPTIONAL), ('propertyValue', 'string', 'sms.version.version1', F_OPTIONAL), ('comparisonOperator', 'sms.list.FilterSpec.ComparisonOperator', 'sms.version.version1', F_OPTIONAL), ('childConstraint', 'sms.list.FilterSpec.Constraint[]', 'sms.version.version1', F_OPTIONAL), ('childConstraintLogicalOperator', 'sms.list.FilterSpec.LogicalOperator', 'sms.version.version1', F_OPTIONAL)])
CreateDataType('sms.list.Metadata', 'Metadata', 'vmodl.DynamicData', 'sms.version.version1', [('numRows', 'int', 'sms.version.version1', 0), ('totalRows', 'int', 'sms.version.version1', 0), ('lastUpdateTime', 'vmodl.DateTime', 'sms.version.version1', F_OPTIONAL), ('propertyName', 'string[]', 'sms.version.version1', F_OPTIONAL)])
CreateDataType('sms.list.QueryResult', 'QueryResult', 'vmodl.DynamicData', 'sms.version.version1', [('row', 'sms.list.RowData[]', 'sms.version.version1', F_OPTIONAL), ('metadata', 'sms.list.Metadata', 'sms.version.version1', 0)])
CreateDataType('sms.list.QuerySpec', 'QuerySpec', 'vmodl.DynamicData', 'sms.version.version1', [('maxCount', 'int', 'sms.version.version1', 0), ('offset', 'int', 'sms.version.version1', 0), ('filterSpec', 'sms.list.FilterSpec', 'sms.version.version1', F_OPTIONAL), ('sortSpec', 'sms.list.SortSpec[]', 'sms.version.version1', F_OPTIONAL)])
CreateDataType('sms.list.RowData', 'RowData', 'vmodl.DynamicData', 'sms.version.version1', [('column', 'string[]', 'sms.version.version1', 0)])
CreateDataType('sms.list.SortSpec', 'SortSpec', 'vmodl.DynamicData', 'sms.version.version1', [('propertyName', 'string', 'sms.version.version1', 0), ('ascending', 'boolean', 'sms.version.version1', 0)])
CreateManagedType('sms.provider.Provider', 'SmsProvider', 'vmodl.ManagedObject', 'sms.version.version2', None, [('queryProviderInfo', 'QueryProviderInfo', 'sms.version.version2', (), (0, 'sms.provider.ProviderInfo', 'sms.provider.ProviderInfo'), 'StorageViews.View', None)])
CreateDataType('sms.provider.ProviderInfo', 'SmsProviderInfo', 'vmodl.DynamicData', 'sms.version.version2', [('uid', 'string', 'sms.version.version2', 0), ('name', 'string', 'sms.version.version2', 0), ('description', 'string', 'sms.version.version2', F_OPTIONAL), ('version', 'string', 'sms.version.version2', F_OPTIONAL)])
CreateDataType('sms.provider.ProviderSpec', 'SmsProviderSpec', 'vmodl.DynamicData', 'sms.version.version2', [('name', 'string', 'sms.version.version2', 0), ('description', 'string', 'sms.version.version2', F_OPTIONAL)])
CreateManagedType('sms.provider.VasaProvider', 'VasaProvider', 'sms.provider.Provider', 'sms.version.version2', None, [('sync', 'VasaProviderSync_Task', 'sms.version.version2', (('arrayId',   'string',   'sms.version.version2',   F_OPTIONAL,   None),), (0, 'sms.Task', 'void'), 'StorageViews.View', ['sms.fault.ProviderSyncFailed'])])
CreateDataType('sms.provider.VasaProviderInfo', 'VasaProviderInfo', 'sms.provider.ProviderInfo', 'sms.version.version2', [('url', 'string', 'sms.version.version2', 0), ('certificate', 'string', 'sms.version.version2', F_OPTIONAL), ('status', 'string', 'sms.version.version2', F_OPTIONAL), ('vasaVersion', 'string', 'sms.version.version2', F_OPTIONAL), ('namespace', 'string', 'sms.version.version2', F_OPTIONAL), ('lastSyncTime', 'string', 'sms.version.version2', F_OPTIONAL), ('supportedVendorModelMapping', 'sms.provider.VasaProviderInfo.SupportedVendorModelMapping[]', 'sms.version.version2', F_OPTIONAL), ('supportedProfile', 'string[]', 'sms.version.version2', F_OPTIONAL), ('supportedProviderProfile', 'string[]', 'sms.version.version4', F_OPTIONAL), ('relatedStorageArray', 'sms.provider.VasaProviderInfo.RelatedStorageArray[]', 'sms.version.version4', F_OPTIONAL), ('providerId', 'string', 'sms.version.version4', F_OPTIONAL)])
CreateDataType('sms.provider.VasaProviderInfo.RelatedStorageArray', 'RelatedStorageArray', 'vmodl.DynamicData', 'sms.version.version4', [('arrayId', 'string', 'sms.version.version4', 0), ('active', 'boolean', 'sms.version.version4', 0), ('manageable', 'boolean', 'sms.version.version4', 0), ('priority', 'int', 'sms.version.version4', 0)])
CreateDataType('sms.provider.VasaProviderInfo.SupportedVendorModelMapping', 'SupportedVendorModelMapping', 'vmodl.DynamicData', 'sms.version.version1', [('vendorId', 'string', 'sms.version.version1', F_OPTIONAL), ('modelId', 'string', 'sms.version.version1', F_OPTIONAL)])
CreateEnumType('sms.provider.VasaProviderInfo.VasaProviderStatus', 'VasaProviderStatus', 'sms.version.version1', ['online', 'offline', 'syncError', 'unknown'])
CreateEnumType('sms.provider.VasaProviderInfo.VasaProviderProfile', 'VasaProviderProfile', 'sms.version.version1', ['blockDevice', 'fileSystem', 'capability'])
CreateDataType('sms.provider.VasaProviderSpec', 'VasaProviderSpec', 'sms.provider.ProviderSpec', 'sms.version.version2', [('username', 'string', 'sms.version.version2', 0), ('password', 'string', 'sms.version.version2', 0), ('url', 'string', 'sms.version.version2', 0), ('certificate', 'string', 'sms.version.version2', F_OPTIONAL)])
CreateDataType('sms.storage.DatastorePair', 'DatastorePair', 'vmodl.DynamicData', 'sms.version.version3', [('datastore1', 'vim.Datastore', 'sms.version.version3', 0), ('datastore2', 'vim.Datastore', 'sms.version.version3', 0)])
CreateDataType('sms.storage.DrsMigrationCapabilityResult', 'DrsMigrationCapabilityResult', 'vmodl.DynamicData', 'sms.version.version3', [('recommendedDatastorePair', 'sms.storage.DatastorePair[]', 'sms.version.version3', F_OPTIONAL), ('nonRecommendedDatastorePair', 'sms.storage.DatastorePair[]', 'sms.version.version3', F_OPTIONAL)])
CreateDataType('sms.storage.FileSystemInfo', 'StorageFileSystemInfo', 'vmodl.DynamicData', 'sms.version.version2', [('fileServerName', 'string', 'sms.version.version2', 0), ('fileSystemPath', 'string', 'sms.version.version2', 0), ('ipAddress', 'string', 'sms.version.version2', F_OPTIONAL)])
CreateDataType('sms.storage.LunHbaAssociation', 'LunHbaAssociation', 'vmodl.DynamicData', 'sms.version.version2', [('canonicalName', 'string', 'sms.version.version2', 0), ('hba', 'vim.host.HostBusAdapter[]', 'sms.version.version2', 0)])
CreateDataType('sms.storage.StorageArray', 'StorageArray', 'vmodl.DynamicData', 'sms.version.version2', [('name', 'string', 'sms.version.version2', 0), ('uuid', 'string', 'sms.version.version2', 0), ('vendorId', 'string', 'sms.version.version2', 0), ('modelId', 'string', 'sms.version.version2', 0), ('firmware', 'string', 'sms.version.version2', F_OPTIONAL), ('alternateName', 'string[]', 'sms.version.version2', F_OPTIONAL), ('supportedBlockInterface', 'string[]', 'sms.version.version2', F_OPTIONAL), ('supportedFileSystemInterface', 'string[]', 'sms.version.version2', F_OPTIONAL), ('supportedProfile', 'string[]', 'sms.version.version3', F_OPTIONAL), ('priority', 'int', 'sms.version.version4', F_OPTIONAL)])
CreateEnumType('sms.storage.StorageArray.BlockDeviceInterface', 'BlockDeviceInterface', 'sms.version.version1', ['fc', 'iscsi', 'fcoe', 'otherBlock'])
CreateEnumType('sms.storage.StorageArray.FileSystemInterface', 'FileSystemInterface', 'sms.version.version1', ['nfs', 'otherFileSystem'])
CreateEnumType('sms.storage.StorageArray.VasaProfile', 'VasaProfile', 'sms.version.version3', ['blockDevice', 'fileSystem', 'capability', 'policy', 'object'])
CreateDataType('sms.storage.StorageCapability', 'StorageCapability', 'vmodl.DynamicData', 'sms.version.version2', [('uuid', 'string', 'sms.version.version2', 0), ('name', 'string', 'sms.version.version2', 0), ('description', 'string', 'sms.version.version2', 0)])
CreateDataType('sms.storage.StorageFileSystem', 'StorageFileSystem', 'vmodl.DynamicData', 'sms.version.version2', [('uuid', 'string', 'sms.version.version2', 0), ('info', 'sms.storage.FileSystemInfo[]', 'sms.version.version2', 0), ('nativeSnapshotSupported', 'boolean', 'sms.version.version2', 0), ('thinProvisioningStatus', 'string', 'sms.version.version2', 0), ('type', 'string', 'sms.version.version2', 0), ('version', 'string', 'sms.version.version2', 0)])
CreateEnumType('sms.storage.StorageFileSystem.FileSystemInterfaceVersion', 'FileSystemInterfaceVersion', 'sms.version.version1', ['NFSV3_0'])
CreateDataType('sms.storage.StorageLun', 'StorageLun', 'vmodl.DynamicData', 'sms.version.version2', [('uuid', 'string', 'sms.version.version2', 0), ('vSphereLunIdentifier', 'string', 'sms.version.version2', 0), ('vendorDisplayName', 'string', 'sms.version.version2', 0), ('capacityInMB', 'long', 'sms.version.version2', 0), ('usedSpaceInMB', 'long', 'sms.version.version2', 0), ('lunThinProvisioned', 'boolean', 'sms.version.version2', 0), ('alternateIdentifier', 'string[]', 'sms.version.version2', F_OPTIONAL), ('drsManagementPermitted', 'boolean', 'sms.version.version2', 0), ('thinProvisioningStatus', 'string', 'sms.version.version2', 0)])
CreateDataType('sms.storage.StoragePort', 'StoragePort', 'vmodl.DynamicData', 'sms.version.version2', [('uuid', 'string', 'sms.version.version2', 0), ('type', 'string', 'sms.version.version2', 0), ('alternateName', 'string[]', 'sms.version.version2', F_OPTIONAL)])
CreateDataType('sms.storage.StorageProcessor', 'StorageProcessor', 'vmodl.DynamicData', 'sms.version.version2', [('uuid', 'string', 'sms.version.version2', 0), ('alternateIdentifer', 'string[]', 'sms.version.version2', F_OPTIONAL)])
CreateEnumType('sms.storage.ThinProvisioningStatus', 'ThinProvisioningStatus', 'sms.version.version2', ['RED', 'YELLOW', 'GREEN'])
CreateDataType('sms.topology.Edge', 'Edge', 'vmodl.DynamicData', 'sms.version.version1', [('sourceEntity', 'sms.EntityReference', 'sms.version.version1', 0), ('destEntity', 'sms.EntityReference', 'sms.version.version1', 0), ('status', 'sms.topology.Edge.Status', 'sms.version.version1', 0), ('direct', 'boolean', 'sms.version.version1', 0)])
CreateEnumType('sms.topology.Edge.Status', 'EdgeStatus', 'sms.version.version1', ['up', 'degraded', 'down', 'unknown', 'notReported'])
CreateDataType('sms.topology.Map', 'Map', 'vmodl.DynamicData', 'sms.version.version1', [('node', 'sms.topology.Node[]', 'sms.version.version1', F_OPTIONAL), ('edge', 'sms.topology.Edge[]', 'sms.version.version1', F_OPTIONAL), ('lastUpdateTime', 'vmodl.DateTime', 'sms.version.version1', F_OPTIONAL)])
CreateDataType('sms.topology.Node', 'Node', 'vmodl.DynamicData', 'sms.version.version1', [('entity', 'sms.EntityReference', 'sms.version.version1', 0), ('name', 'string', 'sms.version.version1', 0), ('status', 'sms.topology.Node.Status', 'sms.version.version1', 0), ('property', 'sms.topology.NodeProperty[]', 'sms.version.version1', F_OPTIONAL)])
CreateEnumType('sms.topology.Node.Status', 'NodeStatus', 'sms.version.version1', ['up', 'degraded', 'down', 'unknown', 'notReported'])
CreateDataType('sms.topology.NodeProperty', 'NodeProperty', 'vmodl.DynamicData', 'sms.version.version1', [('name', 'string', 'sms.version.version1', 0), ('value', 'string', 'sms.version.version1', F_OPTIONAL)])
CreateDataType('sms.fault.CertificateNotTrusted', 'CertificateNotTrusted', 'sms.fault.ProviderRegistrationFault', 'sms.version.version2', [('certificate', 'string', 'sms.version.version2', 0)])
CreateDataType('sms.fault.IncorrectUsernamePassword', 'IncorrectUsernamePassword', 'sms.fault.ProviderRegistrationFault', 'sms.version.version2', None)
CreateDataType('sms.fault.InvalidCertificate', 'InvalidCertificate', 'sms.fault.ProviderRegistrationFault', 'sms.version.version4', [('certificate', 'string', 'sms.version.version4', 0)])
CreateDataType('sms.fault.InvalidUrl', 'InvalidUrl', 'sms.fault.ProviderRegistrationFault', 'sms.version.version4', [('url', 'string', 'sms.version.version4', 0)])
CreateDataType('sms.fault.NoCommonProviderForAllBackings', 'NoCommonProviderForAllBackings', 'sms.fault.QueryExecutionFault', 'sms.version.version2', None)
CreateDataType('sms.fault.ProviderNotFound', 'ProviderNotFound', 'sms.fault.QueryExecutionFault', 'sms.version.version2', None)
CreateDataType('sms.storage.FcStoragePort', 'FcStoragePort', 'sms.storage.StoragePort', 'sms.version.version2', [('portWwn', 'string', 'sms.version.version2', 0), ('nodeWwn', 'string', 'sms.version.version2', 0)])
CreateDataType('sms.storage.FcoeStoragePort', 'FcoeStoragePort', 'sms.storage.StoragePort', 'sms.version.version2', [('portWwn', 'string', 'sms.version.version2', 0), ('nodeWwn', 'string', 'sms.version.version2', 0)])
CreateDataType('sms.storage.IscsiStoragePort', 'IscsiStoragePort', 'sms.storage.StoragePort', 'sms.version.version2', [('identifier', 'string', 'sms.version.version2', 0)])