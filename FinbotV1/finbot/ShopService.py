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
    def buyCoinProduct(self, paymentReservation):
        """
        Parameters:
         - paymentReservation
        """
        pass

    def buyFreeProduct(self, receiverMid, productId, messageTemplate, language, country, packageId):
        """
        Parameters:
         - receiverMid
         - productId
         - messageTemplate
         - language
         - country
         - packageId
        """
        pass

    def buyMustbuyProduct(self, receiverMid, productId, messageTemplate, language, country, packageId, serialNumber):
        """
        Parameters:
         - receiverMid
         - productId
         - messageTemplate
         - language
         - country
         - packageId
         - serialNumber
        """
        pass

    def checkCanReceivePresent(self, recipientMid, packageId, language, country):
        """
        Parameters:
         - recipientMid
         - packageId
         - language
         - country
        """
        pass

    def getActivePurchases(self, start, size, language, country):
        """
        Parameters:
         - start
         - size
         - language
         - country
        """
        pass

    def getActivePurchaseVersions(self, start, size, language, country):
        """
        Parameters:
         - start
         - size
         - language
         - country
        """
        pass

    def getCoinProducts(self, appStoreCode, country, language):
        """
        Parameters:
         - appStoreCode
         - country
         - language
        """
        pass

    def getCoinProductsByPgCode(self, appStoreCode, pgCode, country, language):
        """
        Parameters:
         - appStoreCode
         - pgCode
         - country
         - language
        """
        pass

    def getCoinPurchaseHistory(self, request):
        """
        Parameters:
         - request
        """
        pass

    def getCoinUseAndRefundHistory(self, request):
        """
        Parameters:
         - request
        """
        pass

    def getDownloads(self, start, size, language, country):
        """
        Parameters:
         - start
         - size
         - language
         - country
        """
        pass

    def getEventPackages(self, start, size, language, country):
        """
        Parameters:
         - start
         - size
         - language
         - country
        """
        pass

    def getNewlyReleasedPackages(self, start, size, language, country):
        """
        Parameters:
         - start
         - size
         - language
         - country
        """
        pass

    def getPopularPackages(self, start, size, language, country):
        """
        Parameters:
         - start
         - size
         - language
         - country
        """
        pass

    def getPresentsReceived(self, start, size, language, country):
        """
        Parameters:
         - start
         - size
         - language
         - country
        """
        pass

    def getPresentsSent(self, start, size, language, country):
        """
        Parameters:
         - start
         - size
         - language
         - country
        """
        pass

    def getProduct(self, packageID, language, country):
        """
        Parameters:
         - packageID
         - language
         - country
        """
        pass

    def getProductList(self, productIdList, language, country):
        """
        Parameters:
         - productIdList
         - language
         - country
        """
        pass

    def getProductListWithCarrier(self, productIdList, language, country, carrierCode):
        """
        Parameters:
         - productIdList
         - language
         - country
         - carrierCode
        """
        pass

    def getProductWithCarrier(self, packageID, language, country, carrierCode):
        """
        Parameters:
         - packageID
         - language
         - country
         - carrierCode
        """
        pass

    def getPurchaseHistory(self, start, size, language, country):
        """
        Parameters:
         - start
         - size
         - language
         - country
        """
        pass

    def getTotalBalance(self, appStoreCode):
        """
        Parameters:
         - appStoreCode
        """
        pass

    def notifyDownloaded(self, packageId, language):
        """
        Parameters:
         - packageId
         - language
        """
        pass

    def reserveCoinPurchase(self, request):
        """
        Parameters:
         - request
        """
        pass

    def reservePayment(self, paymentReservation):
        """
        Parameters:
         - paymentReservation
        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def buyCoinProduct(self, paymentReservation):
        """
        Parameters:
         - paymentReservation
        """
        self.send_buyCoinProduct(paymentReservation)
        self.recv_buyCoinProduct()

    def send_buyCoinProduct(self, paymentReservation):
        self._oprot.writeMessageBegin('buyCoinProduct', TMessageType.CALL, self._seqid)
        args = buyCoinProduct_args()
        args.paymentReservation = paymentReservation
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_buyCoinProduct(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = buyCoinProduct_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def buyFreeProduct(self, receiverMid, productId, messageTemplate, language, country, packageId):
        """
        Parameters:
         - receiverMid
         - productId
         - messageTemplate
         - language
         - country
         - packageId
        """
        self.send_buyFreeProduct(receiverMid, productId, messageTemplate, language, country, packageId)
        self.recv_buyFreeProduct()

    def send_buyFreeProduct(self, receiverMid, productId, messageTemplate, language, country, packageId):
        self._oprot.writeMessageBegin('buyFreeProduct', TMessageType.CALL, self._seqid)
        args = buyFreeProduct_args()
        args.receiverMid = receiverMid
        args.productId = productId
        args.messageTemplate = messageTemplate
        args.language = language
        args.country = country
        args.packageId = packageId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_buyFreeProduct(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = buyFreeProduct_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def buyMustbuyProduct(self, receiverMid, productId, messageTemplate, language, country, packageId, serialNumber):
        """
        Parameters:
         - receiverMid
         - productId
         - messageTemplate
         - language
         - country
         - packageId
         - serialNumber
        """
        self.send_buyMustbuyProduct(receiverMid, productId, messageTemplate, language, country, packageId, serialNumber)
        self.recv_buyMustbuyProduct()

    def send_buyMustbuyProduct(self, receiverMid, productId, messageTemplate, language, country, packageId, serialNumber):
        self._oprot.writeMessageBegin('buyMustbuyProduct', TMessageType.CALL, self._seqid)
        args = buyMustbuyProduct_args()
        args.receiverMid = receiverMid
        args.productId = productId
        args.messageTemplate = messageTemplate
        args.language = language
        args.country = country
        args.packageId = packageId
        args.serialNumber = serialNumber
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_buyMustbuyProduct(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = buyMustbuyProduct_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def checkCanReceivePresent(self, recipientMid, packageId, language, country):
        """
        Parameters:
         - recipientMid
         - packageId
         - language
         - country
        """
        self.send_checkCanReceivePresent(recipientMid, packageId, language, country)
        self.recv_checkCanReceivePresent()

    def send_checkCanReceivePresent(self, recipientMid, packageId, language, country):
        self._oprot.writeMessageBegin('checkCanReceivePresent', TMessageType.CALL, self._seqid)
        args = checkCanReceivePresent_args()
        args.recipientMid = recipientMid
        args.packageId = packageId
        args.language = language
        args.country = country
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_checkCanReceivePresent(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = checkCanReceivePresent_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def getActivePurchases(self, start, size, language, country):
        """
        Parameters:
         - start
         - size
         - language
         - country
        """
        self.send_getActivePurchases(start, size, language, country)
        return self.recv_getActivePurchases()

    def send_getActivePurchases(self, start, size, language, country):
        self._oprot.writeMessageBegin('getActivePurchases', TMessageType.CALL, self._seqid)
        args = getActivePurchases_args()
        args.start = start
        args.size = size
        args.language = language
        args.country = country
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getActivePurchases(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getActivePurchases_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getActivePurchases failed: unknown result")

    def getActivePurchaseVersions(self, start, size, language, country):
        """
        Parameters:
         - start
         - size
         - language
         - country
        """
        self.send_getActivePurchaseVersions(start, size, language, country)
        return self.recv_getActivePurchaseVersions()

    def send_getActivePurchaseVersions(self, start, size, language, country):
        self._oprot.writeMessageBegin('getActivePurchaseVersions', TMessageType.CALL, self._seqid)
        args = getActivePurchaseVersions_args()
        args.start = start
        args.size = size
        args.language = language
        args.country = country
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getActivePurchaseVersions(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getActivePurchaseVersions_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getActivePurchaseVersions failed: unknown result")

    def getCoinProducts(self, appStoreCode, country, language):
        """
        Parameters:
         - appStoreCode
         - country
         - language
        """
        self.send_getCoinProducts(appStoreCode, country, language)
        return self.recv_getCoinProducts()

    def send_getCoinProducts(self, appStoreCode, country, language):
        self._oprot.writeMessageBegin('getCoinProducts', TMessageType.CALL, self._seqid)
        args = getCoinProducts_args()
        args.appStoreCode = appStoreCode
        args.country = country
        args.language = language
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getCoinProducts(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getCoinProducts_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getCoinProducts failed: unknown result")

    def getCoinProductsByPgCode(self, appStoreCode, pgCode, country, language):
        """
        Parameters:
         - appStoreCode
         - pgCode
         - country
         - language
        """
        self.send_getCoinProductsByPgCode(appStoreCode, pgCode, country, language)
        return self.recv_getCoinProductsByPgCode()

    def send_getCoinProductsByPgCode(self, appStoreCode, pgCode, country, language):
        self._oprot.writeMessageBegin('getCoinProductsByPgCode', TMessageType.CALL, self._seqid)
        args = getCoinProductsByPgCode_args()
        args.appStoreCode = appStoreCode
        args.pgCode = pgCode
        args.country = country
        args.language = language
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getCoinProductsByPgCode(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getCoinProductsByPgCode_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getCoinProductsByPgCode failed: unknown result")

    def getCoinPurchaseHistory(self, request):
        """
        Parameters:
         - request
        """
        self.send_getCoinPurchaseHistory(request)
        return self.recv_getCoinPurchaseHistory()

    def send_getCoinPurchaseHistory(self, request):
        self._oprot.writeMessageBegin('getCoinPurchaseHistory', TMessageType.CALL, self._seqid)
        args = getCoinPurchaseHistory_args()
        args.request = request
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getCoinPurchaseHistory(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getCoinPurchaseHistory_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getCoinPurchaseHistory failed: unknown result")

    def getCoinUseAndRefundHistory(self, request):
        """
        Parameters:
         - request
        """
        self.send_getCoinUseAndRefundHistory(request)
        return self.recv_getCoinUseAndRefundHistory()

    def send_getCoinUseAndRefundHistory(self, request):
        self._oprot.writeMessageBegin('getCoinUseAndRefundHistory', TMessageType.CALL, self._seqid)
        args = getCoinUseAndRefundHistory_args()
        args.request = request
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getCoinUseAndRefundHistory(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getCoinUseAndRefundHistory_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getCoinUseAndRefundHistory failed: unknown result")

    def getDownloads(self, start, size, language, country):
        """
        Parameters:
         - start
         - size
         - language
         - country
        """
        self.send_getDownloads(start, size, language, country)
        return self.recv_getDownloads()

    def send_getDownloads(self, start, size, language, country):
        self._oprot.writeMessageBegin('getDownloads', TMessageType.CALL, self._seqid)
        args = getDownloads_args()
        args.start = start
        args.size = size
        args.language = language
        args.country = country
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getDownloads(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getDownloads_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getDownloads failed: unknown result")

    def getEventPackages(self, start, size, language, country):
        """
        Parameters:
         - start
         - size
         - language
         - country
        """
        self.send_getEventPackages(start, size, language, country)
        return self.recv_getEventPackages()

    def send_getEventPackages(self, start, size, language, country):
        self._oprot.writeMessageBegin('getEventPackages', TMessageType.CALL, self._seqid)
        args = getEventPackages_args()
        args.start = start
        args.size = size
        args.language = language
        args.country = country
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getEventPackages(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getEventPackages_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getEventPackages failed: unknown result")

    def getNewlyReleasedPackages(self, start, size, language, country):
        """
        Parameters:
         - start
         - size
         - language
         - country
        """
        self.send_getNewlyReleasedPackages(start, size, language, country)
        return self.recv_getNewlyReleasedPackages()

    def send_getNewlyReleasedPackages(self, start, size, language, country):
        self._oprot.writeMessageBegin('getNewlyReleasedPackages', TMessageType.CALL, self._seqid)
        args = getNewlyReleasedPackages_args()
        args.start = start
        args.size = size
        args.language = language
        args.country = country
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getNewlyReleasedPackages(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getNewlyReleasedPackages_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getNewlyReleasedPackages failed: unknown result")

    def getPopularPackages(self, start, size, language, country):
        """
        Parameters:
         - start
         - size
         - language
         - country
        """
        self.send_getPopularPackages(start, size, language, country)
        return self.recv_getPopularPackages()

    def send_getPopularPackages(self, start, size, language, country):
        self._oprot.writeMessageBegin('getPopularPackages', TMessageType.CALL, self._seqid)
        args = getPopularPackages_args()
        args.start = start
        args.size = size
        args.language = language
        args.country = country
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getPopularPackages(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getPopularPackages_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getPopularPackages failed: unknown result")

    def getPresentsReceived(self, start, size, language, country):
        """
        Parameters:
         - start
         - size
         - language
         - country
        """
        self.send_getPresentsReceived(start, size, language, country)
        return self.recv_getPresentsReceived()

    def send_getPresentsReceived(self, start, size, language, country):
        self._oprot.writeMessageBegin('getPresentsReceived', TMessageType.CALL, self._seqid)
        args = getPresentsReceived_args()
        args.start = start
        args.size = size
        args.language = language
        args.country = country
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getPresentsReceived(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getPresentsReceived_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getPresentsReceived failed: unknown result")

    def getPresentsSent(self, start, size, language, country):
        """
        Parameters:
         - start
         - size
         - language
         - country
        """
        self.send_getPresentsSent(start, size, language, country)
        return self.recv_getPresentsSent()

    def send_getPresentsSent(self, start, size, language, country):
        self._oprot.writeMessageBegin('getPresentsSent', TMessageType.CALL, self._seqid)
        args = getPresentsSent_args()
        args.start = start
        args.size = size
        args.language = language
        args.country = country
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getPresentsSent(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getPresentsSent_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getPresentsSent failed: unknown result")

    def getProduct(self, packageID, language, country):
        """
        Parameters:
         - packageID
         - language
         - country
        """
        self.send_getProduct(packageID, language, country)
        return self.recv_getProduct()

    def send_getProduct(self, packageID, language, country):
        self._oprot.writeMessageBegin('getProduct', TMessageType.CALL, self._seqid)
        args = getProduct_args()
        args.packageID = packageID
        args.language = language
        args.country = country
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getProduct(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getProduct_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getProduct failed: unknown result")

    def getProductList(self, productIdList, language, country):
        """
        Parameters:
         - productIdList
         - language
         - country
        """
        self.send_getProductList(productIdList, language, country)
        return self.recv_getProductList()

    def send_getProductList(self, productIdList, language, country):
        self._oprot.writeMessageBegin('getProductList', TMessageType.CALL, self._seqid)
        args = getProductList_args()
        args.productIdList = productIdList
        args.language = language
        args.country = country
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getProductList(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getProductList_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getProductList failed: unknown result")

    def getProductListWithCarrier(self, productIdList, language, country, carrierCode):
        """
        Parameters:
         - productIdList
         - language
         - country
         - carrierCode
        """
        self.send_getProductListWithCarrier(productIdList, language, country, carrierCode)
        return self.recv_getProductListWithCarrier()

    def send_getProductListWithCarrier(self, productIdList, language, country, carrierCode):
        self._oprot.writeMessageBegin('getProductListWithCarrier', TMessageType.CALL, self._seqid)
        args = getProductListWithCarrier_args()
        args.productIdList = productIdList
        args.language = language
        args.country = country
        args.carrierCode = carrierCode
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getProductListWithCarrier(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getProductListWithCarrier_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getProductListWithCarrier failed: unknown result")

    def getProductWithCarrier(self, packageID, language, country, carrierCode):
        """
        Parameters:
         - packageID
         - language
         - country
         - carrierCode
        """
        self.send_getProductWithCarrier(packageID, language, country, carrierCode)
        return self.recv_getProductWithCarrier()

    def send_getProductWithCarrier(self, packageID, language, country, carrierCode):
        self._oprot.writeMessageBegin('getProductWithCarrier', TMessageType.CALL, self._seqid)
        args = getProductWithCarrier_args()
        args.packageID = packageID
        args.language = language
        args.country = country
        args.carrierCode = carrierCode
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getProductWithCarrier(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getProductWithCarrier_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getProductWithCarrier failed: unknown result")

    def getPurchaseHistory(self, start, size, language, country):
        """
        Parameters:
         - start
         - size
         - language
         - country
        """
        self.send_getPurchaseHistory(start, size, language, country)
        return self.recv_getPurchaseHistory()

    def send_getPurchaseHistory(self, start, size, language, country):
        self._oprot.writeMessageBegin('getPurchaseHistory', TMessageType.CALL, self._seqid)
        args = getPurchaseHistory_args()
        args.start = start
        args.size = size
        args.language = language
        args.country = country
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getPurchaseHistory(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getPurchaseHistory_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getPurchaseHistory failed: unknown result")

    def getTotalBalance(self, appStoreCode):
        """
        Parameters:
         - appStoreCode
        """
        self.send_getTotalBalance(appStoreCode)
        return self.recv_getTotalBalance()

    def send_getTotalBalance(self, appStoreCode):
        self._oprot.writeMessageBegin('getTotalBalance', TMessageType.CALL, self._seqid)
        args = getTotalBalance_args()
        args.appStoreCode = appStoreCode
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getTotalBalance(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getTotalBalance_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getTotalBalance failed: unknown result")

    def notifyDownloaded(self, packageId, language):
        """
        Parameters:
         - packageId
         - language
        """
        self.send_notifyDownloaded(packageId, language)
        return self.recv_notifyDownloaded()

    def send_notifyDownloaded(self, packageId, language):
        self._oprot.writeMessageBegin('notifyDownloaded', TMessageType.CALL, self._seqid)
        args = notifyDownloaded_args()
        args.packageId = packageId
        args.language = language
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_notifyDownloaded(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = notifyDownloaded_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "notifyDownloaded failed: unknown result")

    def reserveCoinPurchase(self, request):
        """
        Parameters:
         - request
        """
        self.send_reserveCoinPurchase(request)
        return self.recv_reserveCoinPurchase()

    def send_reserveCoinPurchase(self, request):
        self._oprot.writeMessageBegin('reserveCoinPurchase', TMessageType.CALL, self._seqid)
        args = reserveCoinPurchase_args()
        args.request = request
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_reserveCoinPurchase(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = reserveCoinPurchase_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "reserveCoinPurchase failed: unknown result")

    def reservePayment(self, paymentReservation):
        """
        Parameters:
         - paymentReservation
        """
        self.send_reservePayment(paymentReservation)
        return self.recv_reservePayment()

    def send_reservePayment(self, paymentReservation):
        self._oprot.writeMessageBegin('reservePayment', TMessageType.CALL, self._seqid)
        args = reservePayment_args()
        args.paymentReservation = paymentReservation
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_reservePayment(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = reservePayment_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "reservePayment failed: unknown result")


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["buyCoinProduct"] = Processor.process_buyCoinProduct
        self._processMap["buyFreeProduct"] = Processor.process_buyFreeProduct
        self._processMap["buyMustbuyProduct"] = Processor.process_buyMustbuyProduct
        self._processMap["checkCanReceivePresent"] = Processor.process_checkCanReceivePresent
        self._processMap["getActivePurchases"] = Processor.process_getActivePurchases
        self._processMap["getActivePurchaseVersions"] = Processor.process_getActivePurchaseVersions
        self._processMap["getCoinProducts"] = Processor.process_getCoinProducts
        self._processMap["getCoinProductsByPgCode"] = Processor.process_getCoinProductsByPgCode
        self._processMap["getCoinPurchaseHistory"] = Processor.process_getCoinPurchaseHistory
        self._processMap["getCoinUseAndRefundHistory"] = Processor.process_getCoinUseAndRefundHistory
        self._processMap["getDownloads"] = Processor.process_getDownloads
        self._processMap["getEventPackages"] = Processor.process_getEventPackages
        self._processMap["getNewlyReleasedPackages"] = Processor.process_getNewlyReleasedPackages
        self._processMap["getPopularPackages"] = Processor.process_getPopularPackages
        self._processMap["getPresentsReceived"] = Processor.process_getPresentsReceived
        self._processMap["getPresentsSent"] = Processor.process_getPresentsSent
        self._processMap["getProduct"] = Processor.process_getProduct
        self._processMap["getProductList"] = Processor.process_getProductList
        self._processMap["getProductListWithCarrier"] = Processor.process_getProductListWithCarrier
        self._processMap["getProductWithCarrier"] = Processor.process_getProductWithCarrier
        self._processMap["getPurchaseHistory"] = Processor.process_getPurchaseHistory
        self._processMap["getTotalBalance"] = Processor.process_getTotalBalance
        self._processMap["notifyDownloaded"] = Processor.process_notifyDownloaded
        self._processMap["reserveCoinPurchase"] = Processor.process_reserveCoinPurchase
        self._processMap["reservePayment"] = Processor.process_reservePayment

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

    def process_buyCoinProduct(self, seqid, iprot, oprot):
        args = buyCoinProduct_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = buyCoinProduct_result()
        try:
            self._handler.buyCoinProduct(args.paymentReservation)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
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
        oprot.writeMessageBegin("buyCoinProduct", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_buyFreeProduct(self, seqid, iprot, oprot):
        args = buyFreeProduct_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = buyFreeProduct_result()
        try:
            self._handler.buyFreeProduct(args.receiverMid, args.productId, args.messageTemplate, args.language, args.country, args.packageId)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
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
        oprot.writeMessageBegin("buyFreeProduct", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_buyMustbuyProduct(self, seqid, iprot, oprot):
        args = buyMustbuyProduct_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = buyMustbuyProduct_result()
        try:
            self._handler.buyMustbuyProduct(args.receiverMid, args.productId, args.messageTemplate, args.language, args.country, args.packageId, args.serialNumber)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
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
        oprot.writeMessageBegin("buyMustbuyProduct", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_checkCanReceivePresent(self, seqid, iprot, oprot):
        args = checkCanReceivePresent_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = checkCanReceivePresent_result()
        try:
            self._handler.checkCanReceivePresent(args.recipientMid, args.packageId, args.language, args.country)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
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
        oprot.writeMessageBegin("checkCanReceivePresent", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getActivePurchases(self, seqid, iprot, oprot):
        args = getActivePurchases_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getActivePurchases_result()
        try:
            result.success = self._handler.getActivePurchases(args.start, args.size, args.language, args.country)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
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
        oprot.writeMessageBegin("getActivePurchases", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getActivePurchaseVersions(self, seqid, iprot, oprot):
        args = getActivePurchaseVersions_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getActivePurchaseVersions_result()
        try:
            result.success = self._handler.getActivePurchaseVersions(args.start, args.size, args.language, args.country)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
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
        oprot.writeMessageBegin("getActivePurchaseVersions", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getCoinProducts(self, seqid, iprot, oprot):
        args = getCoinProducts_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getCoinProducts_result()
        try:
            result.success = self._handler.getCoinProducts(args.appStoreCode, args.country, args.language)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
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
        oprot.writeMessageBegin("getCoinProducts", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getCoinProductsByPgCode(self, seqid, iprot, oprot):
        args = getCoinProductsByPgCode_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getCoinProductsByPgCode_result()
        try:
            result.success = self._handler.getCoinProductsByPgCode(args.appStoreCode, args.pgCode, args.country, args.language)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
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
        oprot.writeMessageBegin("getCoinProductsByPgCode", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getCoinPurchaseHistory(self, seqid, iprot, oprot):
        args = getCoinPurchaseHistory_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getCoinPurchaseHistory_result()
        try:
            result.success = self._handler.getCoinPurchaseHistory(args.request)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
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
        oprot.writeMessageBegin("getCoinPurchaseHistory", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getCoinUseAndRefundHistory(self, seqid, iprot, oprot):
        args = getCoinUseAndRefundHistory_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getCoinUseAndRefundHistory_result()
        try:
            result.success = self._handler.getCoinUseAndRefundHistory(args.request)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
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
        oprot.writeMessageBegin("getCoinUseAndRefundHistory", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getDownloads(self, seqid, iprot, oprot):
        args = getDownloads_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getDownloads_result()
        try:
            result.success = self._handler.getDownloads(args.start, args.size, args.language, args.country)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
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
        oprot.writeMessageBegin("getDownloads", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getEventPackages(self, seqid, iprot, oprot):
        args = getEventPackages_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getEventPackages_result()
        try:
            result.success = self._handler.getEventPackages(args.start, args.size, args.language, args.country)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
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
        oprot.writeMessageBegin("getEventPackages", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getNewlyReleasedPackages(self, seqid, iprot, oprot):
        args = getNewlyReleasedPackages_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getNewlyReleasedPackages_result()
        try:
            result.success = self._handler.getNewlyReleasedPackages(args.start, args.size, args.language, args.country)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
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
        oprot.writeMessageBegin("getNewlyReleasedPackages", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getPopularPackages(self, seqid, iprot, oprot):
        args = getPopularPackages_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getPopularPackages_result()
        try:
            result.success = self._handler.getPopularPackages(args.start, args.size, args.language, args.country)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
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
        oprot.writeMessageBegin("getPopularPackages", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getPresentsReceived(self, seqid, iprot, oprot):
        args = getPresentsReceived_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getPresentsReceived_result()
        try:
            result.success = self._handler.getPresentsReceived(args.start, args.size, args.language, args.country)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
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
        oprot.writeMessageBegin("getPresentsReceived", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getPresentsSent(self, seqid, iprot, oprot):
        args = getPresentsSent_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getPresentsSent_result()
        try:
            result.success = self._handler.getPresentsSent(args.start, args.size, args.language, args.country)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
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
        oprot.writeMessageBegin("getPresentsSent", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getProduct(self, seqid, iprot, oprot):
        args = getProduct_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getProduct_result()
        try:
            result.success = self._handler.getProduct(args.packageID, args.language, args.country)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
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
        oprot.writeMessageBegin("getProduct", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getProductList(self, seqid, iprot, oprot):
        args = getProductList_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getProductList_result()
        try:
            result.success = self._handler.getProductList(args.productIdList, args.language, args.country)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
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
        oprot.writeMessageBegin("getProductList", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getProductListWithCarrier(self, seqid, iprot, oprot):
        args = getProductListWithCarrier_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getProductListWithCarrier_result()
        try:
            result.success = self._handler.getProductListWithCarrier(args.productIdList, args.language, args.country, args.carrierCode)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
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
        oprot.writeMessageBegin("getProductListWithCarrier", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getProductWithCarrier(self, seqid, iprot, oprot):
        args = getProductWithCarrier_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getProductWithCarrier_result()
        try:
            result.success = self._handler.getProductWithCarrier(args.packageID, args.language, args.country, args.carrierCode)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
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
        oprot.writeMessageBegin("getProductWithCarrier", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getPurchaseHistory(self, seqid, iprot, oprot):
        args = getPurchaseHistory_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getPurchaseHistory_result()
        try:
            result.success = self._handler.getPurchaseHistory(args.start, args.size, args.language, args.country)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
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
        oprot.writeMessageBegin("getPurchaseHistory", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getTotalBalance(self, seqid, iprot, oprot):
        args = getTotalBalance_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getTotalBalance_result()
        try:
            result.success = self._handler.getTotalBalance(args.appStoreCode)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
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
        oprot.writeMessageBegin("getTotalBalance", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_notifyDownloaded(self, seqid, iprot, oprot):
        args = notifyDownloaded_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = notifyDownloaded_result()
        try:
            result.success = self._handler.notifyDownloaded(args.packageId, args.language)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
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
        oprot.writeMessageBegin("notifyDownloaded", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_reserveCoinPurchase(self, seqid, iprot, oprot):
        args = reserveCoinPurchase_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = reserveCoinPurchase_result()
        try:
            result.success = self._handler.reserveCoinPurchase(args.request)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
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
        oprot.writeMessageBegin("reserveCoinPurchase", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_reservePayment(self, seqid, iprot, oprot):
        args = reservePayment_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = reservePayment_result()
        try:
            result.success = self._handler.reservePayment(args.paymentReservation)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
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
        oprot.writeMessageBegin("reservePayment", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class buyCoinProduct_args(object):
    """
    Attributes:
     - paymentReservation
    """


    def __init__(self, paymentReservation=None,):
        self.paymentReservation = paymentReservation

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
                    self.paymentReservation = PaymentReservation()
                    self.paymentReservation.read(iprot)
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
        oprot.writeStructBegin('buyCoinProduct_args')
        if self.paymentReservation is not None:
            oprot.writeFieldBegin('paymentReservation', TType.STRUCT, 2)
            self.paymentReservation.write(oprot)
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
all_structs.append(buyCoinProduct_args)
buyCoinProduct_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRUCT, 'paymentReservation', [PaymentReservation, None], None, ),  # 2
)


class buyCoinProduct_result(object):
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
                    self.e = TalkException()
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
        oprot.writeStructBegin('buyCoinProduct_result')
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
all_structs.append(buyCoinProduct_result)
buyCoinProduct_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class buyFreeProduct_args(object):
    """
    Attributes:
     - receiverMid
     - productId
     - messageTemplate
     - language
     - country
     - packageId
    """


    def __init__(self, receiverMid=None, productId=None, messageTemplate=None, language=None, country=None, packageId=None,):
        self.receiverMid = receiverMid
        self.productId = productId
        self.messageTemplate = messageTemplate
        self.language = language
        self.country = country
        self.packageId = packageId

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
                    self.receiverMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.productId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.messageTemplate = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.language = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.country = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I64:
                    self.packageId = iprot.readI64()
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
        oprot.writeStructBegin('buyFreeProduct_args')
        if self.receiverMid is not None:
            oprot.writeFieldBegin('receiverMid', TType.STRING, 2)
            oprot.writeString(self.receiverMid.encode('utf-8') if sys.version_info[0] == 2 else self.receiverMid)
            oprot.writeFieldEnd()
        if self.productId is not None:
            oprot.writeFieldBegin('productId', TType.STRING, 3)
            oprot.writeString(self.productId.encode('utf-8') if sys.version_info[0] == 2 else self.productId)
            oprot.writeFieldEnd()
        if self.messageTemplate is not None:
            oprot.writeFieldBegin('messageTemplate', TType.I32, 4)
            oprot.writeI32(self.messageTemplate)
            oprot.writeFieldEnd()
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 5)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        if self.country is not None:
            oprot.writeFieldBegin('country', TType.STRING, 6)
            oprot.writeString(self.country.encode('utf-8') if sys.version_info[0] == 2 else self.country)
            oprot.writeFieldEnd()
        if self.packageId is not None:
            oprot.writeFieldBegin('packageId', TType.I64, 7)
            oprot.writeI64(self.packageId)
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
all_structs.append(buyFreeProduct_args)
buyFreeProduct_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'receiverMid', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'productId', 'UTF8', None, ),  # 3
    (4, TType.I32, 'messageTemplate', None, None, ),  # 4
    (5, TType.STRING, 'language', 'UTF8', None, ),  # 5
    (6, TType.STRING, 'country', 'UTF8', None, ),  # 6
    (7, TType.I64, 'packageId', None, None, ),  # 7
)


class buyFreeProduct_result(object):
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
                    self.e = TalkException()
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
        oprot.writeStructBegin('buyFreeProduct_result')
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
all_structs.append(buyFreeProduct_result)
buyFreeProduct_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class buyMustbuyProduct_args(object):
    """
    Attributes:
     - receiverMid
     - productId
     - messageTemplate
     - language
     - country
     - packageId
     - serialNumber
    """


    def __init__(self, receiverMid=None, productId=None, messageTemplate=None, language=None, country=None, packageId=None, serialNumber=None,):
        self.receiverMid = receiverMid
        self.productId = productId
        self.messageTemplate = messageTemplate
        self.language = language
        self.country = country
        self.packageId = packageId
        self.serialNumber = serialNumber

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
                    self.receiverMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.productId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.messageTemplate = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.language = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.country = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I64:
                    self.packageId = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.serialNumber = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('buyMustbuyProduct_args')
        if self.receiverMid is not None:
            oprot.writeFieldBegin('receiverMid', TType.STRING, 2)
            oprot.writeString(self.receiverMid.encode('utf-8') if sys.version_info[0] == 2 else self.receiverMid)
            oprot.writeFieldEnd()
        if self.productId is not None:
            oprot.writeFieldBegin('productId', TType.STRING, 3)
            oprot.writeString(self.productId.encode('utf-8') if sys.version_info[0] == 2 else self.productId)
            oprot.writeFieldEnd()
        if self.messageTemplate is not None:
            oprot.writeFieldBegin('messageTemplate', TType.I32, 4)
            oprot.writeI32(self.messageTemplate)
            oprot.writeFieldEnd()
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 5)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        if self.country is not None:
            oprot.writeFieldBegin('country', TType.STRING, 6)
            oprot.writeString(self.country.encode('utf-8') if sys.version_info[0] == 2 else self.country)
            oprot.writeFieldEnd()
        if self.packageId is not None:
            oprot.writeFieldBegin('packageId', TType.I64, 7)
            oprot.writeI64(self.packageId)
            oprot.writeFieldEnd()
        if self.serialNumber is not None:
            oprot.writeFieldBegin('serialNumber', TType.STRING, 8)
            oprot.writeString(self.serialNumber.encode('utf-8') if sys.version_info[0] == 2 else self.serialNumber)
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
all_structs.append(buyMustbuyProduct_args)
buyMustbuyProduct_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'receiverMid', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'productId', 'UTF8', None, ),  # 3
    (4, TType.I32, 'messageTemplate', None, None, ),  # 4
    (5, TType.STRING, 'language', 'UTF8', None, ),  # 5
    (6, TType.STRING, 'country', 'UTF8', None, ),  # 6
    (7, TType.I64, 'packageId', None, None, ),  # 7
    (8, TType.STRING, 'serialNumber', 'UTF8', None, ),  # 8
)


class buyMustbuyProduct_result(object):
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
                    self.e = TalkException()
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
        oprot.writeStructBegin('buyMustbuyProduct_result')
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
all_structs.append(buyMustbuyProduct_result)
buyMustbuyProduct_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class checkCanReceivePresent_args(object):
    """
    Attributes:
     - recipientMid
     - packageId
     - language
     - country
    """


    def __init__(self, recipientMid=None, packageId=None, language=None, country=None,):
        self.recipientMid = recipientMid
        self.packageId = packageId
        self.language = language
        self.country = country

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
                    self.recipientMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.packageId = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.language = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.country = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('checkCanReceivePresent_args')
        if self.recipientMid is not None:
            oprot.writeFieldBegin('recipientMid', TType.STRING, 2)
            oprot.writeString(self.recipientMid.encode('utf-8') if sys.version_info[0] == 2 else self.recipientMid)
            oprot.writeFieldEnd()
        if self.packageId is not None:
            oprot.writeFieldBegin('packageId', TType.I64, 3)
            oprot.writeI64(self.packageId)
            oprot.writeFieldEnd()
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 4)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        if self.country is not None:
            oprot.writeFieldBegin('country', TType.STRING, 5)
            oprot.writeString(self.country.encode('utf-8') if sys.version_info[0] == 2 else self.country)
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
all_structs.append(checkCanReceivePresent_args)
checkCanReceivePresent_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'recipientMid', 'UTF8', None, ),  # 2
    (3, TType.I64, 'packageId', None, None, ),  # 3
    (4, TType.STRING, 'language', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'country', 'UTF8', None, ),  # 5
)


class checkCanReceivePresent_result(object):
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
                    self.e = TalkException()
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
        oprot.writeStructBegin('checkCanReceivePresent_result')
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
all_structs.append(checkCanReceivePresent_result)
checkCanReceivePresent_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getActivePurchases_args(object):
    """
    Attributes:
     - start
     - size
     - language
     - country
    """


    def __init__(self, start=None, size=None, language=None, country=None,):
        self.start = start
        self.size = size
        self.language = language
        self.country = country

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
                    self.start = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.size = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.language = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.country = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('getActivePurchases_args')
        if self.start is not None:
            oprot.writeFieldBegin('start', TType.I64, 2)
            oprot.writeI64(self.start)
            oprot.writeFieldEnd()
        if self.size is not None:
            oprot.writeFieldBegin('size', TType.I32, 3)
            oprot.writeI32(self.size)
            oprot.writeFieldEnd()
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 4)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        if self.country is not None:
            oprot.writeFieldBegin('country', TType.STRING, 5)
            oprot.writeString(self.country.encode('utf-8') if sys.version_info[0] == 2 else self.country)
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
all_structs.append(getActivePurchases_args)
getActivePurchases_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.I64, 'start', None, None, ),  # 2
    (3, TType.I32, 'size', None, None, ),  # 3
    (4, TType.STRING, 'language', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'country', 'UTF8', None, ),  # 5
)


class getActivePurchases_result(object):
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
                    self.success = ProductList()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
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
        oprot.writeStructBegin('getActivePurchases_result')
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
all_structs.append(getActivePurchases_result)
getActivePurchases_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [ProductList, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getActivePurchaseVersions_args(object):
    """
    Attributes:
     - start
     - size
     - language
     - country
    """


    def __init__(self, start=None, size=None, language=None, country=None,):
        self.start = start
        self.size = size
        self.language = language
        self.country = country

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
                    self.start = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.size = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.language = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.country = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('getActivePurchaseVersions_args')
        if self.start is not None:
            oprot.writeFieldBegin('start', TType.I64, 2)
            oprot.writeI64(self.start)
            oprot.writeFieldEnd()
        if self.size is not None:
            oprot.writeFieldBegin('size', TType.I32, 3)
            oprot.writeI32(self.size)
            oprot.writeFieldEnd()
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 4)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        if self.country is not None:
            oprot.writeFieldBegin('country', TType.STRING, 5)
            oprot.writeString(self.country.encode('utf-8') if sys.version_info[0] == 2 else self.country)
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
all_structs.append(getActivePurchaseVersions_args)
getActivePurchaseVersions_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.I64, 'start', None, None, ),  # 2
    (3, TType.I32, 'size', None, None, ),  # 3
    (4, TType.STRING, 'language', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'country', 'UTF8', None, ),  # 5
)


class getActivePurchaseVersions_result(object):
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
                    self.success = ProductSimpleList()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
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
        oprot.writeStructBegin('getActivePurchaseVersions_result')
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
all_structs.append(getActivePurchaseVersions_result)
getActivePurchaseVersions_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [ProductSimpleList, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getCoinProducts_args(object):
    """
    Attributes:
     - appStoreCode
     - country
     - language
    """


    def __init__(self, appStoreCode=None, country=None, language=None,):
        self.appStoreCode = appStoreCode
        self.country = country
        self.language = language

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
                if ftype == TType.I32:
                    self.appStoreCode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.country = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.language = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('getCoinProducts_args')
        if self.appStoreCode is not None:
            oprot.writeFieldBegin('appStoreCode', TType.I32, 2)
            oprot.writeI32(self.appStoreCode)
            oprot.writeFieldEnd()
        if self.country is not None:
            oprot.writeFieldBegin('country', TType.STRING, 3)
            oprot.writeString(self.country.encode('utf-8') if sys.version_info[0] == 2 else self.country)
            oprot.writeFieldEnd()
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 4)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
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
all_structs.append(getCoinProducts_args)
getCoinProducts_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.I32, 'appStoreCode', None, None, ),  # 2
    (3, TType.STRING, 'country', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'language', 'UTF8', None, ),  # 4
)


class getCoinProducts_result(object):
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
                    (_etype1323, _size1320) = iprot.readListBegin()
                    for _i1324 in range(_size1320):
                        _elem1325 = CoinProductItem()
                        _elem1325.read(iprot)
                        self.success.append(_elem1325)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
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
        oprot.writeStructBegin('getCoinProducts_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter1326 in self.success:
                iter1326.write(oprot)
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
all_structs.append(getCoinProducts_result)
getCoinProducts_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT, [CoinProductItem, None], False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getCoinProductsByPgCode_args(object):
    """
    Attributes:
     - appStoreCode
     - pgCode
     - country
     - language
    """


    def __init__(self, appStoreCode=None, pgCode=None, country=None, language=None,):
        self.appStoreCode = appStoreCode
        self.pgCode = pgCode
        self.country = country
        self.language = language

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
                if ftype == TType.I32:
                    self.appStoreCode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.pgCode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.country = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.language = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('getCoinProductsByPgCode_args')
        if self.appStoreCode is not None:
            oprot.writeFieldBegin('appStoreCode', TType.I32, 2)
            oprot.writeI32(self.appStoreCode)
            oprot.writeFieldEnd()
        if self.pgCode is not None:
            oprot.writeFieldBegin('pgCode', TType.I32, 3)
            oprot.writeI32(self.pgCode)
            oprot.writeFieldEnd()
        if self.country is not None:
            oprot.writeFieldBegin('country', TType.STRING, 4)
            oprot.writeString(self.country.encode('utf-8') if sys.version_info[0] == 2 else self.country)
            oprot.writeFieldEnd()
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 5)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
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
all_structs.append(getCoinProductsByPgCode_args)
getCoinProductsByPgCode_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.I32, 'appStoreCode', None, None, ),  # 2
    (3, TType.I32, 'pgCode', None, None, ),  # 3
    (4, TType.STRING, 'country', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'language', 'UTF8', None, ),  # 5
)


class getCoinProductsByPgCode_result(object):
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
                    (_etype1330, _size1327) = iprot.readListBegin()
                    for _i1331 in range(_size1327):
                        _elem1332 = CoinProductItem()
                        _elem1332.read(iprot)
                        self.success.append(_elem1332)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
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
        oprot.writeStructBegin('getCoinProductsByPgCode_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter1333 in self.success:
                iter1333.write(oprot)
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
all_structs.append(getCoinProductsByPgCode_result)
getCoinProductsByPgCode_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT, [CoinProductItem, None], False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getCoinPurchaseHistory_args(object):
    """
    Attributes:
     - request
    """


    def __init__(self, request=None,):
        self.request = request

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
                    self.request = CoinHistoryCondition()
                    self.request.read(iprot)
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
        oprot.writeStructBegin('getCoinPurchaseHistory_args')
        if self.request is not None:
            oprot.writeFieldBegin('request', TType.STRUCT, 2)
            self.request.write(oprot)
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
all_structs.append(getCoinPurchaseHistory_args)
getCoinPurchaseHistory_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRUCT, 'request', [CoinHistoryCondition, None], None, ),  # 2
)


class getCoinPurchaseHistory_result(object):
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
                    self.success = CoinHistoryResult()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
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
        oprot.writeStructBegin('getCoinPurchaseHistory_result')
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
all_structs.append(getCoinPurchaseHistory_result)
getCoinPurchaseHistory_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [CoinHistoryResult, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getCoinUseAndRefundHistory_args(object):
    """
    Attributes:
     - request
    """


    def __init__(self, request=None,):
        self.request = request

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
                    self.request = CoinHistoryCondition()
                    self.request.read(iprot)
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
        oprot.writeStructBegin('getCoinUseAndRefundHistory_args')
        if self.request is not None:
            oprot.writeFieldBegin('request', TType.STRUCT, 2)
            self.request.write(oprot)
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
all_structs.append(getCoinUseAndRefundHistory_args)
getCoinUseAndRefundHistory_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRUCT, 'request', [CoinHistoryCondition, None], None, ),  # 2
)


class getCoinUseAndRefundHistory_result(object):
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
                    self.success = CoinHistoryResult()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
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
        oprot.writeStructBegin('getCoinUseAndRefundHistory_result')
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
all_structs.append(getCoinUseAndRefundHistory_result)
getCoinUseAndRefundHistory_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [CoinHistoryResult, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getDownloads_args(object):
    """
    Attributes:
     - start
     - size
     - language
     - country
    """


    def __init__(self, start=None, size=None, language=None, country=None,):
        self.start = start
        self.size = size
        self.language = language
        self.country = country

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
                    self.start = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.size = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.language = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.country = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('getDownloads_args')
        if self.start is not None:
            oprot.writeFieldBegin('start', TType.I64, 2)
            oprot.writeI64(self.start)
            oprot.writeFieldEnd()
        if self.size is not None:
            oprot.writeFieldBegin('size', TType.I32, 3)
            oprot.writeI32(self.size)
            oprot.writeFieldEnd()
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 4)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        if self.country is not None:
            oprot.writeFieldBegin('country', TType.STRING, 5)
            oprot.writeString(self.country.encode('utf-8') if sys.version_info[0] == 2 else self.country)
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
all_structs.append(getDownloads_args)
getDownloads_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.I64, 'start', None, None, ),  # 2
    (3, TType.I32, 'size', None, None, ),  # 3
    (4, TType.STRING, 'language', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'country', 'UTF8', None, ),  # 5
)


class getDownloads_result(object):
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
                    self.success = ProductList()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
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
        oprot.writeStructBegin('getDownloads_result')
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
all_structs.append(getDownloads_result)
getDownloads_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [ProductList, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getEventPackages_args(object):
    """
    Attributes:
     - start
     - size
     - language
     - country
    """


    def __init__(self, start=None, size=None, language=None, country=None,):
        self.start = start
        self.size = size
        self.language = language
        self.country = country

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
                    self.start = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.size = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.language = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.country = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('getEventPackages_args')
        if self.start is not None:
            oprot.writeFieldBegin('start', TType.I64, 2)
            oprot.writeI64(self.start)
            oprot.writeFieldEnd()
        if self.size is not None:
            oprot.writeFieldBegin('size', TType.I32, 3)
            oprot.writeI32(self.size)
            oprot.writeFieldEnd()
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 4)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        if self.country is not None:
            oprot.writeFieldBegin('country', TType.STRING, 5)
            oprot.writeString(self.country.encode('utf-8') if sys.version_info[0] == 2 else self.country)
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
all_structs.append(getEventPackages_args)
getEventPackages_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.I64, 'start', None, None, ),  # 2
    (3, TType.I32, 'size', None, None, ),  # 3
    (4, TType.STRING, 'language', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'country', 'UTF8', None, ),  # 5
)


class getEventPackages_result(object):
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
                    self.success = ProductList()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
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
        oprot.writeStructBegin('getEventPackages_result')
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
all_structs.append(getEventPackages_result)
getEventPackages_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [ProductList, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getNewlyReleasedPackages_args(object):
    """
    Attributes:
     - start
     - size
     - language
     - country
    """


    def __init__(self, start=None, size=None, language=None, country=None,):
        self.start = start
        self.size = size
        self.language = language
        self.country = country

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
                    self.start = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.size = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.language = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.country = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('getNewlyReleasedPackages_args')
        if self.start is not None:
            oprot.writeFieldBegin('start', TType.I64, 2)
            oprot.writeI64(self.start)
            oprot.writeFieldEnd()
        if self.size is not None:
            oprot.writeFieldBegin('size', TType.I32, 3)
            oprot.writeI32(self.size)
            oprot.writeFieldEnd()
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 4)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        if self.country is not None:
            oprot.writeFieldBegin('country', TType.STRING, 5)
            oprot.writeString(self.country.encode('utf-8') if sys.version_info[0] == 2 else self.country)
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
all_structs.append(getNewlyReleasedPackages_args)
getNewlyReleasedPackages_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.I64, 'start', None, None, ),  # 2
    (3, TType.I32, 'size', None, None, ),  # 3
    (4, TType.STRING, 'language', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'country', 'UTF8', None, ),  # 5
)


class getNewlyReleasedPackages_result(object):
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
                    self.success = ProductList()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
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
        oprot.writeStructBegin('getNewlyReleasedPackages_result')
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
all_structs.append(getNewlyReleasedPackages_result)
getNewlyReleasedPackages_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [ProductList, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getPopularPackages_args(object):
    """
    Attributes:
     - start
     - size
     - language
     - country
    """


    def __init__(self, start=None, size=None, language=None, country=None,):
        self.start = start
        self.size = size
        self.language = language
        self.country = country

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
                    self.start = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.size = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.language = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.country = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('getPopularPackages_args')
        if self.start is not None:
            oprot.writeFieldBegin('start', TType.I64, 2)
            oprot.writeI64(self.start)
            oprot.writeFieldEnd()
        if self.size is not None:
            oprot.writeFieldBegin('size', TType.I32, 3)
            oprot.writeI32(self.size)
            oprot.writeFieldEnd()
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 4)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        if self.country is not None:
            oprot.writeFieldBegin('country', TType.STRING, 5)
            oprot.writeString(self.country.encode('utf-8') if sys.version_info[0] == 2 else self.country)
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
all_structs.append(getPopularPackages_args)
getPopularPackages_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.I64, 'start', None, None, ),  # 2
    (3, TType.I32, 'size', None, None, ),  # 3
    (4, TType.STRING, 'language', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'country', 'UTF8', None, ),  # 5
)


class getPopularPackages_result(object):
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
                    self.success = ProductList()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
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
        oprot.writeStructBegin('getPopularPackages_result')
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
all_structs.append(getPopularPackages_result)
getPopularPackages_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [ProductList, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getPresentsReceived_args(object):
    """
    Attributes:
     - start
     - size
     - language
     - country
    """


    def __init__(self, start=None, size=None, language=None, country=None,):
        self.start = start
        self.size = size
        self.language = language
        self.country = country

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
                    self.start = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.size = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.language = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.country = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('getPresentsReceived_args')
        if self.start is not None:
            oprot.writeFieldBegin('start', TType.I64, 2)
            oprot.writeI64(self.start)
            oprot.writeFieldEnd()
        if self.size is not None:
            oprot.writeFieldBegin('size', TType.I32, 3)
            oprot.writeI32(self.size)
            oprot.writeFieldEnd()
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 4)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        if self.country is not None:
            oprot.writeFieldBegin('country', TType.STRING, 5)
            oprot.writeString(self.country.encode('utf-8') if sys.version_info[0] == 2 else self.country)
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
all_structs.append(getPresentsReceived_args)
getPresentsReceived_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.I64, 'start', None, None, ),  # 2
    (3, TType.I32, 'size', None, None, ),  # 3
    (4, TType.STRING, 'language', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'country', 'UTF8', None, ),  # 5
)


class getPresentsReceived_result(object):
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
                    self.success = ProductList()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
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
        oprot.writeStructBegin('getPresentsReceived_result')
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
all_structs.append(getPresentsReceived_result)
getPresentsReceived_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [ProductList, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getPresentsSent_args(object):
    """
    Attributes:
     - start
     - size
     - language
     - country
    """


    def __init__(self, start=None, size=None, language=None, country=None,):
        self.start = start
        self.size = size
        self.language = language
        self.country = country

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
                    self.start = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.size = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.language = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.country = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('getPresentsSent_args')
        if self.start is not None:
            oprot.writeFieldBegin('start', TType.I64, 2)
            oprot.writeI64(self.start)
            oprot.writeFieldEnd()
        if self.size is not None:
            oprot.writeFieldBegin('size', TType.I32, 3)
            oprot.writeI32(self.size)
            oprot.writeFieldEnd()
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 4)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        if self.country is not None:
            oprot.writeFieldBegin('country', TType.STRING, 5)
            oprot.writeString(self.country.encode('utf-8') if sys.version_info[0] == 2 else self.country)
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
all_structs.append(getPresentsSent_args)
getPresentsSent_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.I64, 'start', None, None, ),  # 2
    (3, TType.I32, 'size', None, None, ),  # 3
    (4, TType.STRING, 'language', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'country', 'UTF8', None, ),  # 5
)


class getPresentsSent_result(object):
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
                    self.success = ProductList()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
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
        oprot.writeStructBegin('getPresentsSent_result')
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
all_structs.append(getPresentsSent_result)
getPresentsSent_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [ProductList, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getProduct_args(object):
    """
    Attributes:
     - packageID
     - language
     - country
    """


    def __init__(self, packageID=None, language=None, country=None,):
        self.packageID = packageID
        self.language = language
        self.country = country

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
                    self.packageID = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.language = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.country = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('getProduct_args')
        if self.packageID is not None:
            oprot.writeFieldBegin('packageID', TType.I64, 2)
            oprot.writeI64(self.packageID)
            oprot.writeFieldEnd()
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 3)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        if self.country is not None:
            oprot.writeFieldBegin('country', TType.STRING, 4)
            oprot.writeString(self.country.encode('utf-8') if sys.version_info[0] == 2 else self.country)
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
all_structs.append(getProduct_args)
getProduct_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.I64, 'packageID', None, None, ),  # 2
    (3, TType.STRING, 'language', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'country', 'UTF8', None, ),  # 4
)


class getProduct_result(object):
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
                    self.success = Product()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
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
        oprot.writeStructBegin('getProduct_result')
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
all_structs.append(getProduct_result)
getProduct_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [Product, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getProductList_args(object):
    """
    Attributes:
     - productIdList
     - language
     - country
    """


    def __init__(self, productIdList=None, language=None, country=None,):
        self.productIdList = productIdList
        self.language = language
        self.country = country

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
                if ftype == TType.LIST:
                    self.productIdList = []
                    (_etype1337, _size1334) = iprot.readListBegin()
                    for _i1338 in range(_size1334):
                        _elem1339 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.productIdList.append(_elem1339)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.language = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.country = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('getProductList_args')
        if self.productIdList is not None:
            oprot.writeFieldBegin('productIdList', TType.LIST, 2)
            oprot.writeListBegin(TType.STRING, len(self.productIdList))
            for iter1340 in self.productIdList:
                oprot.writeString(iter1340.encode('utf-8') if sys.version_info[0] == 2 else iter1340)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 3)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        if self.country is not None:
            oprot.writeFieldBegin('country', TType.STRING, 4)
            oprot.writeString(self.country.encode('utf-8') if sys.version_info[0] == 2 else self.country)
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
all_structs.append(getProductList_args)
getProductList_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.LIST, 'productIdList', (TType.STRING, 'UTF8', False), None, ),  # 2
    (3, TType.STRING, 'language', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'country', 'UTF8', None, ),  # 4
)


class getProductList_result(object):
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
                    self.success = ProductList()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
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
        oprot.writeStructBegin('getProductList_result')
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
all_structs.append(getProductList_result)
getProductList_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [ProductList, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getProductListWithCarrier_args(object):
    """
    Attributes:
     - productIdList
     - language
     - country
     - carrierCode
    """


    def __init__(self, productIdList=None, language=None, country=None, carrierCode=None,):
        self.productIdList = productIdList
        self.language = language
        self.country = country
        self.carrierCode = carrierCode

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
                if ftype == TType.LIST:
                    self.productIdList = []
                    (_etype1344, _size1341) = iprot.readListBegin()
                    for _i1345 in range(_size1341):
                        _elem1346 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.productIdList.append(_elem1346)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.language = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.country = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.carrierCode = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('getProductListWithCarrier_args')
        if self.productIdList is not None:
            oprot.writeFieldBegin('productIdList', TType.LIST, 2)
            oprot.writeListBegin(TType.STRING, len(self.productIdList))
            for iter1347 in self.productIdList:
                oprot.writeString(iter1347.encode('utf-8') if sys.version_info[0] == 2 else iter1347)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 3)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        if self.country is not None:
            oprot.writeFieldBegin('country', TType.STRING, 4)
            oprot.writeString(self.country.encode('utf-8') if sys.version_info[0] == 2 else self.country)
            oprot.writeFieldEnd()
        if self.carrierCode is not None:
            oprot.writeFieldBegin('carrierCode', TType.STRING, 5)
            oprot.writeString(self.carrierCode.encode('utf-8') if sys.version_info[0] == 2 else self.carrierCode)
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
all_structs.append(getProductListWithCarrier_args)
getProductListWithCarrier_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.LIST, 'productIdList', (TType.STRING, 'UTF8', False), None, ),  # 2
    (3, TType.STRING, 'language', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'country', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'carrierCode', 'UTF8', None, ),  # 5
)


class getProductListWithCarrier_result(object):
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
                    self.success = ProductList()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
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
        oprot.writeStructBegin('getProductListWithCarrier_result')
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
all_structs.append(getProductListWithCarrier_result)
getProductListWithCarrier_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [ProductList, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getProductWithCarrier_args(object):
    """
    Attributes:
     - packageID
     - language
     - country
     - carrierCode
    """


    def __init__(self, packageID=None, language=None, country=None, carrierCode=None,):
        self.packageID = packageID
        self.language = language
        self.country = country
        self.carrierCode = carrierCode

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
                    self.packageID = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.language = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.country = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.carrierCode = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('getProductWithCarrier_args')
        if self.packageID is not None:
            oprot.writeFieldBegin('packageID', TType.I64, 2)
            oprot.writeI64(self.packageID)
            oprot.writeFieldEnd()
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 3)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        if self.country is not None:
            oprot.writeFieldBegin('country', TType.STRING, 4)
            oprot.writeString(self.country.encode('utf-8') if sys.version_info[0] == 2 else self.country)
            oprot.writeFieldEnd()
        if self.carrierCode is not None:
            oprot.writeFieldBegin('carrierCode', TType.STRING, 5)
            oprot.writeString(self.carrierCode.encode('utf-8') if sys.version_info[0] == 2 else self.carrierCode)
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
all_structs.append(getProductWithCarrier_args)
getProductWithCarrier_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.I64, 'packageID', None, None, ),  # 2
    (3, TType.STRING, 'language', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'country', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'carrierCode', 'UTF8', None, ),  # 5
)


class getProductWithCarrier_result(object):
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
                    self.success = Product()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
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
        oprot.writeStructBegin('getProductWithCarrier_result')
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
all_structs.append(getProductWithCarrier_result)
getProductWithCarrier_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [Product, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getPurchaseHistory_args(object):
    """
    Attributes:
     - start
     - size
     - language
     - country
    """


    def __init__(self, start=None, size=None, language=None, country=None,):
        self.start = start
        self.size = size
        self.language = language
        self.country = country

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
                    self.start = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.size = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.language = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.country = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('getPurchaseHistory_args')
        if self.start is not None:
            oprot.writeFieldBegin('start', TType.I64, 2)
            oprot.writeI64(self.start)
            oprot.writeFieldEnd()
        if self.size is not None:
            oprot.writeFieldBegin('size', TType.I32, 3)
            oprot.writeI32(self.size)
            oprot.writeFieldEnd()
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 4)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        if self.country is not None:
            oprot.writeFieldBegin('country', TType.STRING, 5)
            oprot.writeString(self.country.encode('utf-8') if sys.version_info[0] == 2 else self.country)
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
all_structs.append(getPurchaseHistory_args)
getPurchaseHistory_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.I64, 'start', None, None, ),  # 2
    (3, TType.I32, 'size', None, None, ),  # 3
    (4, TType.STRING, 'language', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'country', 'UTF8', None, ),  # 5
)


class getPurchaseHistory_result(object):
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
                    self.success = ProductList()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
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
        oprot.writeStructBegin('getPurchaseHistory_result')
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
all_structs.append(getPurchaseHistory_result)
getPurchaseHistory_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [ProductList, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getTotalBalance_args(object):
    """
    Attributes:
     - appStoreCode
    """


    def __init__(self, appStoreCode=None,):
        self.appStoreCode = appStoreCode

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
                if ftype == TType.I32:
                    self.appStoreCode = iprot.readI32()
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
        oprot.writeStructBegin('getTotalBalance_args')
        if self.appStoreCode is not None:
            oprot.writeFieldBegin('appStoreCode', TType.I32, 2)
            oprot.writeI32(self.appStoreCode)
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
all_structs.append(getTotalBalance_args)
getTotalBalance_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.I32, 'appStoreCode', None, None, ),  # 2
)


class getTotalBalance_result(object):
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
                    self.success = Coin()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
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
        oprot.writeStructBegin('getTotalBalance_result')
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
all_structs.append(getTotalBalance_result)
getTotalBalance_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [Coin, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class notifyDownloaded_args(object):
    """
    Attributes:
     - packageId
     - language
    """


    def __init__(self, packageId=None, language=None,):
        self.packageId = packageId
        self.language = language

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
                    self.packageId = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.language = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('notifyDownloaded_args')
        if self.packageId is not None:
            oprot.writeFieldBegin('packageId', TType.I64, 2)
            oprot.writeI64(self.packageId)
            oprot.writeFieldEnd()
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 3)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
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
all_structs.append(notifyDownloaded_args)
notifyDownloaded_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.I64, 'packageId', None, None, ),  # 2
    (3, TType.STRING, 'language', 'UTF8', None, ),  # 3
)


class notifyDownloaded_result(object):
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
                if ftype == TType.I64:
                    self.success = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
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
        oprot.writeStructBegin('notifyDownloaded_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.I64, 0)
            oprot.writeI64(self.success)
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
all_structs.append(notifyDownloaded_result)
notifyDownloaded_result.thrift_spec = (
    (0, TType.I64, 'success', None, None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class reserveCoinPurchase_args(object):
    """
    Attributes:
     - request
    """


    def __init__(self, request=None,):
        self.request = request

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
                    self.request = CoinPurchaseReservation()
                    self.request.read(iprot)
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
        oprot.writeStructBegin('reserveCoinPurchase_args')
        if self.request is not None:
            oprot.writeFieldBegin('request', TType.STRUCT, 2)
            self.request.write(oprot)
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
all_structs.append(reserveCoinPurchase_args)
reserveCoinPurchase_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRUCT, 'request', [CoinPurchaseReservation, None], None, ),  # 2
)


class reserveCoinPurchase_result(object):
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
                    self.success = PaymentReservationResult()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
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
        oprot.writeStructBegin('reserveCoinPurchase_result')
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
all_structs.append(reserveCoinPurchase_result)
reserveCoinPurchase_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [PaymentReservationResult, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class reservePayment_args(object):
    """
    Attributes:
     - paymentReservation
    """


    def __init__(self, paymentReservation=None,):
        self.paymentReservation = paymentReservation

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
                    self.paymentReservation = PaymentReservation()
                    self.paymentReservation.read(iprot)
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
        oprot.writeStructBegin('reservePayment_args')
        if self.paymentReservation is not None:
            oprot.writeFieldBegin('paymentReservation', TType.STRUCT, 2)
            self.paymentReservation.write(oprot)
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
all_structs.append(reservePayment_args)
reservePayment_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRUCT, 'paymentReservation', [PaymentReservation, None], None, ),  # 2
)


class reservePayment_result(object):
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
                    self.success = PaymentReservationResult()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
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
        oprot.writeStructBegin('reservePayment_result')
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
all_structs.append(reservePayment_result)
reservePayment_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [PaymentReservationResult, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)
fix_spec(all_structs)
del all_structs

