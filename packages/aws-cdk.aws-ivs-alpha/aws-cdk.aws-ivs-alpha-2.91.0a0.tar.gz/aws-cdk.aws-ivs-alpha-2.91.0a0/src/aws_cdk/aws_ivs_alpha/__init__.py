'''
# AWS::IVS Construct Library

<!--BEGIN STABILITY BANNER-->---


![cdk-constructs: Experimental](https://img.shields.io/badge/cdk--constructs-experimental-important.svg?style=for-the-badge)

> The APIs of higher level constructs in this module are experimental and under active development.
> They are subject to non-backward compatible changes or removal in any future version. These are
> not subject to the [Semantic Versioning](https://semver.org/) model and breaking changes will be
> announced in the release notes. This means that while you may use them, you may need to update
> your source code when upgrading to a newer version of this package.

---
<!--END STABILITY BANNER-->

Amazon Interactive Video Service (Amazon IVS) is a managed live streaming
solution that is quick and easy to set up, and ideal for creating interactive
video experiences. Send your live streams to Amazon IVS using streaming software
and the service does everything you need to make low-latency live video
available to any viewer around the world, letting you focus on building
interactive experiences alongside the live video. You can easily customize and
enhance the audience experience through the Amazon IVS player SDK and timed
metadata APIs, allowing you to build a more valuable relationship with your
viewers on your own websites and applications.

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

## Channels

An Amazon IVS channel stores configuration information related to your live
stream. You first create a channel and then contribute video to it using the
channel’s stream key to start your live stream.

You can create a channel

```python
my_channel = ivs.Channel(self, "Channel")
```

### Importing an existing channel

You can reference an existing channel, for example, if you need to create a
stream key for an existing channel

```python
my_channel = ivs.Channel.from_channel_arn(self, "Channel", my_channel_arn)
```

## Stream Keys

A Stream Key is used by a broadcast encoder to initiate a stream and identify
to Amazon IVS which customer and channel the stream is for. If you are
storing this value, it should be treated as if it were a password.

You can create a stream key for a given channel

```python
my_stream_key = my_channel.add_stream_key("StreamKey")
```

## Private Channels

Amazon IVS offers the ability to create private channels, allowing
you to restrict your streams by channel or viewer. You control access
to video playback by enabling playback authorization on channels and
generating signed JSON Web Tokens (JWTs) for authorized playback requests.

A playback token is a JWT that you sign (with a playback authorization key)
and include with every playback request for a channel that has playback
authorization enabled.

In order for Amazon IVS to validate the token, you need to upload
the public key that corresponds to the private key you use to sign the token.

```python
key_pair = ivs.PlaybackKeyPair(self, "PlaybackKeyPair",
    public_key_material=my_public_key_pem_string
)
```

Then, when creating a channel, specify the authorized property

```python
my_channel = ivs.Channel(self, "Channel",
    authorized=True
)
```
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import aws_cdk as _aws_cdk_ceddda9d
import constructs as _constructs_77d1e7e8


@jsii.data_type(
    jsii_type="@aws-cdk/aws-ivs-alpha.ChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "authorized": "authorized",
        "channel_name": "channelName",
        "latency_mode": "latencyMode",
        "type": "type",
    },
)
class ChannelProps:
    def __init__(
        self,
        *,
        authorized: typing.Optional[builtins.bool] = None,
        channel_name: typing.Optional[builtins.str] = None,
        latency_mode: typing.Optional["LatencyMode"] = None,
        type: typing.Optional["ChannelType"] = None,
    ) -> None:
        '''(experimental) Properties for creating a new Channel.

        :param authorized: (experimental) Whether the channel is authorized. If you wish to make an authorized channel, you will need to ensure that a PlaybackKeyPair has been uploaded to your account as this is used to validate the signed JWT that is required for authorization Default: false
        :param channel_name: (experimental) A name for the channel. Default: Automatically generated name
        :param latency_mode: (experimental) Channel latency mode. Default: LatencyMode.LOW
        :param type: (experimental) The channel type, which determines the allowable resolution and bitrate. If you exceed the allowable resolution or bitrate, the stream will disconnect immediately Default: ChannelType.STANDARD

        :stability: experimental
        :exampleMetadata: infused

        Example::

            my_channel = ivs.Channel(self, "Channel",
                authorized=True
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ebf6a0e98bbd5b88d9676fbe616666a44f837cba80675eade5df1fea22c9d22)
            check_type(argname="argument authorized", value=authorized, expected_type=type_hints["authorized"])
            check_type(argname="argument channel_name", value=channel_name, expected_type=type_hints["channel_name"])
            check_type(argname="argument latency_mode", value=latency_mode, expected_type=type_hints["latency_mode"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if authorized is not None:
            self._values["authorized"] = authorized
        if channel_name is not None:
            self._values["channel_name"] = channel_name
        if latency_mode is not None:
            self._values["latency_mode"] = latency_mode
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def authorized(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether the channel is authorized.

        If you wish to make an authorized channel, you will need to ensure that
        a PlaybackKeyPair has been uploaded to your account as this is used to
        validate the signed JWT that is required for authorization

        :default: false

        :stability: experimental
        '''
        result = self._values.get("authorized")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def channel_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) A name for the channel.

        :default: Automatically generated name

        :stability: experimental
        '''
        result = self._values.get("channel_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def latency_mode(self) -> typing.Optional["LatencyMode"]:
        '''(experimental) Channel latency mode.

        :default: LatencyMode.LOW

        :stability: experimental
        '''
        result = self._values.get("latency_mode")
        return typing.cast(typing.Optional["LatencyMode"], result)

    @builtins.property
    def type(self) -> typing.Optional["ChannelType"]:
        '''(experimental) The channel type, which determines the allowable resolution and bitrate.

        If you exceed the allowable resolution or bitrate, the stream will disconnect immediately

        :default: ChannelType.STANDARD

        :stability: experimental
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional["ChannelType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/aws-ivs-alpha.ChannelType")
class ChannelType(enum.Enum):
    '''(experimental) The channel type, which determines the allowable resolution and bitrate.

    If you exceed the allowable resolution or bitrate, the stream probably will disconnect immediately.

    :stability: experimental
    '''

    STANDARD = "STANDARD"
    '''(experimental) Multiple qualities are generated from the original input, to automatically give viewers the best experience for their devices and network conditions.

    :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-channel.html
    :stability: experimental
    '''
    BASIC = "BASIC"
    '''(experimental) delivers the original input to viewers.

    The viewer’s video-quality choice is limited to the original input.

    :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-channel.html
    :stability: experimental
    '''


@jsii.interface(jsii_type="@aws-cdk/aws-ivs-alpha.IChannel")
class IChannel(_aws_cdk_ceddda9d.IResource, typing_extensions.Protocol):
    '''(experimental) Represents an IVS Channel.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="channelArn")
    def channel_arn(self) -> builtins.str:
        '''(experimental) The channel ARN.

        For example: arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh

        :stability: experimental
        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="addStreamKey")
    def add_stream_key(self, id: builtins.str) -> "StreamKey":
        '''(experimental) Adds a stream key for this IVS Channel.

        :param id: construct ID.

        :stability: experimental
        '''
        ...


class _IChannelProxy(
    jsii.proxy_for(_aws_cdk_ceddda9d.IResource), # type: ignore[misc]
):
    '''(experimental) Represents an IVS Channel.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-ivs-alpha.IChannel"

    @builtins.property
    @jsii.member(jsii_name="channelArn")
    def channel_arn(self) -> builtins.str:
        '''(experimental) The channel ARN.

        For example: arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "channelArn"))

    @jsii.member(jsii_name="addStreamKey")
    def add_stream_key(self, id: builtins.str) -> "StreamKey":
        '''(experimental) Adds a stream key for this IVS Channel.

        :param id: construct ID.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__809e7d60e77d2ede718027f4d99dcf810db3b33f39daebb557b424c6457e2f22)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        return typing.cast("StreamKey", jsii.invoke(self, "addStreamKey", [id]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IChannel).__jsii_proxy_class__ = lambda : _IChannelProxy


@jsii.interface(jsii_type="@aws-cdk/aws-ivs-alpha.IPlaybackKeyPair")
class IPlaybackKeyPair(_aws_cdk_ceddda9d.IResource, typing_extensions.Protocol):
    '''(experimental) Represents an IVS Playback Key Pair.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="playbackKeyPairArn")
    def playback_key_pair_arn(self) -> builtins.str:
        '''(experimental) Key-pair ARN.

        For example: arn:aws:ivs:us-west-2:693991300569:playback-key/f99cde61-c2b0-4df3-8941-ca7d38acca1a

        :stability: experimental
        :attribute: true
        '''
        ...


class _IPlaybackKeyPairProxy(
    jsii.proxy_for(_aws_cdk_ceddda9d.IResource), # type: ignore[misc]
):
    '''(experimental) Represents an IVS Playback Key Pair.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-ivs-alpha.IPlaybackKeyPair"

    @builtins.property
    @jsii.member(jsii_name="playbackKeyPairArn")
    def playback_key_pair_arn(self) -> builtins.str:
        '''(experimental) Key-pair ARN.

        For example: arn:aws:ivs:us-west-2:693991300569:playback-key/f99cde61-c2b0-4df3-8941-ca7d38acca1a

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "playbackKeyPairArn"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPlaybackKeyPair).__jsii_proxy_class__ = lambda : _IPlaybackKeyPairProxy


@jsii.interface(jsii_type="@aws-cdk/aws-ivs-alpha.IStreamKey")
class IStreamKey(_aws_cdk_ceddda9d.IResource, typing_extensions.Protocol):
    '''(experimental) Represents an IVS Stream Key.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="streamKeyArn")
    def stream_key_arn(self) -> builtins.str:
        '''(experimental) The stream-key ARN.

        For example: arn:aws:ivs:us-west-2:123456789012:stream-key/g1H2I3j4k5L6

        :stability: experimental
        :attribute: true
        '''
        ...


class _IStreamKeyProxy(
    jsii.proxy_for(_aws_cdk_ceddda9d.IResource), # type: ignore[misc]
):
    '''(experimental) Represents an IVS Stream Key.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-ivs-alpha.IStreamKey"

    @builtins.property
    @jsii.member(jsii_name="streamKeyArn")
    def stream_key_arn(self) -> builtins.str:
        '''(experimental) The stream-key ARN.

        For example: arn:aws:ivs:us-west-2:123456789012:stream-key/g1H2I3j4k5L6

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "streamKeyArn"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStreamKey).__jsii_proxy_class__ = lambda : _IStreamKeyProxy


@jsii.enum(jsii_type="@aws-cdk/aws-ivs-alpha.LatencyMode")
class LatencyMode(enum.Enum):
    '''(experimental) Channel latency mode.

    :stability: experimental
    '''

    LOW = "LOW"
    '''(experimental) Use LOW to minimize broadcaster-to-viewer latency for interactive broadcasts.

    :stability: experimental
    '''
    NORMAL = "NORMAL"
    '''(experimental) Use NORMAL for broadcasts that do not require viewer interaction.

    :stability: experimental
    '''


@jsii.implements(IPlaybackKeyPair)
class PlaybackKeyPair(
    _aws_cdk_ceddda9d.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-ivs-alpha.PlaybackKeyPair",
):
    '''(experimental) A new IVS Playback Key Pair.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        key_pair = ivs.PlaybackKeyPair(self, "PlaybackKeyPair",
            public_key_material=my_public_key_pem_string
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        public_key_material: builtins.str,
        playback_key_pair_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param public_key_material: (experimental) The public portion of a customer-generated key pair.
        :param playback_key_pair_name: (experimental) An arbitrary string (a nickname) assigned to a playback key pair that helps the customer identify that resource. The value does not need to be unique. Default: Automatically generated name

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75931c57bc0ba240c98824ea65da9a0bc0a3bc48be2344ac7b70c03f259e632f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = PlaybackKeyPairProps(
            public_key_material=public_key_material,
            playback_key_pair_name=playback_key_pair_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="playbackKeyPairArn")
    def playback_key_pair_arn(self) -> builtins.str:
        '''(experimental) Key-pair ARN.

        For example: arn:aws:ivs:us-west-2:693991300569:playback-key/f99cde61-c2b0-4df3-8941-ca7d38acca1a

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "playbackKeyPairArn"))

    @builtins.property
    @jsii.member(jsii_name="playbackKeyPairFingerprint")
    def playback_key_pair_fingerprint(self) -> builtins.str:
        '''(experimental) Key-pair identifier.

        For example: 98:0d:1a:a0:19:96:1e:ea:0a:0a:2c:9a:42:19:2b:e7

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "playbackKeyPairFingerprint"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-ivs-alpha.PlaybackKeyPairProps",
    jsii_struct_bases=[],
    name_mapping={
        "public_key_material": "publicKeyMaterial",
        "playback_key_pair_name": "playbackKeyPairName",
    },
)
class PlaybackKeyPairProps:
    def __init__(
        self,
        *,
        public_key_material: builtins.str,
        playback_key_pair_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Properties for creating a new Playback Key Pair.

        :param public_key_material: (experimental) The public portion of a customer-generated key pair.
        :param playback_key_pair_name: (experimental) An arbitrary string (a nickname) assigned to a playback key pair that helps the customer identify that resource. The value does not need to be unique. Default: Automatically generated name

        :stability: experimental
        :exampleMetadata: infused

        Example::

            key_pair = ivs.PlaybackKeyPair(self, "PlaybackKeyPair",
                public_key_material=my_public_key_pem_string
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f26b3314acb516329ef76511a5408ac87ae783446cab3f1be9ed1d0b81fa5b7)
            check_type(argname="argument public_key_material", value=public_key_material, expected_type=type_hints["public_key_material"])
            check_type(argname="argument playback_key_pair_name", value=playback_key_pair_name, expected_type=type_hints["playback_key_pair_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "public_key_material": public_key_material,
        }
        if playback_key_pair_name is not None:
            self._values["playback_key_pair_name"] = playback_key_pair_name

    @builtins.property
    def public_key_material(self) -> builtins.str:
        '''(experimental) The public portion of a customer-generated key pair.

        :stability: experimental
        '''
        result = self._values.get("public_key_material")
        assert result is not None, "Required property 'public_key_material' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def playback_key_pair_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) An arbitrary string (a nickname) assigned to a playback key pair that helps the customer identify that resource.

        The value does not need to be unique.

        :default: Automatically generated name

        :stability: experimental
        '''
        result = self._values.get("playback_key_pair_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlaybackKeyPairProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IStreamKey)
class StreamKey(
    _aws_cdk_ceddda9d.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-ivs-alpha.StreamKey",
):
    '''(experimental) A new IVS Stream Key.

    :stability: experimental
    :exampleMetadata: fixture=with-channel infused

    Example::

        my_stream_key = my_channel.add_stream_key("StreamKey")
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        channel: IChannel,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param channel: (experimental) Channel ARN for the stream.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67fad0f56ffbc15680b0f651250d8bb5cf4dacb899e5c5bbf4abdcfc3ae39632)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = StreamKeyProps(channel=channel)

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="streamKeyArn")
    def stream_key_arn(self) -> builtins.str:
        '''(experimental) The stream-key ARN.

        For example: arn:aws:ivs:us-west-2:123456789012:stream-key/g1H2I3j4k5L6

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "streamKeyArn"))

    @builtins.property
    @jsii.member(jsii_name="streamKeyValue")
    def stream_key_value(self) -> builtins.str:
        '''(experimental) The stream-key value.

        For example: sk_us-west-2_abcdABCDefgh_567890abcdef

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "streamKeyValue"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-ivs-alpha.StreamKeyProps",
    jsii_struct_bases=[],
    name_mapping={"channel": "channel"},
)
class StreamKeyProps:
    def __init__(self, *, channel: IChannel) -> None:
        '''(experimental) Properties for creating a new Stream Key.

        :param channel: (experimental) Channel ARN for the stream.

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_ivs_alpha as ivs_alpha
            
            # channel: ivs_alpha.Channel
            
            stream_key_props = ivs_alpha.StreamKeyProps(
                channel=channel
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10474702d05a8d909166c4d0ef1de9632d82c17ae609436e3980c1bd4fa2ddb3)
            check_type(argname="argument channel", value=channel, expected_type=type_hints["channel"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel": channel,
        }

    @builtins.property
    def channel(self) -> IChannel:
        '''(experimental) Channel ARN for the stream.

        :stability: experimental
        '''
        result = self._values.get("channel")
        assert result is not None, "Required property 'channel' is missing"
        return typing.cast(IChannel, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StreamKeyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IChannel)
class Channel(
    _aws_cdk_ceddda9d.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-ivs-alpha.Channel",
):
    '''(experimental) A new IVS channel.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        my_channel = ivs.Channel(self, "Channel")
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        authorized: typing.Optional[builtins.bool] = None,
        channel_name: typing.Optional[builtins.str] = None,
        latency_mode: typing.Optional[LatencyMode] = None,
        type: typing.Optional[ChannelType] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param authorized: (experimental) Whether the channel is authorized. If you wish to make an authorized channel, you will need to ensure that a PlaybackKeyPair has been uploaded to your account as this is used to validate the signed JWT that is required for authorization Default: false
        :param channel_name: (experimental) A name for the channel. Default: Automatically generated name
        :param latency_mode: (experimental) Channel latency mode. Default: LatencyMode.LOW
        :param type: (experimental) The channel type, which determines the allowable resolution and bitrate. If you exceed the allowable resolution or bitrate, the stream will disconnect immediately Default: ChannelType.STANDARD

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07139327925dc97a551bbf17c849a0f698e0c9c60d3da3f65f2b3d2bea0e0c50)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ChannelProps(
            authorized=authorized,
            channel_name=channel_name,
            latency_mode=latency_mode,
            type=type,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromChannelArn")
    @builtins.classmethod
    def from_channel_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        channel_arn: builtins.str,
    ) -> IChannel:
        '''(experimental) Import an existing channel.

        :param scope: -
        :param id: -
        :param channel_arn: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5efa416339cc500736f229c9a2b3b3b1143c18d7a26fe2712053e5511d370c5f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument channel_arn", value=channel_arn, expected_type=type_hints["channel_arn"])
        return typing.cast(IChannel, jsii.sinvoke(cls, "fromChannelArn", [scope, id, channel_arn]))

    @jsii.member(jsii_name="addStreamKey")
    def add_stream_key(self, id: builtins.str) -> StreamKey:
        '''(experimental) Adds a stream key for this IVS Channel.

        :param id: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65e1f25de7c3a0e391031082a65ee02865e1f85fe29f43a74bbc59866b95e50a)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        return typing.cast(StreamKey, jsii.invoke(self, "addStreamKey", [id]))

    @builtins.property
    @jsii.member(jsii_name="channelArn")
    def channel_arn(self) -> builtins.str:
        '''(experimental) The channel ARN.

        For example: arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "channelArn"))

    @builtins.property
    @jsii.member(jsii_name="channelIngestEndpoint")
    def channel_ingest_endpoint(self) -> builtins.str:
        '''(experimental) Channel ingest endpoint, part of the definition of an ingest server, used when you set up streaming software.

        For example: a1b2c3d4e5f6.global-contribute.live-video.net

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "channelIngestEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="channelPlaybackUrl")
    def channel_playback_url(self) -> builtins.str:
        '''(experimental) Channel playback URL.

        For example:
        https://a1b2c3d4e5f6.us-west-2.playback.live-video.net/api/video/v1/us-west-2.123456789012.channel.abcdEFGH.m3u8

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "channelPlaybackUrl"))


__all__ = [
    "Channel",
    "ChannelProps",
    "ChannelType",
    "IChannel",
    "IPlaybackKeyPair",
    "IStreamKey",
    "LatencyMode",
    "PlaybackKeyPair",
    "PlaybackKeyPairProps",
    "StreamKey",
    "StreamKeyProps",
]

publication.publish()

def _typecheckingstub__0ebf6a0e98bbd5b88d9676fbe616666a44f837cba80675eade5df1fea22c9d22(
    *,
    authorized: typing.Optional[builtins.bool] = None,
    channel_name: typing.Optional[builtins.str] = None,
    latency_mode: typing.Optional[LatencyMode] = None,
    type: typing.Optional[ChannelType] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__809e7d60e77d2ede718027f4d99dcf810db3b33f39daebb557b424c6457e2f22(
    id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75931c57bc0ba240c98824ea65da9a0bc0a3bc48be2344ac7b70c03f259e632f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    public_key_material: builtins.str,
    playback_key_pair_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f26b3314acb516329ef76511a5408ac87ae783446cab3f1be9ed1d0b81fa5b7(
    *,
    public_key_material: builtins.str,
    playback_key_pair_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67fad0f56ffbc15680b0f651250d8bb5cf4dacb899e5c5bbf4abdcfc3ae39632(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    channel: IChannel,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10474702d05a8d909166c4d0ef1de9632d82c17ae609436e3980c1bd4fa2ddb3(
    *,
    channel: IChannel,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07139327925dc97a551bbf17c849a0f698e0c9c60d3da3f65f2b3d2bea0e0c50(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    authorized: typing.Optional[builtins.bool] = None,
    channel_name: typing.Optional[builtins.str] = None,
    latency_mode: typing.Optional[LatencyMode] = None,
    type: typing.Optional[ChannelType] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5efa416339cc500736f229c9a2b3b3b1143c18d7a26fe2712053e5511d370c5f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    channel_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65e1f25de7c3a0e391031082a65ee02865e1f85fe29f43a74bbc59866b95e50a(
    id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
