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
"""Auto-generated from spec: urn:broadband-forum-org:tr-104-1-1."""

import core
from tr104_v1_0 import VoiceService_v1_0


class VoiceService_v1_1(VoiceService_v1_0):
  """Represents VoiceService_v1_1."""

  def __init__(self, **defaults):
    VoiceService_v1_0.__init__(self, defaults=defaults)
    self.Export(lists=['VoiceService'])

  class VoiceService(VoiceService_v1_0.VoiceService):
    """Represents VoiceService_v1_1.VoiceService.{i}."""

    def __init__(self, **defaults):
      VoiceService_v1_0.VoiceService.__init__(self, defaults=defaults)
      self.Export(params=['Alias'],
                  objects=['Capabilities'],
                  lists=['PhyInterface',
                         'VoiceProfile'])

    class Capabilities(VoiceService_v1_0.VoiceService.Capabilities):
      """Represents VoiceService_v1_1.VoiceService.{i}.Capabilities."""

      def __init__(self, **defaults):
        VoiceService_v1_0.VoiceService.Capabilities.__init__(self, defaults=defaults)
        self.Export(lists=['Codecs'])

      class Codecs(VoiceService_v1_0.VoiceService.Capabilities.Codecs):
        """Represents VoiceService_v1_1.VoiceService.{i}.Capabilities.Codecs.{i}."""

        def __init__(self, **defaults):
          VoiceService_v1_0.VoiceService.Capabilities.Codecs.__init__(self, defaults=defaults)
          self.Export(params=['Alias'])

    class PhyInterface(VoiceService_v1_0.VoiceService.PhyInterface):
      """Represents VoiceService_v1_1.VoiceService.{i}.PhyInterface.{i}."""

      def __init__(self, **defaults):
        VoiceService_v1_0.VoiceService.PhyInterface.__init__(self, defaults=defaults)
        self.Export(params=['Alias'])

    class VoiceProfile(VoiceService_v1_0.VoiceService.VoiceProfile):
      """Represents VoiceService_v1_1.VoiceService.{i}.VoiceProfile.{i}."""

      def __init__(self, **defaults):
        VoiceService_v1_0.VoiceService.VoiceProfile.__init__(self, defaults=defaults)
        self.Export(params=['Alias'],
                    objects=['ButtonMap',
                             'NumberingPlan',
                             'SIP',
                             'Tone'],
                    lists=['Line'])

      class ButtonMap(VoiceService_v1_0.VoiceService.VoiceProfile.ButtonMap):
        """Represents VoiceService_v1_1.VoiceService.{i}.VoiceProfile.{i}.ButtonMap."""

        def __init__(self, **defaults):
          VoiceService_v1_0.VoiceService.VoiceProfile.ButtonMap.__init__(self, defaults=defaults)
          self.Export(lists=['Button'])

        class Button(VoiceService_v1_0.VoiceService.VoiceProfile.ButtonMap.Button):
          """Represents VoiceService_v1_1.VoiceService.{i}.VoiceProfile.{i}.ButtonMap.Button.{i}."""

          def __init__(self, **defaults):
            VoiceService_v1_0.VoiceService.VoiceProfile.ButtonMap.Button.__init__(self, defaults=defaults)
            self.Export(params=['Alias'])

      class Line(VoiceService_v1_0.VoiceService.VoiceProfile.Line):
        """Represents VoiceService_v1_1.VoiceService.{i}.VoiceProfile.{i}.Line.{i}."""

        def __init__(self, **defaults):
          VoiceService_v1_0.VoiceService.VoiceProfile.Line.__init__(self, defaults=defaults)
          self.Export(params=['Alias'],
                      objects=['Codec',
                               'Ringer',
                               'SIP'])

        class Codec(VoiceService_v1_0.VoiceService.VoiceProfile.Line.Codec):
          """Represents VoiceService_v1_1.VoiceService.{i}.VoiceProfile.{i}.Line.{i}.Codec."""

          def __init__(self, **defaults):
            VoiceService_v1_0.VoiceService.VoiceProfile.Line.Codec.__init__(self, defaults=defaults)
            self.Export(lists=['List'])

          class List(VoiceService_v1_0.VoiceService.VoiceProfile.Line.Codec.List):
            """Represents VoiceService_v1_1.VoiceService.{i}.VoiceProfile.{i}.Line.{i}.Codec.List.{i}."""

            def __init__(self, **defaults):
              VoiceService_v1_0.VoiceService.VoiceProfile.Line.Codec.List.__init__(self, defaults=defaults)
              self.Export(params=['Alias'])

        class Ringer(VoiceService_v1_0.VoiceService.VoiceProfile.Line.Ringer):
          """Represents VoiceService_v1_1.VoiceService.{i}.VoiceProfile.{i}.Line.{i}.Ringer."""

          def __init__(self, **defaults):
            VoiceService_v1_0.VoiceService.VoiceProfile.Line.Ringer.__init__(self, defaults=defaults)
            self.Export(lists=['Description',
                               'Event',
                               'Pattern'])

          class Description(VoiceService_v1_0.VoiceService.VoiceProfile.Line.Ringer.Description):
            """Represents VoiceService_v1_1.VoiceService.{i}.VoiceProfile.{i}.Line.{i}.Ringer.Description.{i}."""

            def __init__(self, **defaults):
              VoiceService_v1_0.VoiceService.VoiceProfile.Line.Ringer.Description.__init__(self, defaults=defaults)
              self.Export(params=['Alias'])

          class Event(VoiceService_v1_0.VoiceService.VoiceProfile.Line.Ringer.Event):
            """Represents VoiceService_v1_1.VoiceService.{i}.VoiceProfile.{i}.Line.{i}.Ringer.Event.{i}."""

            def __init__(self, **defaults):
              VoiceService_v1_0.VoiceService.VoiceProfile.Line.Ringer.Event.__init__(self, defaults=defaults)
              self.Export(params=['Alias'])

          class Pattern(VoiceService_v1_0.VoiceService.VoiceProfile.Line.Ringer.Pattern):
            """Represents VoiceService_v1_1.VoiceService.{i}.VoiceProfile.{i}.Line.{i}.Ringer.Pattern.{i}."""

            def __init__(self, **defaults):
              VoiceService_v1_0.VoiceService.VoiceProfile.Line.Ringer.Pattern.__init__(self, defaults=defaults)
              self.Export(params=['Alias'])

        class SIP(VoiceService_v1_0.VoiceService.VoiceProfile.Line.SIP):
          """Represents VoiceService_v1_1.VoiceService.{i}.VoiceProfile.{i}.Line.{i}.SIP."""

          def __init__(self, **defaults):
            VoiceService_v1_0.VoiceService.VoiceProfile.Line.SIP.__init__(self, defaults=defaults)
            self.Export(lists=['EventSubscribe'])

          class EventSubscribe(VoiceService_v1_0.VoiceService.VoiceProfile.Line.SIP.EventSubscribe):
            """Represents VoiceService_v1_1.VoiceService.{i}.VoiceProfile.{i}.Line.{i}.SIP.EventSubscribe.{i}."""

            def __init__(self, **defaults):
              VoiceService_v1_0.VoiceService.VoiceProfile.Line.SIP.EventSubscribe.__init__(self, defaults=defaults)
              self.Export(params=['Alias'])

      class NumberingPlan(VoiceService_v1_0.VoiceService.VoiceProfile.NumberingPlan):
        """Represents VoiceService_v1_1.VoiceService.{i}.VoiceProfile.{i}.NumberingPlan."""

        def __init__(self, **defaults):
          VoiceService_v1_0.VoiceService.VoiceProfile.NumberingPlan.__init__(self, defaults=defaults)
          self.Export(lists=['PrefixInfo'])

        class PrefixInfo(VoiceService_v1_0.VoiceService.VoiceProfile.NumberingPlan.PrefixInfo):
          """Represents VoiceService_v1_1.VoiceService.{i}.VoiceProfile.{i}.NumberingPlan.PrefixInfo.{i}."""

          def __init__(self, **defaults):
            VoiceService_v1_0.VoiceService.VoiceProfile.NumberingPlan.PrefixInfo.__init__(self, defaults=defaults)
            self.Export(params=['Alias'])

      class SIP(VoiceService_v1_0.VoiceService.VoiceProfile.SIP):
        """Represents VoiceService_v1_1.VoiceService.{i}.VoiceProfile.{i}.SIP."""

        def __init__(self, **defaults):
          VoiceService_v1_0.VoiceService.VoiceProfile.SIP.__init__(self, defaults=defaults)
          self.Export(lists=['EventSubscribe',
                             'ResponseMap'])

        class EventSubscribe(VoiceService_v1_0.VoiceService.VoiceProfile.SIP.EventSubscribe):
          """Represents VoiceService_v1_1.VoiceService.{i}.VoiceProfile.{i}.SIP.EventSubscribe.{i}."""

          def __init__(self, **defaults):
            VoiceService_v1_0.VoiceService.VoiceProfile.SIP.EventSubscribe.__init__(self, defaults=defaults)
            self.Export(params=['Alias'])

        class ResponseMap(VoiceService_v1_0.VoiceService.VoiceProfile.SIP.ResponseMap):
          """Represents VoiceService_v1_1.VoiceService.{i}.VoiceProfile.{i}.SIP.ResponseMap.{i}."""

          def __init__(self, **defaults):
            VoiceService_v1_0.VoiceService.VoiceProfile.SIP.ResponseMap.__init__(self, defaults=defaults)
            self.Export(params=['Alias'])

      class Tone(VoiceService_v1_0.VoiceService.VoiceProfile.Tone):
        """Represents VoiceService_v1_1.VoiceService.{i}.VoiceProfile.{i}.Tone."""

        def __init__(self, **defaults):
          VoiceService_v1_0.VoiceService.VoiceProfile.Tone.__init__(self, defaults=defaults)
          self.Export(lists=['Description',
                             'Event',
                             'Pattern'])

        class Description(VoiceService_v1_0.VoiceService.VoiceProfile.Tone.Description):
          """Represents VoiceService_v1_1.VoiceService.{i}.VoiceProfile.{i}.Tone.Description.{i}."""

          def __init__(self, **defaults):
            VoiceService_v1_0.VoiceService.VoiceProfile.Tone.Description.__init__(self, defaults=defaults)
            self.Export(params=['Alias'])

        class Event(VoiceService_v1_0.VoiceService.VoiceProfile.Tone.Event):
          """Represents VoiceService_v1_1.VoiceService.{i}.VoiceProfile.{i}.Tone.Event.{i}."""

          def __init__(self, **defaults):
            VoiceService_v1_0.VoiceService.VoiceProfile.Tone.Event.__init__(self, defaults=defaults)
            self.Export(params=['Alias'])

        class Pattern(VoiceService_v1_0.VoiceService.VoiceProfile.Tone.Pattern):
          """Represents VoiceService_v1_1.VoiceService.{i}.VoiceProfile.{i}.Tone.Pattern.{i}."""

          def __init__(self, **defaults):
            VoiceService_v1_0.VoiceService.VoiceProfile.Tone.Pattern.__init__(self, defaults=defaults)
            self.Export(params=['Alias'])


if __name__ == '__main__':
  print core.DumpSchema(VoiceService_v1_1)
