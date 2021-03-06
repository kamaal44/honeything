#!/usr/bin/python
# Copyright 2011 Google Inc. All Rights Reserved.
#
# AUTO-GENERATED BY parse-schema.py
#
# DO NOT EDIT!!
#
#pylint: disable-msg=C6202
#pylint: disable-msg=C6409
#pylint: disable-msg=C6310
# These should not actually be necessary (bugs in gpylint?):
#pylint: disable-msg=E1101
#pylint: disable-msg=W0231
#
"""Auto-generated from spec: urn:broadband-forum-org:tr-181-1-1."""

import core
from tr157_v1_3 import Device_v1_7


class Device_v1_8(Device_v1_7):
  """Represents Device_v1_8."""

  def __init__(self, **defaults):
    Device_v1_7.__init__(self, defaults=defaults)
    self.Export(objects=['DeviceInfo',
                         'DownloadAvailability',
                         'LAN',
                         'ManagementServer',
                         'NSLookupDiagnostics',
                         'PeriodicStatistics',
                         'SoftwareModules',
                         'USBHosts'],
                lists=['SmartCardReader',
                       'User'])

  class DeviceInfo(Device_v1_7.DeviceInfo):
    """Represents Device_v1_8.DeviceInfo."""

    def __init__(self, **defaults):
      Device_v1_7.DeviceInfo.__init__(self, defaults=defaults)
      self.Export(objects=['ProxierInfo',
                           'TemperatureStatus'],
                  lists=['Processor',
                         'SupportedDataModel',
                         'VendorConfigFile',
                         'VendorLogFile'])

    class Processor(Device_v1_7.DeviceInfo.Processor):
      """Represents Device_v1_8.DeviceInfo.Processor.{i}."""

      def __init__(self, **defaults):
        Device_v1_7.DeviceInfo.Processor.__init__(self, defaults=defaults)
        self.Export(params=['Alias'])

    class ProxierInfo(core.Exporter):
      """Represents Device_v1_8.DeviceInfo.ProxierInfo."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['ManufacturerOUI',
                            'ProductClass',
                            'ProxyProtocol',
                            'SerialNumber'])

    class SupportedDataModel(Device_v1_7.DeviceInfo.SupportedDataModel):
      """Represents Device_v1_8.DeviceInfo.SupportedDataModel.{i}."""

      def __init__(self, **defaults):
        Device_v1_7.DeviceInfo.SupportedDataModel.__init__(self, defaults=defaults)
        self.Export(params=['Alias'])

    class TemperatureStatus(Device_v1_7.DeviceInfo.TemperatureStatus):
      """Represents Device_v1_8.DeviceInfo.TemperatureStatus."""

      def __init__(self, **defaults):
        Device_v1_7.DeviceInfo.TemperatureStatus.__init__(self, defaults=defaults)
        self.Export(lists=['TemperatureSensor'])

      class TemperatureSensor(Device_v1_7.DeviceInfo.TemperatureStatus.TemperatureSensor):
        """Represents Device_v1_8.DeviceInfo.TemperatureStatus.TemperatureSensor.{i}."""

        def __init__(self, **defaults):
          Device_v1_7.DeviceInfo.TemperatureStatus.TemperatureSensor.__init__(self, defaults=defaults)
          self.Export(params=['Alias'])

    class VendorConfigFile(Device_v1_7.DeviceInfo.VendorConfigFile):
      """Represents Device_v1_8.DeviceInfo.VendorConfigFile.{i}."""

      def __init__(self, **defaults):
        Device_v1_7.DeviceInfo.VendorConfigFile.__init__(self, defaults=defaults)
        self.Export(params=['Alias'])

    class VendorLogFile(Device_v1_7.DeviceInfo.VendorLogFile):
      """Represents Device_v1_8.DeviceInfo.VendorLogFile.{i}."""

      def __init__(self, **defaults):
        Device_v1_7.DeviceInfo.VendorLogFile.__init__(self, defaults=defaults)
        self.Export(params=['Alias'])

  class DownloadAvailability(Device_v1_7.DownloadAvailability):
    """Represents Device_v1_8.DownloadAvailability."""

    def __init__(self, **defaults):
      Device_v1_7.DownloadAvailability.__init__(self, defaults=defaults)
      self.Export(objects=['Announcement'])

    class Announcement(Device_v1_7.DownloadAvailability.Announcement):
      """Represents Device_v1_8.DownloadAvailability.Announcement."""

      def __init__(self, **defaults):
        Device_v1_7.DownloadAvailability.Announcement.__init__(self, defaults=defaults)
        self.Export(lists=['Group'])

      class Group(Device_v1_7.DownloadAvailability.Announcement.Group):
        """Represents Device_v1_8.DownloadAvailability.Announcement.Group.{i}."""

        def __init__(self, **defaults):
          Device_v1_7.DownloadAvailability.Announcement.Group.__init__(self, defaults=defaults)
          self.Export(params=['Alias'])

  class LAN(Device_v1_7.LAN):
    """Represents Device_v1_8.LAN."""

    def __init__(self, **defaults):
      Device_v1_7.LAN.__init__(self, defaults=defaults)
      self.Export(lists=['DHCPOption'])

    class DHCPOption(Device_v1_7.LAN.DHCPOption):
      """Represents Device_v1_8.LAN.DHCPOption.{i}."""

      def __init__(self, **defaults):
        Device_v1_7.LAN.DHCPOption.__init__(self, defaults=defaults)
        self.Export(params=['Alias'])

  class ManagementServer(Device_v1_7.ManagementServer):
    """Represents Device_v1_8.ManagementServer."""

    def __init__(self, **defaults):
      Device_v1_7.ManagementServer.__init__(self, defaults=defaults)
      self.Export(params=['AliasBasedAddressing',
                          'AutoCreateInstances',
                          'InstanceMode'])

  class NSLookupDiagnostics(Device_v1_7.NSLookupDiagnostics):
    """Represents Device_v1_8.NSLookupDiagnostics."""

    def __init__(self, **defaults):
      Device_v1_7.NSLookupDiagnostics.__init__(self, defaults=defaults)
      self.Export(params=['DiagnosticsState'])

  class PeriodicStatistics(Device_v1_7.PeriodicStatistics):
    """Represents Device_v1_8.PeriodicStatistics."""

    def __init__(self, **defaults):
      Device_v1_7.PeriodicStatistics.__init__(self, defaults=defaults)
      self.Export(lists=['SampleSet'])

    class SampleSet(Device_v1_7.PeriodicStatistics.SampleSet):
      """Represents Device_v1_8.PeriodicStatistics.SampleSet.{i}."""

      def __init__(self, **defaults):
        Device_v1_7.PeriodicStatistics.SampleSet.__init__(self, defaults=defaults)
        self.Export(params=['Alias'],
                    lists=['Parameter'])

      class Parameter(Device_v1_7.PeriodicStatistics.SampleSet.Parameter):
        """Represents Device_v1_8.PeriodicStatistics.SampleSet.{i}.Parameter.{i}."""

        def __init__(self, **defaults):
          Device_v1_7.PeriodicStatistics.SampleSet.Parameter.__init__(self, defaults=defaults)
          self.Export(params=['Alias'])

  class SmartCardReader(Device_v1_7.SmartCardReader):
    """Represents Device_v1_8.SmartCardReader.{i}."""

    def __init__(self, **defaults):
      Device_v1_7.SmartCardReader.__init__(self, defaults=defaults)
      self.Export(params=['Alias'])

  class SoftwareModules(Device_v1_7.SoftwareModules):
    """Represents Device_v1_8.SoftwareModules."""

    def __init__(self, **defaults):
      Device_v1_7.SoftwareModules.__init__(self, defaults=defaults)
      self.Export(lists=['DeploymentUnit',
                         'ExecEnv',
                         'ExecutionUnit'])

    class DeploymentUnit(Device_v1_7.SoftwareModules.DeploymentUnit):
      """Represents Device_v1_8.SoftwareModules.DeploymentUnit.{i}."""

      def __init__(self, **defaults):
        Device_v1_7.SoftwareModules.DeploymentUnit.__init__(self, defaults=defaults)
        self.Export(params=['Alias'])

    class ExecEnv(Device_v1_7.SoftwareModules.ExecEnv):
      """Represents Device_v1_8.SoftwareModules.ExecEnv.{i}."""

      def __init__(self, **defaults):
        Device_v1_7.SoftwareModules.ExecEnv.__init__(self, defaults=defaults)
        self.Export(params=['Alias'])

    class ExecutionUnit(Device_v1_7.SoftwareModules.ExecutionUnit):
      """Represents Device_v1_8.SoftwareModules.ExecutionUnit.{i}."""

      def __init__(self, **defaults):
        Device_v1_7.SoftwareModules.ExecutionUnit.__init__(self, defaults=defaults)
        self.Export(params=['Alias'])

  class USBHosts(Device_v1_7.USBHosts):
    """Represents Device_v1_8.USBHosts."""

    def __init__(self, **defaults):
      Device_v1_7.USBHosts.__init__(self, defaults=defaults)
      self.Export(lists=['Host'])

    class Host(Device_v1_7.USBHosts.Host):
      """Represents Device_v1_8.USBHosts.Host.{i}."""

      def __init__(self, **defaults):
        Device_v1_7.USBHosts.Host.__init__(self, defaults=defaults)
        self.Export(params=['Alias'])

  class User(Device_v1_7.User):
    """Represents Device_v1_8.User.{i}."""

    def __init__(self, **defaults):
      Device_v1_7.User.__init__(self, defaults=defaults)
      self.Export(params=['Alias'])


if __name__ == '__main__':
  print core.DumpSchema(Device_v1_8)
