#!/usr/bin/env python
# -*- coding: ascii -*-

"""
A Monkey Patch for SleekXMPP 1.3.3 to allow for TLS Certificate
date validation for date prior to 2050


Changelog:
    - 2018-12-12 - Initial Commit
"""

__author__ = "Joseph Porcelli (porcej@gmail.com)"
__version__ = "1.0.0"
__version_info__ = (1, 0, 0, '', 0)
__copyright__ = "Copyright (c) 2018 Joseph Porcelli"
__license__ = "MIT"

__all__ = ['sleekmonkey']

import sleekxmpp
import logging

log = logging.getLogger(__name__)



def extract_dates_mp(raw_cert):
    """
    Override SleekXMPP's TLS Certificte to handle all Valid TLS Date Formats
        - Date prior to 1/1/2050:'%y%m%d%H%M%SZ'
        - Date post after 1/1/2050: '%Y%m%d%H%M%SZ' 
    """
    slk_cert = sleekxmpp.xmlstream.cert
    if not slk_cert.HAVE_PYASN1:
        log.warning("Could not find pyasn1 and pyasn1_modules. " + \
                    "SSL certificate expiration COULD NOT BE VERIFIED.")
        return None, None

    log.info("Monkey Patched Date Extration")

    cert = slk_cert.decoder.decode(raw_cert, asn1Spec=slk_cert.Certificate())[0]
    tbs = cert.getComponentByName('tbsCertificate')
    validity = tbs.getComponentByName('validity')

    not_before = validity.getComponentByName('notBefore')
    not_before = str(not_before.getComponent())

    try:
        not_before = slk_cert.datetime.strptime(not_before, '%y%m%d%H%M%SZ')
    except ValueError:
        not_before = slk_cert.datetime.strptime(not_before, '%Y%m%d%H%M%SZ')

    not_after = validity.getComponentByName('notAfter')
    not_after = str(not_after.getComponent())
    try:
        not_after = slk_cert.datetime.strptime(not_after, '%y%m%d%H%M%SZ')
    except ValueError:
        not_after = slk_cert.datetime.strptime(not_after, '%Y%m%d%H%M%SZ')

    return not_before, not_after

def monkey_patch():
    """
    Perform the monkey patching here
    """
    sleekxmpp.xmlstream.cert.extract_dates = extract_dates_mp
    log.debug("SleekXMPP Has been monkey patched!")




if __name__ == '__main__':
    """
    By Default we monkey patch.
    """
    monkey_patch()