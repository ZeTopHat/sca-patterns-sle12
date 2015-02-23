#!/usr/bin/python
#
# Title:       Important Security Announcement for samba SUSE-SU-2015:0353-1
# Description: Security fixes for SUSE Linux Enterprise 12 SP0
# Source:      Security Announcement Parser v1.2.5
# Modified:    2015 Feb 23
#
##############################################################################
# Copyright (C) 2015 SUSE LLC
##############################################################################
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.
#
#  Authors/Contributors:
#   Jason Record (jrecord@suse.com)
#
##############################################################################

import os
import Core
import SUSE

META_CLASS = "Security"
META_CATEGORY = "SLE"
META_COMPONENT = "samba"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2015-02/msg00028.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'samba'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2015:0353-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 12):
	if ( SERVER['DistroPatchLevel'] == 0 ):
		PACKAGES = {
			'libdcerpc-atsvc-devel': '4.1.12-16.1',
			'libdcerpc-atsvc0': '4.1.12-16.1',
			'libdcerpc-atsvc0-debuginfo': '4.1.12-16.1',
			'libdcerpc-binding0': '4.1.12-16.1',
			'libdcerpc-binding0-32bit': '4.1.12-16.1',
			'libdcerpc-binding0-debuginfo': '4.1.12-16.1',
			'libdcerpc-binding0-debuginfo-32bit': '4.1.12-16.1',
			'libdcerpc-devel': '4.1.12-16.1',
			'libdcerpc-samr-devel': '4.1.12-16.1',
			'libdcerpc-samr0': '4.1.12-16.1',
			'libdcerpc-samr0-debuginfo': '4.1.12-16.1',
			'libdcerpc0': '4.1.12-16.1',
			'libdcerpc0-32bit': '4.1.12-16.1',
			'libdcerpc0-debuginfo': '4.1.12-16.1',
			'libdcerpc0-debuginfo-32bit': '4.1.12-16.1',
			'libgensec-devel': '4.1.12-16.1',
			'libgensec0': '4.1.12-16.1',
			'libgensec0-32bit': '4.1.12-16.1',
			'libgensec0-debuginfo': '4.1.12-16.1',
			'libgensec0-debuginfo-32bit': '4.1.12-16.1',
			'libndr-devel': '4.1.12-16.1',
			'libndr-krb5pac-devel': '4.1.12-16.1',
			'libndr-krb5pac0': '4.1.12-16.1',
			'libndr-krb5pac0-32bit': '4.1.12-16.1',
			'libndr-krb5pac0-debuginfo': '4.1.12-16.1',
			'libndr-krb5pac0-debuginfo-32bit': '4.1.12-16.1',
			'libndr-nbt-devel': '4.1.12-16.1',
			'libndr-nbt0': '4.1.12-16.1',
			'libndr-nbt0-32bit': '4.1.12-16.1',
			'libndr-nbt0-debuginfo': '4.1.12-16.1',
			'libndr-nbt0-debuginfo-32bit': '4.1.12-16.1',
			'libndr-standard-devel': '4.1.12-16.1',
			'libndr-standard0': '4.1.12-16.1',
			'libndr-standard0-32bit': '4.1.12-16.1',
			'libndr-standard0-debuginfo': '4.1.12-16.1',
			'libndr-standard0-debuginfo-32bit': '4.1.12-16.1',
			'libndr0': '4.1.12-16.1',
			'libndr0-32bit': '4.1.12-16.1',
			'libndr0-debuginfo': '4.1.12-16.1',
			'libndr0-debuginfo-32bit': '4.1.12-16.1',
			'libnetapi-devel': '4.1.12-16.1',
			'libnetapi0': '4.1.12-16.1',
			'libnetapi0-32bit': '4.1.12-16.1',
			'libnetapi0-debuginfo': '4.1.12-16.1',
			'libnetapi0-debuginfo-32bit': '4.1.12-16.1',
			'libpdb-devel': '4.1.12-16.1',
			'libpdb0': '4.1.12-16.1',
			'libpdb0-32bit': '4.1.12-16.1',
			'libpdb0-debuginfo': '4.1.12-16.1',
			'libpdb0-debuginfo-32bit': '4.1.12-16.1',
			'libregistry-devel': '4.1.12-16.1',
			'libregistry0': '4.1.12-16.1',
			'libregistry0-debuginfo': '4.1.12-16.1',
			'libsamba-credentials-devel': '4.1.12-16.1',
			'libsamba-credentials0': '4.1.12-16.1',
			'libsamba-credentials0-32bit': '4.1.12-16.1',
			'libsamba-credentials0-debuginfo': '4.1.12-16.1',
			'libsamba-credentials0-debuginfo-32bit': '4.1.12-16.1',
			'libsamba-hostconfig-devel': '4.1.12-16.1',
			'libsamba-hostconfig0': '4.1.12-16.1',
			'libsamba-hostconfig0-32bit': '4.1.12-16.1',
			'libsamba-hostconfig0-debuginfo': '4.1.12-16.1',
			'libsamba-hostconfig0-debuginfo-32bit': '4.1.12-16.1',
			'libsamba-policy-devel': '4.1.12-16.1',
			'libsamba-policy0': '4.1.12-16.1',
			'libsamba-policy0-debuginfo': '4.1.12-16.1',
			'libsamba-util-devel': '4.1.12-16.1',
			'libsamba-util0': '4.1.12-16.1',
			'libsamba-util0-32bit': '4.1.12-16.1',
			'libsamba-util0-debuginfo': '4.1.12-16.1',
			'libsamba-util0-debuginfo-32bit': '4.1.12-16.1',
			'libsamdb-devel': '4.1.12-16.1',
			'libsamdb0': '4.1.12-16.1',
			'libsamdb0-32bit': '4.1.12-16.1',
			'libsamdb0-debuginfo': '4.1.12-16.1',
			'libsamdb0-debuginfo-32bit': '4.1.12-16.1',
			'libsmbclient-devel': '4.1.12-16.1',
			'libsmbclient-raw-devel': '4.1.12-16.1',
			'libsmbclient-raw0': '4.1.12-16.1',
			'libsmbclient-raw0-32bit': '4.1.12-16.1',
			'libsmbclient-raw0-debuginfo': '4.1.12-16.1',
			'libsmbclient-raw0-debuginfo-32bit': '4.1.12-16.1',
			'libsmbclient0': '4.1.12-16.1',
			'libsmbclient0-32bit': '4.1.12-16.1',
			'libsmbclient0-debuginfo': '4.1.12-16.1',
			'libsmbclient0-debuginfo-32bit': '4.1.12-16.1',
			'libsmbconf-devel': '4.1.12-16.1',
			'libsmbconf0': '4.1.12-16.1',
			'libsmbconf0-32bit': '4.1.12-16.1',
			'libsmbconf0-debuginfo': '4.1.12-16.1',
			'libsmbconf0-debuginfo-32bit': '4.1.12-16.1',
			'libsmbldap-devel': '4.1.12-16.1',
			'libsmbldap0': '4.1.12-16.1',
			'libsmbldap0-32bit': '4.1.12-16.1',
			'libsmbldap0-debuginfo': '4.1.12-16.1',
			'libsmbldap0-debuginfo-32bit': '4.1.12-16.1',
			'libsmbsharemodes-devel': '4.1.12-16.1',
			'libsmbsharemodes0': '4.1.12-16.1',
			'libsmbsharemodes0-debuginfo': '4.1.12-16.1',
			'libtevent-util-devel': '4.1.12-16.1',
			'libtevent-util0': '4.1.12-16.1',
			'libtevent-util0-32bit': '4.1.12-16.1',
			'libtevent-util0-debuginfo': '4.1.12-16.1',
			'libtevent-util0-debuginfo-32bit': '4.1.12-16.1',
			'libwbclient-devel': '4.1.12-16.1',
			'libwbclient0': '4.1.12-16.1',
			'libwbclient0-32bit': '4.1.12-16.1',
			'libwbclient0-debuginfo': '4.1.12-16.1',
			'libwbclient0-debuginfo-32bit': '4.1.12-16.1',
			'samba': '4.1.12-16.1',
			'samba-32bit': '4.1.12-16.1',
			'samba-client': '4.1.12-16.1',
			'samba-client-32bit': '4.1.12-16.1',
			'samba-client-debuginfo': '4.1.12-16.1',
			'samba-client-debuginfo-32bit': '4.1.12-16.1',
			'samba-core-devel': '4.1.12-16.1',
			'samba-debuginfo': '4.1.12-16.1',
			'samba-debuginfo-32bit': '4.1.12-16.1',
			'samba-debugsource': '4.1.12-16.1',
			'samba-doc': '4.1.12-16.1',
			'samba-libs': '4.1.12-16.1',
			'samba-libs-32bit': '4.1.12-16.1',
			'samba-libs-debuginfo': '4.1.12-16.1',
			'samba-libs-debuginfo-32bit': '4.1.12-16.1',
			'samba-test-devel': '4.1.12-16.1',
			'samba-winbind': '4.1.12-16.1',
			'samba-winbind-32bit': '4.1.12-16.1',
			'samba-winbind-debuginfo': '4.1.12-16.1',
			'samba-winbind-debuginfo-32bit': '4.1.12-16.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

