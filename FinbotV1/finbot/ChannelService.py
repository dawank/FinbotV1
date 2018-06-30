from FinbotServer.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from FinbotServer.protocol.TProtocol import TProtocolException
from FinbotServer.TRecursive import fix_spec
import sys
import logging
from .ttypes import *
from FinbotServer.Thrift import TProcessor
from FinbotServer.transport import TTransport
all_structs = []

class Iface(object):
    def issueOTP(self, channelId):
        """
        Parameters:
         - channelId
        """
        pass

    def approveChannelAndIssueChannelToken(self, channelId):
        """
        Parameters:
         - channelId
        """
        pass

    def approveChannelAndIssueRequestToken(self, channelId, otpId):
        """
        Parameters:
         - channelId
         - otpId
        """
        pass

    def fetchNotificationItems(self, localRev):
        """
        Parameters:
         - localRev
        """
        pass

    def getApprovedChannels(self, lastSynced, locale):
        """
        Parameters:
         - lastSynced
         - locale
        """
        pass

    def getChannelInfo(self, channelId, locale):
        """
        Parameters:
         - channelId
         - locale
        """
        pass

    def getChannelNotificationSetting(self, channelId, locale):
        """
        Parameters:
         - channelId
         - locale
        """
        pass

    def getChannelNotificationSettings(self, locale):
        """
        Parameters:
         - locale
        """
        pass

    def getChannels(self, lastSynced, locale):
        """
        Parameters:
         - lastSynced
         - locale
        """
        pass

    def getDomains(self, lastSynced):
        """
        Parameters:
         - lastSynced
        """
        pass

    def getFriendChannelMatrices(self, channelIds):
        """
        Parameters:
         - channelIds
        """
        pass

    def updateChannelSettings(self, channelSettings):
        """
        Parameters:
         - channelSettings
        """
        pass

    def getCommonDomains(self, lastSynced):
        """
        Parameters:
         - lastSynced
        """
        pass

    def getNotificationBadgeCount(self, localRev):
        """
        Parameters:
         - localRev
        """
        pass

    def issueChannelToken(self, channelId):
        """
        Parameters:
         - channelId
        """
        pass

    def issueRequestToken(self, channelId, otpId):
        """
        Parameters:
         - channelId
         - otpId
        """
        pass

    def issueRequestTokenWithAuthScheme(self, channelId, otpId, authScheme, returnUrl):
        """
        Parameters:
         - channelId
         - otpId
         - authScheme
         - returnUrl
        """
        pass

    def issueRequestTokenForAutoLogin(self, channelId, otpId, redirectUrl):
        """
        Parameters:
         - channelId
         - otpId
         - redirectUrl
        """
        pass

    def getUpdatedChannelIds(self, channelIds):
        """
        Parameters:
         - channelIds
        """
        pass

    def reserveCoinUse(self, request, locale):
        """
        Parameters:
         - request
         - locale
        """
        pass

    def revokeChannel(self, channelId):
        """
        Parameters:
         - channelId
        """
        pass

    def syncChannelData(self, lastSynced, locale):
        """
        Parameters:
         - lastSynced
         - locale
        """
        pass

    def updateChannelNotificationSetting(self, setting):
        """
        Parameters:
         - setting
        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def issueOTP(self, channelId):
        """
        Parameters:
         - channelId
        """
        self.send_issueOTP(channelId)
        return self.recv_issueOTP()

    def send_issueOTP(self, channelId):
        self._oprot.writeMessageBegin('issueOTP', TMessageType.CALL, self._seqid)
        args = issueOTP_args()
        args.channelId = channelId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_issueOTP(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = issueOTP_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "issueOTP failed: unknown result")

    def approveChannelAndIssueChannelToken(self, channelId):
        """
        Parameters:
         - channelId
        """
        self.send_approveChannelAndIssueChannelToken(channelId)
        return self.recv_approveChannelAndIssueChannelToken()

    def send_approveChannelAndIssueChannelToken(self, channelId):
        self._oprot.writeMessageBegin('approveChannelAndIssueChannelToken', TMessageType.CALL, self._seqid)
        args = approveChannelAndIssueChannelToken_args()
        args.channelId = channelId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_approveChannelAndIssueChannelToken(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = approveChannelAndIssueChannelToken_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "approveChannelAndIssueChannelToken failed: unknown result")

    def approveChannelAndIssueRequestToken(self, channelId, otpId):
        """
        Parameters:
         - channelId
         - otpId
        """
        self.send_approveChannelAndIssueRequestToken(channelId, otpId)
        return self.recv_approveChannelAndIssueRequestToken()

    def send_approveChannelAndIssueRequestToken(self, channelId, otpId):
        self._oprot.writeMessageBegin('approveChannelAndIssueRequestToken', TMessageType.CALL, self._seqid)
        args = approveChannelAndIssueRequestToken_args()
        args.channelId = channelId
        args.otpId = otpId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_approveChannelAndIssueRequestToken(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = approveChannelAndIssueRequestToken_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "approveChannelAndIssueRequestToken failed: unknown result")

    def fetchNotificationItems(self, localRev):
        """
        Parameters:
         - localRev
        """
        self.send_fetchNotificationItems(localRev)
        return self.recv_fetchNotificationItems()

    def send_fetchNotificationItems(self, localRev):
        self._oprot.writeMessageBegin('fetchNotificationItems', TMessageType.CALL, self._seqid)
        args = fetchNotificationItems_args()
        args.localRev = localRev
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_fetchNotificationItems(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = fetchNotificationItems_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "fetchNotificationItems failed: unknown result")

    def getApprovedChannels(self, lastSynced, locale):
        """
        Parameters:
         - lastSynced
         - locale
        """
        self.send_getApprovedChannels(lastSynced, locale)
        return self.recv_getApprovedChannels()

    def send_getApprovedChannels(self, lastSynced, locale):
        self._oprot.writeMessageBegin('getApprovedChannels', TMessageType.CALL, self._seqid)
        args = getApprovedChannels_args()
        args.lastSynced = lastSynced
        args.locale = locale
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getApprovedChannels(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getApprovedChannels_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getApprovedChannels failed: unknown result")

    def getChannelInfo(self, channelId, locale):
        """
        Parameters:
         - channelId
         - locale
        """
        self.send_getChannelInfo(channelId, locale)
        return self.recv_getChannelInfo()

    def send_getChannelInfo(self, channelId, locale):
        self._oprot.writeMessageBegin('getChannelInfo', TMessageType.CALL, self._seqid)
        args = getChannelInfo_args()
        args.channelId = channelId
        args.locale = locale
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getChannelInfo(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getChannelInfo_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getChannelInfo failed: unknown result")

    def getChannelNotificationSetting(self, channelId, locale):
        """
        Parameters:
         - channelId
         - locale
        """
        self.send_getChannelNotificationSetting(channelId, locale)
        return self.recv_getChannelNotificationSetting()

    def send_getChannelNotificationSetting(self, channelId, locale):
        self._oprot.writeMessageBegin('getChannelNotificationSetting', TMessageType.CALL, self._seqid)
        args = getChannelNotificationSetting_args()
        args.channelId = channelId
        args.locale = locale
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getChannelNotificationSetting(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getChannelNotificationSetting_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getChannelNotificationSetting failed: unknown result")

    def getChannelNotificationSettings(self, locale):
        """
        Parameters:
         - locale
        """
        self.send_getChannelNotificationSettings(locale)
        return self.recv_getChannelNotificationSettings()

    def send_getChannelNotificationSettings(self, locale):
        self._oprot.writeMessageBegin('getChannelNotificationSettings', TMessageType.CALL, self._seqid)
        args = getChannelNotificationSettings_args()
        args.locale = locale
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getChannelNotificationSettings(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getChannelNotificationSettings_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getChannelNotificationSettings failed: unknown result")

    def getChannels(self, lastSynced, locale):
        """
        Parameters:
         - lastSynced
         - locale
        """
        self.send_getChannels(lastSynced, locale)
        return self.recv_getChannels()

    def send_getChannels(self, lastSynced, locale):
        self._oprot.writeMessageBegin('getChannels', TMessageType.CALL, self._seqid)
        args = getChannels_args()
        args.lastSynced = lastSynced
        args.locale = locale
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getChannels(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getChannels_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getChannels failed: unknown result")

    def getDomains(self, lastSynced):
        """
        Parameters:
         - lastSynced
        """
        self.send_getDomains(lastSynced)
        return self.recv_getDomains()

    def send_getDomains(self, lastSynced):
        self._oprot.writeMessageBegin('getDomains', TMessageType.CALL, self._seqid)
        args = getDomains_args()
        args.lastSynced = lastSynced
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getDomains(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getDomains_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getDomains failed: unknown result")

    def getFriendChannelMatrices(self, channelIds):
        """
        Parameters:
         - channelIds
        """
        self.send_getFriendChannelMatrices(channelIds)
        return self.recv_getFriendChannelMatrices()

    def send_getFriendChannelMatrices(self, channelIds):
        self._oprot.writeMessageBegin('getFriendChannelMatrices', TMessageType.CALL, self._seqid)
        args = getFriendChannelMatrices_args()
        args.channelIds = channelIds
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getFriendChannelMatrices(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getFriendChannelMatrices_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getFriendChannelMatrices failed: unknown result")

    def updateChannelSettings(self, channelSettings):
        """
        Parameters:
         - channelSettings
        """
        self.send_updateChannelSettings(channelSettings)
        return self.recv_updateChannelSettings()

    def send_updateChannelSettings(self, channelSettings):
        self._oprot.writeMessageBegin('updateChannelSettings', TMessageType.CALL, self._seqid)
        args = updateChannelSettings_args()
        args.channelSettings = channelSettings
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_updateChannelSettings(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = updateChannelSettings_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "updateChannelSettings failed: unknown result")

    def getCommonDomains(self, lastSynced):
        """
        Parameters:
         - lastSynced
        """
        self.send_getCommonDomains(lastSynced)
        return self.recv_getCommonDomains()

    def send_getCommonDomains(self, lastSynced):
        self._oprot.writeMessageBegin('getCommonDomains', TMessageType.CALL, self._seqid)
        args = getCommonDomains_args()
        args.lastSynced = lastSynced
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getCommonDomains(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getCommonDomains_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getCommonDomains failed: unknown result")

    def getNotificationBadgeCount(self, localRev):
        """
        Parameters:
         - localRev
        """
        self.send_getNotificationBadgeCount(localRev)
        return self.recv_getNotificationBadgeCount()

    def send_getNotificationBadgeCount(self, localRev):
        self._oprot.writeMessageBegin('getNotificationBadgeCount', TMessageType.CALL, self._seqid)
        args = getNotificationBadgeCount_args()
        args.localRev = localRev
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getNotificationBadgeCount(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getNotificationBadgeCount_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getNotificationBadgeCount failed: unknown result")

    def issueChannelToken(self, channelId):
        """
        Parameters:
         - channelId
        """
        self.send_issueChannelToken(channelId)
        return self.recv_issueChannelToken()

    def send_issueChannelToken(self, channelId):
        self._oprot.writeMessageBegin('issueChannelToken', TMessageType.CALL, self._seqid)
        args = issueChannelToken_args()
        args.channelId = channelId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_issueChannelToken(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = issueChannelToken_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "issueChannelToken failed: unknown result")

    def issueRequestToken(self, channelId, otpId):
        """
        Parameters:
         - channelId
         - otpId
        """
        self.send_issueRequestToken(channelId, otpId)
        return self.recv_issueRequestToken()

    def send_issueRequestToken(self, channelId, otpId):
        self._oprot.writeMessageBegin('issueRequestToken', TMessageType.CALL, self._seqid)
        args = issueRequestToken_args()
        args.channelId = channelId
        args.otpId = otpId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_issueRequestToken(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = issueRequestToken_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "issueRequestToken failed: unknown result")

    def issueRequestTokenWithAuthScheme(self, channelId, otpId, authScheme, returnUrl):
        """
        Parameters:
         - channelId
         - otpId
         - authScheme
         - returnUrl
        """
        self.send_issueRequestTokenWithAuthScheme(channelId, otpId, authScheme, returnUrl)
        return self.recv_issueRequestTokenWithAuthScheme()

    def send_issueRequestTokenWithAuthScheme(self, channelId, otpId, authScheme, returnUrl):
        self._oprot.writeMessageBegin('issueRequestTokenWithAuthScheme', TMessageType.CALL, self._seqid)
        args = issueRequestTokenWithAuthScheme_args()
        args.channelId = channelId
        args.otpId = otpId
        args.authScheme = authScheme
        args.returnUrl = returnUrl
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_issueRequestTokenWithAuthScheme(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = issueRequestTokenWithAuthScheme_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "issueRequestTokenWithAuthScheme failed: unknown result")

    def issueRequestTokenForAutoLogin(self, channelId, otpId, redirectUrl):
        """
        Parameters:
         - channelId
         - otpId
         - redirectUrl
        """
        self.send_issueRequestTokenForAutoLogin(channelId, otpId, redirectUrl)
        return self.recv_issueRequestTokenForAutoLogin()

    def send_issueRequestTokenForAutoLogin(self, channelId, otpId, redirectUrl):
        self._oprot.writeMessageBegin('issueRequestTokenForAutoLogin', TMessageType.CALL, self._seqid)
        args = issueRequestTokenForAutoLogin_args()
        args.channelId = channelId
        args.otpId = otpId
        args.redirectUrl = redirectUrl
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_issueRequestTokenForAutoLogin(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = issueRequestTokenForAutoLogin_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "issueRequestTokenForAutoLogin failed: unknown result")

    def getUpdatedChannelIds(self, channelIds):
        """
        Parameters:
         - channelIds
        """
        self.send_getUpdatedChannelIds(channelIds)
        return self.recv_getUpdatedChannelIds()

    def send_getUpdatedChannelIds(self, channelIds):
        self._oprot.writeMessageBegin('getUpdatedChannelIds', TMessageType.CALL, self._seqid)
        args = getUpdatedChannelIds_args()
        args.channelIds = channelIds
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getUpdatedChannelIds(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getUpdatedChannelIds_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getUpdatedChannelIds failed: unknown result")

    def reserveCoinUse(self, request, locale):
        """
        Parameters:
         - request
         - locale
        """
        self.send_reserveCoinUse(request, locale)
        return self.recv_reserveCoinUse()

    def send_reserveCoinUse(self, request, locale):
        self._oprot.writeMessageBegin('reserveCoinUse', TMessageType.CALL, self._seqid)
        args = reserveCoinUse_args()
        args.request = request
        args.locale = locale
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_reserveCoinUse(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = reserveCoinUse_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "reserveCoinUse failed: unknown result")

    def revokeChannel(self, channelId):
        """
        Parameters:
         - channelId
        """
        self.send_revokeChannel(channelId)
        self.recv_revokeChannel()

    def send_revokeChannel(self, channelId):
        self._oprot.writeMessageBegin('revokeChannel', TMessageType.CALL, self._seqid)
        args = revokeChannel_args()
        args.channelId = channelId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_revokeChannel(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = revokeChannel_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def syncChannelData(self, lastSynced, locale):
        """
        Parameters:
         - lastSynced
         - locale
        """
        self.send_syncChannelData(lastSynced, locale)
        return self.recv_syncChannelData()

    def send_syncChannelData(self, lastSynced, locale):
        self._oprot.writeMessageBegin('syncChannelData', TMessageType.CALL, self._seqid)
        args = syncChannelData_args()
        args.lastSynced = lastSynced
        args.locale = locale
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_syncChannelData(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = syncChannelData_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "syncChannelData failed: unknown result")

    def updateChannelNotificationSetting(self, setting):
        """
        Parameters:
         - setting
        """
        self.send_updateChannelNotificationSetting(setting)
        self.recv_updateChannelNotificationSetting()

    def send_updateChannelNotificationSetting(self, setting):
        self._oprot.writeMessageBegin('updateChannelNotificationSetting', TMessageType.CALL, self._seqid)
        args = updateChannelNotificationSetting_args()
        args.setting = setting
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_updateChannelNotificationSetting(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = updateChannelNotificationSetting_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["issueOTP"] = Processor.process_issueOTP
        self._processMap["approveChannelAndIssueChannelToken"] = Processor.process_approveChannelAndIssueChannelToken
        self._processMap["approveChannelAndIssueRequestToken"] = Processor.process_approveChannelAndIssueRequestToken
        self._processMap["fetchNotificationItems"] = Processor.process_fetchNotificationItems
        self._processMap["getApprovedChannels"] = Processor.process_getApprovedChannels
        self._processMap["getChannelInfo"] = Processor.process_getChannelInfo
        self._processMap["getChannelNotificationSetting"] = Processor.process_getChannelNotificationSetting
        self._processMap["getChannelNotificationSettings"] = Processor.process_getChannelNotificationSettings
        self._processMap["getChannels"] = Processor.process_getChannels
        self._processMap["getDomains"] = Processor.process_getDomains
        self._processMap["getFriendChannelMatrices"] = Processor.process_getFriendChannelMatrices
        self._processMap["updateChannelSettings"] = Processor.process_updateChannelSettings
        self._processMap["getCommonDomains"] = Processor.process_getCommonDomains
        self._processMap["getNotificationBadgeCount"] = Processor.process_getNotificationBadgeCount
        self._processMap["issueChannelToken"] = Processor.process_issueChannelToken
        self._processMap["issueRequestToken"] = Processor.process_issueRequestToken
        self._processMap["issueRequestTokenWithAuthScheme"] = Processor.process_issueRequestTokenWithAuthScheme
        self._processMap["issueRequestTokenForAutoLogin"] = Processor.process_issueRequestTokenForAutoLogin
        self._processMap["getUpdatedChannelIds"] = Processor.process_getUpdatedChannelIds
        self._processMap["reserveCoinUse"] = Processor.process_reserveCoinUse
        self._processMap["revokeChannel"] = Processor.process_revokeChannel
        self._processMap["syncChannelData"] = Processor.process_syncChannelData
        self._processMap["updateChannelNotificationSetting"] = Processor.process_updateChannelNotificationSetting

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True

    def process_issueOTP(self, seqid, iprot, oprot):
        args = issueOTP_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = issueOTP_result()
        try:
            result.success = self._handler.issueOTP(args.channelId)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except ChannelException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("issueOTP", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_approveChannelAndIssueChannelToken(self, seqid, iprot, oprot):
        args = approveChannelAndIssueChannelToken_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = approveChannelAndIssueChannelToken_result()
        try:
            result.success = self._handler.approveChannelAndIssueChannelToken(args.channelId)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except ChannelException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("approveChannelAndIssueChannelToken", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_approveChannelAndIssueRequestToken(self, seqid, iprot, oprot):
        args = approveChannelAndIssueRequestToken_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = approveChannelAndIssueRequestToken_result()
        try:
            result.success = self._handler.approveChannelAndIssueRequestToken(args.channelId, args.otpId)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except ChannelException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("approveChannelAndIssueRequestToken", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_fetchNotificationItems(self, seqid, iprot, oprot):
        args = fetchNotificationItems_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = fetchNotificationItems_result()
        try:
            result.success = self._handler.fetchNotificationItems(args.localRev)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except ChannelException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("fetchNotificationItems", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getApprovedChannels(self, seqid, iprot, oprot):
        args = getApprovedChannels_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getApprovedChannels_result()
        try:
            result.success = self._handler.getApprovedChannels(args.lastSynced, args.locale)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except ChannelException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getApprovedChannels", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getChannelInfo(self, seqid, iprot, oprot):
        args = getChannelInfo_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getChannelInfo_result()
        try:
            result.success = self._handler.getChannelInfo(args.channelId, args.locale)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except ChannelException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getChannelInfo", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getChannelNotificationSetting(self, seqid, iprot, oprot):
        args = getChannelNotificationSetting_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getChannelNotificationSetting_result()
        try:
            result.success = self._handler.getChannelNotificationSetting(args.channelId, args.locale)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except ChannelException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getChannelNotificationSetting", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getChannelNotificationSettings(self, seqid, iprot, oprot):
        args = getChannelNotificationSettings_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getChannelNotificationSettings_result()
        try:
            result.success = self._handler.getChannelNotificationSettings(args.locale)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except ChannelException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getChannelNotificationSettings", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getChannels(self, seqid, iprot, oprot):
        args = getChannels_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getChannels_result()
        try:
            result.success = self._handler.getChannels(args.lastSynced, args.locale)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except ChannelException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getChannels", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getDomains(self, seqid, iprot, oprot):
        args = getDomains_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getDomains_result()
        try:
            result.success = self._handler.getDomains(args.lastSynced)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except ChannelException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getDomains", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getFriendChannelMatrices(self, seqid, iprot, oprot):
        args = getFriendChannelMatrices_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getFriendChannelMatrices_result()
        try:
            result.success = self._handler.getFriendChannelMatrices(args.channelIds)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except ChannelException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getFriendChannelMatrices", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_updateChannelSettings(self, seqid, iprot, oprot):
        args = updateChannelSettings_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = updateChannelSettings_result()
        try:
            result.success = self._handler.updateChannelSettings(args.channelSettings)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except ChannelException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("updateChannelSettings", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getCommonDomains(self, seqid, iprot, oprot):
        args = getCommonDomains_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getCommonDomains_result()
        try:
            result.success = self._handler.getCommonDomains(args.lastSynced)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except ChannelException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getCommonDomains", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getNotificationBadgeCount(self, seqid, iprot, oprot):
        args = getNotificationBadgeCount_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getNotificationBadgeCount_result()
        try:
            result.success = self._handler.getNotificationBadgeCount(args.localRev)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except ChannelException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getNotificationBadgeCount", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_issueChannelToken(self, seqid, iprot, oprot):
        args = issueChannelToken_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = issueChannelToken_result()
        try:
            result.success = self._handler.issueChannelToken(args.channelId)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except ChannelException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("issueChannelToken", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_issueRequestToken(self, seqid, iprot, oprot):
        args = issueRequestToken_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = issueRequestToken_result()
        try:
            result.success = self._handler.issueRequestToken(args.channelId, args.otpId)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except ChannelException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("issueRequestToken", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_issueRequestTokenWithAuthScheme(self, seqid, iprot, oprot):
        args = issueRequestTokenWithAuthScheme_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = issueRequestTokenWithAuthScheme_result()
        try:
            result.success = self._handler.issueRequestTokenWithAuthScheme(args.channelId, args.otpId, args.authScheme, args.returnUrl)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except ChannelException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("issueRequestTokenWithAuthScheme", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_issueRequestTokenForAutoLogin(self, seqid, iprot, oprot):
        args = issueRequestTokenForAutoLogin_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = issueRequestTokenForAutoLogin_result()
        try:
            result.success = self._handler.issueRequestTokenForAutoLogin(args.channelId, args.otpId, args.redirectUrl)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except ChannelException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("issueRequestTokenForAutoLogin", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getUpdatedChannelIds(self, seqid, iprot, oprot):
        args = getUpdatedChannelIds_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getUpdatedChannelIds_result()
        try:
            result.success = self._handler.getUpdatedChannelIds(args.channelIds)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except ChannelException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getUpdatedChannelIds", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_reserveCoinUse(self, seqid, iprot, oprot):
        args = reserveCoinUse_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = reserveCoinUse_result()
        try:
            result.success = self._handler.reserveCoinUse(args.request, args.locale)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except ChannelException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("reserveCoinUse", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_revokeChannel(self, seqid, iprot, oprot):
        args = revokeChannel_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = revokeChannel_result()
        try:
            self._handler.revokeChannel(args.channelId)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except ChannelException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("revokeChannel", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_syncChannelData(self, seqid, iprot, oprot):
        args = syncChannelData_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = syncChannelData_result()
        try:
            result.success = self._handler.syncChannelData(args.lastSynced, args.locale)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except ChannelException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("syncChannelData", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_updateChannelNotificationSetting(self, seqid, iprot, oprot):
        args = updateChannelNotificationSetting_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = updateChannelNotificationSetting_result()
        try:
            self._handler.updateChannelNotificationSetting(args.setting)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except ChannelException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("updateChannelNotificationSetting", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class issueOTP_args(object):
    """
    Attributes:
     - channelId
    """


    def __init__(self, channelId=None,):
        self.channelId = channelId

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRING:
                    self.channelId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('issueOTP_args')
        if self.channelId is not None:
            oprot.writeFieldBegin('channelId', TType.STRING, 2)
            oprot.writeString(self.channelId.encode('utf-8') if sys.version_info[0] == 2 else self.channelId)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(issueOTP_args)
issueOTP_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'channelId', 'UTF8', None, ),  # 2
)


class issueOTP_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = OTPResult()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = ChannelException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('issueOTP_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(issueOTP_result)
issueOTP_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [OTPResult, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [ChannelException, None], None, ),  # 1
)


class approveChannelAndIssueChannelToken_args(object):
    """
    Attributes:
     - channelId
    """


    def __init__(self, channelId=None,):
        self.channelId = channelId

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.channelId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('approveChannelAndIssueChannelToken_args')
        if self.channelId is not None:
            oprot.writeFieldBegin('channelId', TType.STRING, 1)
            oprot.writeString(self.channelId.encode('utf-8') if sys.version_info[0] == 2 else self.channelId)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(approveChannelAndIssueChannelToken_args)
approveChannelAndIssueChannelToken_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'channelId', 'UTF8', None, ),  # 1
)


class approveChannelAndIssueChannelToken_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = ChannelToken()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = ChannelException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('approveChannelAndIssueChannelToken_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(approveChannelAndIssueChannelToken_result)
approveChannelAndIssueChannelToken_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [ChannelToken, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [ChannelException, None], None, ),  # 1
)


class approveChannelAndIssueRequestToken_args(object):
    """
    Attributes:
     - channelId
     - otpId
    """


    def __init__(self, channelId=None, otpId=None,):
        self.channelId = channelId
        self.otpId = otpId

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.channelId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.otpId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('approveChannelAndIssueRequestToken_args')
        if self.channelId is not None:
            oprot.writeFieldBegin('channelId', TType.STRING, 1)
            oprot.writeString(self.channelId.encode('utf-8') if sys.version_info[0] == 2 else self.channelId)
            oprot.writeFieldEnd()
        if self.otpId is not None:
            oprot.writeFieldBegin('otpId', TType.STRING, 2)
            oprot.writeString(self.otpId.encode('utf-8') if sys.version_info[0] == 2 else self.otpId)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(approveChannelAndIssueRequestToken_args)
approveChannelAndIssueRequestToken_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'channelId', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'otpId', 'UTF8', None, ),  # 2
)


class approveChannelAndIssueRequestToken_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRING:
                    self.success = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = ChannelException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('approveChannelAndIssueRequestToken_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRING, 0)
            oprot.writeString(self.success.encode('utf-8') if sys.version_info[0] == 2 else self.success)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(approveChannelAndIssueRequestToken_result)
approveChannelAndIssueRequestToken_result.thrift_spec = (
    (0, TType.STRING, 'success', 'UTF8', None, ),  # 0
    (1, TType.STRUCT, 'e', [ChannelException, None], None, ),  # 1
)


class fetchNotificationItems_args(object):
    """
    Attributes:
     - localRev
    """


    def __init__(self, localRev=None,):
        self.localRev = localRev

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.I64:
                    self.localRev = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('fetchNotificationItems_args')
        if self.localRev is not None:
            oprot.writeFieldBegin('localRev', TType.I64, 2)
            oprot.writeI64(self.localRev)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(fetchNotificationItems_args)
fetchNotificationItems_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.I64, 'localRev', None, None, ),  # 2
)


class fetchNotificationItems_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = NotificationFetchResult()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = ChannelException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('fetchNotificationItems_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(fetchNotificationItems_result)
fetchNotificationItems_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [NotificationFetchResult, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [ChannelException, None], None, ),  # 1
)


class getApprovedChannels_args(object):
    """
    Attributes:
     - lastSynced
     - locale
    """


    def __init__(self, lastSynced=None, locale=None,):
        self.lastSynced = lastSynced
        self.locale = locale

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.I64:
                    self.lastSynced = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.locale = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getApprovedChannels_args')
        if self.lastSynced is not None:
            oprot.writeFieldBegin('lastSynced', TType.I64, 2)
            oprot.writeI64(self.lastSynced)
            oprot.writeFieldEnd()
        if self.locale is not None:
            oprot.writeFieldBegin('locale', TType.STRING, 3)
            oprot.writeString(self.locale.encode('utf-8') if sys.version_info[0] == 2 else self.locale)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getApprovedChannels_args)
getApprovedChannels_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.I64, 'lastSynced', None, None, ),  # 2
    (3, TType.STRING, 'locale', 'UTF8', None, ),  # 3
)


class getApprovedChannels_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = ApprovedChannelInfos()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = ChannelException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getApprovedChannels_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getApprovedChannels_result)
getApprovedChannels_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [ApprovedChannelInfos, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [ChannelException, None], None, ),  # 1
)


class getChannelInfo_args(object):
    """
    Attributes:
     - channelId
     - locale
    """


    def __init__(self, channelId=None, locale=None,):
        self.channelId = channelId
        self.locale = locale

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRING:
                    self.channelId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.locale = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getChannelInfo_args')
        if self.channelId is not None:
            oprot.writeFieldBegin('channelId', TType.STRING, 2)
            oprot.writeString(self.channelId.encode('utf-8') if sys.version_info[0] == 2 else self.channelId)
            oprot.writeFieldEnd()
        if self.locale is not None:
            oprot.writeFieldBegin('locale', TType.STRING, 3)
            oprot.writeString(self.locale.encode('utf-8') if sys.version_info[0] == 2 else self.locale)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getChannelInfo_args)
getChannelInfo_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'channelId', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'locale', 'UTF8', None, ),  # 3
)


class getChannelInfo_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = ChannelInfo()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = ChannelException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getChannelInfo_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getChannelInfo_result)
getChannelInfo_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [ChannelInfo, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [ChannelException, None], None, ),  # 1
)


class getChannelNotificationSetting_args(object):
    """
    Attributes:
     - channelId
     - locale
    """


    def __init__(self, channelId=None, locale=None,):
        self.channelId = channelId
        self.locale = locale

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.channelId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.locale = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getChannelNotificationSetting_args')
        if self.channelId is not None:
            oprot.writeFieldBegin('channelId', TType.STRING, 1)
            oprot.writeString(self.channelId.encode('utf-8') if sys.version_info[0] == 2 else self.channelId)
            oprot.writeFieldEnd()
        if self.locale is not None:
            oprot.writeFieldBegin('locale', TType.STRING, 2)
            oprot.writeString(self.locale.encode('utf-8') if sys.version_info[0] == 2 else self.locale)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getChannelNotificationSetting_args)
getChannelNotificationSetting_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'channelId', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'locale', 'UTF8', None, ),  # 2
)


class getChannelNotificationSetting_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = ChannelNotificationSetting()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = ChannelException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getChannelNotificationSetting_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getChannelNotificationSetting_result)
getChannelNotificationSetting_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [ChannelNotificationSetting, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [ChannelException, None], None, ),  # 1
)


class getChannelNotificationSettings_args(object):
    """
    Attributes:
     - locale
    """


    def __init__(self, locale=None,):
        self.locale = locale

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.locale = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getChannelNotificationSettings_args')
        if self.locale is not None:
            oprot.writeFieldBegin('locale', TType.STRING, 1)
            oprot.writeString(self.locale.encode('utf-8') if sys.version_info[0] == 2 else self.locale)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getChannelNotificationSettings_args)
getChannelNotificationSettings_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'locale', 'UTF8', None, ),  # 1
)


class getChannelNotificationSettings_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype1267, _size1264) = iprot.readListBegin()
                    for _i1268 in range(_size1264):
                        _elem1269 = ChannelNotificationSetting()
                        _elem1269.read(iprot)
                        self.success.append(_elem1269)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = ChannelException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getChannelNotificationSettings_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter1270 in self.success:
                iter1270.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getChannelNotificationSettings_result)
getChannelNotificationSettings_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT, [ChannelNotificationSetting, None], False), None, ),  # 0
    (1, TType.STRUCT, 'e', [ChannelException, None], None, ),  # 1
)


class getChannels_args(object):
    """
    Attributes:
     - lastSynced
     - locale
    """


    def __init__(self, lastSynced=None, locale=None,):
        self.lastSynced = lastSynced
        self.locale = locale

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.I64:
                    self.lastSynced = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.locale = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getChannels_args')
        if self.lastSynced is not None:
            oprot.writeFieldBegin('lastSynced', TType.I64, 2)
            oprot.writeI64(self.lastSynced)
            oprot.writeFieldEnd()
        if self.locale is not None:
            oprot.writeFieldBegin('locale', TType.STRING, 3)
            oprot.writeString(self.locale.encode('utf-8') if sys.version_info[0] == 2 else self.locale)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getChannels_args)
getChannels_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.I64, 'lastSynced', None, None, ),  # 2
    (3, TType.STRING, 'locale', 'UTF8', None, ),  # 3
)


class getChannels_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = ChannelInfos()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = ChannelException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getChannels_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getChannels_result)
getChannels_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [ChannelInfos, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [ChannelException, None], None, ),  # 1
)


class getDomains_args(object):
    """
    Attributes:
     - lastSynced
    """


    def __init__(self, lastSynced=None,):
        self.lastSynced = lastSynced

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.I64:
                    self.lastSynced = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getDomains_args')
        if self.lastSynced is not None:
            oprot.writeFieldBegin('lastSynced', TType.I64, 2)
            oprot.writeI64(self.lastSynced)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getDomains_args)
getDomains_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.I64, 'lastSynced', None, None, ),  # 2
)


class getDomains_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = ChannelDomains()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = ChannelException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getDomains_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getDomains_result)
getDomains_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [ChannelDomains, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [ChannelException, None], None, ),  # 1
)


class getFriendChannelMatrices_args(object):
    """
    Attributes:
     - channelIds
    """


    def __init__(self, channelIds=None,):
        self.channelIds = channelIds

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.channelIds = []
                    (_etype1274, _size1271) = iprot.readListBegin()
                    for _i1275 in range(_size1271):
                        _elem1276 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.channelIds.append(_elem1276)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getFriendChannelMatrices_args')
        if self.channelIds is not None:
            oprot.writeFieldBegin('channelIds', TType.LIST, 1)
            oprot.writeListBegin(TType.STRING, len(self.channelIds))
            for iter1277 in self.channelIds:
                oprot.writeString(iter1277.encode('utf-8') if sys.version_info[0] == 2 else iter1277)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getFriendChannelMatrices_args)
getFriendChannelMatrices_args.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'channelIds', (TType.STRING, 'UTF8', False), None, ),  # 1
)


class getFriendChannelMatrices_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = FriendChannelMatricesResponse()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = ChannelException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getFriendChannelMatrices_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getFriendChannelMatrices_result)
getFriendChannelMatrices_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [FriendChannelMatricesResponse, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [ChannelException, None], None, ),  # 1
)


class updateChannelSettings_args(object):
    """
    Attributes:
     - channelSettings
    """


    def __init__(self, channelSettings=None,):
        self.channelSettings = channelSettings

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.channelSettings = ChannelSettings()
                    self.channelSettings.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('updateChannelSettings_args')
        if self.channelSettings is not None:
            oprot.writeFieldBegin('channelSettings', TType.STRUCT, 1)
            self.channelSettings.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(updateChannelSettings_args)
updateChannelSettings_args.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'channelSettings', [ChannelSettings, None], None, ),  # 1
)


class updateChannelSettings_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.BOOL:
                    self.success = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = ChannelException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('updateChannelSettings_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.BOOL, 0)
            oprot.writeBool(self.success)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(updateChannelSettings_result)
updateChannelSettings_result.thrift_spec = (
    (0, TType.BOOL, 'success', None, None, ),  # 0
    (1, TType.STRUCT, 'e', [ChannelException, None], None, ),  # 1
)


class getCommonDomains_args(object):
    """
    Attributes:
     - lastSynced
    """


    def __init__(self, lastSynced=None,):
        self.lastSynced = lastSynced

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.lastSynced = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getCommonDomains_args')
        if self.lastSynced is not None:
            oprot.writeFieldBegin('lastSynced', TType.I64, 1)
            oprot.writeI64(self.lastSynced)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getCommonDomains_args)
getCommonDomains_args.thrift_spec = (
    None,  # 0
    (1, TType.I64, 'lastSynced', None, None, ),  # 1
)


class getCommonDomains_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = ChannelDomains()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = ChannelException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getCommonDomains_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getCommonDomains_result)
getCommonDomains_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [ChannelDomains, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [ChannelException, None], None, ),  # 1
)


class getNotificationBadgeCount_args(object):
    """
    Attributes:
     - localRev
    """


    def __init__(self, localRev=None,):
        self.localRev = localRev

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.I64:
                    self.localRev = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getNotificationBadgeCount_args')
        if self.localRev is not None:
            oprot.writeFieldBegin('localRev', TType.I64, 2)
            oprot.writeI64(self.localRev)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getNotificationBadgeCount_args)
getNotificationBadgeCount_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.I64, 'localRev', None, None, ),  # 2
)


class getNotificationBadgeCount_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I32:
                    self.success = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = ChannelException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getNotificationBadgeCount_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getNotificationBadgeCount_result)
getNotificationBadgeCount_result.thrift_spec = (
    (0, TType.I32, 'success', None, None, ),  # 0
    (1, TType.STRUCT, 'e', [ChannelException, None], None, ),  # 1
)


class issueChannelToken_args(object):
    """
    Attributes:
     - channelId
    """


    def __init__(self, channelId=None,):
        self.channelId = channelId

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.channelId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('issueChannelToken_args')
        if self.channelId is not None:
            oprot.writeFieldBegin('channelId', TType.STRING, 1)
            oprot.writeString(self.channelId.encode('utf-8') if sys.version_info[0] == 2 else self.channelId)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(issueChannelToken_args)
issueChannelToken_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'channelId', 'UTF8', None, ),  # 1
)


class issueChannelToken_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = ChannelToken()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = ChannelException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('issueChannelToken_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(issueChannelToken_result)
issueChannelToken_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [ChannelToken, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [ChannelException, None], None, ),  # 1
)


class issueRequestToken_args(object):
    """
    Attributes:
     - channelId
     - otpId
    """


    def __init__(self, channelId=None, otpId=None,):
        self.channelId = channelId
        self.otpId = otpId

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.channelId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.otpId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('issueRequestToken_args')
        if self.channelId is not None:
            oprot.writeFieldBegin('channelId', TType.STRING, 1)
            oprot.writeString(self.channelId.encode('utf-8') if sys.version_info[0] == 2 else self.channelId)
            oprot.writeFieldEnd()
        if self.otpId is not None:
            oprot.writeFieldBegin('otpId', TType.STRING, 2)
            oprot.writeString(self.otpId.encode('utf-8') if sys.version_info[0] == 2 else self.otpId)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(issueRequestToken_args)
issueRequestToken_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'channelId', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'otpId', 'UTF8', None, ),  # 2
)


class issueRequestToken_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRING:
                    self.success = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = ChannelException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('issueRequestToken_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRING, 0)
            oprot.writeString(self.success.encode('utf-8') if sys.version_info[0] == 2 else self.success)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(issueRequestToken_result)
issueRequestToken_result.thrift_spec = (
    (0, TType.STRING, 'success', 'UTF8', None, ),  # 0
    (1, TType.STRUCT, 'e', [ChannelException, None], None, ),  # 1
)


class issueRequestTokenWithAuthScheme_args(object):
    """
    Attributes:
     - channelId
     - otpId
     - authScheme
     - returnUrl
    """


    def __init__(self, channelId=None, otpId=None, authScheme=None, returnUrl=None,):
        self.channelId = channelId
        self.otpId = otpId
        self.authScheme = authScheme
        self.returnUrl = returnUrl

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.channelId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.otpId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.authScheme = []
                    (_etype1281, _size1278) = iprot.readListBegin()
                    for _i1282 in range(_size1278):
                        _elem1283 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.authScheme.append(_elem1283)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.returnUrl = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('issueRequestTokenWithAuthScheme_args')
        if self.channelId is not None:
            oprot.writeFieldBegin('channelId', TType.STRING, 1)
            oprot.writeString(self.channelId.encode('utf-8') if sys.version_info[0] == 2 else self.channelId)
            oprot.writeFieldEnd()
        if self.otpId is not None:
            oprot.writeFieldBegin('otpId', TType.STRING, 2)
            oprot.writeString(self.otpId.encode('utf-8') if sys.version_info[0] == 2 else self.otpId)
            oprot.writeFieldEnd()
        if self.authScheme is not None:
            oprot.writeFieldBegin('authScheme', TType.LIST, 3)
            oprot.writeListBegin(TType.STRING, len(self.authScheme))
            for iter1284 in self.authScheme:
                oprot.writeString(iter1284.encode('utf-8') if sys.version_info[0] == 2 else iter1284)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.returnUrl is not None:
            oprot.writeFieldBegin('returnUrl', TType.STRING, 4)
            oprot.writeString(self.returnUrl.encode('utf-8') if sys.version_info[0] == 2 else self.returnUrl)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(issueRequestTokenWithAuthScheme_args)
issueRequestTokenWithAuthScheme_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'channelId', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'otpId', 'UTF8', None, ),  # 2
    (3, TType.LIST, 'authScheme', (TType.STRING, 'UTF8', False), None, ),  # 3
    (4, TType.STRING, 'returnUrl', 'UTF8', None, ),  # 4
)


class issueRequestTokenWithAuthScheme_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = RequestTokenResponse()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = ChannelException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('issueRequestTokenWithAuthScheme_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(issueRequestTokenWithAuthScheme_result)
issueRequestTokenWithAuthScheme_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [RequestTokenResponse, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [ChannelException, None], None, ),  # 1
)


class issueRequestTokenForAutoLogin_args(object):
    """
    Attributes:
     - channelId
     - otpId
     - redirectUrl
    """


    def __init__(self, channelId=None, otpId=None, redirectUrl=None,):
        self.channelId = channelId
        self.otpId = otpId
        self.redirectUrl = redirectUrl

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRING:
                    self.channelId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.otpId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.redirectUrl = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('issueRequestTokenForAutoLogin_args')
        if self.channelId is not None:
            oprot.writeFieldBegin('channelId', TType.STRING, 2)
            oprot.writeString(self.channelId.encode('utf-8') if sys.version_info[0] == 2 else self.channelId)
            oprot.writeFieldEnd()
        if self.otpId is not None:
            oprot.writeFieldBegin('otpId', TType.STRING, 3)
            oprot.writeString(self.otpId.encode('utf-8') if sys.version_info[0] == 2 else self.otpId)
            oprot.writeFieldEnd()
        if self.redirectUrl is not None:
            oprot.writeFieldBegin('redirectUrl', TType.STRING, 4)
            oprot.writeString(self.redirectUrl.encode('utf-8') if sys.version_info[0] == 2 else self.redirectUrl)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(issueRequestTokenForAutoLogin_args)
issueRequestTokenForAutoLogin_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'channelId', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'otpId', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'redirectUrl', 'UTF8', None, ),  # 4
)


class issueRequestTokenForAutoLogin_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRING:
                    self.success = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = ChannelException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('issueRequestTokenForAutoLogin_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRING, 0)
            oprot.writeString(self.success.encode('utf-8') if sys.version_info[0] == 2 else self.success)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(issueRequestTokenForAutoLogin_result)
issueRequestTokenForAutoLogin_result.thrift_spec = (
    (0, TType.STRING, 'success', 'UTF8', None, ),  # 0
    (1, TType.STRUCT, 'e', [ChannelException, None], None, ),  # 1
)


class getUpdatedChannelIds_args(object):
    """
    Attributes:
     - channelIds
    """


    def __init__(self, channelIds=None,):
        self.channelIds = channelIds

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.channelIds = []
                    (_etype1288, _size1285) = iprot.readListBegin()
                    for _i1289 in range(_size1285):
                        _elem1290 = ChannelIdWithLastUpdated()
                        _elem1290.read(iprot)
                        self.channelIds.append(_elem1290)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getUpdatedChannelIds_args')
        if self.channelIds is not None:
            oprot.writeFieldBegin('channelIds', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.channelIds))
            for iter1291 in self.channelIds:
                iter1291.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getUpdatedChannelIds_args)
getUpdatedChannelIds_args.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'channelIds', (TType.STRUCT, [ChannelIdWithLastUpdated, None], False), None, ),  # 1
)


class getUpdatedChannelIds_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype1295, _size1292) = iprot.readListBegin()
                    for _i1296 in range(_size1292):
                        _elem1297 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.success.append(_elem1297)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = ChannelException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getUpdatedChannelIds_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRING, len(self.success))
            for iter1298 in self.success:
                oprot.writeString(iter1298.encode('utf-8') if sys.version_info[0] == 2 else iter1298)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getUpdatedChannelIds_result)
getUpdatedChannelIds_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRING, 'UTF8', False), None, ),  # 0
    (1, TType.STRUCT, 'e', [ChannelException, None], None, ),  # 1
)


class reserveCoinUse_args(object):
    """
    Attributes:
     - request
     - locale
    """


    def __init__(self, request=None, locale=None,):
        self.request = request
        self.locale = locale

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRUCT:
                    self.request = CoinUseReservation()
                    self.request.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.locale = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('reserveCoinUse_args')
        if self.request is not None:
            oprot.writeFieldBegin('request', TType.STRUCT, 2)
            self.request.write(oprot)
            oprot.writeFieldEnd()
        if self.locale is not None:
            oprot.writeFieldBegin('locale', TType.STRING, 3)
            oprot.writeString(self.locale.encode('utf-8') if sys.version_info[0] == 2 else self.locale)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(reserveCoinUse_args)
reserveCoinUse_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRUCT, 'request', [CoinUseReservation, None], None, ),  # 2
    (3, TType.STRING, 'locale', 'UTF8', None, ),  # 3
)


class reserveCoinUse_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRING:
                    self.success = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = ChannelException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('reserveCoinUse_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRING, 0)
            oprot.writeString(self.success.encode('utf-8') if sys.version_info[0] == 2 else self.success)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(reserveCoinUse_result)
reserveCoinUse_result.thrift_spec = (
    (0, TType.STRING, 'success', 'UTF8', None, ),  # 0
    (1, TType.STRUCT, 'e', [ChannelException, None], None, ),  # 1
)


class revokeChannel_args(object):
    """
    Attributes:
     - channelId
    """


    def __init__(self, channelId=None,):
        self.channelId = channelId

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.channelId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('revokeChannel_args')
        if self.channelId is not None:
            oprot.writeFieldBegin('channelId', TType.STRING, 1)
            oprot.writeString(self.channelId.encode('utf-8') if sys.version_info[0] == 2 else self.channelId)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(revokeChannel_args)
revokeChannel_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'channelId', 'UTF8', None, ),  # 1
)


class revokeChannel_result(object):
    """
    Attributes:
     - e
    """


    def __init__(self, e=None,):
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.e = ChannelException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('revokeChannel_result')
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(revokeChannel_result)
revokeChannel_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [ChannelException, None], None, ),  # 1
)


class syncChannelData_args(object):
    """
    Attributes:
     - lastSynced
     - locale
    """


    def __init__(self, lastSynced=None, locale=None,):
        self.lastSynced = lastSynced
        self.locale = locale

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.I64:
                    self.lastSynced = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.locale = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('syncChannelData_args')
        if self.lastSynced is not None:
            oprot.writeFieldBegin('lastSynced', TType.I64, 2)
            oprot.writeI64(self.lastSynced)
            oprot.writeFieldEnd()
        if self.locale is not None:
            oprot.writeFieldBegin('locale', TType.STRING, 3)
            oprot.writeString(self.locale.encode('utf-8') if sys.version_info[0] == 2 else self.locale)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(syncChannelData_args)
syncChannelData_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.I64, 'lastSynced', None, None, ),  # 2
    (3, TType.STRING, 'locale', 'UTF8', None, ),  # 3
)


class syncChannelData_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = ChannelSyncDatas()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = ChannelException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('syncChannelData_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(syncChannelData_result)
syncChannelData_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [ChannelSyncDatas, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [ChannelException, None], None, ),  # 1
)


class updateChannelNotificationSetting_args(object):
    """
    Attributes:
     - setting
    """


    def __init__(self, setting=None,):
        self.setting = setting

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.setting = []
                    (_etype1302, _size1299) = iprot.readListBegin()
                    for _i1303 in range(_size1299):
                        _elem1304 = ChannelNotificationSetting()
                        _elem1304.read(iprot)
                        self.setting.append(_elem1304)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('updateChannelNotificationSetting_args')
        if self.setting is not None:
            oprot.writeFieldBegin('setting', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.setting))
            for iter1305 in self.setting:
                iter1305.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(updateChannelNotificationSetting_args)
updateChannelNotificationSetting_args.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'setting', (TType.STRUCT, [ChannelNotificationSetting, None], False), None, ),  # 1
)


class updateChannelNotificationSetting_result(object):
    """
    Attributes:
     - e
    """


    def __init__(self, e=None,):
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.e = ChannelException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('updateChannelNotificationSetting_result')
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(updateChannelNotificationSetting_result)
updateChannelNotificationSetting_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [ChannelException, None], None, ),  # 1
)
fix_spec(all_structs)
del all_structs

